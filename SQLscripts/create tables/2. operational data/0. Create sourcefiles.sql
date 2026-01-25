CREATE TABLE "Data.SourceFile" (
	"Id"	INTEGER NOT NULL UNIQUE,
	"DatasetId"	INTEGER NOT NULL,
	"DataFormatId"	INTEGER NOT NULL,
	"FileStatusId"	INTEGER NOT NULL,
	"Note"	TEXT,
	"Hash"	TEXT,
	"DownloadDatetime"	TEXT,
	"NumRows"	INTEGER,
	"ValidFromDatetime"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("FileStatusId") REFERENCES "Enum.FileStatus"("Id"),
	FOREIGN KEY("DatasetId") REFERENCES "Enum.Dataset"("Id"),
    FOREIGN KEY("DataFormatId") REFERENCES "Enum.DataFormat"("Id")
);