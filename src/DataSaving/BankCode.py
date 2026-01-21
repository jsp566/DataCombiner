

import util as util


def interpretationfunction(connection, bankCodeTypeId, relationTypeId):
    def interpretationFunction(dataRow, bankCode):
        interpretBankCode(connection, bankCodeTypeId, bankCode, dataRow, relationTypeId)
    return interpretationFunction

def interpretBICfunction(connection, relationTypeId):
    def interpretationFunction(dataRow, bankCode):
        if len(bankCode) == 8:
            bankCode = bankCode + "XXX"

        biclength = len(bankCode)
        bankCodetypes = {4: util.bankcodetype.BIC4,
                         6: util.bankcodetype.BIC6,
                         8: util.bankcodetype.BIC8,
                        11: util.bankcodetype.BIC11}
        
        for length, bankCodeTypeId in bankCodetypes.items():
            if biclength >= length:
                codePart = bankCode[:length]
                interpretBankCode(connection, bankCodeTypeId, codePart, dataRow, relationTypeId)

    return interpretationFunction



def interpretBankCode(connection, bankCodeTypeId, bankCode, dataRow, relationTypeId):
    bankCodeObj = BankCode(bankCodeTypeId, bankCode)
    bankCodeObj.insertBankCodeIntoDB(connection)
    bankCodeRelationObj = BankCodeRelation(dataRow, bankCodeObj, relationTypeId)
    bankCodeRelationObj.insertBankCodeIntoDB(connection)



class BankCode:
    def __init__(self, bankCodeTypeId, bankCode):
        self.BankCodeId = None
        self.BankCodeTypeId = bankCodeTypeId
        self.BankCode = bankCode
        self.GroupId = None
        self.TableName = util.TableNames["BankCodes"]
        self.RelationTableName = util.TableNames["BankCodeRelations"]

    def insertBankCodeIntoDB(self, connection):
        # Insert bank code into DB if not exists
        query = f"""INSERT OR IGNORE INTO {self.TableName} (BankCodeTypeId, BankCode) VALUES (?, ?)"""
        cursor = connection.execute(
            query, (self.BankCodeTypeId, self.BankCode)
        )
        self.BankCodeId = cursor.lastrowid


class BankCodeRelation:
    def __init__(self, DataRow, bankCode, relationTypeId):
        self.DataRow = DataRow
        self.bankCode = bankCode
        self.relationTypeId = relationTypeId
        self.GroupId = None
        self.TableName = util.TableNames["BankCodeRelations"]

    def insertBankCodeIntoDB(self, connection):
        raise NotImplementedError("Not implemented yet")





