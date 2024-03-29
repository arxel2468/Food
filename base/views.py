from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from .forms import *
from .models import *
from .filters import *

@login_required(login_url='/login')
def profile(request):
    username=request.user.username
    if request.method == 'POST':
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Wrong Password!!!")
        else:
            user.delete()
            return redirect('home')
    return render(request, 'profile.html')

def delete_review(request, pk):
    review = Review.objects.get(id=pk)
    user = request.user
    if user == review.user:
        review.delete()
        messages.success(request, 'Review Deleted Successfully!!!')
        return redirect('profile')
    else:
        messages.error(request, 'You are not authorized to delete this review')
        return redirect('profile')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Successfully signed in as { user }.')
            return redirect('/')
    return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password_confirmation = form.cleaned_data.get('password_confirmation')
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name , email=email, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# Create your views here.

def logout(request):
    auth_logout(request)
    return redirect('login')

# @login_required(login_url='/login')
def index(request): 
    featured_recipes = Recipe.objects.filter(is_featured=True)
    if request.method == 'POST':
        query = request.POST.get('query')
        # Use the query to filter the recipes in the database
        recipes = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(category__name__icontains=query) | Recipe.objects.filter(ingredients__icontains=query)
        
        # paginator = Paginator(recipes, 6)  # Show 6 recipes per page
        # # Get the current page number from the request
        # page = request.GET.get('page')
        # # Get the recipes for the current page
        # recipes = paginator.get_page(page)
        return render(request, 'recipes_list.html', {'recipes': recipes})
    return render(request, 'index.html', {'featured_recipes': featured_recipes})


# @login_required(login_url='/login')
def about(request):
    return render(request, 'about.html')

# @login_required(login_url='/login')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Fmessage = f"""{name}
{email}
{message}"""
            send_mail(
                subject,
                Fmessage,
                settings.EMAIL_HOST_USER,
                ['1amitpandit2468@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Email was sent Successfully!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



@login_required(login_url='/login')
def recipe_add(request):
    categories =  Category.objects.all()
    if request.method == "POST":
        form = RecipeAddForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe', slug=recipe.slug)
    else:
        form = RecipeAddForm()
    return render(request, 'recipe_add.html', {'form': form, 'categories':categories})


@login_required(login_url='/login')
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        username = request.user.username
        if form.is_valid():
            password = request.POST['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Wrong Password!!! Try again.")
            else:
                form.save()
                messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'update_profile.html', context)




def classify_review(comment):
    # import joblib
    # model = joblib.load('E:\\Food-Recipes-Rating-System\\Food_Rating_System\\base\\LinearSVCmodel.pkl')
    # result = model.predict([comment])
    # print(comment)
    # print(result)
    # if result[0] < 3:
    #     return result[0]
    # else:
    #     return result[0]
    from keras import models
    import json
    model=models.load_model('base\LSTM_model_Acc0.81.h5')
    import re
    import string
    from nltk.corpus import stopwords
    setofstopwords=set(stopwords.words('english'))
    from nltk.stem import PorterStemmer, LancasterStemmer # Common stemmers
    from nltk.stem import WordNetLemmatizer # Common Lematizer
    sorted_list = json.load(open('base\sorted.json'))
    porter = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    def stem_terms(row):
        return " ".join([porter.stem(term) for term in row.split()])
    def lemmatize_terms(row):
        return " ".join([lemmatizer.lemmatize(term) for term in row.split()])
    ts= comment
    ts=ts.lower()
    setofstopwords.remove('not')
    ts=ts.replace(r'[^a-zA-Z0-9 ]+',' ')
    def removestops(sentence):
        temp=[]
        for word in sentence.split():
            if word not in setofstopwords:
                temp.append(word)
        return ' '.join(temp)
    ts=removestops(ts)
    ts=stem_terms(ts)
    ts=lemmatize_terms(ts)
    sd={}
    abc=[]
    for word in ts.split():
        abc.append(sorted_list[word])
        
    from keras.preprocessing import sequence
    final_string = sequence.pad_sequences([abc], maxlen=100)
    res=model.predict(final_string)
    acc=res*100
    print(acc)
    if acc > 0 and acc <= 20:
        return 1
    if acc > 20 and acc <=45:
        return 2
    if acc > 45 and acc <=50:
        return 3
    if acc > 50 and acc <=80:
        return 4
    if acc > 80 and acc <= 100:
        return 5


def recipes_list(request):
    recipes = Recipe.objects.all()
    myFilter = RecipesFilter(request.GET, queryset=recipes)
    recipes = myFilter.qs
    # recipes_ratings = {}
    # ratings = {}
    # for recipe in recipes:
    #     reviews = Review.objects.filter(recipe=recipe)
    #     print(reviews[0].rating)
    #     if len(reviews) == 0:
    #         ratings=[0]
    #     else:
    #         for i in range(len(reviews)):
    #             ratings.append(reviews[i].rating)
        
    paginator = Paginator(recipes, 3)  
    page = request.GET.get('page')
    try:
        recipes = paginator.get_page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)
    return render(request, 'recipes_list.html', {'recipes': recipes, 'myFilter':myFilter})

# Use this function in the recipe view
def recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    reviews = Review.objects.filter(recipe=recipe)
    ratings = []
    if len(reviews) == 0:
        ratings=[0]
    else:
        for i in range(len(reviews)):
            ratings.append(reviews[i].rating)
        
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            print(comment)
            rating = classify_review(comment)
            form.save(commit=False)
            review = Review(user=request.user, recipe=recipe, comment=comment, rating=rating)
            review.save()
            
            if rating >= 3:
                message = "Thanks for your positive review!"
            else:
                message = "Thanks for your feedback. We'll try to provide better recipes"
            # review = Review(user=request.user, recipe=recipe, comment=comment, rating=rating)
            messages.success(request, message)
            return redirect('recipe', slug)
    else:
        form = ReviewForm()
    return render(request, 'recipe.html', {'recipe': recipe, 'reviews': reviews, 'form': form,'ratings':sum(ratings)/len(ratings)})


@login_required(login_url='/login')
def recipe_edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    categories = Category.objects.all()
    user = request.user
    if user == recipe.user:
        if request.method == 'POST':
            form = RecipeEditForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                messages.success(request, f'{recipe.title} has been Updated!')
                return redirect('recipe', pk=recipe.pk)
        else:
            form = RecipeEditForm(instance=recipe)
        return render(request, 'recipe_edit.html', {'recipe':recipe, 'form':form, 'categories':categories})
    else:
        messages.error(request, f'You are not authorized to edit this recipe')
        return redirect('profile')

@login_required(login_url='/login')
def recipe_delete(request, pk):
    recipe = Recipe.objects.get(id=pk)
    user=request.user
    if user == recipe.user:
        recipe.delete()
        messages.success(request, "Recipe has been Deleted Successfully!")
        return redirect('profile')
    else:
        messages.error(request, "You are authorized to delete this recipe")
        return redirect('profile')
