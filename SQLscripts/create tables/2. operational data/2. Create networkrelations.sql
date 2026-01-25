CREATE TABLE "Data.NetworkRelation" (
    "Id"	INTEGER NOT NULL,
	"DataEntityId"	INTEGER NOT NULL,
	"BankCodeId"	INTEGER NOT NULL,
	"NetworkId"	INTEGER NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("DataEntityId") REFERENCES "Data.DataEntity"("Id"),
	FOREIGN KEY("BankCodeId") REFERENCES "Data.BankCode"("Id"),
	FOREIGN KEY("NetworkId") REFERENCES "Enum.Network"("Id")
);