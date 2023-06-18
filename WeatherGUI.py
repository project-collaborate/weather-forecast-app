# ToDo: connect the method from the classes to the right button
import tkinter as tk
from tkinter import messagebox
from Geo import Geo
from Current import CurrentWeather
from AirPollutionLevel import AirPollutionLevel
from FourDaysForecast import FourDaysForecast

class WeatherGUI():
    def __init__(self):

        self.root = tk.Tk() # initialize the GUI
        self.root.title('Weather forecast app')

        self.root.geometry() # "500x500+100+100" this is the argument of the function to set the screen.

        # ERROR IS HERE TRY TO FIX IT.

        self.lable = tk.Label(self.root, text="Weather forecast app", font=("Ariel", 25))
        self.lable.pack(padx=10, pady=10) # set the padding of the pack function

        # self.upper_button_frame = tk.Frame(self.root) # use frame to create the grid for the buttons
        # self.upper_button_frame.columnconfigure(0, weight=1)
        # self.upper_button_frame.columnconfigure(1, weight=1)

        # self.city_label = tk.Label(self.root, text='Enter here the name of the city:', font=('Ariel', 15))
        # self.city_label.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.insert_box = tk.Entry(self.root, )
        # self.insert_box.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.insert_box.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Check weather', font=('Ariel', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Ariel', 15))
        self.textbox.pack(fill='x')

        self.textbox2 = tk.Text(self.root, height=5, font=('Ariel', 15))
        self.textbox2.pack(fill='x')

        self.button_frame = tk.Frame(self.root) # use frame to create the grid for the buttons
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        self.dress_recommendation = tk.Button(self.button_frame, text='Dress recommendation', font=('Arial', 15)) # 1st argument specify the position of the button
        self.dress_recommendation.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.history_weather = tk.Button(self.button_frame, text='History Weather', font=('Arial', 15))
        self.history_weather.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.button_frame.pack(fill='x')

        self.root = tk.mainloop()

    def show_message(self):
        messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

WeatherGUI()