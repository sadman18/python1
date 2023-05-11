import json
from datetime import datetime
from math import trunc

import requests
from bs4 import BeautifulSoup
import pandas as pd
from dateutil.parser import parser




def wikipedia(day, month):
    # Format the URL for the specified day and month
    url = f"https://en.wikipedia.org/wiki/{month}_{day}"

    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section of the page with the list of famous birthdays
    section = soup.find('span', {'id': 'Births'}).parent.find_next_sibling()

    # Extract the list of famous birthdays from the section
    names = [li.text.strip() for li in section.find_all('li')]

    # Write the list of names to a text file
    filename = f"{month}_{day}.txt"
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + '\n')

    # Print the name of the file created
    print(f"File created: {filename}")




def main () :
    inputdate = ("23 April 1980")

    day = inputdate.split(" ")[0]
    month = inputdate.split(" ")[1]
    year = inputdate.split(" ")[2]

    date = datetime.strptime(inputdate, "%d %B %Y")

    day = date.day
    month = date.month
    year = date.year

###### functions #######
    # age(day, month, year)
    # zodiac(day,month)
    # one(day,month,year)
    # percentage(day, month)
    # historical(day,month)
    wikipedia(day, month)



if __name__ == "__main__" :
    main()
