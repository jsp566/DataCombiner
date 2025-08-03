import pandas as pd

import DataFetchers.util as util
import DataFetchers.DataClass as DataClass

class SDDB2BAdherence(DataClass.Dataset):
    def __init__(self):
        super().__init__()
        self.name = "SDDB2BAdherence"
        self.sourceDataExtension = "csv"
        self.columnTypes = {}

    def downloadSourceFile(self):
        url = "https://www.europeanpaymentscouncil.eu/sites/default/files/participants_export/sdd_b2b/sdd_b2b.csv"
        filePath = self.getFilePath(util.SourceFileFolderName)
        util.urlToFile(url, filePath)

    def sourceFileToCommonFormat(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, encoding='utf-8')
        df.to_csv(self.getFilePath(util.CommonFormatFileFolderName), index=False, encoding='utf-8')