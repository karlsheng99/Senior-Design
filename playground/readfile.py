import csv

def readfile(file_path):
        file = open(file_path)
        csvreader = csv.reader(file)
        header = next(csvreader)

        color_index = []
        tasks = []
        hours = []
        for row in csvreader:
                color_index.append(int(row[0]))
                tasks.append(row[1])
                hours.append(row[2])
        
        file.close()
        return color_index, tasks, hours

