from datetime import datetime
import util as util
import enums as enums
import hashlib
import os

class SourceFile:
    def __init__(self, connection, sourceFileFolder, DatasetId):
        self.connection = connection
        self.sourceFileFolder = sourceFileFolder
        self.TableName = util.TableNames["SourceFiles"]

        self.DatasetId = DatasetId
        self.SourceFileId = None
        self.path = None

        self.hash = None
        self.downloadDatetime = None

        self.validFromDatetime = None
        self.numRows = None


    def insertSourceFileIntoDB(self):
        query = f"""INSERT INTO {self.TableName} (DatasetId, Status) VALUES (?, ?)"""
        cursor = self.connection.execute(query, (self.DatasetId.value, enums.FileStatus.New.value))
        self.SourceFileId = cursor.lastrowid
        self.path = os.path.join(self.sourceFileFolder, str(self.SourceFileId))

    def updateFileStatus(self, status):
        query = f"""UPDATE {self.TableName} SET Status = ? WHERE SourceFileId = ?"""
        self.connection.execute(query, (status.value, self.SourceFileId))
    
    def addMetadataToDB(self):
        query = f"""UPDATE {self.TableName} 
                   SET Hash = ?, DownloadDatetime = ?, NumRows = ?, ValidFromDatetime = ?
                   WHERE SourceFileId = ?"""
        DownloadDatetimestr = self.downloadDatetime.isoformat() if self.downloadDatetime is not None else None
        ValidFromDatetimestr = self.validFromDatetime.isoformat() if self.validFromDatetime is not None else None
        self.connection.execute(query, (self.hash, DownloadDatetimestr, self.numRows, ValidFromDatetimestr, self.SourceFileId))
        self.updateFileStatus(enums.FileStatus.FileInfoAdded)

    def updateToError(self, Note):
        query = f"""UPDATE {self.TableName} 
                   SET Status = ?, Note = ? 
                   WHERE SourceFileId = ?"""
        self.connection.execute(query, (enums.FileStatus.Error.value, Note, self.SourceFileId))

    def calculateFileHash(self):
        hasher = hashlib.sha256()
        with open(self.path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
                
        self.hash = hasher.hexdigest()

    def getDownloadDatetime(self):
        creationtime = os.path.getctime(self.path)
        self.downloadDatetime =  datetime.fromtimestamp(creationtime)