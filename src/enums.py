from enum import Enum


class Networks(Enum):
    # Define network types here
    SIC = 1
# for networks, add native dataset id and currency

class DatasetId(Enum):
    SIC = 1
    BSBDirectory = 2
    BSBKeys = 3
    BundesSCLFromURL = 4
    OctInstAdherence = 5
    SDDB2BAdherence = 6
    SDDCoreAdherence = 7
    SepaAdherence = 8
    SepaInstAdherence = 9
    SPAAAdherence = 10
    SRTPAdherence = 11
    VOPAdherence = 12
# additional infomation is added in db

class FileStatus(Enum):
    New = 1
    Downloaded = 2
    FileInfoAdded = 3
    RawDataAddedToDB = 4
    InterpretationAddedToDB = 5
    GroupingAddedToDB = 6
    Processed = 10
    Error = 11


class bankcodetype(Enum):
    NAME = 1
    BIC4 = 2
    BIC6 = 3
    BIC8 = 4
    BIC11 = 5
    IID = 6
    SICIID = 7

# for other bank code types, add native dataset id and if it is groupable


class relationtype(Enum):
    SELF = 1
    SPONSOR = 2
    GROUP = 3
    RESULT = 4

