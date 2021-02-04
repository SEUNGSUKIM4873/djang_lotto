from django.contrib import admin
from .models import GuessNumbers  #내가 있는 폴더에서 사용
#from lotto.models import GuessNumbers

# Register your models here.

admin.site.register(GuessNumbers)
