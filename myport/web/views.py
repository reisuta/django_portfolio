from django.shortcuts import render
from .forms import BungoTest

# Create your views here.
def base(request):
    return render(request, 'web/base.html')
    
def index(request):
    params = {
        'title':'文豪性格診断',
        'description':'当サイトは、簡単な問題に答えてもらうことで、あなたに似ている性格の文豪が分かる文豪性格診断を提供しています。',
        'bungoexample':'太宰治、芥川龍之介、夏目漱石、志賀直也、谷崎潤一郎等...',
        'link':'test',
        'link2':'list_bungo',
    }
    return render(request, 'web/index.html',params)

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
        'isizaka':'石坂洋次郎:常識人タイプ',
        'description':'このページでは、診断結果で表示される文豪一覧を見ることができます。',
        'description2':'性格の詳細は、それぞれの文豪名をクリックすることによって、詳細ページに移行できます。',
    }
    return render(request, 'web/list_bungo.html', params)

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



def dazai(request):
    params = {
        'description':'太宰治タイプは、他人にはない独特の感性と、気に入ったものをとことん追求する強い探究心をお持ちの方です。',
        'citedes':'この世では、きっと、あなたが正しくて、私こそ間違っているのだろうとも思いますが、私には、どこが、どんなに間違っているのか、どうしても、わかりません。',
        'citeauth':'太宰治「きりぎりす」',
        'feature':'太宰治タイプの特徴',
        'whatauth':'太宰治はどんな人？',
        'pdes':'　このタイプの人は、良くも悪くも周囲の人々とは違う独特の感性であったり、考え方をする場合が多いです。そのため、創造的な仕事であったり、芸術分野においては、強みを発揮できるでしょう。また、一つのことに没頭する探究心も素晴らしいため、未だ成し遂げていない偉業を残す可能性を秘めた人々とも言えるでしょう。',
        'pdes2':'　一方で、その独特の感性が周囲の人々と衝突し、周囲の無理解に苦しむこともあるかもしれません。その際、破滅的な道を自ら選んだり、快楽に進むことによって、寂しさを埋めようとしてしまうことがあります。',
        'pdes3':'　そのため、このタイプの人は、自身の独特の感性で、成功を収めるか、世の中に受け入れられず、堕落するかといった究極の二択に悩むこととなるでしょう。',
        'pdes4':'　平穏無事に過ごしたいのであれば、あまり快楽に溺れすぎず、周囲の人々の意見を優先すれば、良いでしょうが、おそらくこのタイプの人々はそういう「普通」の生き方自体を嫌っていることもあるでしょう。',
        'pdes5':'　総じて、太宰治タイプは、例えるなら嵐のような人と言えるでしょう。',
        'authdes':'　太宰治は、「人間失格」、「斜陽」、「走れメロス」、「パンドラの匣」などで知られる、主に昭和時代に活躍した作家です。作風の特徴は、初期と後期が破滅的である一方、中期は比較的穏当であり、しばしば日本昔ばなしやハムレットのような、先人の作品を自分なりに解釈して新しく構成するような作品も目立ちます。「新ハムレット」や「お伽草子」に代表されるこの作風は、尊敬していた先輩芥川龍之介の影響もあることでしょう。太宰治の人間性については、矛盾する二面を持つ人と形容でき、例えば、喧嘩をよくする割に、気が弱かったり、酒を浴びるように飲むくせに酒が嫌いと言ったり、良く言えば、文学的、悪く言えば、面倒くさい人です。',
        'authdes2':'　世間一般では、女と心中したクソ野郎というイメージが定着していますが、変人が当たり前の文豪の世界では、そこまで注目すべき点でもないと私は思います。太宰治の特徴は、一見破滅的でのらりくらりしているようですが、実は非常に勤勉であり、戦争の最中においても、作品を執筆し続けた不屈の作家魂がある人です。悪目立ちしていますが、作品も、人間生活の矛盾ややるせない怒りを実に非常に見事に表現しており、やはりその文学的センスに刮目せざるをえません。',
        'authdes3':'　現代では躁鬱病と言われてもおかしくないように、彼の作品は、明るいものから暗いものから非常にバリエーションに富んでいます。また、月次みな表現でいうと、彼は子供っぽいところも多く、例えば志賀直也と派手な口論をしたり、川端康成に「刺す」という文章を送ったり、何かと話題が尽きません。',
        'authdes4':'　そのため、一概に「太宰治はこういう人！」と表現するのは難しいですが、勤勉さとセンスのみを追求しすぎて、常識を失った人と言えるかもしれません。'
    }
    return render(request, 'web/dazai.html',params)
