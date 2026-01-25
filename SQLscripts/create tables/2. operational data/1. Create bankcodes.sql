CREATE TABLE "Data.BankCode" (
	"BankCodeId"	INTEGER NOT NULL,
	"BankCodeTypeId"	INTEGER NOT NULL,
	"BankCode"	TEXT NOT NULL,
	PRIMARY KEY("BankCodeId" AUTOINCREMENT),
	FOREIGN KEY("BankCodeTypeId") REFERENCES "Enum.BankCodeType"("Id")	
);