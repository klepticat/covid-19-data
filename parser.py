import json

# Load COVID-19 Data
data = json.loads(open("covid-data.json", "r").read())

while True:
    # Ask for country
    country = input('What country would you like to know about? ').upper()

    # Set up while loop
    i = 0
    totalCases = ''
    days = ''
    dates = ''

    # Loop through data of a country
    while i < len(data[country]['data']):
        totalCases += str(data[country]['data'][i].get('total_cases') or '0.0') + ' '
        days += str(i) + ' '
        dates += str(data[country]['data'][i].get('date') or 'NONE') + ' '
        i += 10

    # Print Data
    print('Total Cases:\n' + totalCases)
    print('Days Passed:\n' + days)
    print('Dates:\n ' + dates)