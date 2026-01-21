import os
import util as util
import enums as enums
import DataSaving.SourceFile as SourceFile
import datetime

class DataFetcher:
    def __init__(self, connection, SourceFileFolder):
        self.connection = connection
        self.SourceFileFolder = SourceFileFolder

        # Set by subclasses
        self.DatasetId = None

    def downloadSourceFile(self, downloadedFilepath):
        raise NotImplementedError("This method should be overridden by subclasses")

    def getValidFromDatetime(self, downloadedFile): # maybe just path
        raise NotImplementedError("This method should be overridden by subclasses")

    def createDataRowGenerator(self, downloadedFile):
        raise NotImplementedError("This method should be overridden by subclasses")

    def interpretDataRow(self, row):
        raise NotImplementedError("This method should be overridden by subclasses?")

    def getNewSourceFile(self):
        # Create row in DB and get its ID
        downloadedFile = SourceFile.SourceFile(self.connection, self.SourceFileFolder, self.DatasetId)
        downloadedFile.insertSourceFileIntoDB()
        self.connection.commit()

        self.downloadSourceFile(downloadedFile.path)
        downloadedFile.updateFileStatus(enums.FileStatus.Downloaded)
        self.connection.commit()

        downloadedFile.getDownloadDatetime()
        downloadedFile.calculateFileHash()
        downloadedFile.addMetadataToDB()
        self.connection.commit()

        return downloadedFile
    
    def insertSourceFileRowsIntoDB(self, downloadedFile):
        rows = self.createDataRowGenerator(downloadedFile)

        rowCounter = 0
        for row in rows:
            row.insertDataRowIntoDB(self.connection)
            self.interpretDataRow(row)
            rowCounter += 1
        
        downloadedFile.numRows = rowCounter


    def getNewData(self):
        downloadedFile = self.getNewSourceFile()      

        self.getValidFromDatetime(downloadedFile)

        self.insertSourceFileRowsIntoDB(downloadedFile)
        
        downloadedFile.addMetadataToDB()
        
        downloadedFile.updateFileStatus(enums.FileStatus.Processed)
        self.connection.commit()
