from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import InvoiceForm, InvoiceSearchForm, InvoiceUpdateForm, SignUp
from .forms import get_last_invoice_number
from .models import Invoice

deleted = False
updated = False


def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        'title': title
    }
    return render(request, 'home.html', context)


@login_required(redirect_field_name="login")
def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    query = Invoice.objects.order_by('-invoice_number')
    if form.is_valid():
        form.fields['invoice_number'].initial = total_invoices + 1
        form.save()
        messages.success(request=request, message='Form saved successfully!')
        return redirect('/add_invoice')

    context = {
        'form': form,
        'query': query,
        'total_invoices': total_invoices,
        'title': "New Invoice",
    }
    return render(request, "entry.html", context)


@login_required(redirect_field_name="login")
def show_invoices(request):
    title = 'List of Invoices'
    queryset = Invoice.objects.all().order_by('-invoice_number')
    form = InvoiceSearchForm(request.POST or None)
    global deleted
    global updated

    context = {
        'title': title,
        'queryset': queryset,
        'form': form,
        'updated': updated,
        'deleted': deleted,
    }

    if request.method == 'POST':
        if 'reset' in request.POST:
            queryset = Invoice.objects.all().order_by("-invoice_number")
            return redirect("/show_invoices")
        else:
            invoice_number = form["invoice_number"].value()
            name = form["name"].value()
            queryset = Invoice.objects.filter(
                name__icontains=name,
                invoice_number__contains=invoice_number
            )

        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
            "updated": updated,
            "deleted": deleted,
        }

    updated = False
    deleted = False
    return render(request, "invoices.html", context)


@login_required()
def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            global updated
            updated = True
            return redirect('/show_invoices')

    return render(request, 'edit.html', {'form': form})


@login_required()
def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        global deleted
        deleted = True
        return redirect('/show_invoices')
    return render(request, 'delete_invoice.html')


def signup(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = SignUp(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                password_b = form.cleaned_data.get("password2")
                email = form.cleaned_data.get("email")
                if password == password_b:
                    form.save()
                    new_user = authenticate(username=username, password=password)
                    if new_user is not None:
                        login(request, new_user)
                        return redirect('/')
            else:
                password = form.cleaned_data.get("password1")
                password_b = form.cleaned_data.get("password2")
                if password != password_b:
                    messages.success(request, ("Your passwords don't match!"))
    else:
        return redirect('/')

    form = SignUp()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


@login_required()
def logout_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("/")
    return render(request, "logout.html")


def login_user(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                msg = """There was an <span class="errorText">error</span> logging you in!<br>
                Please try again!
                """
                messages.success(request, mark_safe(msg))
                return redirect('login')
        else:
            return render(request, 'login.html')
    else:
        return redirect("/")
