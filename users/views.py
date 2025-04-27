# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Diet
from django.shortcuts import render, redirect
from django.http import JsonResponse

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirect after register
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def home_view(request):
    return render(request, 'users/home.html')

def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

# Diet Page
@login_required
def diet_page(request):
    return render(request, 'users/diet.html')

# Run Tracking Page
@login_required
def run_tracking_page(request):
    return render(request, 'users/run_tracking.html')

# Social Connection Page
@login_required
def connect_page(request):
    return render(request, 'users/connect.html')
def diet_view(request):
    if request.method == 'POST':
        if 'create' in request.POST:  # Add food
            food_name = request.POST['food_name']
            calories = request.POST['calories']
            date = request.POST['date']
            Diet.objects.create(food_name=food_name, calories=calories, date=date)
        elif 'delete' in request.POST:  # Delete food
            diet_id = request.POST['id']
            diet = Diet.objects.get(id=diet_id)
            diet.delete()

        return redirect('diet_view')  # Reload after POST request

    # Retrieve all food items in the diet
    diets = Diet.objects.all()
    return render(request, 'diet.html', {'diets': diets})

# View to load meals (for the GET request)
def get_meals(request):
    meals = Diet.objects.all()  # Get all meals from the Diet model
    meal_list = [{"id": meal.id, "name": meal.name, "description": meal.description} for meal in meals]
    return JsonResponse({"meals": meal_list})

# View to add a new meal (for the POST request)
def add_meal(request):
    if request.method == 'POST':
        meal_name = request.POST.get('meal_name')
        meal_description = request.POST.get('meal_description')

        # Save the new meal
        new_meal = Diet.objects.create(name=meal_name, description=meal_description)
        return JsonResponse({"message": "Meal added successfully!"}, status=200)

# View to delete a meal (for the POST request)
def delete_meal(request):
    if request.method == 'POST':
        meal_id = request.POST.get('meal_id')
        try:
            meal = Diet.objects.get(id=meal_id)
            meal.delete()
            return JsonResponse({"message": "Meal deleted successfully!"}, status=200)
        except Diet.DoesNotExist:
            return JsonResponse({"error": "Meal not found!"}, status=404)