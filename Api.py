import requests
import datetime as dt

class Api:

    def __init__(self):
        self.api_key="71b84af60da741ebfbfede011349f6c8"

    def get_info_by_city_name(self,city):

        data=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,self.api_key)).json()

        try:
            info={
                "current_temperature":str(round(data["main"]["temp"]-273.15,1))+"°",
                "Weather":data["weather"][0]["main"],
                "humidity":data["main"]["humidity"],
                "sunrise":dt.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%A,%B,%d,%Y\n%I:%M:%S %p"),
                "sunset":dt.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%A,%B,%d,%Y\n%I:%S %p"),
                "country":data["sys"]["country"]


            }
            return info
        except:
            return 0
#obj=Api()
#print(obj.get_info_by_city_name("pune"))
