#Import Dari Library Sckit-Learn KNN
from sklearn.neighbors   import KNeighborsClassifier 
from PIL import Image
import os #Literasi Di folder 
import numpy as np #

#Fungsi Load Dataset
def load_dataset():
    kotak = []
    lingkaran = []
    segitiga = []
    gbergelombang = []
    gzigzag = []

    for file in os.listdir("kotak"):
        img = Image.open("kotak/" + file)
        img = np.array(img)
        img = img.flatten() #Flatten
        kotak.append(img)

    for file in os.listdir("lingkaran"):
        img = Image.open("lingkaran/" + file)
        img = np.array(img)
        img = img.flatten()
        lingkaran.append(img)

    for file in os.listdir("segitiga"):
        img = Image.open("segitiga/" + file)
        img = np.array(img)
        img = img.flatten()
        segitiga.append(img)
        
    for file in os.listdir("gbergelombang"):
        img = Image.open("gbergelombang/" + file)
        img = np.array(img)
        img = img.flatten()
        gbergelombang.append(img)
    
    for file in os.listdir("gzigzag"):
        img = Image.open("gzigzag/" + file)
        img = np.array(img)
        img = img.flatten()
        gzigzag.append(img)
    
    return kotak, lingkaran, segitiga, gbergelombang, gzigzag 

#Fungsi Model AI Dari Library
def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Tunggu Sebentar Sedang Proses Loading Dataset")
    kotak, lingkaran, segitiga, gbergelombang, gzigzag  = load_dataset()
    print("[INFO] Tunggu Sebentar Sedang Proses Loading Model")
    
    #Label Hasil Nama 
    y_kotak = np.zeros(len(kotak))
    y_lingkaran = np.ones(len(lingkaran))
    y_segitiga = np.ones(len(segitiga)) * 2
    y_gbergelombang = np.ones(len(gbergelombang)) * 3
    y_gzigzag = np.ones(len(gzigzag)) * 4
    X = kotak + lingkaran + segitiga + gbergelombang + gzigzag 
    y = np.concatenate([y_kotak, y_lingkaran, y_segitiga, y_gbergelombang, y_gzigzag])
    model.fit(X, y)
    return model