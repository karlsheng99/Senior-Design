import csv

def update_task_names(file_path, task_names):
    csvreader = csv.reader(open(file_path))
    lines = list(csvreader)

    for i in range(len(task_names)):
        lines[i+1][1] = task_names[i]

    csvwriter = csv.writer(open(file_path, 'w'))
    csvwriter.writerows(lines)


def update_hour(file_path, task, hour):
    csvreader = csv.reader(open(file_path))
    lines = list(csvreader)

    lines[task+1][2] = str(float(lines[task+1][2]) + hour)
    
    csvwriter = csv.writer(open(file_path, 'w'))
    csvwriter.writerows(lines)

