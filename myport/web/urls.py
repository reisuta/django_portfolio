from django.urls import path
from . import views
from django.conf.urls.static import static # ← これ追加
from django.conf import settings 

urlpatterns = [
    path('',views.index, name='index'),
    path('test.html',views.test, name='test'),
    path('<int:write>/',views.detail, name='detail')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)