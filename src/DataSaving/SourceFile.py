import datetime
import util as util
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
        self.downloadTimestamp = None

        self.validFromTimestamp = None
        self.numRows = None


    def insertSourceFileIntoDB(self):
        query = f"""INSERT INTO {self.TableName} (DatasetId, Status) VALUES (?, ?)"""
        cursor = self.connection.execute(query, (self.DatasetId.value, util.FileStatus.New.value))
        self.SourceFileId = cursor.lastrowid
        self.path = os.path.join(self.sourceFileFolder, str(self.SourceFileId))

    def updateFileStatus(self, status):
        query = f"""UPDATE {self.TableName} SET Status = ? WHERE SourceFileId = ?"""
        self.connection.execute(query, (status.value, self.SourceFileId))
    
    def addMetadataToDB(self):
        query = f"""UPDATE {self.TableName} 
                   SET Hash = ?, DownloadTimestamp = ?, NumRows = ?, ValidFromTimestamp = ?
                   WHERE SourceFileId = ?"""
        self.connection.execute(query, (self.hash, self.downloadTimestamp, self.numRows, self.validFromTimestamp, self.SourceFileId))
        self.updateFileStatus(util.FileStatus.FileInfoAdded)

    def getMetadataFromDB(self):
        query = f"""SELECT Hash, NumRows, DownloadTimestamp, ValidFromTimestamp 
                   FROM {self.TableName} 
                   WHERE SourceFileId = ?"""
        cursor = self.connection.execute(query, (self.SourceFileId,))
        row = cursor.fetchone()
        if row:
            self.hash = row[0]
            self.numRows = row[1]
            self.downloadTimestamp = row[2]
            self.validFromTimestamp = row[3]

    def updateToError(self, Note):
        query = f"""UPDATE {self.TableName} 
                   SET Status = ?, Note = ? 
                   WHERE SourceFileId = ?"""
        self.connection.execute(query, (util.FileStatus.Error.value, Note, self.SourceFileId))

    def calculateFileHash(self):
        hasher = hashlib.sha256()
        with open(self.path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
                
        self.hash = hasher.hexdigest()

    def getDownloadTimestamp(self):
        creationtime = os.path.getctime(self.path)
        dateTimeObj =  datetime.datetime.fromtimestamp(creationtime)
        self.downloadTimestamp =  dateTimeObj.isoformat()