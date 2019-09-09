#! /usr/bin/python

import csv
import os

RAW_DATA_PATH='./RawData/'
STOCK_LIST=RAW_DATA_PATH + 'StockList.csv'
ELEC_LIST=RAW_DATA_PATH + 'elec_list.csv'
OUTPUT_LIST='output.csv'

def load_elec_list():
    with open(ELEC_LIST, mode='r') as infile:
        reader = csv.reader(infile)
        ele_dict = {rows[0] : 1 for rows in reader}
    return ele_dict

def get_stockNo_from_stock_list(row):
    if row[0] == '=':
        return row[2:-1]

def filte(ele_dict):
    with open(STOCK_LIST, mode='r') as infile:
        rows = csv.reader(infile)

        if os.path.exists(OUTPUT_LIST):
            os.remove(OUTPUT_LIST)

        with open(OUTPUT_LIST, 'wb') as outputfile:
            writer = csv.writer(outputfile)
            heading = next(rows)
            heading[0] = heading[0][4:-1]
            writer.writerow(heading)
            for row in rows:
                stockNo = get_stockNo_from_stock_list(row[0])
                if ele_dict.has_key(stockNo):
                    row[0] = row[0][2:-1]
                    writer.writerow(row)

def load_and_filter():
    elec_dict = load_elec_list()
    filte(elec_dict)

load_and_filter()
