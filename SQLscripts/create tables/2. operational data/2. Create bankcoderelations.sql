CREATE TABLE "Data.BankCodeRelation" (
    "Id"	INTEGER NOT NULL,
	"DataEntityId"	INTEGER NOT NULL,
	"BankCodeId"	INTEGER NOT NULL,
	"RelationTypeId"	INTEGER NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("DataEntityId") REFERENCES "Data.DataEntity"("Id"),
	FOREIGN KEY("BankCodeId") REFERENCES "Data.BankCode"("Id"),
	FOREIGN KEY("RelationTypeId") REFERENCES "Enum.RelationType"("Id")
);