# inventory/urls.py
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .models import Accessory, Shoe, String, Racket, Bag, Clothe, Shuttle, Grip

urlpatterns = [
    path('products/', views.product_list, name='product_list'),

    path('add_shoe/', views.add_shoe, name='add_shoe'),
    path('add_accessory/', views.add_accessory, name='add_accessory'),
    path('add_racket/', views.add_racket, name='add_racket'),
    path('add_string/', views.add_string, name='add_string'),
    path('add_clothe/', views.add_clothe, name='add_clothe'),
    path('add_shuttle/', views.add_shuttle, name='add_shuttle'),
    path('add_bag/', views.add_bag, name='add_bag'),

    path('clothe', views.clothe, name='clothe'),
    path('shoe', views.shoe, name='shoe'),
    path('accessory', views.accessory, name='accessory'),
    path('bag', views.bag, name='bag'),
    path('racket', views.racket, name='racket'),
    path('string', views.string, name='string'),
    path('shuttle', views.shuttle, name='shuttle'),

    path('product_update', views.product_update, name='product_update'),
    path('product_update/<str:category>/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product_delete/<str:category>/<int:product_id>/', views.delete_product, name='delete_product'),

    path('add_to_cart/<str:category>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart_item/<str:category>/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove_cart_item/<str:category>/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/', views.cart_detail, name='cart_detail'),

    path('add_to_order/', views.add_to_order, name='add_to_order'),
    path('orders_detail/', views.orders_detail, name='orders_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)