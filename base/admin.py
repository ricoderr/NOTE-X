from django.contrib import admin
from .models import Notes, Sticky_notes

admin.site.site_header = "NOTE-X Admin panel"
admin.site.index_title = "Admin"
admin.site.register(Notes)
admin.site.register(Sticky_notes)
