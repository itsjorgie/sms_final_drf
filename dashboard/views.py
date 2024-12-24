from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from system1.models import ReceivedMessage as System1ReceivedMessage
from system2.models import ReceivedMessage as System2ReceivedMessage
from django.contrib.auth.views import LoginView

# Create your views here.

def dashboard_view(request):
    from system1.models import ReceivedMessage as System1ReceivedMessage
    from system2.models import ReceivedMessage as System2ReceivedMessage

    system1_received_messages = System1ReceivedMessage.objects.all()
    system2_received_messages = System2ReceivedMessage.objects.all()

    print("System1 Messages:", system1_received_messages)
    print("System2 Messages:", system2_received_messages)

    combined_received_messages = list(system1_received_messages) + list(system2_received_messages)

    return render(request, 'dashboard/dashboard.html', {
        'received_messages': combined_received_messages,
    })

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        # Call your system1 API to send the message
        # Make sure to encrypt the message before sending it

        return redirect('inbox')

    return render(request, 'dashboard/send_message.html')

def inbox(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated

    system1_received_messages = System1ReceivedMessage.objects.filter(user=request.user).order_by('-timestamp')
    system2_received_messages = System2ReceivedMessage.objects.filter(user=request.user).order_by('-timestamp')

    combined_received_messages = list(system1_received_messages) + list(system2_received_messages)

    return render(request, 'dashboard/inbox.html', {'messages': combined_received_messages})

# Custom login view
def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard/send_message/')  # Redirect to send-message after login
    else:
        form = AuthenticationForm()

    return render(request, 'dashboard/dashboard.html', {'form': form, 'show_login': True})

class CustomLoginView(LoginView):
    template_name = 'dashboard.html'

#def user_home(request):
#    return render(request, 'dashboard/user_home.html')

