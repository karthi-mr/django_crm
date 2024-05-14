from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from webapp.forms import CreateUserForm, LoginForm, RecordForm
from webapp.models import Record


# ? home
def home(request):
    return render(request, 'webapp/index.html', {})


# * ------------------------------------------ xxx AUTH xxx ----------------------------------------------------------
# ? register
def register_user(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'webapp/register.html', {'form': form})

# ? login
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username: str = request.POST['username']
            password: str = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('dashboard')
    return render(request, 'webapp/my-login.html', {'form': form})

# ? logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect('login')

# * ------------------------------------------ xxx AUTH xxx ----------------------------------------------------------

# ? dashboard
@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()
    return render(request, 'webapp/dashboard.html', context = {'records': my_records})

# ? create a record
@login_required(login_url='login')
def create_record(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record created successfully!")
            return redirect('dashboard')
    return render(request, 'webapp/create-record.html', context = {'form': form})

# ? update a record
@login_required(login_url='login')
def update_record(request, pk: int | None=None):
    record = get_object_or_404(Record, pk=pk)
    form = RecordForm(instance=record)
    if request.method == 'POST':
        form = RecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('dashboard')
    return render(request, 'webapp/update-record.html', context = {'form': form, 'record': record})
    
# ? read a record
@login_required(login_url='login')
def view_record(request, pk: int | None=None):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'webapp/view-record.html', context = {'record': record})

# ? delete a record
@login_required(login_url='login')
def delete_record(request, pk: int | None=None):
    record = get_object_or_404(Record, pk=pk)
    record.delete()
    messages.success(request, "Record deleted successfully!")
    return redirect('dashboard')
