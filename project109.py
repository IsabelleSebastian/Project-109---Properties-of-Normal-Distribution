import plotly.figure_factory as pf
import pandas 
import random
import statistics

df = pandas.read_csv("project109.csv")
data = df["reading score"].tolist()

stdev =  statistics.stdev(data)
mean  =  statistics.stdev(data)

print("Standard Deviation", stdev)
# print("Mean: ", statistics.mean(data))
# print("Median: ", statistics.median(data))
# print("Mode: ", statistics.mode(data))
# print("Standard Deviation: ", statistics.stdev(data))

# square brackets --> [] will specify the data as a list
# graph = pf.create_distplot( [data] , ["Distance Graph"] , show_hist=False)
# graph.show()


firstStandardDevStart , firstStandardDevEnd  = mean-stdev ,  mean+stdev
secondStandardDevStart , secondStandardDevEnd = mean - (2 * stdev) , mean + (2 * stdev)
thirdStandardDevStart , thirdStandardDevEnd = mean - (3 * stdev) , mean + (3 * stdev)


# 10 - 20 --> 11,12,13---------------
#  list = [0,1,...1000]
# listData1 = [11 , 12 , 13,..20]

listData1 = [ result  for result in data if result > firstStandardDevStart and result < firstStandardDevEnd]
listData2 = [ result  for result in data if result > secondStandardDevStart and result < secondStandardDevEnd]
listData3 = [ result  for result in data if result > thirdStandardDevStart and result < thirdStandardDevEnd]


# for result in data:
#     result>start & result<end:
#      return result

# (len(listOfData1) / len(data))*100

percent1 = len(listData1)*100.0/len(data)
percent2 = len(listData2)*100.0/len(data)
percent3 = len(listData3)*100.0/len(data)



print("Percentage of Data Lying Within 1 Standard Deviation Range: ", percent1)
print("Percentage of Data Lying Within 2 Standard Deviation Range: ", percent2)
print("Percentage of Data Lying Within 3 Standard Deviation Range: ", percent3)


