from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(GenreList)
#admin.site.register(UserBook)

@admin.register(UserBook)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","genre", "type","review","review_stars","favorite")
    list_filter = ("type","genre")
