from datetime import datetime, timedelta
from ftplib import all_errors
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from json import dumps
from django.db.models import Sum, Q
from expensesystem.models import *
from django.db.models.functions import ExtractMonth, ExtractYear
from django.core.paginator import Paginator


# from django.db.models import

# Create your views here.

@login_required(login_url='/loginpage')
def index(request):
    today_date = date.today()
    category_exp = [v for v in Expense.objects.filter(
        owner=request.user).filter().values('category').annotate(sum=Sum('amount'))]
        
    ajeeb = [v for v in Expense.objects.filter(owner=request.user).annotate(
        month=ExtractMonth('date')).values('month').annotate(sum=Sum('amount'))]
    ajeeb1 = [v for v in Expense.objects.filter(owner=request.user).annotate(
        year=ExtractYear('date')).values('year').annotate(sum=Sum('amount'))]
    ajeeb2 = [v for v in Income.objects.filter(owner=request.user).annotate(
        year=ExtractYear('date')).values('year').annotate(sum=Sum('income'))]

    
    expenses = Expense.objects.filter(owner=request.user)
    income = Income.objects.filter(owner=request.user)
    total_inc=0
    dayInc=0
    yrInc=0
    monInc=0
    for inc in income:
        total_inc+=inc.income
        if inc.date == today_date:
            dayInc += inc.income
        if inc.date.year == today_date.year:
            yrInc += inc.income
            # for this month of this year
            if inc.date.month == today_date.month:
                monInc += inc.income



    total_exp = 0
    daysum = 0
    yrsum = 0
    monsum = 0
    new=[]
    for exp in expenses:
        # print(exp.date)
        total_exp += exp.amount
        # for today expense
        if exp.date == today_date:
            daysum += exp.amount
        #  for this year expense
        if exp.date.year == today_date.year:
            yrsum += exp.amount
            # for this month of this year
            if exp.date.month == today_date.month:
                monsum += exp.amount
                new.append(exp)
    # for week expense
    weekexpenses = Expense.objects.filter(owner=request.user, date__range=[
                                          today_date - timedelta(days=7), today_date])
    weekexp = 0
    for week in weekexpenses:
        weekexp += week.amount

    weekIncome = Income.objects.filter(owner=request.user, date__range=[
                                          today_date - timedelta(days=7), today_date])
    weekInc = 0
    for week in weekIncome:
        weekInc += week.income
    # for this month of this year
    # new=[]
    # for item in expenses:
    #     if item.date.year==today_date.year:
    #         new.append(item)
    # monsum=0
    # for i in new :
    #     if i.date.month==today_date.month:
    #         monsum +=i.amount

#  for this year expense

    # yr=Expense.objects.filter(owner=request.user).filter().annotate(year=ExtractYear('date')).values('year').annotate(sum=Sum('amount'))
    # for i in yr :
    #     if i['year']==today_date.year:
    #         year=i['sum']
    balnce_amount=total_inc-total_exp


    today = today_date.strftime("%B %d %Y %A")
    dataJSON = dumps(ajeeb)
    dataJSON3 = dumps(ajeeb1)
    dataJSON2 = dumps(ajeeb2)
    dataJSON1 = dumps(category_exp)
    return render(request, 'index.html', {'data3':dataJSON3,'data2':dataJSON2,'weekInc':weekInc,'monInc':monInc,'yrInc':yrInc ,'dayInc':dayInc ,'balnce_amount': balnce_amount,'new': new, 'data': dataJSON, 'data1': dataJSON1,'total_inc':total_inc ,'total': total_exp, 'year': yrsum, 'month': monsum, 'day': daysum, 'weekexpenses': weekexp, 'today': today, 'today_date': today_date})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "logged in sucessfully..")

                # Profile.objects.create(user=user , bio="hii"  , phone_number="0999" , birth_date=2000-2-2 ,profile_image='avatar-2.jpg ')
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.info(request, "Incorrect password or username ")
    return render(request, 'auth-normal-sign-in.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = NewUserForm()
        context = {'form': form}
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                # obj = Profile(user2)
                # obj.save()
                print("profile")
                user1 = form.cleaned_data.get('username')
                messages.success(
                    request, "Registration successful for " + user1)
                return redirect("/loginpage")
        return render(request, 'auth-sign-up.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/loginpage')


@login_required(login_url='/loginpage')
def list_expense(request):
    if 'query' in request.GET:
        search = request.GET['query']
        multipleQuery = Q(Q(amount__icontains=search) | Q(category__icontains=search) | Q(
            description__icontains=search) | Q(date__icontains=search))
        allexpense = Expense.objects.filter(
            multipleQuery, owner=request.user).order_by('date')
    else:
        allexpense = Expense.objects.filter(
            owner=request.user).order_by('date')

    paginator = Paginator(allexpense, 6)
    # onwhich we are present
    page_number = request.GET.get('page', 1)
    # get that page which is infront of us
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    total_exp = 0
    for exp in allexpense:
        total_exp += exp.amount
    return render(request, 'expenses/list_expense.html', {'page_obj': page_obj, 'expense': page_obj, 'category': categories, 'total': total_exp, 'paginator': paginator, 'page_number': int(page_number)})

# def search(request):
#     if 'query' in request.GET:
#         search = request.GET['query']
#         multipleQuery = Q(Q(amount__icontains=search) | Q(category__icontains=search) | Q(
#             description__icontains=search) | Q(date__icontains=search))
#         allexpense = Expense.objects.filter(multipleQuery, owner=request.user)
#         return render(request , 'expenses/list_expense.html' {'allexpense':allexpense})


def add_expense(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('desc')
        category = request.POST.get('category')
        date = request.POST.get('date')
        expense = Expense(owner=request.user, amount=amount,
                          description=description, category=category, date=date)
        expense.save()
        messages.info(request, "Expense added")
    return redirect('/list_expense')


def delete_expense(request, expense_id):
    expid = Expense.objects.get(pk=expense_id)
    if request.method == 'POST':
        expid.delete()
        return redirect('/list_expense')


def update_expense(request, expense_id):
    editExp = Expense.objects.get(pk=expense_id)
    # if request.method == 'POST':
    editExp.amount = request.POST.get('amount')
    editExp.description = request.POST.get('desc')
    editExp.category = request.POST.get('category')
    editExp.date = request.POST.get('date')
    editExp.save()
    messages.info(request, "Expense updated..")
    return redirect('/list_expense')


def list_category(request):
    categories = Category.objects.all()
    return render(request, 'expenses/list_category.html', {'category': categories})


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('categ')
        category = Category(name=name)
        category.save()
    # allexpense= Expense.objects.filter(owner=request.user)
    return redirect('/list_category')


def update_category(request, category_id):
    editCat = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        editCat.name = request.POST.get('categ')
        editCat.save()
        return redirect('/list_category')


def monthly_expense(request):
    category_exp = [v for v in Expense.objects.filter(
        owner=request.user).filter().values('category').annotate(sum=Sum('amount'))]
    ajeeb = [v for v in Expense.objects.filter(owner=request.user).filter().annotate(
        month=ExtractMonth('date')).values('month').annotate(sum=Sum('amount'))]
    dataJSON = dumps(ajeeb)
    dataJSON1 = dumps(category_exp)
    return render(request, 'chart.html', {'data': dataJSON, 'data1': dataJSON1})


def export_pdf(request):
    template_path = 'expenses/pdf_output.html'
    expenses = Expense.objects.filter(owner=request.user)
    total_exp = 0
    for exp in expenses:
        total_exp += exp.amount
    context = {'expenses': expenses, 'total_exp': total_exp}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline ; attachment ; filename=Expenses ' + \
        str(datetime.now()) + '.pdf '
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    if pisa_status.err:
        return HttpResponse('we had some serrors <pre>' + html + '</pre>')
    return response


def sort(request, name):
    expenses = Expense.objects.filter(owner=request.user).order_by(name)
    paginator = Paginator(expenses, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'expenses/list_expense.html', {'expenses': expenses, 'page_obj': page_obj, 'expense': page_obj, 'paginator': paginator, 'page_number': int(page_number)})


def list_income(request):
    if 'query' in request.GET:
        search = request.GET['query']
        multipleQuery = Q(Q(income__icontains=search) | Q(source__icontains=search) | Q(date__icontains=search))
        income = Income.objects.filter(
            multipleQuery, owner=request.user).order_by('date')
    else:
        income = Income.objects.filter(owner=request.user)
    total_income = 0
    for inc in income:
        total_income += inc.income
    return render(request, 'incomes/list_income.html', {'income': income, 'total_income': total_income})


def add_income(request):
    if request.method == 'POST':
        income = request.POST.get('income')
        source = request.POST.get('source')
        date = request.POST.get('date')
        inc = Income(owner=request.user, income=income,
                    source=source, date=date)
        inc.save()
        messages.info(request, "Income added")
    return redirect('/list_income')

def update_income(request, income_id):
    editInc = Income.objects.get(pk=income_id)
    # if request.method == 'POST':
    editInc.income = request.POST.get('amount')
    editInc.description = request.POST.get('source')
    editInc.date = request.POST.get('date')
    editInc.save()
    messages.info(request, "Income updated..")
    return redirect('/list_income')


def delete_income(request, income_id):
    incId = Income.objects.get(pk=income_id)
    if request.method == 'POST':
        incId .delete()
        return redirect('/list_income')

@login_required(login_url='/loginpage')
def accountSettings(request):
    profile=Profile.objects.filter(user=request.user ,)
    print(profile)
    if profile.exists():
        profile=request.user.profile
        form = ProfileForm(instance=profile)
    else:
        obj = Profile()
        obj.user=request.user
        profile = obj
        form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'account_settings.html', context)
