import pandas as pd
import csv

import enums as enums
import util as util
import DataSaving.DataFetcher as DataFetcher
import DataSaving.DataRow as DataRow


class SDDB2BAdherence(DataFetcher.DataFetcher):
    def __init__(self, connection, SourceFileFolder):
        super().__init__(connection, SourceFileFolder)
        self.DatasetId = enums.DatasetId.SDDB2BAdherence
        self.name = "SDDB2BAdherence"
        self.sourceDataExtension = "csv"
        self.columnTypes = {
            "Country": None,
            "ParticipantName": None,
            "Address": None,
            "City": None,
            "BIC": None,
            "Readiness Date": None,
            "Scheme Leaving Date": None,
            "Scheme Options": None,
        }
        self.documentation = "https://www.europeanpaymentscouncil.eu/what-we-do/be-involved/register-participants/registers-participants-sepa-payment-schemes"
        self.keyColumns = ["BIC"]


    def downloadSourceFile(self, filePath):
        url = "https://www.europeanpaymentscouncil.eu/sites/default/files/participants_export/sdd_b2b/sdd_b2b.csv"
        util.urlToFile(url, filePath)

    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, encoding="utf-8")
        df.to_csv(
            self.getFilePath(util.CSVFileFolderName), index=False, encoding="utf-8"
        )

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
        
        # ParticipantName

        # BIC

        # Presence 
        
        raise NotImplementedError("This method should be overridden by subclasses?")
