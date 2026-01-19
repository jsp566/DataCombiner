import util as util

class DataRow:
    def __init__(self, dateasetid, sourceFileId, FileIndex, Key, dataDict):
        self.DataRowId = None
        self.datasetId = dateasetid
        self.sourceFileId = sourceFileId
        self.FileIndex = FileIndex
        self.Key = Key
        self.DataDict = dataDict
        self.hash = None
        self.TableName = util.TableNames["DataRows"]

    def insertDataRowIntoDB(self, connection):
        query = f"""INSERT INTO {self.TableName} (DatasetId, SourceFileId, FileIndex, Key, DataDict) VALUES (?, ?, ?, ?, ?)"""
        dataDictStr = str(self.DataDict)
        cursor = connection.execute(
            query, (self.datasetId.value, self.sourceFileId, self.FileIndex, self.Key, dataDictStr)
        )
        self.DataRowId = cursor.lastrowid

