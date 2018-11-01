import csv
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from crawling.models import Car

def parse_car():
    with open("Data_Refined_test.csv", "r", encoding="utf-8") as f:
        next(f)
        cars = []
        for lines in f:  # 애초에 lines는 list.
            car = []
            lines = lines.split("\t")
            for i in range(10):
                car.append(lines[i])
            cars.append(car)
    return cars


if __name__=="__main__":
    cars_data = parse_car()
    num = 0
    for car in cars_data:
        Car(Model=car[0], Maker=car[1], Year=int(car[2]), Size=car[3], Fuel=car[4], Accident=car[5], Shift=car[6], Color=car[7], Distance=int(car[8]), Price=int(car[9])).save()
        num += 1
        if num == 3:
            break

