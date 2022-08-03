import pandas as pd


#Legit Software

#aescrypt
aescrypt_read = pd.read_csv('legit/aescrypt/ata_read.csv')
aescrypt_write = pd.read_csv('legit/aescrypt/ata_write.csv')
#excel
excel_read = pd.read_csv('legit/excel/ata_read.csv')
excel_write = pd.read_csv('legit/excel/ata_write.csv')

#Ransomware

#wannacry
wannacry_read = pd.read_csv('ransomware/wannacry/ata_read.csv')
wannacry_write = pd.read_csv('ransomware/wannacry/ata_write.csv')
#ryuk
ryuk_read = pd.read_csv('ransomware/ryuk/ata_read.csv')
ryuk_write = pd.read_csv('ransomware/ryuk/ata_write.csv')

legit_readset = [aescrypt_read, excel_read]  
legit_writeset = [aescrypt_write, excel_write]  

legit_read = aescrypt_read.merge(excel_read)
print(aescrypt_read.shape)
print(excel_read.head())
