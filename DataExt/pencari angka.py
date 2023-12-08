import chardet
import csv
# Script python untuk mencari 6 digit angka dalam sebuah file teks
# Mendeteksi kodek otomatis
with open('text_file.txt', 'rb') as file: # Ganti text_file.txt dengan file yang ada full path file anda
    result = chardet.detect(file.read())

# Membaca file dengan kodek yang terdeteksi
numbers = [int(x) for x in open('text_file.txt', encoding=result['encoding']).read().split() if x.isdigit() and len(x) == 6]
print("Bilangan enam digit yang ditemukan:", numbers)


numbers = [numbers]  # Input nilai ke dalam fungsi csv

# Menyimpan data ke dalam file CSV
with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Menulis header jika diperlukan
    writer.writerow(["Number"])  # Tulis header, jika ada

    # Menulis data
    for number in numbers:
        writer.writerow([number])
