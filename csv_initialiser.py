import csv

def initialiseCsv(filename, header1, header2):
    try: # Try opening the file in read mode (throws an error if empty)
        with open(password_manager, "r") as file: # Open the csv file with the accounts
            reader = csv.DictReader(file) # Using the csv module DictReader function to make a dictionary with values from the csv
            for row in reader: # Go through each row in the csv file
                username = row["Username"]
                password = row["Password"]
    except: # If the file is empty then add the headers into the file
        with open(password_manager, "w", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["Username", "Password"])
