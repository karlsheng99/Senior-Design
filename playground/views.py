from django.views.generic import TemplateView
from django.shortcuts import render
from pathlib import Path
from . import forms
from . import readfile, writefile
from datetime import datetime
import json


colors_list = ['#3366CC', '#DC3912', '#FF9900', '#109618', '#990099',
              '#3B3EAC', '#0099C6', '#DD4477', '#66AA00', '#B82E2E',
              '#316395', '#994499', '#22AA99', '#AAAA11', '#6633CC',
              '#E67300', '#8B0707', '#329262', '#5574A6', '#3B3EAC']


today = str(datetime.date(datetime.now()))
file_path = '/home/pi/TasktopFiles/' + today + '/'

stats_template_path = '/home/pi/TasktopFiles/stats_template.csv'
stats_path = file_path + 'stats.csv'
timestamps_path = file_path + 'timestamps.json'

if not Path(file_path).exists():
    Path(file_path).mkdir()
    writefile.create_files(stats_path, timestamps_path)

class Home(TemplateView):
    template_name = 'Home.html'
    
    def get(self, request):
        json_data = json.load(open(timestamps_path))
        json_string = json.dumps(json_data)
        return render(request, self.template_name, {'django_data': json_string})

class DailySummary(TemplateView):
    template_name = 'daily_summary.html'

    def get(self, request):
        color_index, tasks, hours = readfile.readfile(stats_path)
        
        colors = '['
        for i in range(8):
            colors += '\'' + colors_list[color_index[i]] + '\''
            if i != 7:
                colors += ', '
        colors += ']'

        return render(request, self.template_name,
                      {'task1': tasks[0], 'hour1': hours[0],
                       'task2': tasks[1], 'hour2': hours[1],
                       'task3': tasks[2], 'hour3': hours[2],
                       'task4': tasks[3], 'hour4': hours[3],
                       'task5': tasks[4], 'hour5': hours[4],
                       'task6': tasks[5], 'hour6': hours[5],
                       'task7': tasks[6], 'hour7': hours[6],
                       'task8': tasks[7], 'hour8': hours[7],
                       'colors': colors})


class BarGraph(TemplateView):

    template_name = 'BarGraph.html'

    def get(self, request):
        color_index, tasks, hours = readfile.readfile(stats_path)
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

class ColumnChart(TemplateView):

    template_name = 'ColumnChart.html'

    def get(self, request):
        color_index, tasks, hours = readfile.readfile(stats_path)

        return render(request, self.template_name,
                      { 'task1': tasks[0], 'hour1': hours[0],
                        'task2': tasks[1], 'hour2': hours[1],
                        'task3': tasks[2], 'hour3': hours[2],
                        'task4': tasks[3], 'hour4': hours[3],
                        'task5': tasks[4], 'hour5': hours[4],
                        'task6': tasks[5], 'hour6': hours[5],
                        'task7': tasks[6], 'hour7': hours[6],
                        'task8': tasks[7], 'hour8': hours[7],
                        'd1': (datetime(2022, 3, 27).strftime('%x')),
                        'd2': (datetime(2022, 3, 28).strftime('%x')),
                        'd3': (datetime(2022, 3, 29).strftime('%x')),
                        'd4': (datetime(2022, 3, 30).strftime('%x')),
                        'd5': (datetime(2022, 3, 31).strftime('%x')),
                        'd6': (datetime(2022, 4, 1).strftime('%x')),
                        'd7': (datetime(2022, 4, 2).strftime('%x'))
                        })
                       


class Settings(TemplateView):
    template_name = 'settings.html'

    def get(self, request):
        color_index, tasks, hours = readfile.readfile(stats_path)
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

        writefile.update_task_names(stats_path, task_names)
        writefile.update_task_names(stats_template_path, task_names)
        return render(request, self.template_name,
                      {'form': form, 'instruction': 'Task Names Applied'})
