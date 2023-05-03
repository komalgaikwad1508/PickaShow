from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer, Movie , Book, TicketBooking , Snacks
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class MovieView(View):
     def get(self,request):
         totalitem = 0
         Bollywood = Movie.objects.filter(category= 'B')
         Hollywood = Movie.objects.filter(category= 'H')
         Marathi = Movie.objects.filter(category= 'M')
         South = Movie.objects.filter(category= 'S')
         if request.user.is_authenticated:
             totalitem = len(Book.objects.filter(user=request.user))
         return render(request, 'app/home.html',{'bollywood':Bollywood , 'hollywood':Hollywood, 'marathi':Marathi, 'south':South ,'totalitem':totalitem})
       
class SnacksView(View):
     def get(self,request):
         Snacks = Snacks.objects.filter(category='Sn')
         return render(request, 'app/home.html',{'snacks':Snacks}) 
         

 
class MovieDetailView(View):
     def get(self,request,pk):
         movie = Movie.objects.get(pk=pk)
         ticket_already_in_book = False
         if request.user.is_authenticated:
            ticket_already_in_book = Book.objects.filter(Q(movie=movie.id) & Q(user=request.user)).exists()
         return render(request, 'app/moviedetail.html',{'movie':movie, 'ticket_already_in_book':ticket_already_in_book})

@login_required
def add_to_cart(request):
    user=request.user
    movie_id = request.GET.get('mov_id')
    movie = Movie.objects.get(id=movie_id)
    print(movie)
    Book(user=user, movie=movie).save()
    return redirect('/book')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        book = Book.objects.filter(user=user)
        print(book)
        amount = 0.0
        total_amount = 0.0
        book_movie = [m for m in Book.objects.all() if m.user == user]
        #print(book_movie)
        if book_movie:
            for m in book_movie:
                tempamount = (m.quantity * m.movie.total_price)
                amount += tempamount
                totalamount = amount
            return render(request, 'app/addtocart.html',{'books':book, 'totalamount':totalamount, 'amount':amount}
        )
        else:
            return render(request, 'app/emptybook.html')

def plus_book(request):
    if request.method == 'GET':
        mov_id =  request.GET['mov_id']
        b = Book.objects.get(Q(movie=mov_id) & Q(user=request.user))
        b.quantity+=1
        b.save()
        amount = 0.0
    book_movie = [m for m in Book.objects.all()if m.user == request.user]
    for m in book_movie:
        tempamount = (m.quantity * m.movie.total_price)
        amount += tempamount
        
    data = {
        'quantity' :b.quantity,
        'amount': amount,
        'totalamount': amount       
        }
    return JsonResponse(data)

def minus_book(request):
    if request.method == 'GET':
        mov_id =  request.GET['mov_id']
        b = Book.objects.get(Q(movie=mov_id) & Q(user=request.user))
        b.quantity-=1
        b.save()
        amount = 0.0
    book_movie = [m for m in Book.objects.all()if m.user == request.user]
    for m in book_movie:
        tempamount = (m.quantity * m.movie.total_price)
        amount += tempamount
       
    data = {
        'quantity' :b.quantity,
        'amount': amount,
        'totalamount': amount         
        }
    return JsonResponse(data)

@login_required
def remove_book(request):
    if request.method == 'GET':
        mov_id =  request.GET['mov_id']
        b = Book.objects.get(Q(movie=mov_id) & Q(user=request.user))
        b.delete()
        amount = 0.0
    book_movie = [m for m in Book.objects.all()if m.user == request.user]
    for m in book_movie:
        tempamount = (m.quantity * m.movie.total_price)
        amount += tempamount
        totalamount = amount
    data = {
        'amount': amount,
        'totalamount': amount   
        }
    return JsonResponse(data)



def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
    add= Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

@login_required
def tickets(request):
    tb = TicketBooking.objects.filter(user=request.user)
    return render(request, 'app/tickets.html',{'ticket_booking':tb})

def movie(request, data = None):
    if data == None:
        movies = Movie.objects.filter(category= 'M')
    elif data == 'Bollywood' or data == 'Hollywwod':
        movies = Movie.objects.filter(category= 'M').filter(casts=data)
        return render(request, 'app/movie.html', {'movies':movies})

class CustomerRegistrationView(View):
   def get(self,request):
       form = CustomerRegistrationForm()
       return render(request, 'app/customerregistration.html',{'form':form})  
   
   def post(self,request):
       form = CustomerRegistrationForm(request.POST)
       if form.is_valid():
        messages.success(request, 'Congratulations!! Registered Successfully')
        form.save()
       return render(request,'app/customerregistration.html',{'form':form})

def password_reset(request):
    return render(request , 'app/password_reset.html')


@login_required
def checkout(request):
    user = request.user
    add =  Customer.objects.filter(user=user)
    book_movies = Book.objects.filter(user=user)
    amount = 0.0
    totalamount = 0.0
    book_movie = [m for m in Book.objects.all()if m.user == request.user]
    if book_movies:
        for m in book_movie:
            tempamount = (m.quantity * m.movie.total_price)
            amount += tempamount
        totalamount = amount 
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'book_movies':book_movies})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    book = Book.objects.filter(user=user)
    for b in book:
        TicketBooking(user=user, customer=customer , movie=b.movie, quantity=b.quantity).save()
        b.delete()
    return redirect("tickets")


def snacks(request):
 return render(request, 'app/snacks.html')

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form =  CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            multiplex = form.cleaned_data['multiplex']
            show_time = form.cleaned_data['show_time']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr , name=name, multiplex=multiplex, show_time=show_time, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully.')
            return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
         
