VIT4_Python_Modul_Week_1
#Soru 1 : 1'den 10'a kadar olan sayıları ekrana yazdıran bir Python kodu yazıniz.
#Cevap_1
for i in range(1, 11):
    print(i)

#Soru 2 : Kullanıcıdan bir sayı girişi alın ve bu sayıya kadar olan çift sayıları ekrana yazdıran bir Python programı yazın. Bunu once 'for' ile sonra 'while' donguleri ile yapiniz.
#Cevap_2 for dongulu
sayi = int(input("Bir sayı girin: "))
print("For dongulu cift sayilar:")
for i in range(0, sayi + 1, 2):
    print(i)
#Cevap_2 while dongulu
sayi = int(input("Bir sayı girin: "))
print("While dongulu cift sayilar:")
ciftsayi = 0
while ciftsayi <= sayi:
    print(ciftsayi)
    ciftsayi += 2


#Soru 3 : Kullanıcıdan bir başlangıç ve bitiş değeri alan ve bu değerler arasındaki tüm sayıları ekrana yazdıran bir Python kodu yazınız(bitis degeri dahil).
#Cevap_3
baslangic = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz: "))
print(f"{baslangic} ile {bitis} arasındaki tüm sayılar:")
for i in range(baslangic, bitis + 1):
    print(i, end=" ")


#Soru 4 : Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir Python kodu yazınız.
#Cevap_4
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print(f"{sayi} bir çift sayıdır.")
else:
    print(f"{sayi} bir tek sayıdır.")

#Soru 5 : Kullanıcıdan pozitif bir tam sayı girişi alın ve faktöriyelini hesaplayan bir Python programı yazın. Faktöriyel, bir sayının kendisi ile 1 arasındaki tüm pozitif tam sayıların çarpımıdır. Örneğin: kullanıcı 5 girdiyse program şu çıktıyı vermeli: Kullanıcıdan bir sayı girin: 5 Faktöriyel: 120
#Cevap_5
sayi = int(input("Bir sayi girin: "))
faktoriyel = 1
if sayi < 0:
    print("Negatif sayi girdiniz!.")
elif sayi == 0:
    print("Faktöriyel: 1")
else:
    for i in range(1, sayi + 1):
        faktoriyel *= i
    print(f"{sayi} Faktöriyel:", faktoriyel)


#Soru 6 : Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazınız.
#Cevap_6
x=int(input("Lutfen pozitif bir tamsayi giriniz:"))
if x < 2:
   print(f"{x} asal bir sayi değildir.")
else:
   asal_mi = True
   for i in range(2, int(x ** 0.5) + 1):
       if x % i == 0:
           asal_mi = False
           break
   if asal_mi:
       print(f"{x} asal bir sayidir.")
   else:
       print(f"{x} asal bir sayi değildir.")


#Soru 7 : Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları içeren bir liste olarak döndüren bir döngü nasıl oluşturulur?
#Cevap_7
sinir = int(input("Fibonacci dizisi olusturmek icin bir sinir sayisi girin: "))
fibonacci = [0, 1]
while True:
   yeni_eleman = fibonacci[-1] + fibonacci[-2]
   if yeni_eleman > sinir:
       break
   fibonacci.append(yeni_eleman)
print(f"Fibonacci dizisi {sinir}'a kadar: {fibonacci}")


#Soru 8 : Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazınız.
#Cevap_8
a = input("Bir kelime yaziniz: ")
print(a[::-1])

#Soru 9 : Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom (tersten okunduğunda aynı olan) olup olmadığını
# kontrol eden bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?
#Cevap_9
kelime = input("Lütfen bir kelime giriniz: ")
palindrom = True
bas = 0
son = len(kelime)  # Kelimenin uzunluğunu al
while bas < (len(kelime) / 2) and palindrom:
    if kelime[bas] != kelime[son - 1]:  # Son karaktere dikkat et
        palindrom = False
    bas += 1
    son -= 1
if palindrom:
    print("Girilen kelime palindromdur.")
else:
    print("Girilen kelime palindrom değildir.")


#Soru 10 : Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.
# (kilo indeks hesabı için internete bakabilirsiniz) Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz.
# Kilo indeksi 25’in altında ise zayıf, 25-30 arasında ise normal,
# 30-40dan büyük ise kilolu, 40tan büyük ise aşırı kilolu sonuçlarına varsın.
#Cevap_10
kg = int(input("Kilonuz kg : "))
boy = float(input("Boyunuz cm : ")) / 100

def kilo_indeksi(kg,boy):
   indeks=int(kg / (boy ** 2))

   if indeks<25:
       print(f"indeks {indeks}:Zayif")

   elif 25<=indeks<30:
       print(f"indeks {indeks}:Normal")

   elif 30<=indeks<40:
       print(f"indeks {indeks}:Kilolu")

   else:
       print(f"indeks {indeks}:Asiri kilolu")

kilo_indeksi(kg,boy)



#Soru 11 : Bir kullanıcının girdiği üç sayının en büyüğünü bulan bir Python programı nasıl yazılır?
#Cevap_11_liste ve for döngülü

sayilar = [int(input(f"{i+1}. sayiyi girin: ")) for i in range(3)]
print("En büyük sayi:", max(sayilar))

#Cevap_11_max fonksiyonlu
sayi1=int(input("Birinci sayiyi giriniz:"))
sayi2=int(input("Ikinci sayiyi giriniz:"))
sayi3=int(input("Ucuncu sayiyi giriniz:"))
   enbuyuksayi=max(sayi1,sayi2,sayi3)
print(f"En buyuk sayi: {enbuyuksayi}")


#Soru 12 : Bir ogrenciden herhangi bir ders icin Vize ve Final notlarıni alin. Ara sınav notunun %40'ı ile final notunun %60'ının toplamı yıl sonu ortalamasını verecektir. 
# Ortalama 50'nin altında ise ekranda “BAŞARISIZ”, 50 ve üzerinde ise “BAŞARILI” çıktısı ekrana gelecektir. 
# Bu baskı işlemi 4 derstir. yapılacak ve dersler birbiri ardına yazılacaktır.
#cevap_12
def ortalama_hesapla(vize, final):
    ortalama = (vize * 0.4) + (final * 0.6)
    if ortalama >= 50:
        return "BAŞARILI"
    else:
        return "BAŞARISIZ"

for i in range(4):
    vize = float(input(f"{i+1}. ders vize notunu giriniz: "))
    final = float(input(f"{i+1}. ders final notunu giriniz: "))
    sonuc = ortalama_hesapla(vize, final)
    print(f"{i+1}. ders: {sonuc}")

