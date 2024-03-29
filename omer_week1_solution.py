#1.soru 1den 10a kadar yazdirma
for i in range(1, 11):
    print(i)

#Soru 2 : Kullanıcıdan bir sayı girişi alın ve bu sayıya kadar olan çift sayıları ekrana yazdıran bir Python programı yazın. Bunu once 'for' ile sonra 'while' donguleri ile yapiniz.
#for dongusu ile
sayi=int(input("Bir sayi giriniz: "))
for i in range(0,sayi):
    if i%2==0:
        print(i)

# while dongusu ile
sayi = int(input("Bir sayı girin: "))
sayac = 0

while sayac <= sayi:
    if sayac % 2 == 0:
        print(sayac)
    sayac += 1

#Soru 3Soru 3 : Kullanıcıdan bir başlangıç ve bitiş değeri alan ve bu değerler arasındaki tüm sayıları ekrana yazdıran bir Python kodu yazınız(bitis degeri dahil).
baslangic=int(input("Bir sayi girinz: "))
bitis=int(input("ikinci sayiyi girinz: "))
for i in range(baslangic,bitis+1):
    print(i)
    
#Soru 4Soru 4 : Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir Python kodu yazınız
sayi=int(input("bir sayi girin: "))
if sayi%2 == 0:
    print(sayi ,"cift sayidir")
else:
    print(sayi,"tek sayidir")

#Soru 5 faktoriyel
sayi = int(input("Bir sayı girin: "))
faktoriyel = 1

for i in range(2, sayi + 1):
    faktoriyel *= i

print("{} sayısının faktoriyeli {} dır.".format(sayi, faktoriyel))


#Soru 6 asal sayi
sayi = int(input("Bir sayı girin: "))
if sayi > 1:
    for i in range(2, sayi):
        if (sayi % i) == 0:
            print(sayi, "asal değildir.")
            break
    else:
        print(sayi, "asaldır.")
else:
    print(sayi, "asal değildir.")

#Soru 7 fibonacci dizisi
soru= int(input(" fibonacci sayi dizisi kac sayidan olusturulsun ? "))
sayi1= 0
sayi2= 1
fibonaccilistesi=[0,1]
for i in range (soru-2):
    sayi3= sayi1+sayi2
    fibonaccilistesi.append(sayi3)
    sayi1= sayi2
    sayi2= sayi3
print(fibonaccilistesi)

#Soru 8 Kelime al tersini yazdir
kelime = input("Bir kelime girin: ")
ters_kelime = ""
for i in kelime:
    ters_kelime = i+ters_kelime
print("Kelimenin tersi:", ters_kelime)
# basit yol soru 8
kelime = input("Bir kelime giriniz.")
print(kelime[::-1])

#Soru 9   palindrom durumu
kelime = input("Bir kelime girin: ")
ters_kelime = ""
for i in kelime:
    ters_kelime = i+ters_kelime
if kelime == ters_kelime:
    print("Bu kelime palindromdur")
else:
    print("Bu kelime palindrom degildir.")

#Soru 10      kilo endeksi
kilo = float(input("Kilonuzu giriniz. "))
boy = float(input("Boyunuzu m olarak yaziniz. "))

indeks =  kilo/ (boy**2)
if indeks < 25:
    print("Sonucunuz zayif cikmistir.")
elif 25 <= indeks< 30:
    print("Sonucunuz normal cikmistir.")
elif 30 <= indeks < 40:
    print("Sonucunuz kilolu cikmistir.")
else:
    print("Sonucunuz asiri kilolu cikmistir")

#Soru 11 girilen sayilarin buyugunu bul
liste=[]
liste.append(int(input("1. sayiyi girin: ")))
liste.append(int(input("2. sayiyi girin: ")))
liste.append(int(input("3. sayiyi girin: ")))
buyuk = max(liste)
print("En buyuk sayi: ",buyuk)

# 2.yol
if sayi1 > sayi2 and sayi1 > sayi3:
    print("1. sayi buyuktur.")
elif sayi2> sayi3 and sayi2 > sayi1:
    print("2. sayi buyuktur")
else:
    print("3. sayi buyuktur")

#Soru 12     4 kisiden notlarini al etki oranina gore ortalama bul ve basarili\siz ayir
def dersi_gecme_durumu(vize, final):
    ortalama = (vize * 0.40) + (final * 0.60)
    if ortalama >= 50:
        return "BAŞARILI"
    else:
        return "BAŞARISIZ"

for i in range(1, 5):
    vize = float(input(f"{i}. ders vize notunu girin: "))
    final = float(input(f"{i}. ders final notunu girin: "))
    print(dersi_gecme_durumu(vize, final))
