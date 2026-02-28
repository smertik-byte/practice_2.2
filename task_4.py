import requests

BASE_URL = 'https://api.github.com'

def get_user_profile(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)

    if response.status_code != 200:
        print("Пользователь не найден или ошибка запроса")
        return

    data = response.json()

    print(f"Имя: {data.get('name')}")
    print(f"Профиль: {data.get('html_url')}")
    print(f"Репозитории: {data.get('public_repos')}")
    print(f"Обсуждения: {data.get('public_gists')}")
    print(f"Подписки: {data.get('following')}")
    print(f"Подписчики: {data.get('followers')}")

def get_user_repositories(username):
    url = f'{BASE_URL}/users/{username}/repos'
    params = {'per_page': 100}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print('Не удалось получить репозитории')
        return
    repos = response.json()

    if not repos:
        print("У пользователя нет репозиториев")
        return

    for repo in repos:
        print('-' * 40)
        print(f"Название: {repo.get('name')}")
        print(f"Ссылка: {repo.get('html_url')}")
        print(f"Количество просмотров: {repo.get('watchers_count')}")
        print(f"Язык: {repo.get('language')}")
        print(f"Видимость: {'приватный' if repo.get('private') else 'публичный'}")
        print(f"Ветка по умолчанию: {repo.get('default_branch')}")

def search_repositories(query):
    url = f'{BASE_URL}/search/repositories'
    params = {'q': query, 'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print('Ошибка при поиске репозиториев.')
        return

    data = response.json()
    repos = data.get('items', [])

    if not repos:
        print('Репозитории не найдены.')
        return

    for repo in repos:
        print('-' * 40)
        print(f"Название: {repo.get('name')}")
        print(f"Ссылка: {repo.get('html_url')}")

def main():
    while True:
        print('\nМеню GitHub:')
        print('1. Просмотр профиля пользователя')
        print('2. Получить все репозитории пользователя')
        print('3. Поиск репозиториев по названию')
        print('0. Выход')
        choice = input('Выберите действие: ').strip()

        if choice == '1':
            username = input('Введите имя пользователя GitHub: ').strip()
            get_user_profile(username)
        elif choice == '2':
            username = input('Введите имя пользователя GitHub: ').strip()
            get_user_repositories(username)
        elif choice == '3':
            query = input('Введите название репозитория для поиска: ').strip()
            search_repositories(query)
        elif choice == '0':
            print('Выход из программы. Пока!')
            break
        else:
            print('Некорректный ввод. Попробуйте снова.')

if __name__ == '__main__':
    main()