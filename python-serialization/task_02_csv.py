#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON format and writes it to data.json.
    Returns True if successful, False otherwise.
    """
    try:
        # Read CSV file and convert rows to dictionaries
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Write JSON data to data.json
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False

