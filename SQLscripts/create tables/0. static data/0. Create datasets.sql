CREATE TABLE "Enum.Dataset" (
	"Id"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL UNIQUE,
	"Documentation"	TEXT,
	"Source Type"	TEXT,
	"Source Path"	TEXT,
	"Summary Query"	TEXT,
	"Latest Update Time"	TEXT,
	"Data Time"	TEXT,
	"Update Frequency"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);