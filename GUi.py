import customtkinter as ctk
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
        self.window.title('This is just a try')

        # ----------------------------- Widgets

        self.page_title_label = ctk.CTkLabel(
            self.window,
            text="Weather Forecast App",
            font=("Arial", 25)
        )
        

        self.check_weather_button = ctk.CTkButton(
            self.window,
            text="Check weather", 
            command=self.button_click_event
        )
        
        self.check_weather_frame = ctk.CTkScrollableFrame(
            master=self.window,
            width=1300,
            height=250,
            border_width=2
        )

        self.dress_recommendation_button = ctk.CTkButton(
            self.window,
            text="Dress Recommendation",
            command=self.dress_recommendation_event)

        self.history_button = ctk.CTkButton(
            self.window, 
            text="Dress Recommendation", 
            command=self.check_history_event
        )

  #     ------------------------ Positions

        self.page_title_label.pack(padx=20, pady=20)
        self.check_weather_button.pack(padx=20, pady=20)
        self.check_weather_frame.pack(padx=5, pady=5)
        self.dress_recommendation_button.pack(padx=10, pady=10)
        self.history_button.pack(padx=10, pady=10)

        self.window.mainloop()

    def button_click_event(self):
        dialog = ctk.CTkInputDialog(
            text="Type in a city name",
            title="Test")
        self.req1 = Geo(dialog.get_input())
        self.req2 = CurrentWeather(self.req1.coord)
        self.req3 = AirPollutionLevel(self.req1.coord)
        self.req4 = FourDaysForecast(self.req1.coord)

        self.label_req1 = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"the coordinates of the city are: {self.req1.coord}"
        )

        self.label_req2 = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"The current weather is: {self.req2.return_data().get('main')}, {self.req2.return_data().get('description')}"
        )

        self.label_req3 = ctk.CTkLabel(
            self.check_weather_frame,
            text=f"The level of pollution is: {self.req3.return_data()}"
        )
        
        self.divider = ctk.CTkLabel(
            self.check_weather_frame,
            text='---------------------------------------------------'
        )

        # print(self.req4.return_data())

        self.label_req1.pack(padx= 10, pady= 10)
        self.label_req2.pack()
        self.label_req3.pack()
        self.divider.pack(padx= 10, pady= 10)


    def dress_recommendation_event(self):
        print("dress recommendation button")

    def check_history_event(self):
        print("Check history button")
