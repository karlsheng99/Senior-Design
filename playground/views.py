from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from pathlib import Path
from . import forms
from . import readfile, writefile
from datetime import datetime
from datetime import timedelta
import json


colors_list = ["#3366cc","#dc3912","#ff9900","#109618","#990099",
               "#0099c6","#dd4477","#66aa00","#b82e2e","#316395",
               "#3366cc","#994499","#22aa99","#aaaa11","#6633cc",
               "#e67300","#8b0707","#651067","#329262","#5574a6",
               "#3b3eac","#b77322","#16d620","#b91383","#f4359e",
               "#9c5935","#a9c413","#2a778d","#668d1c","#bea413",
               "#0c5922","#743411"]


today = datetime.date(datetime.now())
file_path = '/home/pi/TasktopFiles/' + str(today) + '/'

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

        return render(request, self.template_name, {'django_data': json_string,
                                                    'colors_list': colors_list
                                                    })

class DailySummary(TemplateView):
    template_name = 'daily_summary.html'

    def get(self, request):
        color_index, tasks, hours = readfile.readfile(stats_path)

        return render(request, self.template_name,
                      {'task1': tasks[0], 'hour1': hours[0], 'color1': colors_list[color_index[0]],
                       'task2': tasks[1], 'hour2': hours[1], 'color2': colors_list[color_index[1]],
                       'task3': tasks[2], 'hour3': hours[2], 'color3': colors_list[color_index[2]],
                       'task4': tasks[3], 'hour4': hours[3], 'color4': colors_list[color_index[3]],
                       'task5': tasks[4], 'hour5': hours[4], 'color5': colors_list[color_index[4]],
                       'task6': tasks[5], 'hour6': hours[5], 'color6': colors_list[color_index[5]],
                       'task7': tasks[6], 'hour7': hours[6], 'color7': colors_list[color_index[6]],
                       'task8': tasks[7], 'hour8': hours[7], 'color8': colors_list[color_index[7]],
                       })

# not used
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

        # table:    date    h1  h2  h3  h4  h5  h6  h7  h8
        #       Sun
        #       Mon
        #       Tue
        #       Wed
        #       Thu
        #       Fri
        #       Sat
        
        table = []

        weekday = today.isoweekday()
        if weekday == 7:
            weekday = 0

        for i in range(7):
            table.append([])
            date = today - timedelta(weekday)
            table[i].append(str(date))
            path = '/home/pi/TasktopFiles/' + str(date) + '/stats.csv'

            if Path(path).exists():
                c_i, t, h = readfile.readfile(path)
                for ii in range(8):
                    if t[ii] == tasks[ii]:
                        table[i].append(h[ii])
                    else:
                        table[i].append(0)
            else:
                for ii in range(8):
                    table[i].append(0)


            weekday -= 1
        

        return render(request, self.template_name,
                      { 'task1': tasks[0], 'task2': tasks[1], 'task3': tasks[2], 'task4': tasks[3], 'task5': tasks[4], 'task6': tasks[5], 'task7': tasks[6], 'task8': tasks[7],
                        'd1': table[0][0], 'd1h1': table[0][1], 'd1h2': table[0][2], 'd1h3': table[0][3], 'd1h4': table[0][4], 'd1h5': table[0][5], 'd1h6': table[0][6], 'd1h7': table[0][7], 'd1h8': table[0][8],
                        'd2': table[1][0], 'd2h1': table[1][1], 'd2h2': table[1][2], 'd2h3': table[1][3], 'd2h4': table[1][4], 'd2h5': table[1][5], 'd2h6': table[1][6], 'd2h7': table[1][7], 'd2h8': table[1][8],
                        'd3': table[2][0], 'd3h1': table[2][1], 'd3h2': table[2][2], 'd3h3': table[2][3], 'd3h4': table[2][4], 'd3h5': table[2][5], 'd3h6': table[2][6], 'd3h7': table[2][7], 'd3h8': table[2][8],
                        'd4': table[3][0], 'd4h1': table[3][1], 'd4h2': table[3][2], 'd4h3': table[3][3], 'd4h4': table[3][4], 'd4h5': table[3][5], 'd4h6': table[3][6], 'd4h7': table[3][7], 'd4h8': table[3][8],
                        'd5': table[4][0], 'd5h1': table[4][1], 'd5h2': table[4][2], 'd5h3': table[4][3], 'd5h4': table[4][4], 'd5h5': table[4][5], 'd5h6': table[4][6], 'd5h7': table[4][7], 'd5h8': table[4][8],
                        'd6': table[5][0], 'd6h1': table[5][1], 'd6h2': table[5][2], 'd6h3': table[5][3], 'd6h4': table[5][4], 'd6h5': table[5][5], 'd6h6': table[5][6], 'd6h7': table[5][7], 'd6h8': table[5][8],
                        'd7': table[6][0], 'd7h1': table[6][1], 'd7h2': table[6][2], 'd7h3': table[6][3], 'd7h4': table[6][4], 'd7h5': table[6][5], 'd7h6': table[6][6], 'd7h7': table[6][7], 'd7h8': table[6][8],
                        'color1': colors_list[color_index[0]],
                        'color2': colors_list[color_index[1]],
                        'color3': colors_list[color_index[2]],
                        'color4': colors_list[color_index[3]],
                        'color5': colors_list[color_index[4]],
                        'color6': colors_list[color_index[5]],
                        'color7': colors_list[color_index[6]],
                        'color8': colors_list[color_index[7]],
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

            return redirect('/playground/settings/')
        return render(request, self.template_name,
                      {'form': form, 'instruction': 'Task Names Applied'})
