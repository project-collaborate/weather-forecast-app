import customtkinter as ctk
from PIL import Image 
from Geo import Geo
from Current import CurrentWeather
from AirPollutionLevel import AirPollutionLevel
from FourDaysForecast import FourDaysForecast

class NewGUI:
    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.set_colour_theam = ctk.set_default_color_theme('green')
        self.set_appearance_mode = ctk.set_appearance_mode('dark')
        self.window.geometry('600x500+200+200')
        self.window.title('Weather Forecast')

        # ----------------------------- Widgets

        self.page_title_label = ctk.CTkLabel(
            self.window,
            text="Weather Forecast App",
            font=("Arial", 25)
        )

        self.input_city_entry = ctk.CTkEntry(
            self.window,
            placeholder_text='enter here a city'
        )

        self.check_weather_button = ctk.CTkButton(
            self.window,
            text="Check weather", 
            command=self.check_weather_event
        )
        
        self.check_weather_frame = ctk.CTkFrame(
            master=self.window,
            width=100,
            height=250,
            border_width=2
        )

        self.dress_recommendation_button = ctk.CTkButton(
            self.window,
            text="Dress Recommendation",
            command=self.dress_recommendation_event)

        self.history_button = ctk.CTkButton(
            self.window, 
            text="Check history", 
            command=self.check_history_event
        )

  #     ------------------------ Positions
        self.window.grid_columnconfigure((0, 1), weight=2)
        self.window.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.page_title_label.grid(
            row=0,
            column=0, 
            padx=20, 
            pady=20,
            sticky='ew',
            columnspan=2
        )

        self.input_city_entry.grid(
            row=1,
            column=0,
            padx=20, 
            pady=20,
            sticky='ew'
        )
        self.check_weather_button.grid(
            row=1,
            column=1, 
            padx=20, 
            pady=20,
            sticky='ew'
        )
        self.check_weather_frame.grid(
            row=2,
            column=0, 
            padx=5, 
            pady=5,
            sticky='ew',
            columnspan=2
        )
        self.dress_recommendation_button.grid(
            row=3,
            column=0, 
            padx=10, 
            pady=10,
            sticky='ew'
        )
        self.history_button.grid(
            row=3,
            column=1, 
            padx=10, 
            pady=10,
            sticky='ew'
        )

        self.window.mainloop()

    # def button_click_event(self):
    #     dialog = ctk.CTkInputDialog(text="Type in a city name", title="Test")

    def check_weather_event(self):

        for widget in self.check_weather_frame.winfo_children():
            widget.destroy() 

        self.req1 = Geo(self.input_city_entry.get())
        self.req2 = CurrentWeather(self.req1.coord)
        self.req3 = AirPollutionLevel(self.req1.coord)
        self.req4 = FourDaysForecast(self.req1.coord)

        self.label_req0 = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"{self.req1.name}"
        )

        self.label_req1 = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"the coordinates of the city are: {self.req1.coord}"
        )

        self.label_req2 = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"{self.req2.return_data().get('weather')[0].get('main')} / {self.req2.return_data().get('weather')[0].get('description')}"
        )

        self.current_weather_icon = ctk.CTkImage(
            dark_image=Image.open(f'Icons/{self.req2.return_data().get("weather")[0].get("icon")}@2x.png'),
            size=(50, 50)
        )
        self.weather_icon_label = ctk.CTkLabel(
            self.check_weather_frame,
            image=self.current_weather_icon,
            text=''
        )

        self.label_req3 = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"The level of pollution is: {self.req3.return_data()[0]} / {self.req3.return_data()[1]}"
        )

        self.temperature_label = ctk.CTkLabel(
            self.check_weather_frame,
            text=f'temp: {self.kelvin_celcius(self.req2.return_data().get("main").get("temp"))}°'
        )
        self.temp_max_label = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"max temp: {self.kelvin_celcius(self.req2.return_data().get('main').get('temp_max'))}°"
        )

        self.temp_min_label = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"min temp: {self.kelvin_celcius(self.req2.return_data().get('main').get('temp_min'))}°"
        )

        # print(self.req4.return_data())
        self.check_weather_frame.grid_columnconfigure((0, 1, 2, 3, 4,5,6,7,8,9,10), weight=1)
        # self.check_weather_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.label_req0.grid(row=0, column=0, padx= 10, pady= 10, sticky='ew', columnspan=2)
        # self.label_req1.grid(row=1, column=0, padx= 10, pady= 10, sticky='w')
        self.label_req2.grid(row=1, column=0, padx= 10, pady= 10, sticky='ew', columnspan=2)
        self.weather_icon_label.grid(row=2, column=0, padx=10, pady=10, sticky='ew', columnspan=2)
        self.label_req3.grid(row=5, column=0, padx= 10, pady= 10, sticky='ew', columnspan=2)
        self.temperature_label.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)
        self.temp_min_label.grid(row=4, column=0, padx=10, pady=10, sticky='ew')
        self.temp_max_label.grid(row=4, column=1, padx=10, pady=10, sticky='ew')


    def kelvin_celcius(self, temperature):
        return "{:.2f}".format(temperature - 273.15)
    
    def dress_recommendation_event(self):
        print("dress recommendation button")

    def check_history_event(self):
        print("Check history button")
