from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.

#user = request.user // this doesn't work here it works directly in the HTML {{request.user}}

def home(request):
    msg = 'Welcome Home'
    if request.user.is_authenticated():
        msg = 'Welcome %s' %(request.user)
    title = "This is the Home page"

    if request.method == 'POST':  # POST is case sensetive
        # print request.POST
        title = "The Form Works"
    #form = SignUpForm(request.POST)  // This turns on the validation: means that the form must take request data or it's not gonna post anything
    form = SignUpForm(request.POST or None) # None is used to be able to send an empty form

    if form.is_valid():
        instance = form.save(commit=False) # This wont commit the form data to the DB
        
#        full_name = self.cleaned_data.get('full_name') # another way to get FORM data
        if not instance.full_name:  # if empty: no value is submitted
            instance.full_name = 'default value'
        instance.save()  # To commit to the DB after data validation and manipulation
        print instance.email
        print instance.timestamp # This is not gonna work if the form is not commited to the DB, for there'll be no timestamp yet

    context = {
        'msg' : msg,
        'title': title,
        'form': SignUpForm,
#        'user' : user  / this doesn't work here it works directly in the HTML {{user}}
    }
    return render(request, "home.html", context)

def form(request):
    form = ContactForm(request.POST or None)
    
    if form.is_valid:
        full_name = form.cleaned_data.get('full_name')
        print full_name
    
    for key, value in form.cleaned_data.iteritems(): # To iterate through form items
        print key, valye

    context = {
        'form': form,
        'full_name': full_name
    }
    return render(request, "forms.html", context)