import pandas
open_ = pandas.read_csv("C:/Users/ASUS\Documents/activity.csv")

sum1 = open_.groupby('date')['steps'].sum()
mean1 = open_.groupby('date')['steps'].mean()
median1 = open_.groupby('date')['steps'].median()

print("The sum of steps is : "+"\n"+str(sum1))
print("the mean of steps is : "+"\n"+str(mean1))
print("the median of steps is: "+"\n"+str(median1))
