from django.contrib import admin

# Register your models here.
from .models import Vinyl
from .models import Genre
from .models import Songs
from .models import Photo

admin.site.register(Vinyl)
admin.site.register(Genre)
admin.site.register(Songs)
admin.site.register(Photo)