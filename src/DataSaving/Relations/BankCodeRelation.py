# Bankcode to datarow
# with relation type
import util as util

class BankCodeRelation:
    def __init__(self, dataRow, bankCode, relationType):
        self.DataRow = dataRow
        self.bankCode = bankCode
        self.relationType = relationType
        self.GroupId = None

        self.TableName = util.TableNames["BankCodeRelations"]

    def insertBankCodeRelationIntoDB(self, connection):
        query = f"""INSERT INTO {self.TableName} (DataRowId, BankCodeId, RelationTypeId) VALUES (?, ?, ?)"""
        connection.execute(
            query, (self.DataRow.DataRowId, self.bankCode.BankCodeId, self.relationType.value)
        )
        