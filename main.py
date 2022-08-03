import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

#Legit Read and write
legit_read = pd.concat([aescrypt_read, excel_read])
legit_write = pd.concat([aescrypt_write, excel_write])
legit_read['ransomware'] = 0 
legit_write['ransomware'] = 0 
#Ransomware Read and write
ran_read = pd.concat([wannacry_read, ryuk_read])
ran_write = pd.concat([wannacry_write, ryuk_write])
ran_read['ransomware'] = 1
ran_write['ransomware'] = 1

write_data = pd.concat([legit_write,ran_write])
read_data = pd.concat([legit_read, ran_read])

# print(read_data)
# print(legit_write.)
# print(ran_read.shape)
# print(ran_write.shape)

# Getting X and Y values for write data
x = write_data.iloc[:,0:-1]
y = write_data.iloc[:,-1:]
# print(y)

#Testing and training
xtrain, xtest, ytrain, ytest = train_test_split(x,y.values.ravel(),test_size=0.25,random_state=1)

#print(xtrain.shape)
#print(xtest.shape)

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(xtrain, ytrain)

y_predict = knn.predict(xtest)

print("Accuracy Score: ",accuracy_score(ytest,y_predict)*100,"%")