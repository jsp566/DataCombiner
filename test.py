import src.DataFetchers.SIC
import src.DataFetchers.BundesSCLFromURL
import src.DataFetchers.SepaAdherence
import src.DataFetchers.SepaInstAdherence
import src.DataFetchers.SRTPAdherence
import src.DataFetchers.SPAAAdherence
import src.DataFetchers.VOPAdherence
import src.DataFetchers.OctInstAdherence
import src.DataFetchers.SDDCoreAdherence
import src.DataFetchers.SDDB2BAdherence

datasets = [
    src.DataFetchers.SIC.SIC(),
    src.DataFetchers.BundesSCLFromURL.BundesSCLFromURL(),
    src.DataFetchers.SepaAdherence.SepaAdherence(),
    src.DataFetchers.SepaInstAdherence.SepaInstAdherence(),
    src.DataFetchers.SRTPAdherence.SRTPAdherence(),
    src.DataFetchers.SPAAAdherence.SPAAAdherence(),
    src.DataFetchers.VOPAdherence.VOPAdherence(),
    src.DataFetchers.OctInstAdherence.OctInstAdherence(),
    src.DataFetchers.SDDCoreAdherence.SDDCoreAdherence(),
    src.DataFetchers.SDDB2BAdherence.SDDB2BAdherence(),
]

for dataset in datasets:
    dataset.insertCSV()