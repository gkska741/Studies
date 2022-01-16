from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        models = get_user_model()
        exclude = UserCreationForm.Meta.fields + ('email',)