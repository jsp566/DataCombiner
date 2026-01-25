CREATE TABLE "Data.CorrespondentRelation" (
    "Id"	INTEGER NOT NULL,
	"DataEntityId"	INTEGER NOT NULL,
	"BankCodeId"	INTEGER NOT NULL,
    "CorrespondentBankCodeId"	INTEGER NOT NULL,
	"CurrencyId"	INTEGER NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("DataEntityId") REFERENCES "Data.DataEntity"("Id"),
	FOREIGN KEY("BankCodeId") REFERENCES "Data.BankCode"("Id"),
    FOREIGN KEY("CorrespondentBankCodeId") REFERENCES "Data.BankCode"("Id"),
	FOREIGN KEY("CurrencyId") REFERENCES "Enum.Currency"("Id")
);