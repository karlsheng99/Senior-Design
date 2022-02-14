import csv

def update_task_names(file_path, task_names):
    csvreader = csv.reader(open(file_path))
    lines = list(csvreader)

    for i in range(len(task_names)):
        lines[i+1][1] = task_names[i]

    csvwriter = csv.writer(open(file_path, 'w'))
    csvwriter.writerows(lines)


def update_stats(file_path, task, hour):
    csvreader = csv.reader(open(file_path))
    lines = list(csvreader)

    lines[task+1][2] = str(float(lines[task+1][2]) + hour)
    
    csvwriter = csv.writer(open(file_path, 'w'))
    csvwriter.writerows(lines)


def update_timestamps(file_path, task, start, end):
    line = [task, 
            start.year, start.month, start.day, start.hour, start.minute, round(start.second, 1),
            end.year, end.month, end.day, end.hour, end.minute, round(end.second, 1)]
    
    csvwriter = csv.writer(open(file_path, 'a'))
    csvwriter.writerow(line)