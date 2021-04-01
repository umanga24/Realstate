from django.urls import path
from chitwanjagga import views

app_name = 'cj'

urlpatterns = [

    path('list_category/', views.CategoryListView.as_view(), name= 'list_category'),
    path('add_category/',  views.CategoryAddView.as_view(), name='add_category'),
    path('edit_category/<int:pk>', views.CategoryEditView.as_view(), name='edit_category'),
    path('delete_category/<int:pk>', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('details_category/<int:pk>', views.CategoryDetailsView.as_view(), name='details_category'),


    path('list_location/', views.locationListView.as_view(), name='list_location'),
    path('add_location/',  views.locationAddView.as_view(), name='add_category'),
    path('edit_location/<int:pk>', views.locationEditView.as_view(), name='edit_location'),
    path('delete_location/<int:pk>', views.locationDeleteView.as_view(), name='delete_location'),
    path('details_location/<int:pk>', views.locationDetailsView.as_view(), name='details_location'),


    path('list_product/', views.ProductListView.as_view(), name='list_product'),
    path('add_product/', views.ProductAddView.as_view(), name='add_product'),
    path('edit_product/<int:pk>', views.ProductEditView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('details_product/<int:pk>', views.ProductDetailsView.as_view(), name='details_product'),

    path('login/', views.LoginUserView.as_view(), name = 'login'),
    path('logout/', views.LogOutUserView.as_view(), name = 'logout'),


]