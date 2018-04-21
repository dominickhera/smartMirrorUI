#!/usr/bin/python

from tkinter import *
# import tkMessageBox 
import time
from datetime import date
import calendar
import pyowm
# import weather-api
# from weather import weather-api
# weather = Weather(unit=Unit.CELSIUS)

root = Tk()

canavasThing = Canvas(root, height = 500, width = 750) 
timeVar = StringVar()
timeLabel = Label( root, textvariable=timeVar, relief=FLAT)
# timeLabel.Font(family="Times", size=10, weight=tkFont.BOLD)
timeVar.set(time.strftime("%I:%M:%S"))
timeLabel.pack()

dateVar = StringVar()
dateLabel = Label( root, textvariable=dateVar, relief=FLAT)
dateVar.set(time.strftime("%d/%m/%Y"))
dateLabel.pack()

my_date = date.today()
dayVar = StringVar()
dayLabel = Label( root, textvariable=dayVar, relief=FLAT)
dayVar.set(calendar.day_name[my_date.weekday()])
dayLabel.pack()

# location = weather.lookup_by_location('guelph')
# condition = location.condition()
# weatherVar = StringVar()
# weatherLabel = Label( root, textvariable=weatherVar, relief=FLAT)
# weatherVar.set(condition.text())
# weatherLabel.pack()

root.title("Smart Mirror GUI")
canavasThing.pack()
root.mainloop()