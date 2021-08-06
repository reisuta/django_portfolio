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
        'ranpo':'江戸川乱歩:放浪タイプ',
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
    if request.POST['ques1']=='1':
        return render(request, 'web/test_result.html',params)
    return render(request, 'web/test2.html',params)


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

def natume(request):
    params = {
        'description':'夏目漱石タイプは、伝統を重んじ、その博学と勤勉さで、周囲の模範たりうる人徳をお持ちの方です。',
        'citedes':'茫々たる薄墨色の世界を、幾条の銀箭が斜めに走るなかを、ひたぶるに濡れて行くわれを、われならぬ人の姿と思えば、詩にもなる、句にも咏まれる。有体なる己を忘れ尽くして純客観に眼をつくる時、始めてわれは画中の人物として、自然の景物と美しき調和を保つ。',
        'citeauth':'夏目漱石「草枕」',
        'feature':'夏目漱石タイプの特徴',
        'whatauth':'夏目漱石はどんな人？',
        'pdes':'　このタイプの人は、非常に努力家であると同時に、天才肌であるため、周囲の信頼が厚い人であることが多いです。そのため、リーダーであったり、組織を導く立場に向いています。',
        'pdes2':'　一方で、努力を欠かさず、常に最善を探るストイックな性質から、自分が正しいと思い込むことも多く、周囲の意見をあまり聞かなかったり、見当違いな偏見を抱いてしまう場合もあります。',
        'pdes3':'　そのため、このタイプの人は、好かれる人からはとことん好かれるが、嫌われる人からはとことん嫌われる可能性を秘めていると言えるでしょう。',
        'pdes4':'　このタイプの人は、素質が豊富で、そもそもできない人の気持ちを理解していない可能性がありますが、相手の立場になって考えて行動することをより一層心がけると、まさに非の打ち所のない人になれるでしょう。',
        'pdes5':'　総じて夏目漱石タイプは、自分が優秀すぎるが故に独善的になる危険がある人です。',
        'authdes':'　夏目漱石は、「こころ」、「行人」、「草枕」、「吾輩は猫である」などで知られる、明治から大正時代にかけて活躍した作家です。作風の特徴は、内省的で、哲学的なものが多く、日本におけるドストエフスキーと言っても過言ではないほど、日本近代文学で一、二を争う、文豪です。',
        'authdes2':'　夏目漱石と言えば、ロンドン留学で、神経衰弱に悩まされたというエピソードが有名な通り、彼は近代化の闇を同時代でいち早く見抜いた知識人としても知られています。',
        'authdes3':'　また文豪にしては珍しく、女嫌いの傾向が見られ、情欲に溺れるタイプの人ではなく、まさにストイックと評するにふさわしい人でしょう。',
        'authdes4':'　夏目漱石がなぜここまで偉大な作家としてもてはやされているのかというと、やはりその人間洞察の深さとそれを作品に落とし込む圧倒的文章力に敬服する人が多いからでしょう。同時代では、芥川龍之介も彼の門下生として知られており、夏目漱石は、後の有名作家の模範たりうる姿を見せていました。しかし、彼の作家デビューは非常に遅く、30代後半でした。それでも、他の若手作家や大家を押しのけて、文壇のトップに君臨したことから、凄まじい資質を感じさせます。',
    }
    return render(request, 'web/natume.html',params)

def akutagawa(request):
    params = {
        'description':'芥川龍之介タイプは、繊細すぎる神経と鋭利すぎる感性で、新しい解釈を提示する人です。',
        'citedes':'それは僕の一生の中でも最も恐しい経験だつた。――僕はもうこの先を書きつづける力を持つてゐない。かう云ふ気もちの中に生きてゐるのは何とも言はれない苦痛である。誰か僕の眠つてゐるうちにそつと絞め殺してくれるものはないか？',
        'citeauth':'芥川龍之介「歯車」',
        'feature':'芥川龍之介タイプの特徴',
        'whatauth':'芥川龍之介はどんな人？',
        'pdes':'　このタイプの人は、感覚や着眼点が鋭いため、議論で相手の矛盾をいち早く見破ったり、誰も気づかなかった解釈をしたりして、周囲を驚かせることでしょう。そのため、頭の回転の速さが求められる仕事や、既存のものを改良して、新しい作品や解釈を提示するような仕事に向いています。',
        'pdes2':'　一方で、繊細すぎる神経故に、憂鬱になりやすく、孤独耐性が充分ではないため、良き理解者であったり、パートナーのような存在が不可欠です。しかし、このタイプの人々は、周囲から羨まれ、時には敵意を向けられることもあるため、必ずしもそのような理解者を得ることは簡単ではありません。',
        'pdes3':'　そのため、このタイプの人は、孤独を強がらず、積極的に弱みを相手に見せることで、距離を縮められるかもしれません。',
        'pdes4':'　このタイプの人は、本質的には人付き合いが苦手なタイプではないため、良き理解者であったり、親友に対しては心を開くタイプでもあります。ただ、繊細な神経や鋭敏な頭脳で、相手の考えや仕草から、必要以上に思慮し、勝手に疲れてしまうことが多いため、人付き合いに積極的になれなかったりするのです。',
        'pdes5':'　総じて、芥川龍之介タイプは、繊細な神経が良くも悪くも作用している人と言えるでしょう。',
        'authdes':'　芥川龍之介は、「羅生門」、「地獄変」、「河童」、「侏儒の言葉」などで知られる、主に大正時代に活躍した作家です。作風の特徴は、古典の新解釈の体をなすものが多く、いわゆる換骨奪胎による作品が特徴です。この作風は、のちの太宰治にも影響を与えました。また、彼の作品のほとんど全てが短編であり、長編と呼べるような作品は、一つもありません。そのため、文豪としては珍しく作風のバリエーションはやや狭いと言えるかもしれません。芥川龍之介の人間性については、繊細な神経を持ち、勉学に秀でていたため、現代で言う陰キャのようかと思いきや、友達は多く、どちらかというと社交的なタイプのようにも受け取れます。また、かなりのヘビースモーカーとしても知られています。',
        'authdes2':'　世間一般では、沈鬱または悲壮といったイメージが定着していますが、親友菊池寛をはじめとして、多くの友人に恵まれていたため、彼の日記などは、意外にも朗らかな文章が書かれており、悲愴さはそこまで感じさせません。芥川龍之介の特徴は、皮肉を利かせた、鋭い人間観察であり、思わず「はっ」とさせられる作品が多いです。また、アフォリズムも手がけており、フランスのラ・ロシュフコーを彷彿とさせます。',
        'authdes3':'　芥川龍之介は、太宰治のように、自ら進んで相手と衝突しに行くというよりは、一歩引いて達観するという位置にいることが多く、それが彼の皮肉たっぷりの作品をより一層魅力的にしているのかもしれません。',
        'authdes4':'　総じて、芥川龍之介は、繊細な神経を持ちながら、多くの友人を持った、一流の皮肉屋と言えるでしょう。',
    }
    return render(request, 'web/akutagawa.html',params)


def ougai(request):
    params = {
        'description':'森鷗外タイプは、圧倒的知識量と博学さで、その道の権威たりうる素質を持つ方です。',
        'citedes':'その今日でなくなった今日には閲歴がある。それが人生の閲歴、生活の閲歴でなくてはならない筈である。それを書こうと思って久しく徒に過ぎ去る記念に、空虚な数字のみを留めた日記の、新しいペエジを開いたのである。',
        'citeauth':'森鷗外「青年」',
        'feature':'森鷗外タイプの特徴',
        'whatauth':'森鷗外はどんな人？',
        'pdes':'　このタイプの人は、勉強が好きなことが多く、勉学において圧倒的な成績を修めている人が多いです。知的好奇心も強く、文系理系関係なく、あらゆる分野の知識を豊富に持っていることでしょう。そのため、大学教授から、医者、弁護士等、その道を究めた専門家が向いているでしょう。',
        'pdes2':'　一方で、知的好奇心が災いして、妙なこだわりを持っていたり、頻繁に論争を起こしたりと、頭が良すぎる故に、周囲から変わりものと評されることも少なくないかもしれません。',
        'pdes3':'　そのため、このタイプの人は、周りを見下さずに、協調の精神を持って、進んで相手の意見を取り入れるなどすると、非常にバランス感覚のよい稀有な人になることができるでしょう。',
        'pdes4':'　このタイプの人は、バイタリティーにあふれることも多く、粘り強いため、経営者やスポーツ選手にも向いているかもしれません。',
        'pdes5':'　総じて、森鷗外タイプは、圧倒的博学によって、自信に満ちていますが、高慢さが生じてしまう点が惜しい人です。',
        'authdes':'　森鷗外は、「舞姫」、「青年」、「阿部一族」、「山椒大夫」などで知られる、主に明治から大正時代に活躍した作家です。作風の特徴は、歴史小説から、芥川龍之介のような換骨奪胎スタイル、恋愛小説まで、非常に幅広いです。また、漢文や詩歌にも秀で、陸軍軍医としての顔も合わせもつことから、まさに多才と評するにふさわしく、文系理系の垣根を感じさせない人です。',
        'authdes2':'　森鷗外といえば、「舞姫」が有名ですが、この話は実話をもとにしていると言われており、実際に森鷗外はドイツ留学で出会った女性を捨てたクソ男としての評判も確立しています。まあ、文豪の中では、まだまだかわいい方だと、私は思いますけどね、、、。',
        'authdes3':'　森鷗外の特徴は、やはりその圧倒的博学にあり、医者としてはもちろん、ドイツ語、フランス語、漢文、文学、詩歌と、あらゆるものに精通しており、歴史的に見ても、その博学度は、トップクラスと言えるかもしれません。',
        'authdes4':'　言うまでもなく、彼は頭が良かったため、一部の作品では、必ずしも読者目線で書かれていないものもあり、特に一部の歴史小説は、彼の博学度合いが分かるものでしかないような作品もあります(個人の感想です)。そのため、森鷗外は、他の文豪に比べて、良くも悪くもキャッチーな作品が少ない作家と言えます。',
    }
    return render(request, 'web/ougai.html',params)


def itiyou(request):
    params = {
        'description':'樋口一葉タイプは、幼少期から才能に恵まれ、早熟で野心にあふれる人です。',
        'citedes':'雪子が繰かへす言の葉は昨日も今日も昨一日をとゝひも、三月の以前も其前も、更に異なる事をば言はざりき、唇に絶えぬは植村といふ名、ゆるし給へと言ふ言葉、學校といひ、手紙といひ、我罪、おあとから行まする、戀しき君、さる詞をば次第なく並べて、身は此處に心はもぬけのからに成りたれば、人の言へるは聞分るよしも無く、樂しげに笑ふは無心の昔しを夢みてなるべく、胸を抱きて苦悶するは遣るかた無かりし當時のさまの再び現にあらはるゝなるべし。',
        'citeauth':'樋口一葉「うつせみ」',
        'feature':'樋口一葉タイプの特徴',
        'whatauth':'樋口一葉はどんな人？',
        'pdes':'　このタイプの人は、何らかの分野において圧倒的な才能に恵まれていることが多く、誰にも真似できない唯一のスタイルを持っている場合が多いです。',
        'pdes2':'　一方で、経済的には恵まれなかったり、友人には恵まれなかったりと、才能以外の点で、何らかの不足を味わっているため、野心が強く、上に立ちたいという思いは人一倍強いと言えるでしょう。',
        'pdes3':'　そのため、しばしば生意気と言われたり、低レベルのいじめの標的にされがちですが、このタイプの人は、反骨心が強く、簡単には屈しないため、そういった相手にも果敢に立ち向かっていくでしょう。',
        'pdes4':'　才能があるのは確かですが、時期によってその才能が世の中に受け入れられず、または時代がこのタイプの人の才能を理解することができず、不遇を味わうこともあるかもしれません。',
        'pdes5':'　平穏な人生を送りたいのであれば、あえて才能を生かさない道に進むというのもありかもしれません。樋口一葉タイプの人は、その才能ゆえ、波乱万丈の人生を送ることが多いでしょう。',
        'authdes':'　樋口一葉は、「たけくらべ」、「にごりえ」、「闇桜」、「十三夜」などで知られる、明治時代に活躍した作家です。作風の特徴は、女の悲しみを描いたものが多く、ほぼすべての作品のテーマが恋愛でありながら、そのほとんどが悲恋であり、悲愴なものが多いです。',
        'authdes2':'　樋口一葉といえば、結核で夭折したことで知られており、わずか、二四才でこの世を去りました。その一生は、苦労の一生でもあり、貧困の中、作品を執筆し、死ぬ直前、次々と佳作を発表したことから、天才作家と評されるようになりました。',
        'authdes3':'　文豪のほとんどが男性である中、女性の文豪は大変貴重であると同時に、その作風は女性ならではの視点と、女性にしか描けない女の姿を克明に描写しているため、その文学的価値は高く、文才の点で、一、二を争う作家と言えるかもしれません。',
        'authdes4':'　彼女は、師匠でもある半井桃水と恋愛関係にあったのではないか？と長らく研究されていましたが、真偽はいまだによくわかりません。しかし、一葉が桃水に恋愛感情を抱いていたことは確かで、作品にも恋する女性の姿が描かれています。',
    }
    return render(request, 'web/itiyou.html',params)