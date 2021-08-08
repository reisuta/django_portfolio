from django import forms
from django.forms.fields import ChoiceField

val = (
    ('5','お酒は飲まない。そして酒に興味もない。酒を飲んでも堕落するだけだ'),
    ('0','お酒は週1、2回程度飲む。お酒にあまり強くないため、付き合いでちょっと飲む程度。'),
    ('0','ほとんど毎日飲む。好きな酒のこだわりはなく、手持ち無沙汰で飲んでいる。お酒を飲める人はかっこいいと思う。'),
    ('5','毎日飲まなきゃやってらんない。酒の味が大好きで、仲間と飲むのが楽しいから毎日飲む。'),
    ('5','毎日飲まなきゃやってらんない。たいてい一人で飲む。そして本当は酒はあまり好きじゃない')
)

val2 = (
    ('5','みな機会において平等であるべきだ。そして、実力があるものこそ上に立つべきだ。'),
    ('0','明るく社交的な人物は優秀であり、暗く内向的な人物は劣等である。'),
    ('0','とにかく分かりやすく役に立ちそうなものを使えばいい。細かいことは考える必要はない。'),
    ('5','何が正しいかなんてわからない。そのため何事も研究が欠かせない。'),
    ('10','え？共感できる思想？それが選べるなら、哲学や文学なんて学問は何のために存在するのさ？')

)

val3 = (
    ('0','非常識にならないためにも、遵守すべき規範であり、絶対に守らなければならないと思う。'),
    ('0','常識がないやつは、変なやつだと思うので、私は嫌いだ。なお私は常識人です。'),
    ('5','常識の定義がいまいちわからないので、答えかねます。'),
    ('10','「世間の常識では」と説教する人が言う、「常識」は、その人の主観でしかないと思う。'),
    ('10','常識が正しいと信じ込むのは、思考停止だと思う。')

)

val4 = (
    ('0','一度もない。'),
    ('5','幼少期に一度あったかもしれない。'),
    ('5','私自身は一度もないが、その問いに悩む人の気持ちはわからなくもない'),
    ('10','青年時代、この問いについて真剣に考えたことがある。'),
    ('10','生まれてこのかた、この問いから目を反らすことができないでいる。')

)

val5 = (
    ('0','自己啓発、ビジネス書などの、ノウハウが書かれており、すぐに役立ちそうなもの'),
    ('5','大衆小説や、漫画など、娯楽や暇つぶしに適している本'),
    ('10','純文学や哲学書、専門書、学術書といった、自分なりに噛み砕いて考える必要がある本。')

)


class BungoTest(forms.Form):
    ques1 = forms.ChoiceField(choices=val,label='問題1')
    ques2 = forms.ChoiceField(choices=val2,label='問題2')
    ques3 = forms.ChoiceField(choices=val3,label='問題3')
    ques4 = forms.ChoiceField(choices=val4,label='問題4')
    ques5 = forms.ChoiceField(choices=val5,label='問題5')


class Test2_a(forms.Form):
    test2_val = (
        ('10','チームで役割分担をし、自ら先頭に立って、みなに指示を出して仕事を進めていく。'),
        ('0','誰の力も借りず一人で黙々と進める。またはそのようにして仕事をしたい。'),
        ('5','自ら先頭に立つことは少ないが、周囲の人と協力して、チームで仕事を進める。'),
        ('0','チームで仕事をするのは正直煩わしい。一人で自由にやりたい。'),
        ('10','リーダーとして、部下に指示を出し、仕事を進めていく。')
        )
    test2_val2 = (
        ('0','早く仕事をしても遅く仕事をしても給料は同じなので、のんびりだらだら進めたい。'),
        ('10','少しでも早く仕事をした方が自身の成長につながるので、可能な限りスピーディーに進めたい。'),
        ('5','早くも遅くもない、その人に合った適切なペースで仕事を進めるべきである。'),
        ('10','だらだら仕事をしても生産性が上がらないので、テキパキ進めたい。'),
        ('0','早く仕事をしてしまったら、次の仕事が来てしまい面倒だから、できるだけだらだら進める。')
    )
    test2_val3 = (
        ('0','相手の都合を聞き、手が空いている際に、単刀直入に伝える。'),
        ('-3','相手の都合など無視して、相手を呼び出して、一方的に伝える。'),
        ('0', '正直、緊張するため、どうしようか悩む'),
        ('0','論争になってでも、自分の意見を貫く'),
        ('0','相手にどう思われるか気になるため、伝えるか悩む')
    )
    test2_val4 = (
        ('-4','恋愛がしたい'),
        ('0','静かな場所でのんびり暮らしたい'),
        ('0','ビジネスマンとして働き続けたい'),
        ('-3','異性に囲まれたい。'),
        ('−4','老いることほど醜悪なことはないので、老いる前に自殺するつもりだ。')
    )
    test2_val5 = (
        ('0','変な本だと思う。'),
        ('0','タイトルが漠然としていて、何を言いたいのか想像がつかない。もっとわかりやすいタイトルにするべきである。'),
        ('-3','わかりやすいタイトルだ。平和な日常というものは、時として「悲愴」に満ちているからである。'),
    )
    ques1 = forms.ChoiceField(choices=test2_val,label='問題1')
    ques2 = forms.ChoiceField(choices=test2_val2,label='問題2')
    ques3 = forms.ChoiceField(choices=test2_val3,label='問題3')
    ques4 = forms.ChoiceField(choices=test2_val4,label='問題4')
    ques5 = forms.ChoiceField(choices=test2_val5,label='問題5')


class Test2_b(forms.Form):
    test2_val = (
        ('3','思わない。けれども、周囲から変わり者と言われることが多い。'),
        ('0','変わり者だと思う。けれどもこれは強みであり、持ち味だと思う。'),
        ('2','そもそも「変わり者」の定義とは？'),
        ('0','思わない。周囲からも変わり者と言われたことがない。'),
        ('-4','思う。なぜなら他人にはない個性と、斬新な考え方をしている自信があるから。')
        )
    test2_val2 = (
        ('−4','無能な部下や上司'),
        ('2','自分自身の耐えられない醜さ'),
        ('0','トマト'),
        ('-5','自分でコントロールできないもの'),
        ('2','月並みな人')
    )
    test2_val3 = (
        ('3','自分自身の存在の謎'),
        ('-3','どうしたら年収を上げられるか'),
        ('0', '今日の晩ごはん'),
        ('3','仕事'),
        ('0','恋愛')
    )
    test2_val4 = (
        ('0','そもそも初めて聞いた言葉なんですけど'),
        ('0','なんでネガティブな言葉ばっかり並んでいるの？'),
        ('3','文学的な言葉だと思う。美しく高等な言葉だと思う。'),
        ('0','え、何自殺するの？(笑)'),
        ('−3','表現が一般的ではないため、あまり積極的に使用するべき言葉ではないと思う。')
    )
    test2_val5 = (
        ('2','酒'),
        ('0','家族や友人'),
        ('-3','自分'),
    )
    ques1 = forms.ChoiceField(choices=test2_val,label='問題1')
    ques2 = forms.ChoiceField(choices=test2_val2,label='問題2')
    ques3 = forms.ChoiceField(choices=test2_val3,label='問題3')
    ques4 = forms.ChoiceField(choices=test2_val4,label='問題4')
    ques5 = forms.ChoiceField(choices=test2_val5,label='問題5')

class Test3a_a(forms.Form):
    test3_val = (
        ('0','あんまり得意ではないが、勉強自体は苦ではない。'),
        ('0','勉強は嫌いである。'),
        ('2','得意である。大抵の人には負けない自信がある。'),
        ('4','勉強は趣味なので、得意だ。'),
        ('0','得意でも苦手でもない')
        )
    test3_val2 = (
        ('0','上司から言われたことをそのままこなす。'),
        ('2','上司に積極的に提案をし、最善の結果が出せるよう、工夫して仕事を進める。'),
        ('0','まじめに働いても、適当に働いても、もらえる給料は同じなので、適当にやる'),
        ('1','計画をあらかじめたて、それを遂行する。'),
        ('2','将来的に起業したいので、ノウハウを全力で盗む')
    )
    test3_val3 = (
        ('3','少年時代は、ガキ大将だったので、強いと思う。'),
        ('3','子分がいるから、強いと思う。'),
        ('0', '弱い。そもそも殴り合いの喧嘩をしたことがない。'),
        ('0','口喧嘩なら弱くはないと思う。'),
        ('0','喧嘩をするのは下等な人間だから、自分とは無関係だ。')
    )
    test3_val4 = (
        ('3','たくさん欲しい。崇拝されたい。'),
        ('0','群れるのは嫌いなので、いらない。'),
        ('0','有能な部下はほしい。無能な部下はいらない。'),
        ('0','信頼できる部下が2、3人ほしい'),
        ('0','一人で仕事を進めたいので、どちらかというとあまりほしくない。')
    )
    test3_val5 = (
        ('3','正直すぎて、愚直と言われることもある。性格的に嘘がつけない。'),
        ('0','社交辞令のような嘘や、付き合いで必要な嘘はつく。'),
        ('0','嘘でいままでのし上がってきた。一流の詐欺師の自信がある。'),
    )
    ques1 = forms.ChoiceField(choices=test3_val,label='問題1')
    ques2 = forms.ChoiceField(choices=test3_val2,label='問題2')
    ques3 = forms.ChoiceField(choices=test3_val3,label='問題3')
    ques4 = forms.ChoiceField(choices=test3_val4,label='問題4')
    ques5 = forms.ChoiceField(choices=test3_val5,label='問題5')

class Test3a_b(forms.Form):
    test3_val = (
        ('10','20人以上'),
        ('3','10人程度'),
        ('0','5人程度'),
        ('0','1人以上5人以下'),
        ('0','0人')
        )
    test3_val2 = (
        ('0','ありきたりというより、それが当たり前だと思う。'),
        ('3','正直飽きてきた'),
        ('0','まさにありきたりだと思う。'),
        ('0','恋愛関係にもいろいろあるので、ありきたりかどうかは簡単には判断できないと思う。'),
        ('5','私にとって「ありきたりな恋愛」は、人間の男女間ではない。')
    )
    test3_val3 = (
        ('3','自分も昔苦手だったけど、克服したから頑張って克服してもらいたい'),
        ('3','自分も苦手なので、気持ちがよく分かる。'),
        ('10','なぜ苦手なのか不思議である。ちょっとやればすぐできない？'),
        ('0','なんとも思わない'),
        ('0','できないやつは、見ていてイライラする。')
    )
    test3_val4 = (
        ('10','暇なときは、空想や思索にふけっている。'),
        ('0','空想や思索にふけるほど暇ではない'),
        ('0','空想にふけるのは、変な人がすることだと思うので、ふけることはほどんどない。'),
        ('0','性的な妄想にふけることはたまにある。'),
        ('10','毎日空想にふけっている')
    )
    test3_val5 = (
        ('10','本当の余命をそのまま伝える'),
        ('0','知らないとごまかす'),
        ('0','実際よりも長い余命を伝えるなど、巧妙な嘘で切り抜ける。'),
    )
    ques1 = forms.ChoiceField(choices=test3_val,label='問題1')
    ques2 = forms.ChoiceField(choices=test3_val2,label='問題2')
    ques3 = forms.ChoiceField(choices=test3_val3,label='問題3')
    ques4 = forms.ChoiceField(choices=test3_val4,label='問題4')
    ques5 = forms.ChoiceField(choices=test3_val5,label='問題5')