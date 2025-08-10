import pandas as pd

import DataCombiner.DataFetchers.util as util
import DataCombiner.DataClass as DataClass

class SDDCoreAdherence(DataClass.Dataset):
    def __init__(self):
        super().__init__()
        self.name = "SDDCoreAdherence"
        self.sourceDataExtension = "csv"
        self.columnTypes = {}
        self.documentation = ""

    def downloadSourceFile(self):
        url = "https://www.europeanpaymentscouncil.eu/sites/default/files/participants_export/sdd_core/sdd_core.csv"
        filePath = self.getFilePath(util.SourceFileFolderName)
        util.urlToFile(url, filePath)

    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, encoding='utf-8')
        df.to_csv(self.getFilePath(util.CSVFileFolderName), index=False, encoding='utf-8')