import csv
import pandas as pd
import os


def read_transactions_from_csv(file_path_csv):
    """Считывает финансовые операции из CSV-файла."""
    transactions = []

    if not os.path.exists(file_path_csv):
        print(f"Ошибка: Файл '{file_path_csv}' не найден.")
        return transactions

    try:
        with open(file_path_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")

    return transactions


def read_transactions_from_excel(file_path_xlsx):
    """Считывает финансовые операции из Excel-файла"""
    transactions = []

    if not os.path.exists(file_path_xlsx):
        print(f"Ошибка: Файл '{file_path_xlsx}' не найден.")
        return transactions

    try:
        df = pd.read_excel(file_path_xlsx)
        transactions = df.to_dict(orient='records')
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")

    return transactions


print("Текущая рабочая директория:", os.getcwd())


csv_path = os.path.abspath('transactions.csv')
excel_path = os.path.abspath('transactions_excel.xlsx')


read_transactions_from_csv(csv_path)
read_transactions_from_excel(excel_path)
