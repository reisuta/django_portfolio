from django.shortcuts import render
from .forms import BungoTest

# Create your views here.
def index(request):
    params = {
        'title':'文豪性格診断',
        'description':'当サイトは、簡単な問題に答えてもらうことで、あなたに似ている性格の文豪が分かる文豪性格診断を提供しています。',
        'bungoexample':'太宰治、芥川龍之介、夏目漱石、志賀直也、谷崎潤一郎等...',
        'link':'test'
    }
    return render(request, 'web/base.html',params)

def detail(request, write):
    return render(request, 'web/detail.html')

def test(request):
    params = {
        'title':'診断ページ',
        'questionnumber':'問題',
        'placeholderdes':'次の選択肢の中から一つ選んでください。',
        'message':'message',
        'forms':BungoTest(),
        'link':'test_result',
    }
    if request.method=='POST':
        params['message']=request.post['ques1']
        params['forms'] =BungoTest(request.POST)
    return render(request, 'web/test.html', params)


def test_result(request):
    msg2 = request.POST['say']
    params = {
        'msg2':msg2,
        'ques1':request.POST['ques1'],
    }
    # params = {
    #     # 'msg2':msg2
    #     'message':'message',
    #     'forms':BungoTest(),
    # }
    # if request.method=='POST':
    #     params['message']=request.post['ques1']
    #     params['forms'] =BungoTest(request.POST)
    return render(request, 'web/test_result.html',params)
