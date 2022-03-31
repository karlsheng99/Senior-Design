from asyncio.windows_events import NULL
import csv
import json

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


def update_timestamps_csv(file_path, task, start, end):
    line = [task, 
            start.year, start.month, start.day, start.hour, start.minute, round(start.second, 1),
            end.year, end.month, end.day, end.hour, end.minute, round(end.second, 1)]
    
    csvwriter = csv.writer(open(file_path, 'a'))
    csvwriter.writerow(line)


def update_timestamps_json(file_path, task_name, start, end):
    start_date = "Date(" + str(start.year) + "," + str(start.month) + "," + str(start.day) + "," + str(start.hour) + "," + str(start.minute) + "," + str(round(start.second)) + ")"
    end_date = "Date(" + str(end.year) + "," + str(end.month) + "," + str(end.day) + "," + str(end.hour) + "," + str(end.minute) + "," + str(round(end.second)) + ")"
    
    new_data = {"c":[
        {"v": task_name, "f": NULL},
        {"v": start_date, "f": NULL},
        {"v": end_date, "f": NULL}
    ]}
    
    with open(file_path, 'r+') as file:
        file_data = json.load(file)
        file_data["rows"].append(new_data)

        file.seek(0)
        json.dump(file_data, file, indent=4)