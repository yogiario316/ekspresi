nama = ["Kalkulator Sederhana", "Credit by Yogi Ario", "Contoh soal:", "2+9 atau 2*9+6-7/2"]
for i in nama:
    print(i)

import re

def calculate_expression(expression):
    # Menghapus spasi dari ekspresi
    expression = expression.replace(' ', '')
    
    # Memeriksa apakah ekspresi hanya berisi angka dan operator yang diizinkan
    if re.match(r'^[0-9+\-*/.()]+$', expression):
        try:
            # Menghitung hasil ekspresi
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {e}"
    else:
        return "Gagal. Hanya angka dan simbol berikut +, -, *, /, . yang diperbolehkan."

def main():
    while True:
        # Meminta input dari pengguna
        user_input = input("Masukkan soal matematikamu: ")
        result = calculate_expression(user_input)
        print(f"Hasil: {result}")
        
        # Memberikan opsi untuk mengulang atau keluar
        choice = input("Tekan Sembarang tombol untuk mengulang perhitungan atau Tekan 1 untuk keluar: ")
        if choice == '1':
            break

if __name__ == "__main__":
    main()
