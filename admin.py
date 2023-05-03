from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
 Customer,
 Movie,
 Book,
 TicketBooking,
 Snacks,
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'name','multiplex','show_time', 'locality', 'city', 'zipcode', 'state']

@admin.register(Movie)
class MovieModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'title', 'ticket_price', 'total_price',  'description', 'casts', 'category', 'movie_image']

@admin.register(Snacks)
class SnackModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'snack_price','total_price','quantity','snack_image']

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'movie', 'quantity']

@admin.register(TicketBooking)
class TicketBookingAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'customer','customer_info', 'movie','movie_info', 'quantity', 'booking_date', 'status']
 
 def customer_info(self,obj):
     link = reverse("admin:app_customer_change",args=[obj.customer.pk])
     return format_html('<a href="{}">{}</a>', link, obj.customer.name)

 def movie_info(self,obj):
     link = reverse("admin:app_movie_change",args=[obj.movie.pk])
     return format_html('<a href="{}">{}</a>', link, obj.movie.title)
