from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home, name="dental"),
    path("about",views.about, name="about"),
    path("service",views.service, name="service"),
    path("contact",views.contact, name="contact"),
    path("blog",views.blog, name="blog"),
    path("price",views.price, name="price"),
    path("detail",views.detail, name="detail"),
    path("feature",views.feature, name="feature"),
    path("quote",views.quote, name="quote"),
    path("team",views.team, name="team"),
    path("testimonial",views.testimonial, name="testimonial"),
    path("loginUser",views.loginUser, name="loginUser"),
    path("logoutUser",views.logoutUser, name="logoutUser"),
]
