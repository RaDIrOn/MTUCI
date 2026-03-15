#coding:utf-8
from django.shortcuts import render, redirect
from django.http import Http404
from models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    """Представление для создания новой статьи"""
    if request.user.is_anonymous():
        return redirect('login')      
    
    if request.method == "POST":
        form = {
            'text': request.POST["text"],
            'title': request.POST["title"]
        }
        
        if form["text"] and form["title"]:
            try:
                Article.objects.get(title=form["title"])
                form['errors'] = u"Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
            except Article.DoesNotExist:
                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})
    
def register(request):
    """Регистрация нового пользователя"""
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        
        if not username or not email or not password or not password2:
            return render(request, 'register.html', 
                         {'errors': 'Все поля должны быть заполнены'})
        
        if password != password2:
            return render(request, 'register.html', 
                         {'errors': 'Пароли не совпадают'})
        
        try:
            User.objects.get(username=username)
            return render(request, 'register.html', 
                         {'errors': 'Пользователь с таким именем уже существует'})
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect('archive')
    
    return render(request, 'register.html', {})

def login_view(request):
    """Авторизация пользователя"""
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        if not username or not password:
            return render(request, 'login.html', 
                         {'errors': 'Заполните все поля'})
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('archive')
            else:
                return render(request, 'login.html', 
                             {'errors': 'Аккаунт заблокирован'})
        else:
            return render(request, 'login.html', 
                         {'errors': 'Неправильное имя пользователя или пароль'})
    
    return render(request, 'login.html', {})

def logout_view(request):
    """Выход из системы"""
    logout(request)
    return redirect('archive')