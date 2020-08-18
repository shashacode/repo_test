# import requests 

# r =requests.get('https://xkcd.com/1906/')
# print(requests.get('https://developer.github.com/'))
# print(r.status_code) #gives response
# print(r.headers['content-type']) #gives info on python dict
# print(r.content)
# print(r.text) #add info on html text
## receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
##with open(r'C:\Users\hp\Desktop\comics\image5.png','wb') as f:
    ## f.write(receive.content)

# ploads = {'things':2,'total':25}
# r = requests.get('https://httpbin.org/get',params=ploads)
# print(r.text)
# print(r.url)
# r = requests.post('https://httpbin.org/post',data = ploads)
# if r.status_code == 200:
#     print('success')
# else:
#     print('fail')

# print(r.text)
# print(r.url)
# print(r.json())

import requests
p = requests.get('http://api.openweathermap.org/data/2.5/weather?q=lagos&appid=fae0688376295dfb73860f94de0cc69c')
# print(p.text)
weather_data = p.text #or p.json no need for ast
print(weather_data)
# print((type)(weather_data))

import ast
owm_data = ast.literal_eval(weather_data)
# print(type(owm_data))
print(owm_data.keys())

print('Time'.center(10),'Temp_in_k'.center(5),'Temp_in_C'.center(5),'Pressure'.center(10) ,'Wind'.center(10),'Cloud_description'.center(5), sep = " | ")
print('-'*90)

def to_celsius(temperature):
    temp_C = round(temperature - 273.15)
    return temp_C
time = (owm_data['timezone'])
cloud_description = (owm_data['weather'][0]['description'])
temperature = (owm_data['main']['temp'])
pressure = (owm_data['main']['pressure'])
wind = (owm_data['wind']['speed'])
temp_C = to_celsius(temperature)

print(f'{time}'.center(10), f'{temperature} k'.center(5), f'{temp_C} C'.center(11),f'{pressure} mbar'.center(10),f'{wind} km\h'.center(7),f'{cloud_description}'.center(5), sep = " | ")

# print(time, cloud_description, temperature, pressure, wind)




