import pandas as pd

import DataFetchers.util as util
import DataFetchers.DataClass as DataClass

class SRTPAdherence(DataClass.Dataset):
    def __init__(self):
        super().__init__()
        self.name = "SRTPAdherence"
        self.sourceDataExtension = "csv"
        self.columnTypes = {}

    def downloadSourceFile(self):
        url = "https://www.europeanpaymentscouncil.eu/sites/default/files/participants_export/srtp/srtp.csv"
        filePath = self.getFilePath(util.SourceFileFolderName)
        util.urlToFile(url, filePath)

    def sourceFileToCommonFormat(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, encoding='utf-8')
        df.to_csv(self.getFilePath(util.CommonFormatFileFolderName), index=False, encoding='utf-8')