CREATE TABLE "Enum.BankCodeType" (
	"Id"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL UNIQUE,
    "Pattern"	TEXT,
    "NativeDatasetId" INTEGER, 
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("NativeDatasetId") REFERENCES "Enum.Dataset"("Id")
);