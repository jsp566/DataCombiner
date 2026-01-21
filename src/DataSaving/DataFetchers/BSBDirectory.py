import csv

import enums as enums
import util as util
import DataSaving.DataFetcher as DataFetcher
import DataSaving.DataRow as DataRow


class BSBDirectory(DataFetcher.DataFetcher):
    def __init__(self, connection, SourceFileFolder):
        super().__init__(connection, SourceFileFolder)
        self.DatasetId = enums.DatasetId.BSBDirectory
        self.name = "BSBDirectory"
        self.documentation = "https://auspaynet.com.au/BSBLinks"
        self.keyColumns = ["BSB Code"]

    def downloadSourceFile(self, filePath):
        url = r"https://auspaynetbsbpublic.blob.core.windows.net/bsb-reports/BSBDirectoryFull.csv"
        util.urlToFile(url, filePath)

    def getValidFromDatetime(self, downloadedFile):
        downloadedFile.validFromDatetime = downloadedFile.downloadDatetime

    def createDataRowGenerator(self, downloadedFile):
        fields = ["BSB Code", 
                  "FI Mnemonic",
                  "BSB Name",
                  "Address",
                  "Suburb",
                  "State",
                  "Postcode",
                  "Stream Code",]
        
        with open(downloadedFile.path, "r") as f:
            data = csv.DictReader(f, fieldnames=fields)

            for entryindex, entry in enumerate(data, start=1):
                key = ",".join([str(entry[col]) for col in self.keyColumns])
                row = DataRow.DataRow(self.DatasetId, downloadedFile.SourceFileId, entryindex, key, entry)
                yield row

    def interpretDataRow(self, row):

        # BSB Code

        # FI Mnemonic

        # BSB Name

        # Stream Code?

        raise NotImplementedError("This method should be overridden by subclasses?")
