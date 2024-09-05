"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp.views import main, my_feed, article_id, article_id_comment, article_id_update, article_id_delete, create, topics, topics_topic_id, topics_topic_id_subscribe, topics_topic_id_unsubscribe, profile, register, set_password, login, logout, year_month


urlpatterns = [
    path('', main),
    path('my-feed/', my_feed),
    path('<int:article_id>/', article_id),
    path('<int:article_id>/comment/', article_id_comment),
    path('<int:article_id>/update/', article_id_update),
    path('<int:article_id>/delete/', article_id_delete),
    path('create/', create),
    path('topics/', topics),
    path('topics/<int:topic_id>/', topics_topic_id),
    path('topics/<int:topic_id>/subscribe/', topics_topic_id_subscribe),
    path('topics/<int:topic_id>/unsubscribe/', topics_topic_id_unsubscribe),
    path('profile/', profile),
    path('register', register),
    path('set-password', set_password),
    path('login', login),
    path('logout', logout),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', year_month),
    path('admin/', admin.site.urls),
]
