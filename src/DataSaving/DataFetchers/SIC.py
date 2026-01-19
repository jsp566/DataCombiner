import pandas as pd
import json
import datetime

import util as util
import DataSaving.DataFetcher as DataFetcher
import DataSaving.DataRow as DataRow


class SIC(DataFetcher.DataFetcher):
    def __init__(self, connection, SourceFileFolder):
        super().__init__(connection, SourceFileFolder)
        self.DatasetId = util.DatasetId.SIC
        self.name = "SIC"
        #self.documentation = "https://www.six-group.com/en/products-services/banking-services/interbank-clearing/online-services/download-bank-master.html#tfl_XRzX2xpc3Q=/year/2025"
        self.keyColumns = ["iid"]

    def downloadSourceFile(self, filePath):
        url = "https://api.six-group.com/api/epcd/bankmaster/v3/bankmaster.json"
        util.urlToFile(url, filePath)

    def getValidFromTimestamp(self, downloadedFile):
        with open(downloadedFile.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        dateStr = data["validOn"]
        downloadedFile.validFromTimestamp = datetime.datetime.strptime(dateStr, "%Y-%m-%d").isoformat()

    def createDataRowGenerator(self, downloadedFile):
        with open(downloadedFile.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for i, entry in enumerate(data["entries"], start=1):
            indexInFile = i
            key = ",".join([str(entry[col]) for col in self.keyColumns])
            row = DataRow.DataRow(self.DatasetId, downloadedFile.SourceFileId, indexInFile, key, entry)
            yield row
            

    def interpretDataRow(self, row):
        # interpret the data row according to SIC dataset specifics
        pass
