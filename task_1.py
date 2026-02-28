import requests
urls = [
    'https://github.com/',
    'https://www.binance.com/en',
    'https://tomtit.tomsk.ru/',
    'https://jsonplaceholder.typicode.com/',
    'https://moodle.tomtit-tomsk.ru/'
]

def chek_url(url):
    try:
        response = requests.get(url)
        code = response.status_code
        if code == 200:
            status = "Доступен"
        elif code == 404:
            status = "Не найден"
        elif code == 500:
            status = "Технические проблемы на стороне сервера"
        elif code == 400:
            status = "Синтатическая ошибка в запросе"
        elif code == 300:
            status = "Перенаправление. Запрос имеет несколько возможных ответов"
        elif code == 403:
            status = "Вход запрещен"
        elif code == 202:
            status = "Запрос был принят на обработку, но она не завершена"
        else:
            status = "Код: " + str(code)
        return f"{url} - {code} - {status}"
    except requests.ConnectionError:
        return f"{url} - Не доступен - Нет соединения"
    except Exception as e:
        return f"{url} - ошибка: {e}"

for url in urls:
    print(chek_url(url))