import json
import csv
import pandas as pd
import re


# Функции для загрузки данных
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def load_xlsx(filename):
    df = pd.read_excel(filename)
    return df.to_dict(orient='records')


# Функции фильтрации
def search_transactions(transactions, search_str):
    pattern = re.compile(search_str, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def filter_by_status(transactions, status):
    status = status.lower()  # Приводим статус к нижнему регистру для корректной работы
    return [transaction for transaction in transactions if transaction.get('status', '').lower() == status]


def count_by_category(transactions, categories):
    category_counts = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
    return category_counts


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Ваш выбор: ")
    if file_choice == '1':
        filename = input("Введите имя JSON-файла: ")
        transactions = load_json(filename)
    elif file_choice == '2':
        filename = input("Введите имя CSV-файла: ")
        transactions = load_csv(filename)
    elif file_choice == '3':
        filename = input("Введите имя XLSX-файла: ")
        transactions = load_xlsx(filename)
    else:
        print("Неверный выбор.")
        return

    print(f"Для обработки выбраны транзакции из файла: {filename}")

    valid_statuses = ['executed', 'canceled', 'pending']
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ")
        if status.lower() in valid_statuses:
            break
        else:
            print(f"Статус операции '{status}' недоступен.")

    filtered_transactions = filter_by_status(transactions, status)

    print(f"Операции отфильтрованы по статусу: {status.upper()}")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = sort_order == 'по убыванию'
        filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == 'да':
        filtered_transactions = [transaction for transaction in filtered_transactions if
                                 'RUB' in transaction.get('amount', '')]

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_choice == 'да':
        search_str = input("Введите слово для поиска в описаниях: ")
        filtered_transactions = search_transactions(filtered_transactions, search_str)

    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction.get('date')} {transaction.get('description')}")
            print(f"Сумма: {transaction.get('amount')}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


main()
