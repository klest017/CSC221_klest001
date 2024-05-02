import urllib.request
import sys
import json
import matplotlib.pyplot as plt

try: 
    # Fetching weather data from Visual Crossing's API
    result_bytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/montego%20bay/last15days?unitGroup=metric&key=NNY4RSBUZ5STS4NHQKUXBYWFN&contentType=json")
    
    # Parse the results as JSON
    json_data = json.load(result_bytes)
    
    # Extracting relevant information for the bar graph
    dates = []
    temperatures = []

    for day in json_data['days']:
        dates.append(day['datetime'])
        temperatures.append(day['temp'])

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(dates, temperatures, color='blue')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature in Montego Bay for the Last 15 Days')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Displaying the graph
    plt.show()

except urllib.error.HTTPError as e:
    error_info = e.read().decode() 
    print('Error code:', e.code, error_info)
    sys.exit()

except urllib.error.URLError as e:
    error_info = e.read().decode() 
    print('Error code:', e.code, error_info)
    sys.exit()
