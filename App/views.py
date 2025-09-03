from django.shortcuts import redirect, render
from django.db.models import Count
from .models import *

# Create your views here.

def home(request):

    if 'user_id' not in request.session:
        print("User not logged in, redirecting to login page")
        return redirect('login')
    
    print("User is logged in with user_id:", request.session['user_id'])

    # verificar o poprque nao ta filtrando
    Status_id = request.POST.get('status', 0)

    print("Filtering tasks with Status_id:", Status_id)

    user = User.objects.get(id=request.session['user_id'])

    if Status_id != "0":
        tasks = Task.objects.filter(user=user, status__id=Status_id).all()
    else:
        tasks = Task.objects.filter(user=user).all()
    
    task_status = Status.objects.all()

    context = {
        "current_user": User,
        "user_tasks": tasks,
        "task_status": task_status
    }

    return render(request, 'home.html', context)

def dashboard(request):
    if 'user_id' not in request.session:
        print("User not logged in, redirecting to login page")
        return redirect('login')
    
    # Filtros do dashboard
    status_filter = request.POST.get('status', '0') if request.method == 'POST' else '0'
    user_filter = request.POST.get('user', '0') if request.method == 'POST' else '0'
    
    # Buscar todas as tarefas com filtros aplicados
    all_tasks = Task.objects.all()
    
    if status_filter != '0':
        all_tasks = all_tasks.filter(status__id=status_filter)
    
    if user_filter != '0':
        all_tasks = all_tasks.filter(user__id=user_filter)
    
    # Estatísticas gerais
    total_tasks = Task.objects.count()
    total_users = User.objects.count()
    
    # Estatísticas por status
    status_stats = Task.objects.values('status__name').annotate(count=Count('id')).order_by('status__name')
    
    # Estatísticas por usuário
    user_stats = Task.objects.values('user__username').annotate(count=Count('id')).order_by('-count')
    
    # Buscar todos os status e usuários para os filtros
    all_status = Status.objects.all()
    all_users = User.objects.all()
    
    # Usuario logado atual
    current_user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'all_tasks': all_tasks,
        'total_tasks': total_tasks,
        'total_users': total_users,
        'status_stats': status_stats,
        'user_stats': user_stats,
        'all_status': all_status,
        'all_users': all_users,
        'current_user': current_user,
        'selected_status': status_filter,
        'selected_user': user_filter,
    }
    
    return render(request, 'dashboard.html', context)

def signup(request):

    if request.method == 'POST':
    
        username = request.POST.get('username')
        password = request.POST.get('password')

        user, created = User.objects.get_or_create(username=username, password=password)

        if created:
            print("User created:", user.username)
        else:
            print("User already exists:", user.username)
            return redirect('login')

    context = {
        'pagename': 'Register',
        'loginPage': False,
    }

    return render(request, 'register.html', context)

def login(request):
    print("Login function called")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            print("Login successful for user:", user.username)
            request.session['user_id'] = user.id
            return redirect('home')
        except User.DoesNotExist:
            print("Login failed: Invalid username or password")
            return redirect('signup')

    context = {
        'pagename': 'Login',
        'loginPage': True,
    }

    return render(request, 'login.html', context)

def logout(request):
    request.session.pop('user_id', None)
    print("user logged out")
    return redirect('login')

def newTask(request):
    if 'user_id' not in request.session:
        print("User not logged in, redirecting to login page")
        return redirect('login')
    
    task_status = Status.objects.all()
    task_users = User.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        status = Status.objects.get(id=request.POST.get('status'))
        description = request.POST.get('description')
        user = User.objects.get(id=request.POST.get('user'))

        task, create = Task.objects.get_or_create(title=title, status=status, description=description, user=user)

        if not create:
            print("Task already exists:", task.title)
            return redirect('newtask')

        print("New task created:", task.title)

        return redirect('home')

    context = {
        'task_status': task_status,
        'newTaskPage': True,
        'task_users': task_users
    }

    return render(request, 'Task.html', context)

def deleteTask(request, task_id):
    if 'user_id' not in request.session:
        print("User not logged in, redirecting to login page")
        return redirect('login')

    try:
        Task.objects.get(id=task_id, user__id=request.session['user_id']).delete()
        print("Task deleted")
    except Task.DoesNotExist:
        print("Task not found or does not belong to the user")

    return redirect('home')

def editTask(request, task_id):
    if 'user_id' not in request.session:
        print("User not logged in, redirecting to login page")
        return redirect('login')

    task_status = Status.objects.all()
    task_users = User.objects.all()

    try:
        task = Task.objects.get(id=task_id, user__id=request.session['user_id'])
    except Task.DoesNotExist:
        print("Task not found or does not belong to the user")
        return redirect('home')

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.status = Status.objects.get(id=request.POST.get('status'))
        task.user = User.objects.get(id=request.POST.get('user'))
        task.description = request.POST.get('description')
        task.save()
        print("Task updated:", task.title)
        return redirect('home')

    context = {
        'task': task,
        'task_status': task_status,
        'newTaskPage': False,
        'task_users': task_users
    }

    return render(request, 'Task.html', context)