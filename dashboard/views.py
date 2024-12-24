from django.shortcuts import render
from system1.models import ReceivedMessage as System1ReceivedMessage
from system2.models import ReceivedMessage as System2ReceivedMessage


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

def user_home(request):
    return render(request, "dashboard/userhome.html")


