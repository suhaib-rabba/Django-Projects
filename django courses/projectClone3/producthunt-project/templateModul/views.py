from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from products.models import Product



# Create your views here.
def home(request):
    return render(request,'templateModul/home.html')

def signup(request):
    if request.method=='POST':
        if request.POST.get('password_post1') == request.POST.get('password_post2'):
            try:
                u = User.objects.get(username=request.POST.get('user'))
                return render(request,'templateModul/signup.html',{'error':"user is already exist"})
            except:
                user=User.objects.create_user(username=request.POST.get('user'),password=request.POST.get('password_post1') )
                login(request, user)
                return redirect('home')
        else:
            return render(request,'templateModul/signup.html',{'error':"password is wrong"})
    else:
        return render(request,'templateModul/signup.html')

def login_views(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('user'), password=request.POST.get('password'))
        if user is not None:
            login( request,user)
            return redirect('home')
        else:
            return render(request,'templateModul/login.html',{'error':"password or username is wrong"})
    else:
        return render(request,'templateModul/login.html')
#---------------------------------------------------------------


def modul_views(request):

    if request.method == 'POST':
        product=Product()
        product.title=request.POST.get('title')
        product.body=request.POST.get('body')
        product.url=request.POST.get('url')
        product.icon=request.FILES.get('icon')
        product.image=request.FILES.get('image')
        product.hunter = request.user
        product.save()

        return redirect('home' )
    else:
        return render(request,'templateModul/modul_form.html')

def modul_render(request):
    objects=Product.objects
    a='جرينة'
    return render(request,'templateModul/modulRender.html',{'z':'yes the variable has a value','objects':objects,a:'المنطقة'})

def modul_detail(request,id):
    object=Product.objects.get(pk=id)
    return render(request,'templateModul/detail.html',{'product':object})
    #-------------------------------------------------------------------------------------

def signup2(request):
    a='first enterance'
    b='first enterance'

    if request.method=='POST':
        if request.POST['password']==request.POST['password_confirm']:
            a='password is correct'
            try:
                user= User.objects.get(username=request.POST['user'])
                b='user is alrady exist'
            except:
                b='create a new user'
                user=User.objects.create_user(username=request.POST['user'], password=request.POST['password'])
                user.save()
                login(request,user)
                return redirect('home')

        else:
            a='password is not correct'

    return render(request,"templateModul/singup_trail2.html",{"reply":a,'reply2':b})
    #-------------------------------------------------------------------------------------
def login_views2(request):
    if request.method=='POST':
        user = authenticate(request, username=request.POST['user'], password=request.POST['password'])
        if user is not None:
             login(request, user)
             return redirect('create')
        else:
             return render(request,'templateModul/login2.html',{'reply':'user or password is not correcct'})





    return render(request,'templateModul/login2.html')
