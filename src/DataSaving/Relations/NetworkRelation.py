# bank code to newtork relation
# with datarow as additional info
import util as util

class NetworkRelation:
    def __init__(self, dataRow, bankCode, network):
        self.DataRow = dataRow
        self.bankCode = bankCode
        self.network = network
        self.GroupId = None
        self.TableName = util.TableNames["NetworkRelations"]


    def insertNetworkRelationIntoDB(self, connection):
        query = f"""INSERT INTO {self.TableName} (DataRowId, BankCodeId, NetworkId) VALUES (?, ?, ?)"""
        connection.execute(
            query, (self.DataRow.DataRowId, self.bankCode.BankCodeId, self.network.value)
        )
