from django.urls import path

from . import views

app_name = "store"
urlpatterns = [
    path('', views.products_all , name='products_all'),
    #<slug:slug> --- datatype:nameof the refer point
    path('book/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail')
]
