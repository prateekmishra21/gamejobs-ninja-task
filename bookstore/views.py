from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import *
# Create your views here.


def LoginForm(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/librarian')
        return redirect('dashboard')
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['username']
        p = d['pwd']
        user = authenticate(username = u,password = p)
        if user:
            login(request,user)
            if request.user.is_superuser:
                return redirect('/librarian')
            else:
                return redirect('dashboard')
        else:
            error = True

    d = {"error":error}

    return render(request,'loginform.html',d)


def SignupForm(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/librarian')
        return redirect('dashboard')
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['username']
        p = d['pwd']
        f = d['fullname']
        e = d['email']
        user = User.objects.filter(username = u)
        if user:
            error = True
        else:
            User.objects.create_user(username=u,password=p,first_name=f,email=e)
            return redirect('login')

    d = {"error": error}

    return render(request,'signupform.html',d)

def LogoutUser(request):
    logout(request)
    return redirect('login')


def UserDashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_superuser:
        return redirect('/librarian')
    allbooks = UserBook.objects.filter(author=request.user)
    paginator = Paginator(allbooks, 6)
    page = request.GET.get('page', 1)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    d = {"allbooks":books,"stars":range(1,6),"pages":len(books.paginator.page_range)}
    return render(request,'user_dashboard.html',d)

def AddNewBook(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_superuser:
        return redirect('/librarian')
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.author = request.user
            data.review_stars = request.POST['stars']
            if data.type == 'Ebook':
                data.bookfile = request.FILES['ebook']
            data.save()
            try:
                cover = request.FILES['cover']
                data.bookcover = cover
                data.save()
            except:
                pass

            return redirect('dashboard')

    d = {"form":form}
    return render(request, 'add_book.html',d)


def DeleteBook(request,bid):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_superuser:
        return redirect('/librarian')
    UserBook.objects.get(id = bid).delete()
    try:
        pagenumber = request.GET['page']
        prevpath = request.GET['next']
        print("path....", request.GET['next'])
        return redirect(prevpath + '?page=' + str(pagenumber))
    except:
        return redirect('dashboard')

def EditBook(request,bid):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_superuser:
        return redirect('/librarian')
    stars = {1:False,2:False,3:False,4:False,5:False}
    data = UserBook.objects.get(id = bid)
    star_num = data.review_stars
    stars[star_num] = 'checked'
    form = BookForm(instance=data)
    if request.method == "POST":
        form = BookForm(request.POST, instance=data)
        if form.is_valid():
            data = form.save()
            data.review_stars = request.POST['stars']
            if data.type == 'Ebook':
                data.bookfile = request.FILES['ebook']
            data.save()
            try:
                cover = request.FILES['cover']
                data.bookcover = cover
                data.save()
            except:
                pass
            try:
                pagenumber = request.GET['page']
                prevpath = request.GET['next']
                print("path....",request.GET['next'])
                return redirect(prevpath+'?page='+str(pagenumber))
            except:
                return redirect('dashboard')

    d = {"form": form,"data":data,"stars":stars}
    return render(request, 'edit_book.html', d)





