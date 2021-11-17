from pyturkce import pyturkce

kelime = pyturkce.Sozluk('televizyon')

print(kelime.anlamlar)
print(kelime.deyimler)
print(kelime.ornekler)
