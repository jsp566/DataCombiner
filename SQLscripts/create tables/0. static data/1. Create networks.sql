CREATE TABLE "Enum.Network" (
	"Id"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL UNIQUE,
    "CurrencyId"	INTEGER,
    "NativeDatasetId" INTEGER, 
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("NativeDatasetId") REFERENCES "Enum.Dataset"("Id"),
    FOREIGN KEY("CurrencyId") REFERENCES "Enum.Currency"("Id")
);