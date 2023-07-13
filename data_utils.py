import csv


def read_csv(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        data_list = []
        for row in csvreader:
            data_list.append(row)
        return data_list


def merge_data(pr_file, st_file):
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
    vidove_data = read_csv(vidove_file)

    for i, row in enumerate(merged_data):
        for vid_row in vidove_data[1:]:
            if row[5] == vid_row[0]:
                merged_data[i].append(vid_row[1])
                break

    return merged_data
