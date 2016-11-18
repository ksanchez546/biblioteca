from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.book_list),
        url(r'^new/book/$', views.new_book, name='new_book'),
]
