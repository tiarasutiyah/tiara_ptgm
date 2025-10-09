#kalkulator (ga) sederhana

while True:
    num_1 = int(input("Masukkan angka pertama: "))
    operator = input("Operator = (+, -, *, /): ")
    num_2 = int(input("Masukkan angka kedua: "))

    if operator == "+":
        hasil = num_1 + num_2
        print("Hasil:", hasil)
    elif operator == "-":
        hasil = num_1 - num_2
        print("Hasil:", hasil)
    elif operator == "*":
        hasil = num_1 * num_2
        print("Hasil:", hasil)
    elif operator == "/":
        if num_2 != 0:
            hasil = num_1 / num_2
            print("Hasil:", hasil)
        else:
            print("EROR: tidak dapat dibagi dengan nol.")
    else:
        print("Masukkan operator yang sesuai!")

    
    ulang = input("Apakah ingin menghitung lagi? (ya/tidak): ").lower()
    if ulang != "ya":
        print("Terima kasih telah menggunakan kalkulator!")
        break