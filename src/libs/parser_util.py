"""A file to parse the given csv file."""
from __future__ import print_function
import re


def _get_dag_name_from_string(dag_str):
    """Returns the selected dag name from the string."""
    if "." in dag_str:
        starting_index = dag_str.find("pr-") + 3
        ending_index = dag_str.find(".")
    elif "-" in dag_str:
        starting_index = dag_str.find("pr-") + 3
        ending_index = dag_str.find("-", starting_index)
    else:
        return dag_str
    dag_name = dag_str[starting_index:ending_index]
    return dag_name


def _get_date_from_string(date_str):
    """Gets the date from a string"""
    match = re.search(r"\d{4}-\d{2}-\d{2}.*$", date_str)
    if match:
        return date_str[match.start():match.end()]
    return None


def get_data_from_line(line):
    """Gets all of the necessary data from the line"""
    alias = _get_dag_name_from_string(line[1])
    event_date = _get_date_from_string(line[1])
    tiny_id = line[2]
    message = line[3]
    status = line[4]
    created_at_date = line[9]
    updated_at_date = line[11]
    count = line[12]
    owner = line[13]
    data = [alias, event_date, tiny_id, message, status,
            created_at_date, updated_at_date, count, owner]
    return data
