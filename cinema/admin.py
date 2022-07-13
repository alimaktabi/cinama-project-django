from django.contrib import admin

from cinema.models import Cinema, Movie, Sans, Ticket

admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Sans)
admin.site.register(Ticket)
