import data
# print(data.weather)
weather_data = data.weather

print(weather_data.keys())

# print(weather_data['list'])

forcast_container = weather_data['list']
print(type(forcast_container))
print(len(forcast_container))

first_item_in_forcast_container = forcast_container[0]
print(first_item_in_forcast_container.keys())

#attempting to access required value for item in forcast list
time = first_item_in_forcast_container['dt_txt']
temp_k = first_item_in_forcast_container['main']['temp']
pressure = first_item_in_forcast_container['main']['pressure']
wind = first_item_in_forcast_container['wind']['speed']
clouds = first_item_in_forcast_container['weather']
print(clouds[0]['description'])
cloud_description = clouds[0]['description']

print(time, temp_k, wind, cloud_description, pressure)

#attempt to access for all 40 forcast in list
print('Time'.center(20), 'Temp_in_k'.center(7), 'Temp_in_C'.center(7), 'Wind'.center(5), 'Pressure'.center(9), 'Cloud_desc'.center(17), sep = " | ")
 print("-"*90)

def display_as_high_or_low(temperature):

    def wrapper(temp_k):
        temp_C = temperature(temp_k)
        if temp_C >= 25:
            return ('high temperature')
        else:
            return ('low temperature')

        return temp_C
    return wrapper

@display_as_high_or_low
def to_celsius (temp_k ):
    temp_C = round(temp_k - 273.15)
    return temp_C

for forcast in forcast_container:
    time              = forcast['dt_txt']
    temp_k              = forcast['main']['temp']
    pressure          = forcast['main']['pressure']
    wind              = forcast['wind']['speed']
    clouds            = forcast['weather']
    # print(clouds[0]['description'])
    cloud_description = clouds[0]['description']
    temp_C            = to_celsius(temp_k)


    # print(time, temp, wind, pressure, cloud_description)
    print(f"{time}".center(20), f'{temp_k} k'.center(7), f'{temp_C} C'.center(7), f'{wind} km/hr'.center(5), f'{pressure} mbar'.center(9), f'{cloud_description}'.center(17), sep = " | ")

# def to_celsius (k ):
#     celsius = k - 273.15
#     return celsius

# c = to_celsius( 298.28)
# print(c)





 
