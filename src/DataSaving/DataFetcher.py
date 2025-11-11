import os
import util as util
import DataSaving.SourceFile
import datetime

class DataFetcher:
    def __init__(self, connection, SourceFileFolder):
        self.connection = connection
        self.SourceFileFolder = SourceFileFolder

        # Set by subclasses
        self.DatasetId = None

    def downloadSourceFile(self, downloadedFile):
        raise NotImplementedError("This method should be overridden by subclasses")

    def createDataRowGenerator(self, downloadedFile):
        raise NotImplementedError("This method should be overridden by subclasses")

    def interpretDataRow(self, row):
        raise NotImplementedError("This method should be overridden by subclasses?")

    def getNewSourceFile(self):
        # Create row in DB and get its ID
        downloadedFile = SourceFile.SourceFile(self.connection, self.SourceFileFolder, self.DatasetId)
        downloadedFile.insertSourceFileIntoDB()

        self.downloadSourceFile(downloadedFile)
        downloadedFile.downloadTimestamp = datetime.datetime.now().isoformat()
        downloadedFile.calculateFileHash()
        downloadedFile.addMetadataToDB()
        return downloadedFile
    
    def insertSourceFileRowsIntoDB(self, downloadedFile):
        rows = self.createDataRowGenerator(downloadedFile)

        rowCounter = 0
        for row in rows:
            row.insertDataRowIntoDB(downloadedFile.FileId, self.connection)
            self.interpretDataRow(row)
            rowCounter += 1
        
        return rowCounter


    def getNewData(self):
        downloadedFile = self.getNewSourceFile()      

        rowCounter = self.insertSourceFileRowsIntoDB(downloadedFile)

        downloadedFile.numRows = rowCounter
        downloadedFile.addMetadataToDB()
        downloadedFile.updateFileStatus(util.FileStatus.Processed)
        self.connection.commit()
