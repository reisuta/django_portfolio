from django.urls import path
from . import views
from django.conf.urls.static import static # ← これ追加
from django.conf import settings 

urlpatterns = [
    path('base',views.base, name=''),
    path('',views.index, name='index'),
    path('test/',views.test, name='test'),
    path('list_bungo/',views.list_bungo, name='list_bungo'),
    path('test/test2/',views.test2, name='test2'),
    path('test/test2/test3/',views.test3a, name='test3a'),
    path('test/test2/test3/',views.test3a, name='test3b'),
    path('test/result/',views.result_3ab, name='result_3ab'),
    path('test/dazai',views.dazai, name='dazai'),
    path('test/natume',views.natume, name='natume'),
    path('test/akutagawa',views.akutagawa, name='akutagawa'),
    path('test/ougai',views.ougai, name='ougai'),
    path('test/itiyou',views.itiyou, name='itiyou'),
    path('test/siga',views.siga, name='siga'),
    path('test/saneatu',views.saneatu, name='saneatu'),
    path('test/tanizaki',views.tanizaki, name='tanizaki'),
    path('test/kahuu',views.kahuu, name='kahuu'),
    path('test/simada',views.simada, name='simada'),
    path('test/kikuti',views.kikuti, name='kikuti'),
    path('test/kazii',views.kazii, name='kazii'),
    path('test/bizan',views.bizan, name='bizan'),
    path('test/kouyou',views.kouyou, name='kouyou'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)