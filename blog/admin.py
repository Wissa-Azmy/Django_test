from django.contrib import admin
from .models import SignUp  # .models: relative import: to import models from the same App
# else use instead AppName.models: absolute import

from .forms import SignUpForm

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["full_name", "__unicode__", "timestamp", "updated"]  #list all the columns you want to add to the admin site
    form = SignUpForm
#    class Meta:  # this is the meta data extension to the model SignUp
#        model = SignUp

admin.site.register(SignUp, SignUpAdmin)