import csv


def read_csv(csv_file):
    # Функция за четене на данни от CSV файла
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        data_list = []
        for row in csvreader:
            data_list.append(row)
        return data_list


def merge_data(pr_file, st_file):
    # Функция за сливане на данни от два CSV файла
    pr_data = read_csv(pr_file)
    st_data = read_csv(st_file)

    merged_data = []
    for pr_row in pr_data[1:]:
        for st_row in st_data[1:]:
            if pr_row[0] == st_row[0]:
                merged_row = pr_row + st_row[1:]
                merged_data.append(merged_row)

    merged_data_sorted = sorted(merged_data, key=lambda x: x[1])
    return merged_data_sorted


def merge_group_data(merged_data, vidove_file):
    # Функция за сливане на данни от трети CSV файл
    vidove_data = read_csv(vidove_file)

    for i, row in enumerate(merged_data):
        for vid_row in vidove_data[1:]:
            if row[5] == vid_row[0]:
                merged_data[i].append(vid_row[1])
                break

    return merged_data


def calculate_group_sum(merged_data):
    # Функция за изчисляване на общата сума за всяка група
    group_sum = {}
    for row in merged_data:
        group_code = row[6]
        quantity = int(row[3])
        price = int(row[2])
        total = quantity * price

        if group_code in group_sum:
            group_sum[group_code] += total
        else:
            group_sum[group_code] = total

    return group_sum


def get_group_name(group_code):
    # Функция за получаване на името на групата по код
    with open('vidove.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            code, name = line.strip().split(',')
            if code == str(group_code):
                return name
    return "Unknown"


def filter_data_by_amount(data, amount):
    # Функция за филтриране на данните според сумата
    filtered_data = []
    for item in data:
        if item['Сума'] >= amount:
            filtered_data.append(item)
    return filtered_data


def merge_data_sum(sales_file, products_file):
    # Функция за сливане на данни и изчисляване на общата сума
    sales_data = read_csv(sales_file)
    products_data = read_csv(products_file)
    merged_data = []

    for sale in sales_data[1:]:
        product_code = sale[0]
        sale_date = sale[1]
        price = float(sale[2])
        quantity = int(sale[3])
        total = price * quantity

        merged_row = [product_code, sale_date, price, quantity, total]
        for product in products_data[1:]:
            if product[0] == product_code:
                merged_row.extend(product[1:])
                break

        merged_data.append(merged_row)

    return merged_data
