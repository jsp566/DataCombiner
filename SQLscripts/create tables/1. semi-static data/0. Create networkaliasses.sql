CREATE TABLE "Alias.NetworkAlias" (
    "Id"	INTEGER NOT NULL,
    "DataFormatId" INTEGER NOT NULL,
	"DataFieldId"	INTEGER NOT NULL,
	"FieldValue"	TEXT NOT NULL,
    "NetworkId" INTEGER NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("DataFormatId") REFERENCES "Enum.DataFormat"("Id"),
    FOREIGN KEY("DataFieldId") REFERENCES "Enum.DataField"("Id"),
    FOREIGN KEY("NetworkId") REFERENCES "Enum.Network"("Id")
);