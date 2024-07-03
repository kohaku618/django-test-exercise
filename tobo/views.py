from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from tobo.models import Task

# Create your views here.
def index(request):
    if request.method == 'POST':
        task = Task(title=request.POST['title'],due_at=make_aware(parse_datetime(request.POST['due_at'])))
        
        task.save()

    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }
    return render(request, 'tobo/index.html', context)