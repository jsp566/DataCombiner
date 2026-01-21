# bank code to newtork relation
# with datarow as additional info

class NetworkRelation:
    def __init__(self, dataRow, bankCode, network):
        self.DataRow = dataRow
        self.bankCode = bankCode
        self.network = network
        self.GroupId = None