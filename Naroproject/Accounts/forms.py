from django.contrib.auth.models import User
from django import forms
from . models import User

class SignUpForm(forms.ModelForm) :
    email = forms.EmailField(
        label = 'E-mail',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'example@naver.com',
                'required': 'True',
            }
        ),
        max_length=255,
        )

    # password에 대해서는 입력 시 *****가 나오도록 하기 위해 커스터 마이징 한다.
    password = forms.CharField(
        label = 'Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'required' : 'True',
            }
        ),
        max_length = 30,
        min_length = 8,
        )

    Repeat_password = forms.CharField(
        label = ' Repeat_password',
        widget=forms.PasswordInput(
           attrs={
            'placeholder' : 'Repeat_Password',
            'required' : 'True',
           }
        ),
        max_length = 30,
        min_length = 8,
        )

    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.SelectDateWidget(
            attrs={
                'type' : 'date',
                'class': 'form-control',
                'required': 'True',
            },
            years=range(2020,1900,-1)
        ),
    )

    # MBTI 기능
    MBTI_CHOICES = (
        ('ISTJ', 'ISTJ'),
        ('ISFJ','ISFJ'),
        ('INFJ','INFJ'),
        ('INTJ','INTJ'),
        ('ISTP','ISTP'),
        ('ISFP','ISFP'),
        ('INFP','INFP'),
        ('INTP','INTP'),
        ('ESTP','ESTP'),
        ('ESFP','ESFP'),
        ('ENTP','ENTP'),
        ('ENFP','ENFP'),
        ('ESTJ','ESTJ'),
        ('ESFJ','ESFJ'),
        ('ENFJ','ENFJ'),
        ('ENTJ','ENTJ'),
    )
    mbti_result = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=MBTI_CHOICES,
    )
    
    
    
    class Meta:
        model = User
        # fields에는 해당 모델에 대해 입력 받을 필드들을 나열한다.
        # + 추가 필드도 포함 될 수 있다.
        fields = [
            'email',
            'password',
            'Repeat_password',
            'date_of_birth',
            'mbti_result',
            ]
        # clean_[필드명]을 통해 cleaned_data를 받아오고 이 받아온 데이터들 중 'password'와 'Repeat_password'를 확인하여 일치 하지 않으면 에러 메시지를 전송한다.
        def clean_Reapet_password(self):
            cd = self.cleaned_data
            if cd['password'] != cd['Repeat_password']:
                raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        #일치하면 일반적으로 'Repeat_password'를 반환한다.
            return cd['Repeat_password']