import csv 
from pathlib import Path

dataFile='data.csv'
cfgFileDirectory='config'
file_path = 'data.csv'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE  = BASE_DIR.joinpath(cfgFileDirectory).joinpath(dataFile)

def get_data():
    data = []
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data=[tuple(row) for row in reader]
    return data
 
print(get_data())

def read_test_data_from_csv():
   test_data = []
   with open(DATA_FILE, newline='') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           test_data.append(row)
   return test_data
