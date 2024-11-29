import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'luas persegi {sisi} * {sisi} = {luas}')
    print(f'keliling persegi adalah {sisi} * {sisi} * {sisi} * {sisi} = {luas}')

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("hasil luas persegi panjang dari", panjang, "x", lebar, "=", luas)

def l_segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print(f"hasil luass segitiga dari", 1/2, "*", alas, tinggi, "=", luas )

def l_lingkaran(r1, r2):
    luas = 3.14 * r1 * r2
    print(f'luas lingkaran {3.14} * {r1} * {r2} = {luas}')

def l_jajargenjang(alas, tinggi):
    luas = alas * tinggi
    print(f'luas jajargenjang {alas} * {tinggi} * = {luas}')

