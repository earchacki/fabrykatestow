import requests
from datetime import datetime
import time

url = 'http://api.currencylayer.com/live'
parameters = {'access_key':'23334123d578c86369a91e2ed47c1d38', 'source':'USD', 'currencies':'PLN'}

def GetResponse(url, parameters):
    try:
        # strzelamy requestem i pobieramy responsa
        response = requests.get(url, params = parameters)
        # zamieniamy responsa (który jest stringiem) w słownik
        data = response.json()
        #print(response.text)
        return response, data

    except:
        print('Błąd z połączeniem')

def DateTimeMeasure(response):
    try:
        # pobranie czasu wykonania zapytania, przeliczenie na milisekundy oraz zaokrąglenie
        requestTime = str((round((response.elapsed.total_seconds() * 1000))))
        # godzina wykonania zapytania
        requestDateAndHour = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        return requestTime, requestDateAndHour

    except:
        print('Błąd danych z responsa')

def PrintAndWriteRates(url, parameters):
    try:
        # pobieramy responsa oraz dane z niego
        response, data = GetResponse(url, parameters)
        # pobieramy czas zapytania i datę zapytania
        requestTime, requestDateAndHour = DateTimeMeasure(response)
        # pobieramy kurs
        quotes = str((data['quotes']['USDPLN']))

        print('========================================================')
        print('Kurs dolara: ' + quotes)
        print('Data i godzina: ' + requestTime)
        print('Czas wykonania zapytania: ' + requestDateAndHour)

        # otwieramy plik, gdy brak to tworzymy plik, a następnie dopisujemy ostatnią linię
        file = open('C:/Temp/currency.csv', 'a+')
        file.write(str(quotes) + ',' + str(requestTime) + ',' + str(requestDateAndHour) + '\n')
        file.close()

    except:
        print('Błąd podczas wydruku lub zapisu danych')

while True:
    PrintAndWriteRates(url, parameters)
    time.sleep(15)