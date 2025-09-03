from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, AddressForm
from store.models import Customer, Address


def register(request):
    """User registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create customer profile
            Customer.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('store:home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('store:home')


@login_required
def profile(request):
    """User profile page"""
    customer = request.user.customer
    addresses = Address.objects.filter(customer=customer)
    
    if request.method == 'POST':
        # Handle profile update
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()
        
        customer.phone = request.POST.get('phone', customer.phone)
        customer.date_of_birth = request.POST.get('date_of_birth', customer.date_of_birth)
        customer.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('accounts:profile')
    
    return render(request, 'accounts/profile.html', {
        'customer': customer,
        'addresses': addresses
    })


@login_required
def add_address(request):
    """Add new address"""
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.customer = request.user.customer
            address.save()
            messages.success(request, 'Address added successfully!')
            return redirect('accounts:profile')
    else:
        form = AddressForm()
    
    return render(request, 'accounts/add_address.html', {'form': form})


@login_required
def edit_address(request, address_id):
    """Edit address"""
    address = Address.objects.get(id=address_id, customer=request.user.customer)
    
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully!')
            return redirect('accounts:profile')
    else:
        form = AddressForm(instance=address)
    
    return render(request, 'accounts/edit_address.html', {'form': form, 'address': address})


@login_required
def delete_address(request, address_id):
    """Delete address"""
    address = Address.objects.get(id=address_id, customer=request.user.customer)
    address.delete()
    messages.success(request, 'Address deleted successfully!')
    return redirect('accounts:profile')

