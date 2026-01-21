import util as util

import DataSaving.DataFetchers.SIC as SICFetcher
import DataSaving.DataFetchers.BSBDirectory as BSBDirectoryFetcher
import DataSaving.DataFetchers.BSBKeys as BSBKeysFetcher
import DataSaving.DataFetchers.BundesSCLFromURL as BundesSCLFromURLFetcher
import DataSaving.DataFetchers.OctInstAdherence as OctInstAdherenceFetcher
import DataSaving.DataFetchers.SDDB2BAdherence as SDDB2BAdherenceFetcher
import DataSaving.DataFetchers.SDDCoreAdherence as SDDCoreAdherenceFetcher
import DataSaving.DataFetchers.SepaAdherence as SepaAdherenceFetcher
import DataSaving.DataFetchers.SepaInstAdherence as SepaInstAdherenceFetcher
import DataSaving.DataFetchers.SPAAAdherence as SPAAAdherenceFetcher
import DataSaving.DataFetchers.SRTPAdherence as SRTPAdherenceFetcher
import DataSaving.DataFetchers.VOPAdherence as VOPAdherenceFetcher

allFetchers = [
    SICFetcher.SIC,
    BSBDirectoryFetcher.BSBDirectory,
    BSBKeysFetcher.BSBKeys,
    BundesSCLFromURLFetcher.BundesSCLFromURL,
    OctInstAdherenceFetcher.OctInstAdherence,
    SDDB2BAdherenceFetcher.SDDB2BAdherence,
    SDDCoreAdherenceFetcher.SDDCoreAdherence,
    SepaAdherenceFetcher.SepaAdherence,
    SepaInstAdherenceFetcher.SepaInstAdherence,
    SPAAAdherenceFetcher.SPAAAdherence,
    SRTPAdherenceFetcher.SRTPAdherence,
    VOPAdherenceFetcher.VOPAdherence,
]

def updateAllDatasets(connection, sourceFileFolder):
    for fetcherClass in allFetchers:
        fetcher = fetcherClass(connection, sourceFileFolder)
        try:
            fetcher.getNewData()
        except NotImplementedError as e:
            print(f"Error updating {fetcher.name}: {e}")

if __name__ == "__main__":
    sqlcon = util.SQLcons["SQLite"]
    sourcefilefolder = util.SourceFileFolderName

    updateAllDatasets(sqlcon, sourcefilefolder)