from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name',)