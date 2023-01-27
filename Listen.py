# import xlwings as xw
import json
import logging

import pandas as pd
from pathlib import Path

import utils


class Listen:
    response = {}
    logging.basicConfig(filename='app.log', filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')

    def __init__(self, source_path, destination_path, vendor_name):
        self.source_path = source_path
        self.destination_path = destination_path
        self.vendor_name = vendor_name
        self.response["message"] = "cleared sheet successfully"
        self.response["source"] = source_path
        self.response["destination"] = destination_path

    def get_response(self):
        return self.response
        # print(self.response())

    def clean_xl(self, source_path, destination_path, response={}):
        # source_path = Path.cwd() / "data/qsc.xlsx"
        # print(source_path)
        # Create Utility class object to use common methods
        ut = utils.Utils()
        df = pd.read_csv(source_path)

        # Remove 3 rows
        # df.drop(index=[0, 1, 2])
        # df = df.iloc[3:]

        # Removing unwanted columns
        df = df.dropna(axis=1, how='all')
        df = df.dropna(thresh=3, inplace=True)

        #df = df[df["RESELLER PRICE "].str.match('[^a-zA-Z]')]
        # Remove empty rows
        # df.dropna(thresh=4, inplace=True)
        # df.dropna(axis=1, how='all', inplace=True)

        # df['Dealer '] = df['Dealer '].str.replace('$', '')

        # df = df[pd.to_numeric(df['Dealer '], errors='coerce').notnull()]
        #
        # for x in range(0, 1):
        #     df['Dealer '] = "$" + df['Dealer ']

        # df = df.fillna(method='ffill')
        # df = df.dropna(thresh=2)

        # Remove first column if we are not using usecols in read_excel method of pd
        # df = df.iloc[:, 1:]

        # Export to CSV
        # df.to_csv(Path.cwd() / "data/cleaned.csv", index=False)
        df.to_csv(destination_path, header=True, sep=',', index=False)

        response['message'] = "Cleaned Xls"
        response['status'] = "success"
        response['filePath'] = destination_path
        # print(df)
        print(json.dumps(response))
