from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Subject, Topic, Note
from .forms import SubjectForm, TopicForm, NoteForm
from .permissions import allowed_users

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    subject_var = Subject.objects.values().all().order_by("-id")
    context = {
        'user' : user,
        'subject' : subject_var,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_panel(request):
    user = request.user
    subject_var = Subject.objects.values().all().order_by("-id")
    context = {
        'user' : user,
        'subject' : subject_var,
    }
    return render(request, 'admin_panel.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SubjectForm
    return render(request, 'add_subject.html', {'form' : form})

@login_required(login_url='login')
def edit_subject(request):
    return render(request, 'edit_subject.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TopicForm
    return render(request, 'add_topic.html', {'form' : form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NoteForm
    return render(request, 'add_note.html', {'form' : form})

@login_required(login_url='login')
def topic_view(request, id):
    subject_obj = get_object_or_404(Subject, id=id)
    topic = Topic.objects.order_by("-id").filter(subject=subject_obj.id, classroom="Y9")
    context = {
        'topic' : topic,
        'subject' : subject_obj
    }
    return render(request, 'topic.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_topic(request, id):
    subject_obj = get_object_or_404(Subject, id=id)
    topic = Topic.objects.order_by("-id").filter(subject=subject_obj.id)
    context = {
        'topic' : topic,
        'subject' : subject_obj
    }
    return render(request, 'admin_topic.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_note(request, id):
    topic_obj = get_object_or_404(Topic, id=id)
    note = Note.objects.order_by("-id").filter(topic=topic_obj.id)
    context = {
        'note' : note,
        'topic': topic_obj
    }
    return render(request, 'admin_note.html', context)

@login_required(login_url='login')
def note_view(request, id):
    topic_obj = get_object_or_404(Topic, id=id)
    note = Note.objects.order_by("-id").filter(topic=topic_obj.id, classroom="Y9")
    context = {
        'note' : note,
        'topic': topic_obj
    }
    return render(request, 'note.html', context)

@login_required(login_url='login')
def privacy_policy(request):
    return render(request, 'pp.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')