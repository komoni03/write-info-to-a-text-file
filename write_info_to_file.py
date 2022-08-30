"""
Importing the datetime module from the datetime library
Importing the requests and datetime modules.
"""

from datetime import datetime
import requests


def create_new_file():
    """
    It creates a new file in the directory C:/Users/cc/temp/
    this gives it a name that the user inputs.
    :return: The name of the file.
    """
    print("This program will help you create a new file and store today's date in it.")
    print('-' * 20)
    name_of_file = str(input("Hi, give the file a name> \n>"))
    name = name_of_file
    # my_dir = "C:/Users/cc/temp/"
    local_dir = str(input("Give the file a directory> \n>"))
    print("")
    new_file = open(f"{local_dir}{name}.txt", 'w', encoding="utf-8")
    new_file.close()
    return new_file.name

def write_date_to_file():
    """
    This function writes the current date to a file
    """
    with open(f"{my_local_file}", "w", encoding="utf-8") as write_file:
        date = datetime.today().strftime("%Y-%m-%d")
        write_file.write(f"Today's date is: {date} \n")


def get_weather_report():
    """
    Getting the weather report from the OpenWeatherMap API.
    """

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = '66075901d3b5956552adb0e7681356a7'
    city = 'London'
    lat = 33.44
    lon = -94.04
    part = 'current,hourly,daily'
    url = f"{base_url}lat={lat}&lon={lon}&exclude={part}&appid={api_key}"
    res = requests.get(url)
    if res.status_code == 200:
    # getting data in the json format
        data = res.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        with open(f"{my_local_file}", "a", encoding="utf-8") as write_file:
            write_file.write("\n")
            write_file.write(f"{city:-^30} \n")
            write_file.write(f"The temperature is: {temperature}k \n")
            write_file.write(f"The humidity is: {humidity} \n")
            write_file.write(f"The pressure is: {pressure} \n")
            write_file.write(f"The weather report is: {report[0]['description']} \n")
    else:
        # showing the error message
        print("Error in the HTTP request")

def read_file():
    """
    It opens the file, reads it, and prints it.
    """
    with open(f"{my_local_file}", "r", encoding="utf-8") as write_file:
        print(write_file.read())


my_local_file = create_new_file()
write_date_to_file()
get_weather_report()
read_file()
