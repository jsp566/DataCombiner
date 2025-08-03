import DataFetchers.SIC
import DataFetchers.BundesSCL
import DataFetchers.SepaAdherence
import DataFetchers.SepaInstAdherence
import DataFetchers.SRTPAdherence
import DataFetchers.SPAAAdherence
import DataFetchers.VOPAdherence
import DataFetchers.OctInstAdherence    
import DataFetchers.SDDCoreAdherence
import DataFetchers.SDDB2BAdherence

DataFetchers.SIC.SIC().update()
DataFetchers.BundesSCL.BundesSCL().update()
DataFetchers.SepaAdherence.SepaAdherence().update()
DataFetchers.SepaInstAdherence.SepaInstAdherence().update()
DataFetchers.SRTPAdherence.SRTPAdherence().update()
DataFetchers.SPAAAdherence.SPAAAdherence().update()
DataFetchers.VOPAdherence.VOPAdherence().update()
DataFetchers.OctInstAdherence.OctInstAdherence().update()
DataFetchers.SDDCoreAdherence.SDDCoreAdherence().update()
DataFetchers.SDDB2BAdherence.SDDB2BAdherence().update()
