from django.views.generic import TemplateView
from django.shortcuts import render
from . import forms
from . import readfile, writefile

csv_path = 'playground/files/test.csv'


class DailySummary(TemplateView):
    template_name = 'daily_summary.html'

    def get(self, request):
        tasks, hours = readfile.readfile(csv_path)
        return render(request, self.template_name,
                      {'task1': tasks[0], 'hour1': hours[0],
                       'task2': tasks[1], 'hour2': hours[1],
                       'task3': tasks[2], 'hour3': hours[2],
                       'task4': tasks[3], 'hour4': hours[3],
                       'task5': tasks[4], 'hour5': hours[4]})


class BarGraph(TemplateView):

    template_name = 'BarGraph.html'

    def get(self, request):
        tasks, hours = readfile.readfile('playground/files/test.csv')
        initial_data = {'task1': tasks[0], 'hour1': hours[0],
                        'task2': tasks[1], 'hour2': hours[1],
                        'task3': tasks[2], 'hour3': hours[2],
                        'task4': tasks[3], 'hour4': hours[3],
                        'task5': tasks[4], 'hour5': hours[4]}
        form = forms.TaskNamesForm(initial=initial_data)
        return render(request, self.template_name,
                      {'task1': tasks[0], 'hour1': hours[0],
                       'task2': tasks[1], 'hour2': hours[1],
                       'task3': tasks[2], 'hour3': hours[2],
                       'task4': tasks[3], 'hour4': hours[3],
                       'task5': tasks[4], 'hour5': hours[4]})


class Settings(TemplateView):
    template_name = 'settings.html'

    def get(self, request):
        tasks, hours = readfile.readfile('playground/files/test.csv')
        initial_data = {'task1': tasks[0],
                        'task2': tasks[1],
                        'task3': tasks[2],
                        'task4': tasks[3],
                        'task5': tasks[4]}

        form = forms.TaskNamesForm(initial=initial_data)
        return render(request, self.template_name,
                      {'form': form, 'instruction': 'Input Task Names'})

    def post(self, request):
        form = forms.TaskNamesForm(request.POST)
        task_names = []
        if form.is_valid():
            task_names.append(form.cleaned_data['task1'])
            task_names.append(form.cleaned_data['task2'])
            task_names.append(form.cleaned_data['task3'])
            task_names.append(form.cleaned_data['task4'])
            task_names.append(form.cleaned_data['task5'])

        writefile.update_task_names(csv_path, task_names)
        return render(request, self.template_name,
                      {'form': form, 'instruction': 'Task Names Applied'})
