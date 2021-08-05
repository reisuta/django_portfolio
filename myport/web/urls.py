from django.urls import path
from . import views
from django.conf.urls.static import static # ← これ追加
from django.conf import settings 

urlpatterns = [
    path('',views.index, name='index'),
    path('test/',views.test, name='test'),
    path('list_bungo/',views.list_bungo, name='list_bungo'),
    path('<int:write>/',views.detail, name='detail'),
    path('test/result/',views.test_result, name='test_result'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)