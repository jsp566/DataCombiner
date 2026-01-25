import enums as enums
import util as util
import DataSaving.BankCode as BankCode
import DataSaving.Relations.BankCodeRelation as BankCodeRelation
import DataSaving.Relations.BankCodeRelation as BankCodeRelation
import DataSaving.Relations.CorrespondentRelation as CorrespondentRelation
import DataSaving.Relations.NetworkRelation as NetworkRelation

class DataRow:
    def __init__(self, connection, dateasetid, sourceFileId, FileIndex, Key, dataDict):
        self.connection = connection
        self.DataRowId = None
        self.datasetId = dateasetid
        self.sourceFileId = sourceFileId
        self.FileIndex = FileIndex
        self.Key = Key
        self.DataDict = dataDict
        self.hash = None
        self.TableName = util.TableNames["DataRows"]

    def insertDataRowIntoDB(self):
        query = f"""INSERT INTO {self.TableName} (DatasetId, SourceFileId, FileIndex, Key, DataDict) VALUES (?, ?, ?, ?, ?)"""
        dataDictStr = str(self.DataDict)
        cursor = self.connection.execute(
            query, (self.datasetId.value, self.sourceFileId, self.FileIndex, self.Key, dataDictStr)
        )
        self.DataRowId = cursor.lastrowid

    def createBankCode(self, bankCode, bankCodeType):
        bankCodeObj = BankCode.BankCode(bankCodeType, bankCode)
        bankCodeObj.insertBankCodeIntoDB(self.connection)
        return bankCodeObj

    def createBankCodeRelation(self, bankCode, bankCodeType, relationType):
        bankCodeObj = self.createBankCode(bankCode, bankCodeType)

        bankCodeRelationObj = BankCodeRelation.BankCodeRelation(self, bankCodeObj, relationType)
        bankCodeRelationObj.insertBankCodeRelationIntoDB(self.connection)
        return bankCodeObj

    def createNetworkRelation(self, bankCodeObj, network):
        networkRelationObj = NetworkRelation.NetworkRelation(self, bankCodeObj, network)
        networkRelationObj.insertNetworkRelationIntoDB(self.connection)

    def createCorrespondentRelation(self, correspondentKey, relationType):
        pass
        
    def interpretBIC(self, bicCode, relationType):
        if len(bicCode) == 8:
            bicCode = bicCode + "XXX"

        assert len(bicCode) == 11

        biclength = len(bicCode)
        bankCodetypes = {4: enums.bankcodetype.BIC4,
                         6: enums.bankcodetype.BIC6,
                         8: enums.bankcodetype.BIC8,
                        11: enums.bankcodetype.BIC11}
        
        for length, bankCodeTypeId in bankCodetypes.items():
            if biclength >= length:
                codePart = bicCode[:length]
                self.createBankCodeRelation(codePart, bankCodeTypeId, relationType)
