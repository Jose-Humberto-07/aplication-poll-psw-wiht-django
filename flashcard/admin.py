from django.contrib import admin

# Register your models here.
from .models import Categoria, Flashcard

admin.site.register(Categoria)
admin.site.register(Flashcard)
