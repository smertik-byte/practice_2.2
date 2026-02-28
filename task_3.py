import requests
import json

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
SAVE_FILE = 'resourse/save.json'

def need_groups():
    try:
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def fetch_data():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def show_all_currencies(data):
    print("Курс всех валют:")
    for val in data['Valute'].values():
        print(f"{val['CharCode']} {val['Name']}: {val['Value']}")

def get_currency(data, code):
    for val in data['Valute'].values():
        if val['CharCode'].upper() == code.upper():
            print(f"{val['CharCode']}: {val['Name']} - {val['Value']}")
            return
    print("Валюта не найдена")

def add_currency_to_group(groups, group_name, currency_code, data):
    if currency_code.upper() not in [c['CharCode'] for c in data['Valute'].values()]:
        print("Такой валюты нет в списке всех валют.")
        return
    if group_name not in groups:
        groups[group_name] = []

    if currency_code.upper() not in [c.upper() for c in groups[group_name]]:
        groups[group_name].append(currency_code.upper())
        print(f"Валюта {currency_code.upper()} добавлена в группу {group_name}.")
    else:
        print(f"Валюта {currency_code.upper()} уже есть в группе {group_name}.")


def remove_currency_from_group(groups, group_name, currency_code):
    if group_name in groups:
        currencies = groups[group_name]
        for c in currencies:
            if c.upper() == currency_code.upper():
                currencies.remove(c)
                print(f"Валюта {c} удалена из группы {group_name}")
                return
        print("Такой валюты в группе не существует")
    else:
        print("Группа не найдена")

def save_groups(groups):
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(groups, f, ensure_ascii=False, indent=4)

def show_groups(groups):
    if not groups:
        print("Нет созданных групп")
        return
    for name, currencies in groups.items():
        print(f"Группа: {name}")
        print(f"Валюты: {', '.join(currencies)}")
        print('-' * 20)

def main():
    groups = need_groups()
    data = fetch_data()

    while True:
        print("\nМеню:")
        print("1. Просмотреть текущий курс всех валют")
        print("2. Посмотреть валюту по ее коду")
        print("3. Создать группу валют для отслеживания")
        print("4. Посмотреть все группы")
        print("5. Удалить валюту из группы")
        print("6. Добавить валюту в группу")
        print("7. Сохранить группы")
        print("8. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            show_all_currencies(data)
        elif choice == '2':
            code = input("Введите код валюты: ").strip()
            get_currency(data, code)
        elif choice == '3':
            group_name = input("Введите имя новой группы: ").strip()
            if group_name:
                if group_name in groups:
                    print(f"Группа '{group_name}' уже существует.")
                else:
                    groups[group_name] = []
                    print(f"Группа '{group_name}' создана.")
            else:
                print("Имя группы не может быть пустым.")
        elif choice == '4':
            show_groups(groups)
        elif choice == '5':
            group_name = input("Введите имя группы: ").strip()
            code = input("Введите валютный код для удаления: ").strip()
            remove_currency_from_group(groups, group_name, code)
        elif choice == '6':
            group_name = input("Введите имя группы: ").strip()
            code = input("Введите валютный код для добавления: ").strip()
            add_currency_to_group(groups, group_name, code, data)
        elif choice == '7':
            save_groups(groups)
            print("Группы сохранены.")
        elif choice == '8':
            save_groups(groups)
            print("Данные сохранены. Выход.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")




