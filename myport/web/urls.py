from django.urls import path
from . import views
from django.conf.urls.static import static # ← これ追加
from django.conf import settings 

urlpatterns = [
    path('base',views.base, name=''),
    path('',views.index, name='index'),
    path('test/',views.test, name='test'),
    path('list_bungo/',views.list_bungo, name='list_bungo'),
    path('test/result/',views.test_result, name='test_result'),
    path('test/dazai',views.dazai, name='dazai'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)