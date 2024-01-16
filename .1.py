
# 1. Look in the CSV file, and find the station code for Seattle (you can do this manually).
# 2. Use this station code to select all the measurements belonging to it from the JSON data.
# 3. Calculate the total_monthly_precipitation: a list with the total precipitation per month,
# for that location
# 4. Save the results to a results.json file, in the format as specified.
# 5. Commit your script and your output results.json to your version history

import json
with open ('precipitation.json', encoding = 'utf-8') as file:
    precipitation = json.load(file)
    precipitation_list = list(precipitation)

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
    if datapoint['station'] == 'GHCND:US1WAKG0038':
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
print(total_monthly_precipitation)


with open('results.json', 'w', encoding = 'utf-8') as file:
   json.dump(total_monthly_precipitation, file, indent=4, ensure_ascii=False)


    #datapoint_split= datapoint['date'].split("-") 




       
        #     total_precipitation = total_precipitation + datapoint['value']
        # elif datapoint['date'].startswith(e)



#         total_monthly_precipitation.append()
#         if datapoint['date'.startswith(0, 6)] in total_monthly_precipitation:
#             total_monthly_precipitation
#         total_precipitation = total_precipitation + datapoint["value"]
# total_monthly_precipitation = total_precipitation/12
# print(total_monthly_precipitation)

        