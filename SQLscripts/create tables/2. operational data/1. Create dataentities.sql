CREATE TABLE "Data.DataEntity" (
    "Id"	INTEGER NOT NULL,
    "DataFormatId" INTEGER NOT NULL,
	"DataDict"	INTEGER NOT NULL,
	"Hash"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("DataFormatId") REFERENCES "Enum.DataFormat"("Id")
);