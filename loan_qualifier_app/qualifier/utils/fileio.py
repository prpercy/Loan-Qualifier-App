# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, data):
    """Writes the data into the CSV file at the path provided.

    Args:
        csvpath (Path): The csv file path.
        data: list that needs to be written in csv file
        header: header in the csv file
    """
    with open(csvpath, "w", newline='') as csvfile:
       csvwriter =  csv.writer(csvfile)
       
       # if just one row in the list then write row or else write rows
       if len(data) <=1:
            csvwriter.writerow(data)
       else:
            csvwriter.writerows(data)