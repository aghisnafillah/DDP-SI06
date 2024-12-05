from Gempa import *

#  Membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa('Banten', 1.2)

# Info Gempa
print('## Gempa Bumi ##')
print()
gempa1.dampak() # memanggil method dampak()

#  Membuat objek gempa dengan lokasi dan skala
gempa2 = Gempa('Palu', 6.1)

# Info Gempa
print('## Gempa Bumi ##')
print()
gempa2.dampak() # memanggil method dampak()

#  Membuat objek gempa dengan lokasi dan skala
gempa4 = Gempa('Cianjur', 5.6)

# Info Gempa
print('## Gempa Bumi ##')
print()
gempa4.dampak() # memanggil method dampak()

#  Membuat objek gempa dengan lokasi dan skala
gempa5 = Gempa('Jayapura', 3.3)

# Info Gempa
print('## Gempa Bumi ##')
print()
gempa5.dampak() # memanggil method dampak()

#  Membuat objek gempa dengan lokasi dan skala
gempa6 = Gempa('Garut', 4.0)

# Info Gempa
print('## Gempa Bumi ##')
print()
gempa6.dampak() # memanggil method dampak()
