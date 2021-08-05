from django.shortcuts import render
from .forms import BungoTest

# Create your views here.
def index(request):
    params = {
        'title':'文豪性格診断',
        'description':'当サイトは、簡単な問題に答えてもらうことで、あなたに似ている性格の文豪が分かる文豪性格診断を提供しています。',
        'bungoexample':'太宰治、芥川龍之介、夏目漱石、志賀直也、谷崎潤一郎等...',
        'link':'test',
        'link2':'list_bungo',
    }
    return render(request, 'web/base.html',params)

def list_bungo(request):
    params = {
        'dazai':'太宰治:破産型タイプ',
        'akutagawa':'芥川龍之介:繊細タイプ',
        'natume':'夏目漱石:権威タイプ',
        'ougai':'森鷗外:博学タイプ',
        'itiyou':'樋口一葉:天才タイプ',
        'siga':'志賀直也:金持ちタイプ',
        'saneatu':'武者小路実篤:愚直タイプ',
        'tanizaki':'谷崎潤一郎:変態タイプ',
        'kahuu':'永井荷風:性欲タイプ',
        'simada':'島田清次郎:刹那タイプ',
        'kikuti':'菊池寛:ビジネスタイプ',
        'kazii':'梶井基次郎:センスタイプ',
        'kouyou':'尾崎紅葉:親分タイプ',
        'bizan':'川上眉山:無冠の天才タイプ',
        'isizaka':'石坂洋次郎:常識人タイプ'
    }
    return render(request, 'web/list_bungo.html', params)

def detail(request, write):
    return render(request, 'web/detail.html')

def test(request):
    params = {
        'title':'診断ページ',
        'ques1':'問題1:お酒はどれぐらい飲みますか？',
        'ques2':'問題2:お酒のことをどう思いますか？',
        'ques3':'問題3:読書がどれぐらい好きで、どのような本を読みますか？',
        'ques4':'問題4:今まで「「私」とは何か？」と、自問したことはどれぐらいありましたか？',
        'ques5':'問題5:ずばり、あなたは文学が好きですか？',
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
    # msg2 = request.POST['say']
    params = {
        # 'msg2':msg2,
        'ques1':request.POST['ques1'],
        'ques2':request.POST['ques2'],
        'ques3':request.POST['ques3'],
        'ques4':request.POST['ques4'],
        'ques5':request.POST['ques5'],
        'ques_sum':int(request.POST['ques1']) + int(request.POST['ques2']) + int(request.POST['ques3']) + int(request.POST['ques4']) + int(request.POST['ques5'])
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
