from django.shortcuts import render
from git import Repo

from portal.settings import PROJECT_ROOT
from .models import Main


# Create your views here.
def main(request):
    print(PROJECT_ROOT)
    repo = Repo(PROJECT_ROOT)
    branch = repo.active_branch.name
    context = {'branch': branch}
    if request.method == 'POST':
        record = Main()
        record.login=request.POST.get('email', 'default')
        record.password = request.POST.get('pass', 'default')
        record.save()

    return render(request, 'index.html', context)
