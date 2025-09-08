import DataCombiner.DataFetchers.SIC
import DataCombiner.DataFetchers.BundesSCLFromURL
import DataCombiner.DataFetchers.SepaAdherence
import DataCombiner.DataFetchers.SepaInstAdherence
import DataCombiner.DataFetchers.SRTPAdherence
import DataCombiner.DataFetchers.SPAAAdherence
import DataCombiner.DataFetchers.VOPAdherence
import DataCombiner.DataFetchers.OctInstAdherence
import DataCombiner.DataFetchers.SDDCoreAdherence
import DataCombiner.DataFetchers.SDDB2BAdherence

datasets = [
    DataCombiner.DataFetchers.SIC.SIC(),
    DataCombiner.DataFetchers.BundesSCLFromURL.BundesSCLFromURL(),
    DataCombiner.DataFetchers.SepaAdherence.SepaAdherence(),
    DataCombiner.DataFetchers.SepaInstAdherence.SepaInstAdherence(),
    DataCombiner.DataFetchers.SRTPAdherence.SRTPAdherence(),
    DataCombiner.DataFetchers.SPAAAdherence.SPAAAdherence(),
    DataCombiner.DataFetchers.VOPAdherence.VOPAdherence(),
    DataCombiner.DataFetchers.OctInstAdherence.OctInstAdherence(),
    DataCombiner.DataFetchers.SDDCoreAdherence.SDDCoreAdherence(),
    DataCombiner.DataFetchers.SDDB2BAdherence.SDDB2BAdherence(),
]

for dataset in datasets:
    dataset.insertCSV()