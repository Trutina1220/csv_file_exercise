import csv
steps_and_date ={}
with open("C:/Users/ASUS\Documents/activity.csv","rt") as csv_data:
    csv_reader = csv.DictReader(csv_data)
    next(csv_reader)

    for line in csv_reader:
        if line[1] not in steps_and_date:
            steps_and_date[f"{line[1]}"] = 0

print(steps_and_date)
