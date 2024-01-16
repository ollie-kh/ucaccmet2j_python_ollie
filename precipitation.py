#0.1
#load in files
import json
with open ('precipitation.json', encoding = 'utf-8') as file:
    precipitation = json.load(file)
    precipitation_list = list(precipitation)



#create results_monthly total dictionary
results_monthly_total = {}

#calculating monthly total precipitation for each place
#create empty variables for each month
total_precipitation_01 = 0
total_precipitation_02 = 0
total_precipitation_03 = 0
total_precipitation_04 = 0
total_precipitation_05 = 0
total_precipitation_06 = 0
total_precipitation_07 = 0
total_precipitation_08 = 0
total_precipitation_09 = 0
total_precipitation_10 = 0
total_precipitation_11 = 0
total_precipitation_12 = 0
for datapoint in precipitation_list:
    
    if datapoint['station'] not in results_monthly_total:
         
        #add together precipitation for each month
        if datapoint['date'].startswith("2010-01") == True:
            total_precipitation_01 = total_precipitation_01 + datapoint['value']
        if datapoint['date'].startswith("2010-02") == True:
            total_precipitation_02 = total_precipitation_02 + datapoint['value']
        if datapoint['date'].startswith("2010-03") == True:
            total_precipitation_03 = total_precipitation_03 + datapoint['value']
        if datapoint['date'].startswith("2010-04") == True:
            total_precipitation_04 = total_precipitation_04 + datapoint['value']
        if datapoint['date'].startswith("2010-05") == True:
            total_precipitation_05 = total_precipitation_05 + datapoint['value']
        if datapoint['date'].startswith("2010-06") == True:
            total_precipitation_06 = total_precipitation_06 + datapoint['value']
        if datapoint['date'].startswith("2010-07") == True:
            total_precipitation_07 = total_precipitation_07 + datapoint['value']
        if datapoint['date'].startswith("2010-08") == True:
            total_precipitation_08 = total_precipitation_08 + datapoint['value']
        if datapoint['date'].startswith("2010-09") == True:
            total_precipitation_09 = total_precipitation_09 + datapoint['value']
        if datapoint['date'].startswith("2010-10") == True:
            total_precipitation_10 = total_precipitation_10 + datapoint['value']
        if datapoint['date'].startswith("2010-11") == True:
            total_precipitation_11 = total_precipitation_11 + datapoint['value']
        if datapoint['date'].startswith("2010-12") == True:
            total_precipitation_12 = total_precipitation_12 + datapoint['value']
        total_monthly_precipitation = [total_precipitation_01, total_precipitation_02, total_precipitation_03, total_precipitation_04, total_precipitation_05, total_precipitation_06, total_precipitation_07, total_precipitation_08, total_precipitation_09, total_precipitation_10, total_precipitation_11, total_precipitation_12]
        results_monthly_total[datapoint['station']] = total_monthly_precipitation
    
    elif datapoint['station'] in results_monthly_total:

        if datapoint['date'].startswith("2010-01") == True:
            total_precipitation_01 = total_precipitation_01 + datapoint['value']
        if datapoint['date'].startswith("2010-02") == True:
            total_precipitation_02 = total_precipitation_02 + datapoint['value']
        if datapoint['date'].startswith("2010-03") == True:
            total_precipitation_03 = total_precipitation_03 + datapoint['value']
        if datapoint['date'].startswith("2010-04") == True:
            total_precipitation_04 = total_precipitation_04 + datapoint['value']
        if datapoint['date'].startswith("2010-05") == True:
            total_precipitation_05 = total_precipitation_05 + datapoint['value']
        if datapoint['date'].startswith("2010-06") == True:
            total_precipitation_06 = total_precipitation_06 + datapoint['value']
        if datapoint['date'].startswith("2010-07") == True:
            total_precipitation_07 = total_precipitation_07 + datapoint['value']
        if datapoint['date'].startswith("2010-08") == True:
            total_precipitation_08 = total_precipitation_08 + datapoint['value']
        if datapoint['date'].startswith("2010-09") == True:
            total_precipitation_09 = total_precipitation_09 + datapoint['value']
        if datapoint['date'].startswith("2010-10") == True:
            total_precipitation_10 = total_precipitation_10 + datapoint['value']
        if datapoint['date'].startswith("2010-11") == True:
            total_precipitation_11 = total_precipitation_11 + datapoint['value']
        if datapoint['date'].startswith("2010-12") == True:
            total_precipitation_12 = total_precipitation_12 + datapoint['value']
        total_monthly_precipitation = [total_precipitation_01, total_precipitation_02, total_precipitation_03, total_precipitation_04, total_precipitation_05, total_precipitation_06, total_precipitation_07, total_precipitation_08, total_precipitation_09, total_precipitation_10, total_precipitation_11, total_precipitation_12]
        results_monthly_total[datapoint['station']] = total_monthly_precipitation
       
    


#0.2
#calculate total yearly precipitation for each city
results_total_yearly = {}
total_yearly_precipitation = 0
for datapoint in precipitation_list:
    if datapoint['station'] in results_total_yearly:
        total_yearly_precipitation = total_yearly_precipitation + datapoint['value']
    elif datapoint['station'] not in results_total_yearly:
      total_yearly_precipitation = total_yearly_precipitation + datapoint['value']
    results_total_yearly[datapoint['station']] = total_yearly_precipitation

print(results_total_yearly)
print(results_monthly_total)

#save information on seattle exclusively as json file (for question 0.2 - only runs in commit "finished 0.2")
# with open('results.json', 'w', encoding = 'utf-8') as file:
#    json.dump(total_monthly_precipitation, file, indent=4, ensure_ascii=False)
#    json.dump(total_yearly_precipitation, file, indent=4, ensure_ascii=False)
#    json.dump(relative_monthly_precipitation, file, indent=4, ensure_ascii=False)


#calculate relative monthly precipitation for each city
#cannot find a way to do this by deadline due to inefficient coding previously... but this is what i was trying:

# relative_monthly_precipitation = {}

# for datapoint in precipitation_list:
#     if datapoint['station'] in relative_monthly_precipitation:
#         relative_monthly_precipitation_01 = results_monthly_total[datapoint][0]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_02 = results_monthly_total[datapoint][1]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_03 = results_monthly_total[datapoint][2]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_04 = results_monthly_total[datapoint][3]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_05 = results_monthly_total[datapoint][4]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_06 = results_monthly_total[datapoint][5]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_07 = results_monthly_total[datapoint][6]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_08 = results_monthly_total[datapoint][7]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_09 = results_monthly_total[datapoint][8]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_10 = results_monthly_total[datapoint][9]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_11 = results_monthly_total[datapoint][10]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_12 = results_monthly_total[datapoint][11]/results_total_yearly[datapoint]

#         relative_monthly_precipitation_list = [relative_monthly_precipitation_01, relative_monthly_precipitation_02, relative_monthly_precipitation_03, relative_monthly_precipitation_04, relative_monthly_precipitation_05, relative_monthly_precipitation_06, relative_monthly_precipitation_07, relative_monthly_precipitation_08, relative_monthly_precipitation_09, relative_monthly_precipitation_10, relative_monthly_precipitation_11, relative_monthly_precipitation_12 ]

#     elif datapoint['station'] not in relative_monthly_precipitation:
#         relative_monthly_precipitation_01 = results_monthly_total[datapoint][0]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_02 = results_monthly_total[datapoint][1]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_03 = results_monthly_total[datapoint][2]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_04 = results_monthly_total[datapoint][3]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_05 = results_monthly_total[datapoint][4]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_06 = results_monthly_total[datapoint][5]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_07 = results_monthly_total[datapoint][6]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_08 = results_monthly_total[datapoint][7]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_09 = results_monthly_total[datapoint][8]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_10 = results_monthly_total[datapoint][9]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_11 = results_monthly_total[datapoint][10]/results_total_yearly[datapoint]
#         relative_monthly_precipitation_12 = results_monthly_total[datapoint][11]/results_total_yearly[datapoint]

#         relative_monthly_precipitation_list = [relative_monthly_precipitation_01, relative_monthly_precipitation_02, relative_monthly_precipitation_03, relative_monthly_precipitation_04, relative_monthly_precipitation_05, relative_monthly_precipitation_06, relative_monthly_precipitation_07, relative_monthly_precipitation_08, relative_monthly_precipitation_09, relative_monthly_precipitation_10, relative_monthly_precipitation_11, relative_monthly_precipitation_12 ]
#     relative_monthly_precipitation[datapoint['station']] = relative_monthly_precipitation_list
        