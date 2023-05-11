import json
from datetime import datetime
from math import trunc

import requests
from bs4 import BeautifulSoup
import pandas as pd
from dateutil.parser import parser


def age(day, month, year) :
    today = datetime.now()
    birthDate = f'{day} {month} {year}'
    formated_date = parser.parse(birthDate)
    age = trunc((today - formated_date).days / 365)
    print(age)

def zodiac(day, month) :
        zodiac_signs = {
            "Aries": [(3, 21), (4, 19)],
            "Taurus": [(4, 20), (5, 20)],
            "Gemini": [(5, 21), (6, 20)],
            "Cancer": [(6, 21), (7, 22)],
            "Leo": [(7, 23), (8, 22)],
            "Virgo": [(8, 23), (9, 22)],
            "Libra": [(9, 23), (10, 22)],
            "Scorpio": [(10, 23), (11, 21)],
            "Sagittarius": [(11, 22), (12, 21)],
            "Capricorn": [(12, 22), (1, 19)],
            "Aquarius": [(1, 20), (2, 18)],
            "Pisces": [(2, 19), (3, 20)]
        }

        for sign, (start, end) in zodiac_signs.items():
            if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
                print("Zodiac sign: ",sign)

def percentage(day, month):

    # Read data from CSV file into a pandas DataFrame
    data = pd.read_csv('data.csv')
    # Set the specific day and month

    day = int(day)
    month = int(month)

    population = data['births'].sum()
    # Filter data for the specific day and month across all years
    filtered_data = data[(data['date_of_month'] == day) & (data['month'] == month)]

    # Calculate the total number of births on the specific day and month
    total_births = filtered_data['births'].sum()

    # Calculate the percentage of people born on the specific day and month
    percent_same_day = (total_births /population) * 100              #62187024

    # Print the result rounded to 2 decimal places
    print(f"Percentage of people born on same day: {percent_same_day:.2f} %")

def historical(day, month):
    url = "https://historical-events-by-api-ninjas.p.rapidapi.com/v1/historicalevents"
    querystring = {"month": str(month), "day": str(day)}

    headers = {
        "X-RapidAPI-Key": "6ead7dc6cemsh190a8f4e8b305d8p10c440jsn8a3a3a4b12c5",
        "X-RapidAPI-Host": "historical-events-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    parsed_data = (response.json())

    #
    if len(parsed_data) == 0:
        print("No historical events found for this date.")


    for events in parsed_data:
        event = events['event']
        year = events['year']
        print(year,event)


    #
    #     print(f" {year},{event}") # Output: 'A temple is built on the Capitoline Hill dedicated to Venus Erycina to commemorate the Roman defeat at Lake Trasimene.'
    # parsed_data = json.loads(response)
    # event = parsed_data[0]['event']
    # year = parsed_data[0]['year']
    # print(event,year)

def one(day, month, year) :
    url = "https://www.onthisday.com/date/1985/march/3"
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    songs = soup.find_all('ul', {"class" : "event-list"})
    y = ""
    for song in songs:
        song= song.get_text()

    print("Number one hit:",song.splitlines()[0].split(":")[1].strip())

def main () :
    inputdate = ("23 April 1980")

    day = inputdate.split(" ")[0]
    month = inputdate.split(" ")[1]
    year = inputdate.split(" ")[2]
    formated_date = parser.parse(inputdate)
    date = datetime.strptime(formated_date, "%d %B %Y")

    day = date.day
    month = date.month
    year = date.year

###### functions #######
    age(4, 'April', 1980)
    # zodiac(day,month)
    # one(day,month,year)
    # percentage(day, month)
    # historical(day,month)


if __name__ == "__main__" :
    main()
    //////
