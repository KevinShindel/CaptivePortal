from django.shortcuts import render
from .models import Main

# Create your views here.
def main(request):
    if request.method == 'POST':
        record = Main()
        record.login=request.POST.get('email', 'default')
        record.password = request.POST.get('pass', 'default')
        record.save()

    # context = ''
    return render(request, 'index.html', )
