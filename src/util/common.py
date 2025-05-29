import csv 
from datetime import datetime
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


def getTimestamp():
    filename1 = datetime.now().strftime("%d%m%y_%H%M")
    timestamp_string = str(filename1)
    return timestamp_string

def read_test_data_from_csv():
   test_data = []
   with open(DATA_FILE, newline='') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           test_data.append(row)
   return test_data

def waitfor(interval):
    self.driver.implicitly_wait(interval) # seconds


