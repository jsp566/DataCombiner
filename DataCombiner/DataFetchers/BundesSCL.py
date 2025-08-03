import pandas as pd

import DataFetchers.util as util
import DataFetchers.DataClass as DataClass

class BundesSCL(DataClass.Dataset):
    def __init__(self):
        super().__init__()
        self.name = "BundesSCL"
        self.sourceDataExtension = "csv"
        self.columnTypes = {}

    def downloadSourceFile(self):
        url = "https://www.bundesbank.de/scl-directory"
        filePath = self.getFilePath(util.SourceFileFolderName)
        util.urlToFile(url, filePath)
    
    def sourceFileToCommonFormat(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, sep=";", encoding='utf-8')
        df.to_csv(self.getFilePath(util.CommonFormatFileFolderName), index=False, encoding='utf-8')