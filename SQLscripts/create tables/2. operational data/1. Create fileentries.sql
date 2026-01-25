CREATE TABLE "Data.FileEntry" (
	"Id"	INTEGER NOT NULL UNIQUE,
    "SourceFileId"	INTEGER NOT NULL,
    "FileIndex"	INTEGER NOT NULL,
	"FileKey"	TEXT NOT NULL,
    "DataEntityId"	TEXT NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
	FOREIGN KEY("SourceFileId") REFERENCES "Data.SourceFile"("Id")
);