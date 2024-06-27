from django.urls import path
from .import views as v


urlpatterns = [
    path('',v.IndexView.as_view(),name='index'),
    path('abouts',v.AboutView.as_view(),name='abouts'),
    path('service',v.ServiceView.as_view(),name='service'),
    path('blog',v.BlogView.as_view(),name='blog'),
    path('blogs/<slug:slug>',v.BlogDetailView.as_view(),name='blog-detail'),
    path('category/<slug:slug>',v.CategoryDetailView.as_view(),name='category-detail'),
    path('search/',v.BlogSearchView.as_view(),name='blog-search'),
    path('contact',v.ContactView.as_view(),name='contact'),
    path('register/',v.registerPage,name='register'),
    path('login/',v.loginPage,name='login'),
    path('logout/',v.logoutUser,name='logout'),

]