from django.urls import path
from.import views


urlpatterns = [
    path('', views.index,name='index'),
    path('Blog/create/', views.create,name='create'),
    path('Blog/create/createDado/', views.createDado,name='createDado'),
    path('deletar/<int:id>', views.deletar,name='deletar'),
    path('update/<int:id>', views.update,name='update'),
    path('update/updateDado/<int:id>', views.updateDado,name='updateDado'),
]
