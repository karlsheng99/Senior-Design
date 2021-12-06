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
                       'task5': tasks[4], 'hour5': hours[4],
                       'task6': tasks[5], 'hour6': hours[5],
                       'task7': tasks[6], 'hour7': hours[6],
                       'task8': tasks[7], 'hour8': hours[7]})


class BarGraph(TemplateView):

    template_name = 'BarGraph.html'

    def get(self, request):
        tasks, hours = readfile.readfile('playground/files/test.csv')
        initial_data = {'task1': tasks[0], 'hour1': hours[0],
                        'task2': tasks[1], 'hour2': hours[1],
                        'task3': tasks[2], 'hour3': hours[2],
                        'task4': tasks[3], 'hour4': hours[3],
                        'task5': tasks[4], 'hour5': hours[4],
                        'task6': tasks[5], 'hour6': hours[5],
                        'task7': tasks[6], 'hour7': hours[6],
                        'task8': tasks[7], 'hour8': hours[7]}
        form = forms.TaskNamesForm(initial=initial_data)
        return render(request, self.template_name,
                      { 'task1': tasks[0], 'hour1': hours[0],
                        'task2': tasks[1], 'hour2': hours[1],
                        'task3': tasks[2], 'hour3': hours[2],
                        'task4': tasks[3], 'hour4': hours[3],
                        'task5': tasks[4], 'hour5': hours[4],
                        'task6': tasks[5], 'hour6': hours[5],
                        'task7': tasks[6], 'hour7': hours[6],
                        'task8': tasks[7], 'hour8': hours[7]})

class BarGraph2(TemplateView):

    template_name = 'BarGraph2.html'

    def get(self, request):
        tasks, hours = readfile.readfile('playground/files/test.csv')
        initial_data = {'task1': tasks[0], 'hour1': hours[0],
                        'task2': tasks[1], 'hour2': hours[1],
                        'task3': tasks[2], 'hour3': hours[2],
                        'task4': tasks[3], 'hour4': hours[3],
                        'task5': tasks[4], 'hour5': hours[4],
                        'task6': tasks[5], 'hour6': hours[5],
                        'task7': tasks[6], 'hour7': hours[6],
                        'task8': tasks[7], 'hour8': hours[7]}
        form = forms.TaskNamesForm(initial=initial_data)
        return render(request, self.template_name,
                      { 'task1': tasks[0], 'hour1': hours[0],
                        'task2': tasks[1], 'hour2': hours[1],
                        'task3': tasks[2], 'hour3': hours[2],
                        'task4': tasks[3], 'hour4': hours[3],
                        'task5': tasks[4], 'hour5': hours[4],
                        'task6': tasks[5], 'hour6': hours[5],
                        'task7': tasks[6], 'hour7': hours[6],
                        'task8': tasks[7], 'hour8': hours[7]},
                        'd1' : '12.05.2021',
                        'd2' : '12.06.2021',
                        'd3' : '12.07.2021',
                        'd4' : '12.08.2021',
                        'd5' : '12.09.2021',
                        'd6' : '12.10.2021',
                        'd7' : '12.11.2021')
                       


class Settings(TemplateView):
    template_name = 'settings.html'

    def get(self, request):
        tasks, hours = readfile.readfile('playground/files/test.csv')
        initial_data = {'task1': tasks[0],
                        'task2': tasks[1],
                        'task3': tasks[2],
                        'task4': tasks[3],
                        'task5': tasks[4],
                        'task6': tasks[5],
                        'task7': tasks[6],
                        'task8': tasks[7]}

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
            task_names.append(form.cleaned_data['task6'])
            task_names.append(form.cleaned_data['task7'])
            task_names.append(form.cleaned_data['task8'])

        writefile.update_task_names(csv_path, task_names)
        return render(request, self.template_name,
                      {'form': form, 'instruction': 'Task Names Applied'})
