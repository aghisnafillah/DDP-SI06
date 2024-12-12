from animals import *

class Burung(Animal):
  def __init__(self, nama, makanan, hidup, berkembangbiak, jenis_bulu, bunyi):
     super().__init__(nama, makanan, hidup, berkembangbiak,)
     self.jenis_bulu = jenis_bulu
     self.bunyi = bunyi

  def cetak_Burung(self):
    super().cetak()
    print(f'hewan ini berbulu{self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

beo = Burung('burung beo', 'biji-bijian', 'udara', 'bertelur', 'biru dan orange', 'kamu jelek')
beo.cetak_Burung()

#object kedua
print("==== object kedua ====")
emprit = Burung('burung emprit', 'pisang', 'udara', 'bertelur', 'hijau', 'pipit')
emprit.cetak_Burung()
