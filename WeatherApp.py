#Amal Kariyawasam, 26/06/2025, WeatherApp using OpenWeatherMap

from flask import Flask, render_template, request 
import requests 
app = Flask(__name__)

#Function to query Weather API and to return data 
def weather(location_input): 
        API_key="4e0be172ba5affd1c6fb97aceabe2940" # API Key from Openweather MAP
        api_address=f"https://api.openweathermap.org/data/2.5/weather?q={location_input}&appid={API_key}&units=metric" # Query to get the weather
        api_response=requests.get(api_address) # Save response into a variable
        api_to_dict=api_response.json() # Convert the API response into a Python Dictionary
        status_code=api_to_dict["cod"] # This will check the API response code, 200=City found 404=City not found

        #Following code will run for Correct location
        if status_code==200:
                weather_desc=api_to_dict["weather"][0]["description"] 
                current_temp=api_to_dict["main"]["temp"] 
                weather_feels=api_to_dict["main"]["feels_like"]
                pressure=api_to_dict["main"]["pressure"] 
                humidity=api_to_dict["main"]["humidity"]
                selected_location=api_to_dict["name"] 
                selected_country=api_to_dict["sys"]["country"] 
                
                # Below variable will save all weather data to final_output variable
                final_output=f"Current weather in {selected_location}, {selected_country} is {weather_desc} and the temperature is {current_temp}°C and it feels like {weather_feels}°C. The pressure is {pressure} hpa and the humidity is {humidity}%"
        
        # Following code will run for incorrect location
        else:
                final_output=f"Apologies, I can't find that location, please enter [city],[two digit country code] i.e. https://amaldevelops.pythonanywhere.com/colombo,lk"
        
        # This will return data saved in variable "final_output"
        return (final_output) 


# Following function will declare the index function and call index.html and the weather () function
@app.route("/",methods=["GET"]) 
def main_route(): 
    return render_template("index.html", weather=weather("Melbourne,au")) #Render the template by passing default variables

# Following function will get the the location from URL and try to pass this to the weather() function
@app.route("/<location>",methods=["GET"]) #Setup App route and Method
def weather_by_location(location): # Define route function
    return render_template("index.html",weather=weather(location)) #Render the template by passing variables

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="100", debug=False) # Start the server listening for requests