from django import forms

val = (
    ('1','お酒は楽しい'),
    ('2','お酒はやばい')
)

class BungoTest(forms.Form):
    ques1 = forms.ChoiceField(choices=val)
    # ques2 = 