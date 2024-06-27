
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Slider, About, Service, Blog, Category
from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm,CreateUserForm,CommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



class BaseView(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()
        context['PBlogs'] = Blog.objects.order_by('-views')[:5]
        context['most_common_tags']=Tag.objects.annotate(num_times=Count('taggit_taggeditem_items')).order_by('-num_times')[:5]

        return context


class IndexView(TemplateView):
    template_name = 'index.html'
    model = Slider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Sliders'] = Slider.objects.all() #select * from Slider mənasını verir
        context['Abouts'] = About.objects.first()
        context['Services'] = Service.objects.all()
        context['Blogs'] = Blog.objects.all()
        return context

class AboutView(ListView):
    template_name = 'about.html'
    context_object_name = 'Abouts'
    queryset = About.objects.first()

class ServiceView(ListView):
    template_name = 'service.html'
    context_object_name = 'Services'
    queryset = Service.objects.all()

class BlogView(BaseView,ListView):
    template_name = 'blog.html'
    context_object_name = 'Blogs'
    queryset = Blog.objects.all()
    paginate_by = 2


class BlogDetailView(BaseView,DetailView):
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'

    def get_object(self,queryset=None):
        obj=super().get_object(queryset=queryset)
        obj.views +=1
        obj.save()
        return obj

class BlogSearchView(BaseView,ListView):
    model = Blog
    template_name = 'blog_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Blog.objects.filter(title__icontains=query)
        return Blog.objects.none()



class CategoryDetailView(BaseView,ListView):
    model = Blog
    template_name = 'category-details.html'
    context_object_name = 'Blogs'

    def get_queryset(self):
        slug=self.kwargs.get('slug')
        category=Category.objects.get(slug=slug)
        return Blog.objects.filter(category=category)

class ContactView(TemplateView):
    template_name = 'contact.html'

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')


        context={'form':form}
        return render(request, 'account/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Username or password is incorrect')

        context={}
        return render(request, 'account/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('index')


class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self,request,*args,**kwargs):
        fullName=request.POST.get('fullName')
        phoneNumber=request.POST.get('phoneNumber')
        email=request.POST.get('email')
        message=request.POST.get('message')

        try:
            send_mail(
                f'{fullName} tərəfindən mesaj',
                f'Mesaj: {message} \n Telefon {phoneNumber} \n Email {email}',
                'gamidovmumin660@gmail.com',
                ['hamidovmumin089@gmail.com'],
                fail_silently=False,
            )
            messages.success(request,'Message sent successfully')
        except Exception as e:
            messages.error(request,f'Something went wrong {e}')

        return HttpResponseRedirect(reverse('contact'))

