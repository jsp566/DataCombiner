# bankcode to bankcode relation
# with currency and datarow as additional info

class CorrespondentRelation:
    def __init__(self, dataRow, bankCodeFrom, bankCodeTo, currency):
        self.DataRow = dataRow
        self.bankCodeFrom = bankCodeFrom
        self.bankCodeTo = bankCodeTo
        self.currency = currency
        self.GroupId = None

        