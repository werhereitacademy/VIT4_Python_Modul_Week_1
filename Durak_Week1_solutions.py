#Answer 1 
a = list(range(0,11,1))
print(a)

#Answer 2
#With ''for''
sayi = input("Bir Sayi Giriniz :")
cift = []

for i in range(1,int(sayi)+1):
    if i%2 == 0:
        cift.append(i)
print(cift)

#With ''while''
sayi = input("Bir Sayi Giriniz :")
sayi = int(sayi)
cift = 0
ciftl =[]

while cift <= sayi:
    if cift % 2 == 0:
        ciftl.append(cift)
    cift += 1
print(ciftl)

#Answer 3
bassayi = input("Bir sayi giriniz :")
bitsayi = input("Bir sayi daha giriniz :")
aralik = list(range(int(bassayi),int(bitsayi)+1))
print(aralik)

#Answer 4
sayi = int(input("Bir sayi giriniz :"))
if sayi%2==0:
    print("Bu cift bir sayidir.")
else:
    print("Bu tek bir sayidir.")

#Answer 5 
sayi = int(input("Bir sayi giriniz :"))
faktor = 1
for i in range(1, sayi + 1):
    faktor = faktor * i
print(faktor)

#Answer 6 Bu cevabi chat gpt den aldim, tam olarak anladigimi soyleyemem
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

#Answer 7
ilksayi=0
ikincisayi=1
tekrar=20
print("Fibonacci serisi : ")
while(tekrar-2):
   ucuncusayi = ilksayi + ikincisayi
   ilksayi=ikincisayi
   ikincisayi=ucuncusayi
   print(ucuncusayi)
   tekrar=tekrar-1

#Answer 8
a = input("Bir kelime yaziniz: ")
print(a[::-1])

#Answer 9 orijinal cozumum.
a = input("Bir kelime yaziniz: ")
b = (a[::-1])
print(b)
if a == b:
    print("Evet bu bir palindromdur")
else:
    print("Hayir degildir")
#Muserref hanimin uyarisi uzerine (dongu ile olmaliydi) Duzeltilmis cevabim
y = input("Lutfen bir kelime giriniz:")


for i in range(len(y) // 2):
   if y[i] != y[len(y) - 1 - i]:
       print("Girdiginiz kelime bir palindrom degildir.")
       break
else:
   print("Girdiginiz kelime bir palindromdur.")

#Answer 10
kilo = int(input("Kilonuzu kilogram cinsinden giriniz: "))
boy = int(input("Boyunuzu santimetre cinsinden giriniz: "))
boy = boy/100
bki= kilo/(boy*boy)
print("Beden kitle indeksiniz :", bki, "dir")
if int(bki) <=25:
    print ("Zayifsiniz")
elif int(bki) < 30:
    print("Normal")
elif int(bki) < 40:
    print("Kilolu")
else:
    print("Asiri Kilolu")

#Answer 11
a = int(input("Bir sayi giriniz: "))
b = int(input("Bir sayi daha giriniz: "))
c = int(input("Son bir sayi daha giriniz: "))
hepsi=[]
hepsi.append(a)
hepsi.append(b)
hepsi.append(c)
print(max(hepsi))

#Answer 12
ders1vize = int(input("Ders 1 Vize notunuzu giriniz :"))
ders1final = int(input("Ders 1 Final notunuzu giriniz :"))
ders1ort = (ders1vize*40+ders1final*60)/100
ders2vize = int(input("Ders 2 Vize notunuzu giriniz :"))
ders2final = int(input("Ders 2 Final notunuzu giriniz :"))
ders2ort = (ders2vize*40+ders2final*60)/100
ders3vize = int(input("Ders 3 Vize notunuzu giriniz :"))
ders3final = int(input("Ders 3 Final notunuzu giriniz :"))
ders3ort = (ders3vize*40+ders3final*60)/100
ders4vize = int(input("Ders 4 Vize notunuzu giriniz :"))
ders4final = int(input("Ders 4 Final notunuzu giriniz :"))
ders4ort = (ders4vize*40+ders4final*60)/100

if ders1ort<50:
    print("Ders1 ortalamaniz,", ders1ort, "dir","basarisiz")
else:
    print("Ders1 ortalamaniz,", ders1ort, "dir","basarili")
if ders2ort<50:
    print("Ders2 ortalamaniz,", ders2ort, "dir","basarisiz")
else:
    print("Ders2 ortalamaniz,", ders2ort, "dir","basarili")
if ders3ort<50:
    print("Ders3 ortalamaniz,", ders3ort, "dir","basarisiz")
else:
    print("Ders3 ortalamaniz,", ders3ort, "dir","basarili")
if ders4ort<50:
    print("Ders4 ortalamaniz,", ders4ort, "dir","basarisiz")
else:
    print("Ders4 ortalamaniz,", ders4ort, "dir","basarili")
