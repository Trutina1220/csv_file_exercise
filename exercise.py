import csv
import statistics
import matplotlib.pyplot as plt
from _collections import defaultdict
import numpy as np
from datetime import datetime
steps_and_date_data = defaultdict(list)
average_steps_day = {}
median_steps_day ={}
sum_date ={}
time_series_plot = defaultdict(list)
average_steps_interval = {}

csv_data =open("C:/Users/ASUS\Documents/activity.csv","rt")
csv_reader = csv.DictReader(csv_data)
next(csv_reader)

for line in csv_reader:
    if line['steps'] != "NA":
        if line["date"] not in steps_and_date_data :  #getting the sum
            steps_and_date_data[line["date"]] = []
        else:
            steps_and_date_data[line["date"]].append(int(line['steps']))
csv_data.close()


for everyDate,values in steps_and_date_data.items():
    average_steps_day[everyDate] = statistics.mean(values)
    median_steps_day[everyDate] = statistics.median(values)
    sum_date[everyDate] = sum(values)

# plt.hist(sum_date.values())
# plt.title("Histogram of total steps taken each day")
# plt.xlabel("Total steps taken each day ")
# plt.ylabel("Count")
# plt.show()
# for everyDate,values in average_steps_day.items():
#     print("The average for date "+everyDate+" is "+str(values))
#
# for everyDate,values in median_steps_day.items():
#     print("The median for date "+everyDate+" is "+str(values))

csv_data =open("C:/Users/ASUS\Documents/activity.csv","rt")
csv_reader = csv.DictReader(csv_data)
next(csv_reader)

for line in csv_reader:
    if line['steps'] != "NA":
        if line["interval"] not in time_series_plot :  #getting the sum
            time_series_plot[line["interval"]] = []
        else:
            time_series_plot[line["interval"]].append(int(line['steps']))

for everyInterval,values in time_series_plot.items():
    average_steps_interval[everyInterval] = statistics.mean(values)
x =list(average_steps_interval)
y =average_steps_interval.values()
plt.figure(figsize=(10,3))
plt.bar(x,y, align='center', width=1.0)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()()






