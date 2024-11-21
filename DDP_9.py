print('==== No 1 ====')
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)

print('/n==== No 2 ====')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

# rata rata nilai kelulusan 70
print('=== No 3 ===')
def skor(nilai):
    if nilai >= 70:
        print('lulus')
    else:
        print('gagal')

skor(70)
skor(80)

print("=== No 4 ===")
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end='')
bil_ganjil(20)