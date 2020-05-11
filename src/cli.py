"""A file to extract the csv files"""
from __future__ import print_function
import csv
from src.libs.parser_util import get_data_from_line


DATA_INPUT_DIR = "../data/input/final_alert_data.csv"
DATA_OUTPUT_DIR = "../data/output/parsed_alert_data.csv"
WRITING_HEADER = ["Alias", "EventDate", "Date" "TinyID", "Message", "Status", "CreatedAtDate",
                  "UpdatedAtDate", "Count", "Owner"]


def get_data_from_csv(file_name):
    """Returns selected and formatted data in a nested list"""
    lines = list()
    with open(file_name, "r+") as f_handle:
        csv_reader = csv.reader(f_handle)
        for line in csv_reader:
            message = line[3]
            if message.startswith("[AIRFLOW ALERT]"):
                lines.append(get_data_from_line(line))
    return lines


def write_data_to_csv(file_name, data):
    """Writes the data from a nested list into a csv file"""
    with open(file_name, "w+") as f_handle:
        csv_writer = csv.writer(f_handle)
        csv_writer.writerow(WRITING_HEADER)
        for line in data:
            csv_writer.writerow(line)


def run():
    """Main function of the program"""
    data = get_data_from_csv(DATA_INPUT_DIR)
    write_data_to_csv(DATA_OUTPUT_DIR, data)


run()
