class Animal:
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak 

    def cetak(self):
        print(f'Hewan {self.nama} ini memakan {self.makanan}, hewan ini juga hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembangbiak}')

C1 = Animal('buaya', 'daging', 'Amphibi', 'bertelur')
C1.cetak()
