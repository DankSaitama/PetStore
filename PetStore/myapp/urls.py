from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from myapp import views 

urlpatterns = [
    path('base',views.base,name='base'),
    path('register',views.register_page,name="register"),
    path('',views.login_page,name="login"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('dogs',views.dogs_market,name="dogs"),
    path('birds',views.birds_market,name="birds"),
    path('upcoming',views.upcoming,name="upcoming"),
    path('my_orders',views.my_order,name="MyOrders"),
    # path('images',views.image_upload,name='images'),
    path('upload',views.upload_view,name='upload'),
    path('set_cookie',views.set_cookie,name="set_cookie"),
    path('get_cookie',views.get_cookie,name="get_cookie"),
    path('del_cookie',views.del_cookie,name="del_cookie"),
    path('setsession',views.set_session,name="setsession"),
    path('getsession',views.get_session,name="getsession"),
    path('delsession',views.del_session,name="delsession"),
    path('search',views.search_results,name='search_results'),
    path('cartpage/',views.cart_home,name='cartpage'),
    path('updatecart/',views.update_cart,name="updatecart")
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)