import pandas as pd

import DataCombiner.DataFetchers.util as util
import DataCombiner.DataClass as DataClass

class SIC(DataClass.Dataset):
    def __init__(self):
        super().__init__()
        self.name = "SIC"
        self.sourceDataExtension = "csv"
        self.columnTypes = {}
        self.documentation = ""

    def downloadSourceFile(self):
        url = "https://api.six-group.com/api/epcd/bankmaster/v3/bankmaster_V3.csv"
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        util.urlToFile(url, filePath)

    def sourceFileToCSV(self):
        filePath = self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension)
        df = pd.read_csv(filePath, sep=";", encoding='utf-8')
        df.to_csv(self.getFilePath(util.CSVFileFolderName), index=False, encoding='utf-8')