import pandas as pd

import util as util
import DataSaving.DataFetcher as DataFetcher


class SDDCoreAdherence(DataFetcher.DataFetcher):
    def __init__(self):
        super().__init__()
        self.name = "SDDCoreAdherence"
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

    def downloadSourceFile(self):
        url = "https://www.europeanpaymentscouncil.eu/sites/default/files/participants_export/sdd_core/sdd_core.csv"
        filePath = self.getFilePath(util.SourceFileFolderName)
        util.urlToFile(url, filePath)

    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, encoding="utf-8")
        df.to_csv(
            self.getFilePath(util.CSVFileFolderName), index=False, encoding="utf-8"
        )
