# !/usr/bin/env python3

# api

# https://api.covid19api.com/world/total
# https://api.covid19api.com/summary
# https://api.covid19api.com/total/country/

# library


import requests
from rich.console import Console
from rich.table import Table
from pyfiglet import figlet_format
from termcolor import colored

# header

print(colored(figlet_format("Novel Coronavirus (COVID-19)",
                            font="slant"), 'red', attrs=['bold']))

console = Console()

# get response from api

response = requests.get("https://api.covid19api.com/summary")

# commands list
options = ['-a','-b', '-c', '-x', '-q', '-h']

# country name for flag

# countryFlag = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua_&_Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia_&_Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina_Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape_Verde', 'Central_African_Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo_-_Brazzaville', 'Congo_-_Kinshasa', 'Costa_Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', "Côte_d’Ivoire", 'Denmark', 'Djibouti', 'Dominica', 'Dominican_Republic', 'Ecuador', 'Egypt', 'El_Salvador', 'Equatorial_Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Vatican_City', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'South_Korea', 'Kuwait', 'Kyrgyzstan', 'laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
#              'Luxembourg', 'Macau_SAR_China', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall_Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar_(Burma)', 'Namibia', 'Nepal', 'Netherlands', 'New_Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestinian_Territories', 'Panama', 'Papua_New_Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Kosovo', 'Romania', 'Russia', 'Rwanda', 'Réunion', 'St._Kitts_&_Nevis', 'St._Lucia', 'St._Vincent_&_Grenadines', 'San_Marino', 'São_Tomé_&_Príncipe', 'Saudi_Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra_Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon_Islands', 'Somalia', 'South_Africa', 'South_Sudan', 'Spain', 'Sri_Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad_&_Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'United_States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'VietNam', 'Western_Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

# help commands

option = """
[bold cyan]-a[/bold cyan] => [bold green]get all statistics[/bold green]
[bold cyan]-b[/bold cyan] =>  [bold green]get all statistics for country[/bold green]
[bold cyan]-c[/bold cyan] =>  [bold green]get all statistics for today in the world[/bold green]
[bold cyan]-x[/bold cyan] =>  [bold green]get all statistics for today in country[/bold green]
[bold cyan]-q[/bold cyan] =>  [bold green]for exit[/bold green]
[bold cyan]-h[/bold cyan] =>  [bold green]get Commands[/bold green]
"""

console.print(option, style="bold red", end='\n')


# function


def commands():
    

    command = input('=>  ')
    if command[0:2] in options:
        
        
        cmd(command)
    else:
        print('command is not found')
    commands()


def cmd(cmd):
    
    if cmd == '-a':
        all_country_info()
    if cmd == '-h':
        console.print(option, style="bold red", end='\n')
    if cmd == '-q':
        exit()
    if cmd == '-b' :
        pass


def all_covid_info():
    allinfo = response.json()['Global']
    for i, x in allinfo.items():
        print(i)
        print(x)


def all_country_info():
    allinfo = response.json()['Countries']
    table = Table(show_header=True, style="cyan")
    table.add_column("country", style="magenta", width=34, no_wrap=True)

    table.add_column("countrycode", style="cyan", width=20,
                     no_wrap=True)
    table.add_column("NewConfirmed", style="white", width=20,
                     no_wrap=True)
    table.add_column("TotalConfirmed", style="white", width=20,
                     no_wrap=True)
    table.add_column("NewDeaths", style="red", width=20,
                     no_wrap=True)
    table.add_column("TotalDeaths", style="red", width=20,
                     no_wrap=True)
    table.add_column("NewRecovered", style="green", width=20,
                     no_wrap=True)
    table.add_column("TotalRecovered", style="green", width=20, no_wrap=True)
    table.add_column("Date", width=34)

    for i in allinfo:
        table.add_row(f"{i['Country']}", f"{i['CountryCode']}", f"{i['NewConfirmed']}", f"{i['TotalConfirmed']}",
                      f"{i['NewDeaths']}", f"{i['TotalDeaths']}", f"{i['NewRecovered']}", f"{i['TotalRecovered']}", f"{i['Date']}",)
    console.print(table)

def all_covid_info_by_country(Country):
    allCountry = response.json()['Countries']
    dictionary = {}
    for country in allCountry:
        dictionary.update({country['Country']:country['Slug']})
        return dictionary.get(Country)


commands()





