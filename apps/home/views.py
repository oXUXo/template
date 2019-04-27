from django.shortcuts import render
from .models import Message
from .forms import MessageForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            m = Message(contact = contact, email = email, message = message)
            m.save()
            return  HttpResponseRedirect('/thanks/')
    else:
        form = MessageForm()
    return render(request, 'pages/home.html', {'form': form})
