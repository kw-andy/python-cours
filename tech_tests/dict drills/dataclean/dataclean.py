import csv
from datetime import datetime


def data_csv_opener(csvinput):
    with open(csvinput, newline="") as datafile:
        linereader = csv.reader(datafile)
        end_list = []
        for line in linereader:
            end_list.append(list(line))
        headers = end_list[1]
        fin_raw_data = end_list[2:]
        return headers, fin_raw_data


def data_add_dictionaries(input):
    headers, data = input
    dictio = {}
    final_liste = []
    for elts in data:
        for idx_elts, val_elts in enumerate(elts):
            dictio[headers[idx_elts]] = val_elts
        final_liste.append(dictio.copy())
    return final_liste


def change_string_date(data):
    input = data
    for idx_in_input, values_in_input in enumerate(input):
        for key in "hiredate", "departdate":
            if values_in_input.get(key) not in {"", None}:
                values_in_input[key] = datetime.strptime(
                    values_in_input[key], "%d/%m/%y"
                ).strftime("%d-%m-%Y")
    return input


if __name__ == "__main__":
    change_string_date(data_add_dictionaries(data_csv_opener("data.csv")))
