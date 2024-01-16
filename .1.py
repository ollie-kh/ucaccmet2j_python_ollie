#0.1
#load in file
import json
with open ('precipitation.json', encoding = 'utf-8') as file:
    precipitation = json.load(file)
    precipitation_list = list(precipitation)

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
    #select exclusively data from Seattle
    if datapoint['station'] == 'GHCND:US1WAKG0038':
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
#create list of monthly precipitation
total_monthly_precipitation = [total_precipitation_01, total_precipitation_02, total_precipitation_03, total_precipitation_04, total_precipitation_05, total_precipitation_06, total_precipitation_07, total_precipitation_08, total_precipitation_09, total_precipitation_10, total_precipitation_11, total_precipitation_12]
print(total_monthly_precipitation)


#0.2
#calculate total yearly precipitation
total_yearly_precipitation = 0
for datapoint in precipitation_list:
        if datapoint['station'] == 'GHCND:US1WAKG0038':
            total_yearly_precipitation = total_yearly_precipitation + datapoint['value']
print(total_yearly_precipitation)

#calculate relative monthly precipitation
relative_monthly_precipitation_01 = total_precipitation_01/total_yearly_precipitation
relative_monthly_precipitation_02 = total_precipitation_02/total_yearly_precipitation
relative_monthly_precipitation_03 = total_precipitation_03/total_yearly_precipitation
relative_monthly_precipitation_04 = total_precipitation_04/total_yearly_precipitation
relative_monthly_precipitation_05 = total_precipitation_05/total_yearly_precipitation
relative_monthly_precipitation_06 = total_precipitation_06/total_yearly_precipitation
relative_monthly_precipitation_07 = total_precipitation_07/total_yearly_precipitation
relative_monthly_precipitation_08 = total_precipitation_08/total_yearly_precipitation
relative_monthly_precipitation_09 = total_precipitation_09/total_yearly_precipitation
relative_monthly_precipitation_10 = total_precipitation_10/total_yearly_precipitation
relative_monthly_precipitation_11 = total_precipitation_11/total_yearly_precipitation
relative_monthly_precipitation_12 = total_precipitation_12/total_yearly_precipitation

relative_monthly_precipitation = [relative_monthly_precipitation_01, relative_monthly_precipitation_02, relative_monthly_precipitation_03, relative_monthly_precipitation_04, relative_monthly_precipitation_05, relative_monthly_precipitation_06, relative_monthly_precipitation_07, relative_monthly_precipitation_08, relative_monthly_precipitation_09, relative_monthly_precipitation_10, relative_monthly_precipitation_11, relative_monthly_precipitation_12 ]

#save information as json file
with open('results.json', 'w', encoding = 'utf-8') as file:
   json.dump(total_monthly_precipitation, file, indent=4, ensure_ascii=False)
   json.dump(total_yearly_precipitation, file, indent=4, ensure_ascii=False)
   json.dump(relative_monthly_precipitation, file, indent=4, ensure_ascii=False)

#date_split = datapoint['date'].split("-") 





       
        #     total_precipitation = total_precipitation + datapoint['value']
        # elif datapoint['date'].startswith(e)



#         total_monthly_precipitation.append()
#         if datapoint['date'.startswith(0, 6)] in total_monthly_precipitation:
#             total_monthly_precipitation
#         total_precipitation = total_precipitation + datapoint["value"]
# total_monthly_precipitation = total_precipitation/12
# print(total_monthly_precipitation)

        