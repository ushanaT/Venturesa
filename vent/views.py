from django.shortcuts import render , redirect
from .models import Accounts, Investment_plans, Activated_plans,Withdrawals, Deposit_request ,Coin_rate,Admin_account_no
from django.contrib.auth.models import auth, User
from django.contrib import messages



# Create your views here.

def index(request):
  return render(request,"index.html")

#login function and user authentication
def login(request):
  if request.method == 'POST':
    username = request.POST['usern']
    email = request.POST['email']
    passwd = request.POST['passwd1']
    if username and email and passwd != '':
      user= auth.authenticate(email=email,password=passwd, username=username)
      if user is not None:
        auth.login(request, user)
        return redirect('user')
      else:
        messages.info(request, 'Invalid Information')
        return redirect('login')
  else:
    return render(request, 'login.html')

#loging out user
def logout(request):
  auth.logout(request)
  return redirect('/')

#sign up function
def register(request):
  if request.method == 'POST':
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    email = request.POST['email']
    username =request.POST['uname']
    passwd1 = request.POST['passwd1']
    passwd2 =request.POST['passwd2']
    

    if firstname and lastname and email and username and passwd1 and passwd2 != '':
      if passwd1 != passwd2:
        messages.info(request, 'Password does not match')
        return redirect('register')
      elif User.objects.filter(email=email).exists():
        messages.info(request,'Email already in use')
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.info(request,'Username already taken')
        return redirect('register')
      else:
        if len(passwd1) < 6:
           messages.info(request,'Password must not be less than 6 Characters')
           return redirect('register')
        else:
           user =User.objects.create_user(username=username,password=passwd1, email=email, first_name=firstname, last_name=lastname)
           user.save()
           new_account =Accounts.objects.create(fname=firstname, lname=lastname,  username=username, email=email , password=passwd1)
           new_account.save()
           messages.info(request,'Account created successfully')
           return redirect('login')
        
    else:
      messages.info(request, 'please fill the neccessary fieds')
      return redirect('register')

  else:
    return render(request, 'register.html')


#accunt part starts here

def user(request):
  user_logged_in = Accounts.objects.all()
  return render(request, 'useracct.html',{"useractive" :user_logged_in})
 

def investplans(request):
  if request.method == "POST":
    duration =request.POST['duration']
    profit = request.POST['profit']
    plan= request.POST['pname']
    activeuser= request.POST['actuser']
    deposited_amount =request.POST['depost']
    amtint = int(deposited_amount)
    usera = Accounts.objects.get(username=activeuser)
    actb=int(usera.acctb)

    if amtint > actb:
      messages.info(request, 'Accout balance is too low please fund your account and try again')
      return redirect('investplans')
    else:
      actb = actb- amtint
      Accounts.objects.filter(username=activeuser).update(acctb=actb)
      newPlan=Activated_plans.objects.create(planName=plan,profit=profit, duration=duration, depositedAmount= deposited_amount ,usern= activeuser)
      newPlan.save()
      messages.info(request, 'plan activated successfully, you will start Earning in 24 hours ')
      return redirect('investplans')
  else:
    plans = Investment_plans.objects.all()
    return render(request, 'investplans.html' ,{"plans":plans})

#withdrawal starts here

def withdrawal(request):
    if request.method == "POST":
      amount= request.POST['amt']
      gmail= request.POST['umail']
      actn=request.POST['waddres']
      username= request.POST['usname']
      accts= Accounts.objects.all()
      if amount and gmail and actn != "" :
        for i in accts:
          if Accounts.objects.filter(email=gmail).exists():
            curt=Accounts.objects.get(email=gmail)
            acb=int(curt.acctb)
            norm=int(amount)
            if norm <=99:
              messages.info(request, 'mininmmun withdrawal is $100')
              return redirect('withdrawal')
            elif norm > acb :
              messages.info(request, 'insufficient account balance')
              return redirect('withdrawal')
            else:
              acb = acb - norm
              Accounts.objects.filter(email=gmail).update(acctb=acb)
              his=Withdrawals.objects.create(accountnumber=actn, amount=amount, user_requested=username)#add the user here later
              his.save()
              messages.info(request, 'request submited you will be credited in 12 hours ')
              return redirect('withdrawal')
            break
          else:
            messages.info(request, 'email does not exists, use your registered email')
            return redirect('withdrawal')
      else:
        messages.info(request, 'fill the form correctly')
        return redirect('withdrawal')
      
    else:
      use =Accounts.objects.all()
      return render(request, 'withdraw.html', {"useractive":use})


def history(request):
    current_user =request.user
    usern = current_user.username
    userh =Withdrawals.objects.filter(user_requested=usern)
    return render(request, 'history.html',{"logeduserh":userh})

def widthdrawhistory(request):
  return render(request, 'widthdrawhistory.html')


def investp(request):
    current_user =request.user
    usern = current_user.username
    userh =Activated_plans.objects.filter(usern=usern)
    return render(request, 'investments.html', {"planh":userh})



def deposit(request):
  if request.method== "POST":
    amount= request.POST['dammnt']
    if amount == "":
      messages.info(request, 'please enter amount')
      return redirect('deposit')      
    else:
     intamt =int(amount)
     if intamt <= 0:
       messages.info(request, 'INVALID AMOUNT')
       return redirect('deposit')
     else :
       current_user= request.user
       current_username= current_user.username
       convert=Coin_rate.objects.all()
       bamt=0.00023
       conv =int(amount)
       converted =bamt*conv
       convertedd=converted
       new_deposit_request= Deposit_request.objects.create(amount=amount, user_requested=current_username , bitcoin_amount=convertedd)
       new_deposit_request.save()
       return redirect('easypay')
  else:
    return render(request, 'deposite.html')


def account(request):
  return render(request, 'account.html')



#vvvvvv


def easypay(request):
  if request.method == 'POST':
      messages.info(request, 'Transaction submited You will credited in less than two minutes')
      return redirect('deposit')
  else:
    current_user= request.user
    username= current_user.username
    depor=Deposit_request.objects.filter(user_requested=username)
    w = []
    for i in depor:
      j=i.id
      w.append(j)
    holder=0
    for j in w:
      if j >= holder:
        holder=j
      else:
        pass
    current_request=Deposit_request.objects.get(id=holder)
    walletaddres= Admin_account_no.objects.all()

    return render(request,'easypay.html' ,{"w":current_request , "wa": walletaddres})
  

  