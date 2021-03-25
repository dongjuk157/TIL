from django.urls import path
from . import views

app_name= 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comment/', views.comment, name='comment'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),

]
