import calendar
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
  ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  ('Andhra Pradesh','Andhra Pradesh'),
  ('Arunachal Pradesh','Arunachal Pradesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chhattisgarh','Chhattisgarh'),
  ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  ('Daman and Diu','Daman and Diu'),
  ('Delhi','Delhi'),
  ('Goa','Goa'),
  ('Gujarat','Gujarat'),
  ('Haryana','Haryana'),
  ('Himachal Pradesh','Himachal Pradesh'),
  ('Jammu & Kashmir','Jammu & Kashmir'),
  ('Jharkhand','Jharkhand'),
  ('Karnataka','Karnataka'),
  ('Kerala','Kerala'),
  ('Lakshadweep','Lakshadweep'),
  ('Madhya Pradesh','Madhya Pradesh'),
  ('Maharashtra','Maharashtra'),
  ('Manipur','Manipur'),
  ('Meghalaya','Meghalaya'),
  ('Mizoram','Mizoram'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Puducherry','Puducherry'),
  ('Punjab','Punjab'),
  ('Rajasthan','Rajasthan'),
  ('Sikkim','Sikkim'),
  ('Tamil Nadu','Tamil Nadu'),
  ('Telangana','Telangana'),
  ('Tripura','Tripura'),
  ('Uttarakhand','Uttarakhand'),
  ('Uttar Pradesh','Uttar Pradesh'),
  ('West Bengal','West Bengal')
)
MULTIPLEX_CHOICES = (
  ('Abhiruchi City Pride Sinhagad Road','Abhiruchi City Pride Sinhagad Road'),
  ('Ashok Theatre Pimpri','Ashok Theatre Pimpri'),
  ('Bollywood Multiplex Kharadi','Bollywood Multiplex Kharadi'),
  ('Carnival Cinemas Moshi Pradhikaran','Carnival Cinemas Moshi Pradhikaran'),
  ('Carnival Premier Plaza Chinchwad','Carnival Premier Plaza Chinchwad'),
  ('CinePRO Vasant Cinema Shivaji Maharaj Chowk Pune','CinePRO Vasant Cinema Shivaji Maharaj Chowk Pune'),
  ('Cinepolis Nexus WESTEND Mall Aundh','Cinepolis Nexus WESTEND Mall Aundh'),
  ('Cinepolis  Seasons Mall Pune','Cinepolis  Seasons Mall Pune'),
  ('City Pride Kothrud','City Pride Kothrud'),
  ('City Pride Satara Road','City Pride Satara Road'),
  ('Mangala Cinema Shivajinagar','Mangala Cinema Shivajinagar'),
  ('E-Square ELITE Hinjawadi','E-Square ELITE Hinjawadi'),
  ('fun Time Multiplex Sinhagad Road','fun Time Multiplex Sinhagad Road'),
  ('INOX Amanora Town centre Hadapsar','INOX Amanora Town centre Hadapsar'),
  ('PVR ICON  Pavillion Pune senapati bapat road','PVR ICON  Pavillion Pune senapati bapat road'),
  ('PVR  Kumar pacific shankarsheth road','PVR  Kumar pacific shankarsheth road'),
  ('Rahul 70 MM Shivajinagar','Rahul 70 MM Shivajinagar'),
  ('Rajhans Cinemas Fatimanagar','Rajhans Cinemas Fatimanagar'),
  ('Satyam Theatre Rajgurunagar','Satyam Theatre Rajgurunagar'),
  ('Victory Theatre Camp Pune','Victory Theatre Camp Pune'),
  ('Vilux talkies Khadki','Vilux talkies Khadki'),
  ('Vishal Cinemas Pimpri','Vishal Cinemas Pimpri'),
  ('Apsara Tokies Seven loves chowk','Apsara Tokies  Seven loves chowk'),
  ('Laxmi Narayan theatre Swargate','Laxmi Narayan theatre Swargate'),
  ('Nilayam tokies Parvati','Nilayam tokies  Parvati')
)
TIME_CHOICES = (
  ('Morning 10 am','Morning 10 am'),
  ('Afternoon 1pm','Afternoon 1pm'),
  ('Evening 5pm','Evening 5pm'),
  ('Night 9pm','Night 9pm')
)
class Customer(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 multiplex = models.CharField(choices=MULTIPLEX_CHOICES,default="Abhiruchi City Pride Sinhagad Road", max_length=50)
 show_time = models.CharField(choices=TIME_CHOICES,default="morning 9am", max_length=50)
 locality = models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES,default="state", max_length=50)

 def __str__(self):
  # return self.user.username
  return str(self.id)


CATEGORY_CHOICES = (
 ('B', 'Bollywood'),
 ('H', 'Hollywood'),
 ('M', 'Marathi'),
 ('S', 'South'),
 ('Sn','Snacks')
)

class Movie(models.Model):
 title = models.CharField(max_length=200)
 ticket_price = models.FloatField()
 total_price = models.FloatField()
 description = models.TextField()
 casts = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
 movie_image = models.ImageField(upload_to='movieimg')

 def __str__(self):
  return str(self.id)

class Snacks(models.Model):
 name = models.CharField(max_length=200)
 snack_price = models.FloatField()
 total_price = models.FloatField()
 quantity = models.PositiveIntegerField(default=1)
 snack_image = models.ImageField(upload_to='snackimg')

 def __str__(self):
  return str(self.id)

class Book(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)

 def __str__(self):
  return str(self.id)

@property
def total_cost(self):
  return self.quantity * self.movie.total_price
  
  

STATUS_CHOICES = (
  ('Confirm','Confirm'),
  ('Cancel','Cancel')
)

class TicketBooking(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)
 booking_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Confirm')

  # Below Property will be used by orders.html page to show total cost
 @property
 def total_cost(self):
   return self.quantity * self.movie.total_price