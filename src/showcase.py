
from datetime import datetime
import util as util

sqlcon = util.SQLcons["SQLite"]
sourcefilefolder = util.SourceFileFolderName
datasetid = util.DatasetId.SIC

import DataSaving.SourceFile as SourceFile

# Create file id in DB
downloadedFile = SourceFile.SourceFile(sqlcon, sourcefilefolder, datasetid)
downloadedFile.insertSourceFileIntoDB()


# Download file ()
import DataSaving.DataFetchers.SIC as SICFetcher
fetcher = SICFetcher.SIC(sqlcon, sourcefilefolder)
fetcher.downloadSourceFile(downloadedFile.path)

downloadedFile.updateFileStatus(util.FileStatus.Downloaded)

# get meta data
downloadedFile.getDownloadTimestamp()
downloadedFile.calculateFileHash()
downloadedFile.addMetadataToDB()

# read data and insert each row into db
# interpret each row
# Create bank codes if not present
# Create bank code relations
# Create network relation (networks should be pre-defined)

fetcher.getValidFromTimestamp(downloadedFile)

rowgenerator = fetcher.createDataRowGenerator(downloadedFile)

rowCounter = 0
for row in rowgenerator:
    row.insertDataRowIntoDB(sqlcon)
    fetcher.interpretDataRow(row)
    rowCounter += 1

downloadedFile.numRows = rowCounter

downloadedFile.addMetadataToDB()

downloadedFile.updateFileStatus(util.FileStatus.Processed)




# group data


