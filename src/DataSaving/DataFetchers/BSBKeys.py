import csv

import enums as enums
import util as util
import DataSaving.DataFetcher as DataFetcher
import DataSaving.DataRow as DataRow


class BSBKeys(DataFetcher.DataFetcher):
    def __init__(self, connection, SourceFileFolder):
        super().__init__(connection, SourceFileFolder)
        self.DatasetId = enums.DatasetId.BSBKeys
        self.name = "BSBKeys"
        self.documentation = "https://auspaynet.com.au/BSBLinks"
        self.keyColumns = ["BSB Owner"]

    def downloadSourceFile(self, filePath):
        url = r"https://auspaynetbsbpublic.blob.core.windows.net/bsb-reports/key%20to%20abbreviations%20and%20bsb%20numbers.csv"
        util.urlToFile(url, filePath)

    def getValidFromDatetime(self, downloadedFile):
        downloadedFile.validFromDatetime = downloadedFile.downloadDatetime
        
    def createDataRowGenerator(self, downloadedFile):
        with open(downloadedFile.path, "r") as f:
            data = csv.DictReader(f)

            for entryindex, entry in enumerate(data, start=1):
                key = ",".join([str(entry[col]) for col in self.keyColumns])
                row = DataRow.DataRow(self.DatasetId, downloadedFile.SourceFileId, entryindex, key, entry)
                yield row

    def interpretDataRow(self, row):

        # BSB Owner
        

        # Owner Name

        # BSB Prefix

        raise NotImplementedError("This method should be overridden by subclasses?")
