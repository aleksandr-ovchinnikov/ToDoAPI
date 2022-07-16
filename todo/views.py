import json
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

from .models import Task
from .encoders import ExtendedEncoder


@csrf_exempt
def addTask(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task = Task(
            title=data["title"],
            description=data['description'],
            accomplishmentDate=data['accomplishmentDate']
        )
        task.save()
        return HttpResponse("Task created")
    else:
        return HttpResponse("Wrong HTTP method")


@csrf_exempt
def completeTask(request, pk):
    try:
        if request.method == 'POST':
            task = Task.objects.get(id=pk)
            task.completed = 'True'
            task.save()
            return HttpResponse("Done")
    except:
        return HttpResponse("Smth wrong")


def getAllTasks(request):
    if request.method == "GET":
        tasks = serialize('json', Task.objects.all(), cls=ExtendedEncoder)
        return HttpResponse(tasks, content_type="application/json")
    else:
        return HttpResponseForbidden()


def getTask(request, pk):
    if request.method == 'GET':
        task = serialize('json', Task.objects.filter(
            id=pk), cls=ExtendedEncoder)
        return HttpResponse(task, content_type="application/json")
    else:
        return HttpResponseForbidden()


@csrf_exempt
def deleteTask(request, pk):
    if request.method == 'DELETE':
        task = Task.objects.filter(id=pk)
        task.delete()
        return HttpResponse("Task Deleted")
    else:
        return HttpResponseForbidden()
