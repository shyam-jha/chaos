from django.contrib import admin

# Register your models here.


from .models import Genre, Universe, Movie, Message, UserProfile

admin.site.register(Genre)
admin.site.register(Universe)
admin.site.register(Movie)
admin.site.register(Message)
admin.site.register(UserProfile)
