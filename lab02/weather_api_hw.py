import requests

city = "Moscow,RU"
appid = "d5345014334fff0db5e298a113b4a37a"

while True:
	method = input("Если хотите увидеть данные на текущий момент времени, введите 1. Если хотите увидеть прогноз данных на неделю, введите 2. Прекратить работу программы: exit \n")
	if method == '1':
		res = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
		data = res.json()
		#################
		print("Город:", city)
		print("Текущая скорость ветра:", data['wind']['speed'])
		print("Видимость:", data['visibility'])
		#################
	if method == '2':
		res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
		data = res.json()
		for i in data['list']:
			#################
			print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", i['wind'], "> \r\nВидимость <", i['visibility'], ">")
			print("____________________________")
			#################
		break
	if method == "exit":
		break
	if method != '1' or method != '2':
		print("ввести либо 1, либо 2 \n")
		continue