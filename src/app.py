import util
import DataSaving.DataFetchers.SIC
import DataSaving.DataFetchers.BundesSCLFromURL
import DataSaving.DataFetchers.SepaAdherence
import DataSaving.DataFetchers.SepaInstAdherence
import DataSaving.DataFetchers.SRTPAdherence
import DataSaving.DataFetchers.SPAAAdherence
import DataSaving.DataFetchers.VOPAdherence
import DataSaving.DataFetchers.OctInstAdherence
import DataSaving.DataFetchers.SDDCoreAdherence
import DataSaving.DataFetchers.SDDB2BAdherence

dataFetchers = {util.DatasetId.SIC: DataSaving.DataFetchers.SIC.SIC,
                util.DatasetId.BundesSCLFromURL: DataSaving.DataFetchers.BundesSCLFromURL.BundesSCLFromURL,
                util.DatasetId.SepaAdherence: DataSaving.DataFetchers.SepaAdherence.SepaAdherence,
                util.DatasetId.SepaInstAdherence: DataSaving.DataFetchers.SepaInstAdherence.SepaInstAdherence,
                util.DatasetId.SRTPAdherence: DataSaving.DataFetchers.SRTPAdherence.SRTPAdherence,
                util.DatasetId.SPAAAdherence: DataSaving.DataFetchers.SPAAAdherence.SPAAAdherence,
                util.DatasetId.VOPAdherence: DataSaving.DataFetchers.VOPAdherence.VOPAdherence,
                util.DatasetId.OctInstAdherence: DataSaving.DataFetchers.OctInstAdherence.OctInstAdherence,
                util.DatasetId.SDDCoreAdherence: DataSaving.DataFetchers.SDDCoreAdherence.SDDCoreAdherence,
                util.DatasetId.SDDB2BAdherence: DataSaving.DataFetchers.SDDB2BAdherence.SDDB2BAdherence}


