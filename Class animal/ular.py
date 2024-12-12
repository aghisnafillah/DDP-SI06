from animals import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembangbiak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.warna = warna_ular
        self.jenis = jenis_ular

    def cetak_ular(self):
        super().cetak()
        print(f'ular ini memiliki warna {self.warna} dan hewan ini jenisnya ular {self.jenis}')

sanca = ular('ular sanca', 'mamalia kecil', 'hutan', 'bertelur', 'hijau', 'Sanca hijau')
sanca.cetak_ular()        

#object kedua
print("==== object kedua ====")

anakonda = ular('ular anakonda', 'reptil', 'hutan', 'bertelur', 'coklat', 'tidak berbisa')
anakonda.cetak_ular() 
         

