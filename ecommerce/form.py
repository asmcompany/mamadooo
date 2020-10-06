from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


user_model = get_user_model()


class contactForm(forms.Form):


    name = forms.CharField(
        label=' نام ',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'})
        )
   
    email = forms.EmailField(
        label=' ایمیل ',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل برای تماس با شما', 'style':'margin: 10px auto;'}))

    msg = forms.CharField(
        label=' پیام ',
        widget=forms.Textarea(attrs={'class':'form-control','style':'margin: 10px auto;', 'placeholder':'پیام شما از طریق این فرم برای ما ارسال و در اسرع وقت پیگیری میشود'}))



class LoginForm(forms.Form):


    username = forms.CharField(

        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام کاربری',  })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز عبور' })
    )



class RegisterForm(forms.Form):

    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        help_text='<br>'
    )

    email = forms.EmailField(
        label='ایمیل خود را وارد کنید',
        widget=(forms.EmailInput(attrs={'class':'form-control', 'placeholder':'برای مثال example@gmail.com '})),
        help_text=('<br>')
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':' حداقل 4 کاراکتر ' })
    )

    password2 = forms.CharField(
        label='تایید رمز عبور',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز را دوباره وارد کنید' })
    )

    # make sure username is unique #
    def clean_username(self):

        username = self.cleaned_data.get('username')
        querryset = User.objects.filter(username=username)
        if querryset.exists():
            raise forms.ValidationError('این نام کاربری قبلا استفاده شده ')
        return username
        
    # make sur emails are unique #
    def clean_email(self):

        email = self.cleaned_data.get('email')
        querryset = User.objects.filter(email=email)
        if querryset.exists():
            raise forms.ValidationError('این ایمیل قبلا استفاده شده ')
        return email    

    # make sure passwords on registery match #
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('رمز ها یکسان نیستند')

        return data
