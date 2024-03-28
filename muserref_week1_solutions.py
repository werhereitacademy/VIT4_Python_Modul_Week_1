#Soru 1 : 1'den 10'a kadar olan sayıları ekrana yazdıran bir Python
for i in range(1,10):
    print(i)

print([i for i in range(1,10)])


#Soru 2 : Kullanıcıdan bir sayı girişi alın ve bu sayıya kadar olan çift
# sayıları ekrana yazdıran. Bunu once 'for' ile sonra 'while' donguleri ile yapiniz.
x=int(input("Lutfen bir sayi giriniz:"))
for i in range(x):
    if i%2==0:
        print(i)


print([i for i in range(x)if i%2==0 ])

x=int(input("Lutfen bir sayi giriniz:"))
i=0
while i <= x:
    if i%2==0:
         print(i)
    i+=1


#Soru 3 : Kullanıcıdan bir başlangıç ve bitiş değeri alan ve bu değerler arasındaki
# tüm sayıları ekrana yazdıran bir Python kodu yazınız    
baslangic=int(input("Lutfen bir baslangic sayisi giriniz:"))
bitis=int(input("Lutfen bir bitis sayisi giriniz:"))

for i in range(baslangic,bitis+1):
    print(i)

print([i for i in range(baslangic,bitis+1)])


#Soru 4 : Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir Python kodu yazınız.
x=int(input("Lutfen bir sayi giriniz:"))
if x % 2 == 0:
    print(f"{x} sayisi cift sayidir")
else:
    print(f"{x} sayisi tek sayidir")


#Soru 5 : Kullanıcıdan pozitif bir tam sayı girişi alın ve faktöriyelini hesaplayan bir Python programı yazın.
x=int(input("Lutfen pozitif bir tamsayi giriniz:"))
faktoriyel=1
for i in range(1,x+1):
    faktoriyel*=i
    if x==0:
        print(f"{x} sayisinin faktoriyeli:0")    
print(f"{x} sayisinin faktoriyeli: {faktoriyel}")


from functools import reduce

a = int(input("Lütfen bir pozitif tamsayi girin: "))

result = reduce(lambda x, y: x * y, range(1, a+1))

print("{} sayisinin faktoruyeli: {}".format(x, result))




#Soru 6 : Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazınız.
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
    
#Soru 7 : Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları içeren 
#bir liste olarak döndüren bir döngü nasıl oluşturulur?
sinir = int(input("Fibonacci dizisi olusturmek icin bir sinir sayisi girin: "))

fibonacci = [0, 1]
while True:
    yeni_eleman = fibonacci[-1] + fibonacci[-2]
    if yeni_eleman > sinir:
        break
    fibonacci.append(yeni_eleman)

print(f"Fibonacci dizisi (sinira kadar): {fibonacci}")       

#Soru 8 : Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazınız.

y=input("Lutfen bir kelime giriniz:")
kelimenin_tersi=y[::-1]
print(kelimenin_tersi)

#Soru 9 : Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom (tersten okunduğunda aynı olan) 
#olup olmadığını kontrol eden bir döngü ve koşullu ifade kombinasyonu
y=input("Lutfen bir kelime giriniz:")
kelimenin_tersi=y[::-1]
if kelimenin_tersi=y:
    print(f"{y} kelimesi bir palindromdur")
else:
    print(f"{y} kelimesi bir palindrom degildir") 

y = input("Lutfen bir kelime giriniz:")

for i in range(len(y) // 2):
    if y[i] != y[len(y) - 1 - i]:
        print("Girdiginiz kelime bir palindrom degildir.")
        break
else:
    print("Girdiginiz kelime bir palindromdur.")

cikti=["Girdiginiz kelime bir palindrom degildir." if y[i] != y[len(y) - 1 - i] else "Girdiginiz kelime bir palindromdur." for i in range(len(y) // 2)]
print(cikti)
#Soru 10 : Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.
#(kilo indeks hesabı için internete bakabilirsiniz) Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz.
# Kilo indeksi 25’in altında ise zayıf, 25-30 arasında ise normal, 30-40dan büyük ise kilolu, 40tan büyük ise aşırı kilolu sonuçlarına varsın.
#vücut ağırlığının (kg), boy uzunluğunun (m cinsinden) karesine (BKI=kg/m2) bölünmesiyle elde edilen bir değerdir

kg = float(input("Kilonuzu kilogram cinsinden girin: "))
boy = float(input("Boyunuzu metre cinsinden girin: "))

def kilo_indeksi(a,b):
    indeks=int(a / (b ** 2))
    if indeks<25:
        print("Zayifsiniz")
    elif 25<=indeks<30:
        print("Normalsiniz")
    elif 30<=indeks<40:
        print("Kilolusunuz")
    else:
        print("Asiri kilolusunuz")

kilo_indeksi(kg,boy)

#Soru 11 : Bir kullanıcının girdiği üç sayının en büyüğünü bulan bir Python programı nasıl yazılır?

# Kullanıcıdan üç sayı girişi alınır ve bu sayılar arasındaki en büyüğü ekrana yazdırılır

sayi1=int(input("Birinci sayiyi giriniz:"))
sayi2=int(input("Ikinci sayiyi giriniz:"))
sayi3=int(input("Ucuncu sayiyi giriniz:"))

enbuyuksayi=max(sayi1,sayi2,sayi3)
print(f"En buyuk sayi: {enbuyuksayi}")

print("En büyük sayi:", max(float(input("Birinci sayiyi girin: ")), float(input("İkinci sayiyi girin: ")), float(input("Üçüncü sayiyi girin: "))))

sayilar = [int(input(f"{i+1}. sayiyi girin: ")) for i in range(3)]
print("En büyük sayi:", max(sayilar))


#Soru 12 : Bir ogrenciden herhangi bir ders icin Vize ve Final notlarıni alin.
# Ara sınav notunun %40'ı ile final notunun %60'ının toplamı yıl sonu ortalamasını verecektir. 
#Ortalama 50'nin altında ise ekranda “BAŞARISIZ”, 50 ve üzerinde ise “BAŞARILI” çıktısı ekrana gelecektir. 
#Bu baskı işlemi 4 derstir. yapılacak ve dersler birbiri ardına yazılacaktır.
def yilsonu_ort(a,b):
    ysortalama=a*0.4+b*0.6
    if ysortalama<50:
        print("BASARISIZ")
    else:
        print("BASARILI")
for i in range(4):
    ders_adi=input("Lutfen dersinizin adini yaziniz:")
    vize = float(input("Vize notunuzu girin: "))
    final = float(input("Final notunuzu girin: "))
    print(ders_adi)
    yilsonu_ort(vize,final)


derssayisi=4
for i in range(1, derssayisi+1):
    final=int(input("Final notunuzu giriniz:"))
    vize=int(input("Vize notunuzu giriniz:"))
    yilsonuort=final*0.6+ vize*0.4
    if yilsonuort<50:
        print("Basarisiz")
    else:
        print("Basarili")

