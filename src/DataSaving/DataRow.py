import util as util

class DataRow:
    def __init__(self, FileIndex, Key, dataDict):
        self.DataRowId = None
        self.FileIndex = FileIndex
        self.Key = Key
        self.DataDict = dataDict
        self.hash = None
        self.TableName = util.TableNames["DataRows"]

    def insertDataRowIntoDB(self, FileId, connection):
        query = f"""INSERT INTO {self.TableName} (FileId, FileIndex, Key, DataDict) VALUES (?, ?, ?, ?)"""
        dataDictStr = str(self.DataDict)
        cursor = connection.execute(
            query, (FileId, self.FileIndex, self.Key, dataDictStr)
        )
        self.DataRowId = cursor.lastrowid

