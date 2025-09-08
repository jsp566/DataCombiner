import pandas as pd

import DataCombiner.util as util
import DataCombiner.DataClass as DataClass


class BundesSCLFromURL(DataClass.Dataset):
    def __init__(self):
        super().__init__()
        self.name = "BundesSCLFromURL"
        self.sourceDataExtension = "csv"
        self.columnTypes = {
            "BIC": None,
            "Name": None,
            "SERVICE SCT": None,
            "SERVICE COR": None,
            "SERVICE COR1": None,
            "SERVICE B2B": None,
            "SERVICE SCC": None,
        }
        self.documentation = "https://www.bundesbank.de/en/tasks/payment-systems/rps/sepa-clearer/scl-directory/scl-directory-626672"

    def downloadSourceFile(self):
        url = "https://www.bundesbank.de/scl-directory"
        filePath = self.getFilePath(util.SourceFileFolderName)
        util.urlToFile(url, filePath)

    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, sep=";", encoding="utf-8", skiprows=1)
        df.to_csv(
            self.getFilePath(util.CSVFileFolderName), index=False, encoding="utf-8"
        )
