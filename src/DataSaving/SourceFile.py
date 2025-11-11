import util as util
import hashlib
import os

class SourceFile:
    def __init__(self, connection, sourceFileFolder, DatasetId):
        self.connection = connection
        self.sourceFileFolder = sourceFileFolder
        self.DatasetId = DatasetId
        self.TableName = util.TableNames["SourceFiles"]
        self.FileId = None
        self.path = None
        self.hash = None
        self.numRows = None
        self.downloadTimestamp = None
        self.validFromTimestamp = None

    def insertSourceFileIntoDB(self):
        query = f"""INSERT INTO {self.TableName} (DatasetId, Status) VALUES (?, ?)"""
        cursor = self.connection.execute(query, (self.DatasetId, util.FileStatus.New.value))
        self.FileId = cursor.lastrowid
        self.path = os.path.join(self.sourceFileFolder, str(self.FileId))

    def updateFileStatus(self, status):
        query = f"""UPDATE {self.TableName} SET Status = ? WHERE FileId = ?"""
        self.connection.execute(query, (status.value, self.FileId))
    
    def addMetadataToDB(self):
        query = f"""UPDATE {self.TableName} 
                   SET Hash = ?, NumRows = ?, DownloadTimestamp = ?, ValidFromTimestamp = ? 
                   WHERE FileId = ?"""
        self.connection.execute(query, (self.hash, self.numRows, self.downloadTimestamp, self.validFromTimestamp, self.FileId))

    def getMetadataFromDB(self):
        query = f"""SELECT Hash, NumRows, DownloadTimestamp, ValidFromTimestamp 
                   FROM {self.TableName} 
                   WHERE FileId = ?"""
        cursor = self.connection.execute(query, (self.FileId,))
        row = cursor.fetchone()
        if row:
            self.hash = row[0]
            self.numRows = row[1]
            self.downloadTimestamp = row[2]
            self.validFromTimestamp = row[3]

    def updateToError(self, Note):
        query = f"""UPDATE {self.TableName} 
                   SET Status = ?, Note = ? 
                   WHERE FileId = ?"""
        self.connection.execute(query, (util.FileStatus.Error.value, Note, self.FileId))

    def calculateFileHash(self):
        hasher = hashlib.sha256()
        with open(self.path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
                
        self.hash = hasher.hexdigest()