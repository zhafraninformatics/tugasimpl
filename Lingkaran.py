#Terdapat Beberapa Clas untuk Bangun Datar yaitu Lingkaran,Persegi, Operatorion

#Membuat Class untuk Lingkaran
class LingkaranSempurna:

    def __init__(self, radius):
        self.radius = radius

#Membuat Class untuk Persegi        
class BangunDatarPersegi:

    def __init__(self, panjang):
        self.panjang = panjang
        
#Import Math untuk operation matematika
import math

#Membuat Class untuk  Operation
class Operation:

    def __init__(self, *args):
        self.bangunDatar = args

    def calculate(self):
        listLuas = []
        for objek in self.bangunDatar:
            luas = 0
            if type(objek).__name__ == 'BangunDatarPersegi':
                luas = math.pow(objek.panjang, 2)
            elif type(objek).__name__ == 'LingkaranSempurna':
                luas = math.pi * math.pow(objek.radius, 2)
            listLuas.append(luas)

        return sum(listLuas)

    def output(self):
        return self.calculate()

#Membuat Class main
if __name__ == "__main__":

    result = Operation(
        LingkaranSempurna(2),
        BangunDatarPersegi(4),
        BangunDatarPersegi(8)
    )

    print("Hasil Dari Perhitungan Jumlah luas adalah : ", result.output())