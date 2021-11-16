import csv

def readfile(file_path):
	file = open(file_path)
	csvreader = csv.reader(file)
        header = next(csvreader)

        tasks = []
        hours = []
        for row in csvreader:
            tasks.append(row[1])
            hours.append(row[2])
        
        file.close()
        return tasks, hours
