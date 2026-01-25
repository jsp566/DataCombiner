

import util as util
import DataSaving.Relations.BankCodeRelation as BankCodeRelation

class BankCode:
    def __init__(self, bankCodeType, bankCode):
        self.BankCodeId = None
        self.BankCodeType = bankCodeType
        self.BankCode = bankCode
        self.GroupId = None
        self.TableName = util.TableNames["BankCodes"]
        self.RelationTableName = util.TableNames["BankCodeRelations"]

    def setBankCodeId(self, connection):
        query = f"""SELECT BankCodeId FROM {self.TableName} WHERE BankCodeTypeId = ? AND BankCode = ?"""
        cursor = connection.execute(
            query, (self.BankCodeType.value, self.BankCode)
        )
        result = cursor.fetchone()
        if result:
            self.BankCodeId = result[0]
        else:
            self.BankCodeId = None

    def insertBankCodeIntoDB(self, connection):
        # Insert bank code into DB if not exists
        self.setBankCodeId(connection)
        if self.BankCodeId is not None:
            return

        query = f"""INSERT INTO {self.TableName} (BankCodeTypeId, BankCode) VALUES (?, ?)"""
        cursor = connection.execute(
            query, (self.BankCodeType.value, self.BankCode)
        )
        self.BankCodeId = cursor.lastrowid





