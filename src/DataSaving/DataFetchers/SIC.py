import pandas as pd

import util as util
import DataSaving.DataFetcher as DataFetcher


class SIC(DataFetcher.DataFetcher):
    def __init__(self):
        super().__init__()
        self.name = "SIC"
        self.sourceDataExtension = "csv"
        self.columnTypes = {
            "IID/QR-IID": None,
            "Valid on": None,
            "Concatenation": None,
            "New IID/QR-IID": None,
            "SIC IID": None,
            "Headquarters": None,
            "IID type": None,
            "QR-IID allocation": None,
            "Name of bank/institution": None,
            "Street Name": None,
            "Building Number": None,
            "Post Code": None,
            "Town Name": None,
            "Country": None,
            "BIC": None,
            "SIC participation": None,
            "RTGS customer payments, CHF": None,
            "IP customer payments, CHF": None,
            "euroSIC participation": None,
            "LSV+/BDD, CHF": None,
            "LSV+/BDD, EUR": None,
        }
        self.documentation = "https://www.six-group.com/en/products-services/banking-services/interbank-clearing/online-services/download-bank-master.html#tfl_XRzX2xpc3Q=/year/2025"

    def downloadSourceFile(self):
        url = "https://api.six-group.com/api/epcd/bankmaster/v3/bankmaster_V3.csv"
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        util.urlToFile(url, filePath)

    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(
            filePath,
            sep=";",
            encoding="utf-8",
            dtype=str,
            usecols=list(self.columnTypes.keys()),
        )
        df.to_csv(
            self.getFilePath(util.CSVFileFolderName), index=False, encoding="utf-8"
        )
