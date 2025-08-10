import pandas as pd

import DataCombiner.DataFetchers.util as util
import DataCombiner.DataClass as DataClass

class BundesSCL(DataClass.Dataset):
    def __init__(self):
        super().__init__()
        self.name = "BundesSCL"
        self.sourceDataExtension = "csv"
        self.columnTypes = {}
        self.documentation = ""

    def downloadSourceFile(self):
        url = "https://www.bundesbank.de/scl-directory"
        filePath = self.getFilePath(util.SourceFileFolderName)
        util.urlToFile(url, filePath)
    
    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, sep=";", encoding='utf-8')
        df.to_csv(self.getFilePath(util.CSVFileFolderName), index=False, encoding='utf-8')