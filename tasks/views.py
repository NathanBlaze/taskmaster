from django.shortcuts import render

from tasks import forms
from tasks.models import Subject, Task


def homepage(request):
    return render(
        request,
        "tasks/homepage.html",
        {
            "title": "TaskMaster homepage",
        },
    )


def list_tasks(request):
    tasks = Task.objects.all()
    return render(
        request,
        "tasks/list_tasks.html",
        {
            "title": "Tareas activas",
            "tasks": tasks,
        },
    )


# def list_high_priority(request):
#     tasks = Task.objects.filter(priority="H")
#     return render(
#         request,
#         "tasks/list_tasks.html",
#         {
#             "title": "Tareas de prioridad alta",
#             "tasks": tasks,
#         },
#     )


# def list_normal_priority(request):
#     tasks = Task.objects.filter(priority="N")
#     return render(
#         request,
#         "tasks/list_tasks.html",
#         {
#             "title": "Tareas de prioridad normal",
#             "tasks": tasks,
#         },
#     )


# def list_low_priority(request):
#     tasks = Task.objects.filter(priority="L")
#     return render(
#         request,
#         "tasks/list_tasks.html",
#         {
#             "title": "Tareas de prioridad baja",
#             "tasks": tasks,
#         },
#     )


def list_by_priority(request, priority):
    tasks = Task.objects.filter(priority=priority.upper())
    return render(
        request,
        "tasks/list_tasks.html",
        {
            "title": f"Tareas de prioridad {priority}",
            "tasks": tasks,
        },
    )


def list_subjects(request):
    subjects = Subject.objects.all()
    return render(
        request,
        "tasks/list_subjects.html",
        {
            "title": "Temas",
            "subjects": subjects,
        },
    )


def subject_detail(request, pk):
    subject = Subject.objects.get(pk=pk)

    return render(
        request,
        "tasks/subject_detail.html",
        {
            "title": f"Tema {subject.name}",
            "subject": subject,
        },
    )


def search(request):
    tasks = []
    query = ""
    if request.method == "POST":
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            tasks = Task.objects.filter(title__icontains=query)
            priority = form.cleaned_data.get("priority") or []
            if priority:
                tasks = tasks.filter(priority__in=priority)

    else:
        form = forms.SearchForm()

    # query = request.POST.get("query")
    # if not query:
    #     query = request.GET.get("query", "")
    # tasks = Task.objects.filter(title__icontains=query)
    # priorities = request.POST.getlist("priority")
    # if priorities:
    #     tasks = tasks.filter(priority__in=priorities)
    return render(
        request,
        "tasks/search.html",
        {
            "title": "Buscar tareas",
            "form": form,
            "tasks": tasks,
            "query": query,
        },
    )


def lab_view(request):
    return render(request, "tasks/lab.html", {"title": "Labs page"})


def create_task(request):
    form = forms.CreateTaskForm()
    return render(
        request,
        "tasks/create_task.html",
        {
            "title": "Nueva tarea",
            "form": form,
        },
    )
