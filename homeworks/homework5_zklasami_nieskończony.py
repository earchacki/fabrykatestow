import requests
from datetime import datetime
import time

parameters = {'access_key':'1831daaa5b6b5c3b6497960ea2d6af1c'}
address = 'http://data.fixer.io/api/latest?'
x = 0
y = 1

class CurrencyRate():
    def __init__(self, address, parameters):
        self.address = address
        self.parameters = parameters

    def function(self):
        print('startujemy')

    def GetCurrencyRate(self, address, parameters):
        # try:
        url = requests.get(address, params=parameters)
        dict = (url.json())
        # print(dict)
        timestamp = dict["timestamp"]
        # Date = dict["date"]
        rate = dict["rates"]["AFN"]
        # print(Timestamp)
        # print(datetime.fromtimestamp(Timestamp))
        print("------------------------------------------------------------")
        print("Kurs waluty względem EURO:")
        print(rate)
        # print(type(dict))
        # print(Url.elapsed.total_seconds())
        TimeMeasure(url, timestamp)
        #print(Rate, datetime.fromtimestamp(timestamp), url.elapsed.total_seconds())
        # except NameError:
        #     print('Upsss... jakiś błąd')
        #     print(sys.exc_info()[0])


    def TimeMeasure(self, url, timestamp):
        print("Data zapytania:")
        print(datetime.fromtimestamp(timestamp))
        print("Czas wykonania zapytania:")
        print(url.elapsed.total_seconds())

object = CurrencyRate(address, parameters)
while True:
    print(object.GetCurrencyRate(address, parameters))
    x += 1
    if x == y:
        print("------------------------------------------------------------")
        print("Program wyłączył się automatycznie po " + str(x) + " odpytaniach o kurs.")
        break
    time.sleep(3)
    print()





# d = {"name1":'jan', 'name2':'kon'}
# print(d['name1'])