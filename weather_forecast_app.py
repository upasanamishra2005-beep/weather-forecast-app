import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "4584839a0c0d623c264b644df0786b5b"  # <-- Replace this with your real API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = f"City: {city_name}\nTemperature: {temp}°C\nWeather: {weather}\nHumidity: {humidity}%\nWind Speed: {wind} m/s"
            result_label.config(text=result)
        else:
            messagebox.showerror("Error", f"City not found: {city}")
    except:
        messagebox.showerror("Error", "Could not retrieve weather data.")

# GUI Setup
root = tk.Tk()
root.title("🌦️ Weather Forecast App")
root.geometry("350x350")
root.config(bg="#DFF6FF")

title_label = tk.Label(root, text="Weather Forecast", font=("Arial", 16, "bold"), bg="#DFF6FF", fg="#06283D")
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), bg="#47B5FF", fg="white", command=get_weather)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#DFF6FF", fg="#06283D", justify="left")
result_label.pack(pady=10)

root.mainloop()
