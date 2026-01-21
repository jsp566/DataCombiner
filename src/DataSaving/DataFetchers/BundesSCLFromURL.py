import pandas as pd
from datetime import datetime
import csv

import enums as enums
import util as util
import DataSaving.DataFetcher as DataFetcher
import DataSaving.DataRow as DataRow


class BundesSCLFromURL(DataFetcher.DataFetcher):
    def __init__(self, connection, SourceFileFolder):
        super().__init__(connection, SourceFileFolder)
        self.DatasetId = enums.DatasetId.BundesSCLFromURL
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
        self.keyColumns = ["BIC"]

    def downloadSourceFile(self, filePath):
        url = "https://www.bundesbank.de/scl-directory"
        util.urlToFile(url, filePath)

    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, sep=";", encoding="utf-8", skiprows=1)
        df.to_csv(
            self.getFilePath(util.CSVFileFolderName), index=False, encoding="utf-8"
        )

    def getValidFromDatetime(self, downloadedFile):
        with open(downloadedFile.path, "r") as f:
            first_line = f.readline()

        dateStr = first_line.split(";")[0].replace("Gueltig ab / valid from ", "")
        
        downloadedFile.validFromDatetime = datetime.strptime(dateStr, "%d.%m.%Y")
        
    def createDataRowGenerator(self, downloadedFile):
        fields = [
            "BIC",
            "Name",
            "SERVICE SCT",
            "SERVICE COR",
            "SERVICE COR1",
            "SERVICE B2B",
            "SERVICE SCC",
        ]
        with open(downloadedFile.path, "r") as f:
            data = csv.DictReader(f, delimiter=";", fieldnames=fields)

            next(data) # Skip first line with date info
            next(data)  # Skip header row

            for entryindex, entry in enumerate(data, start=1):
                key = ",".join([str(entry[col]) for col in self.keyColumns])
                row = DataRow.DataRow(self.DatasetId, downloadedFile.SourceFileId, entryindex, key, entry)
                yield row

    def interpretDataRow(self, row):

        # BIC
         
        # Name
         
        # SERVICE SCT
         
        # SERVICE COR

        # SERVICE COR1
        
        # SERVICE B2B
        
        # SERVICE SCC

        raise NotImplementedError("This method should be overridden by subclasses?")
