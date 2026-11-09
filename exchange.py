import requests






url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json" 
response =requests.get(url)
data=response.json()

print("===============Курс Валют НБУ===============")

kurs=input("Введи валюту=  ")
kilk=input("Введи кількість=  ")





for currensy in data:
    if currensy["cc"] in [kurs]:
        print(currensy["cc"],"-", currensy["rate"],"грн")
        print(float(currensy["rate"])*float(kilk))











































































