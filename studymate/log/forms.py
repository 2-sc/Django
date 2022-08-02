from django import forms

class Boardform(forms.Form):
    contents = forms.CharField(
        error_messages={
            # 상황별 에러메세지 설정 
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label='내용')
