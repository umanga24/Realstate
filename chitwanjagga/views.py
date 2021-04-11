from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from chitwanjagga.forms import *
from chitwanjagga.models import *


def sample_view(request):
    return render(request, 'index.html')



class CategoryListView(ListView):
    model = Category
    template_name = 'cj/list_category.html'
    context_object_name = 'categories'

class CategoryAddView(LoginRequiredMixin, CreateView):
    login_url =reverse_lazy('cj:login')
    model = Category
    template_name = 'cj/add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('cj:list_category')

class CategoryEditView(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('cj:login')
    model = Category
    fields ='__all__'
    template_name = 'cj/edit_category.html'
    success_url = reverse_lazy('cj:list_category')

class CategoryDetailsView(DetailView):
    model = Category
    template_name = 'cj/details_category.html'
    context_object_name =  'category'

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('cj:login')
    model = Category
    template_name = 'cj/delete_category.html'
    fields = '__all__'
    success_url =reverse_lazy('cj:list_category')
    context_object_name = 'category'

class locationListView(ListView):
    model = Location
    template_name = 'cj/list_location.html'
    context_object_name = 'locations'

class locationAddView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('cj:login')
    model = Location
    template_name = 'cj/add_location.html'
    fields = '__all__'
    success_url = reverse_lazy('cj:list_location')

class locationEditView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('cj:login')
    model = Location
    template_name = 'cj/edit_location.html'
    fields = '__all__'
    success_url = reverse_lazy('cj:list_location')

class locationDetailsView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('cj:login')
    model = Location
    template_name = 'cj/detail_location.html'
    context_object_name = 'location'

class locationDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('cj:login')
    model = Location
    template_name = 'cj/delete_location.html'
    fields  = '__all__'
    success_url = reverse_lazy('cj:list_location')
    context_object_name = 'location'


class ProductListView(ListView):
    model = Product
    template_name = 'cj/list_product.html'
    context_object_name = 'products'

class ProductAddView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('cj:login')
    model = Product
    template_name = 'cj/add_product.html'
    fields = '__all__'
    success_url = reverse_lazy('cj:list_product')

class ProductEditView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('cj:login')
    model = Product
    template_name = 'cj/edit_product.html'
    fields = '__all__'
    success_url = reverse_lazy('cj:list_product')

class ProductDetailsView(DetailView):
    model = Product
    template_name = 'cj/details_product.html'
    context_object_name = 'product'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('cj:login')
    model = Product
    template_name = 'cj/delete_product.html'
    fields = '__all__'
    success_url = reverse_lazy('cj:list_product')
    context_object_name = 'product'


class LoginUserView(views.View):
    def get(self, request):
        loginform = LoginForm()
        return render(request, 'cj/login.html',{'loginform': loginform})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password )
        if user is None:
            return redirect('cj:login_user')
        else:
            if user.is_active:
                login(request, user=user)
                return redirect('cj:list_product')
            else:
                return redirect('cj:login_user')

class LogOutUserView(views.View):
    def get(self, request):
        logout(request)
        return redirect('home')

