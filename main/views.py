from django.shortcuts import render

from .models import Task


def index(request):
    data = {
        'title': 'Описание сайта'
    }
    return render(request=request, template_name='main/index.html', context=data)


class CRUD:

    @staticmethod
    def show_tasks(request):
        tasks = Task.objects.filter(users_id_id=request.user.id)
        data = {
            'title': 'Задачи',
            'tasks': tasks
        }
        CRUD.add_task(request)
        CRUD.update_task(request)
        CRUD.delete_task(request)

        return render(request=request, template_name='main/tasks.html', context=data)

    @staticmethod
    def add_task(request):
        if request.POST.get('new_task'):
            task_text = request.POST['new_task']
            new_task = Task()
            new_task.text = task_text
            new_task.users_id_id = request.user.id
            new_task.save()

    @staticmethod
    def update_task(request):
        if request.POST.get('enter_text'):
            task_text = request.POST['enter_text']
            if request.POST.get('update-task'):
                task_id = request.POST['update-task']
                update = Task.objects.get(pk=task_id)
                update.text = task_text
                update.save()

    @staticmethod
    def delete_task(request):
        if request.POST:
            if request.POST.get('delete-task'):
                task_id = request.POST.get('delete-task')
                Task.objects.filter(id=task_id).delete()
