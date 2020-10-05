# Nomor 1

bil1, bil2, bil3, bil4, bil5 = 100,80,70,75,100
rata = (bil1 + bil2 + bil3 + bil4 + bil5) / 5
print("Bilangan = ", bil1, bil2, bil3, bil4, bil5)
print("Jumlah Data = ", 5)
print("Rata-Rata = ", rata)

# Nomor 2

print("Program menghitung luas dan keliling persegi panjang")
p = int(input("Masukkan panjang (cm) = "))
l = int(input("Masukkan lebar (cm) = "))
luas = p*l
keliling = 2*(p+l)

print("")
print("Hasil Perhitungan")
print("="*20)
print("Panjang =", p, "cm")
print("Lebar =", l, "cm")
print("Luas =", luas, "cm")
print("Keliling =", keliling, "cm")

# Nomor 3

print("="*30)
print(""*5, "Program perhitungan BMI", ""*5)
print("="*30)

berat_badan = float(input("Masukkan berat Anda (kg) = "))
tinggi_badan = float(input("Masukkan tinggi Anda (m) = "))
bmi = berat_badan/(tinggi_badan*tinggi_badan)

print("BMI Anda adalah", bmi)
if bmi < 18.5:
    print("Berat badan kurang")
elif bmi >= 18.5 and bmi <= 22.9:
    print("Berat badan kurang")
elif bmi >= 23 and bmi <= 29.9:
    print("Berat badan berlebih (kecenderungan obesitas)")
else:
    print("Obesitas")

# Nomor 4

data = []
n = int(input("Masukkan jumlah data = "))

for i in range(n):
    bil = int(input("Masukkan bilangan ke-{} = ".format(i+1)))
    data.append(bil)
    
maximal = 0
minimal = 0
for i in data:
    if maximal == 0 or minimal == 0:
        maximal = i
        minimal = i
    else:
        if i > maximal:
            maximal = i
            
        if i < minimal:
            minimal = i
        
print("Maximal = ", maximal)
print("Minimal = ", minimal)

# Nomor 5

percobaan = 0
isSuccess = False

config_user = "huda"
config_pass = "huda123"

while (isSuccess != True) and (percobaan < 3):
    username = input("Masukkan username Anda = ")
    password = input("Masukkan password Anda = ")
    
    if (username == config_user) and (password == config_pass):
        isSuccess = True
        print("Anda berhasil masuk")
    else:
        print("Maaf username salah dan password Anda salah!")
        percobaan += 1
        
if percobaan >= 3:
    print("Akun anda terblokir karena telah mencoba 3 kali, mohon coba lagi..")