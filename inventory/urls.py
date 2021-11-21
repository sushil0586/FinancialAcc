from django.urls import path
from inventory import views


app_name = 'inventory'

urlpatterns  = [

    path('createProduct',views.CreateTodoApiView.as_view(), name = 'product1'),
    path('ListProduct',views.ListproductApiView.as_view(), name = 'listproduct'),
    path('product',views.productApiView.as_view(), name = 'product'),
    path('<int:id>',views.productupdatedel.as_view(), name = 'product2'),
   
]