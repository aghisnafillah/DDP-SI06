import math

def kubus(sisi): #6xsisixsisi
    luas = 6 * sisi * sisi
    print(f'luas kubus adalah {6} * {sisi} * {sisi} = {luas}')

def balok(panjang, lebar, tinggi):
    luas = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
    print(f'luas permukaan balok adalah {2} * {(panjang*lebar + panjang*tinggi + lebar*tinggi)} = {luas}')

def tabung(jari2, tinggi):
    luas = 2 * math.pi * (jari2+tinggi)
    print(f'luas tabung adalah = {luas}')

def limas(alas, sisitegak): #luasalas+luassisitegak
    luas = alas + sisitegak
    print(f'luas permukaan limas adalah {alas} + {sisitegak} = {luas}')

def l_bola(jari2, diameter):
    luas = jari2 * math.pi
    print(f'luas permukaan bola adalah {jari2} * {diameter} = {luas}')
