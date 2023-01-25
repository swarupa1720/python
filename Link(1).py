# import xlwings as xw
import json
import logging

import pandas as pd
from pathlib import Path

import utils


class Link(1):
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
        df1 = pd.DataFrame(df, index=range(0, 186))
        df1.dropna(thresh=4, inplace=True)
        df1.dropna(axis=1, how='all', inplace=True)
        df1.columns = df1.iloc[0]
        df1.drop(0, inplace=True)
        df1 = df1[df1["Pro User "].str.match('[^a-zA-Z]')]
        df2 = pd.DataFrame(df, index=range(186, 598))
        df2.dropna(thresh=3, inplace=True)
        df2.dropna(axis=1, how='all', inplace=True)
        df2.columns = df2.iloc[0]
        df2.drop(186, inplace=True)
        df2 = df2[df2["Pro User "].str.match('[^a-zA-Z]')]
        df3 = pd.DataFrame(df, index=range(598, 686))
        df3.dropna(thresh=2, inplace=True)
        df3.dropna(axis=1, how='all', inplace=True)
        df3.columns = df3.iloc[0]
        df3.drop(598, inplace=True)
        df3 = df3[df3["Pro User "].str.match('[^a-zA-Z]')]
        frames = [df1, df2, df3]
        df = pd.concat(frames, ignore_index=True)
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
