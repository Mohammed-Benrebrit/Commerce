from django.contrib import admin
from .models import User, listing, bids, comment, selled


# Register your models here.
admin.site.register(User)
admin.site.register(listing)
admin.site.register(bids)
admin.site.register(comment)
admin.site.register(selled)
