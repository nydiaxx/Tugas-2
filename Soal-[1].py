while True:
    print("Selamat datang!")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    pilih = int(input("Pilih Menu : "))
    if pilih == 1:
        def func_kontak1 (nama, notelp):
            print("Daftar Kontak")
            print("Nama\t\t : " + nama)
            print("No Telepon\t : ", notelp)
            print("=========================")
        func_kontak1("Nydia", 20)
        func_kontak1("Nina", 37)
    elif pilih == 2:
        def func_kontak2():
            nama = str(input("Nama\t\t: "))
            notelp = int(input("No Telepon\t: "))
        func_kontak2()
        print("kontak berhasil ditambah!")
        print("==============================")
    elif pilih == 3:
        print("Program selesai, sampai jumpa!")
        print("================================")
        break
    else:
        print("Menu tidak tersedia")
        
    
