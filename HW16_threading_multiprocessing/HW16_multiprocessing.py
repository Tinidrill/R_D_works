import requests
import threading
import time
import json

cities = [{"city": "Lviv","latitude":49.84, "longitude":49.84},
          {"city": "Zagreb", "latitude":45.81, "longitude":15.98},
          {"city": "Kyiv", "latitude":50.45, "longitude":30.52},
          {"city": "Split", "latitude":43.51, "longitude":16.44},
          {"city": "Dubrovnik", "latitude":42.64,"longitude":18.11}]

def one_thread(lst):
    start_one = time.time()
    for i in lst:
        respond = requests.get(
            url = "https://api.open-meteo.com/v1/forecast",
            params =
              {
                  "latitude":i.get("latitude"),
                  "longitude":i.get("longitude"),
                  "hourly":"temperature_2m"
              })
        temperature_list = respond.json()["hourly"]["temperature_2m"]
        temperature_average = round(sum(temperature_list) / len(temperature_list), 1)
        print(f"Average temperature for {i.get('city')} is {temperature_average}\n")
    end_one = time.time()
    time_one_thread = end_one - start_one
    print(f"One thread time is {time_one_thread}")

def multi_thread(lst):
    temperature = []

    def request(city, latitude, longitude):
        print(f"Start of {city}")
        resp = requests.get(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "hourly": "temperature_2m",
            }
        )
        # temperatures can be analyzed and used
        temperature_list = resp.json()["hourly"]["temperature_2m"]
        temperature_average = round(sum(temperature_list)/len(temperature_list),1)
        temp = {"city" : city, "average_temperature" : temperature_average}
        temperature.append(temp)
        print(f"Average temperature for {city} is {temperature_average}\n")
#       print(temperature_list)
#       print(f"End of {city}\n")

    start = time.time()
    threads = []
    for n in cities:
        threads.append(threading.Thread(target=request, args=(n.get("city"), n.get("latitude"), n.get("longitude"))))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    max_temperature = {}
    for i in temperature:
        if max_temperature == {}:
            max_temperature = i
        if i.get("average_temperature") > max_temperature.get("average_temperature"):
            max_temperature = i
    print(f"The {max_temperature.get('city')} has highest temperature {max_temperature.get('average_temperature')}")

    end = time.time()
    time_multithread = end - start
    print(f"Multi thread time is {time_multithread}")


if __name__ == "__main__":
    one_thread(cities)
    multi_thread(cities)

