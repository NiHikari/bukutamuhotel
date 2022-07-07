import os
import csv
import datetime

csv_file = 'tamuhotelpandawa.csv'
csvco = 'tamuhotelpandawaco.csv'

def bersihlayar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_awal():
    bersihlayar()
    print("="*31)
    print("Selamat Datang di Hotel Pandawa")
    print("="*31)
    print("""
    1. Check-In Tamu
    2. Cek Data Tamu
    3. Check-Out Tamu
    4. Ubah Nomor Kamar
    5. Cari Tamu
    6. Hapus Data Tamu
    7. Keluar
    """)
    pilihan = input("Pilih Nomor Menu : ")
    
    if pilihan == '1':
        checkin()
    elif pilihan =='2':
        cekdata()
    elif pilihan == '3':
        checkout()
    elif pilihan == '4':
        ubahkamar()
    elif pilihan == '5':
        caritamu()
    elif pilihan == '6':
        hapusdata()
    elif pilihan == '7':
        exit()
    elif pilihan == '8':
        maintenance()
    else :
        print("Masukan pilihan yang benar!!!")
        kembalimenu()

def kembalimenu():
    input("\nTekan ENTER untuk kembali...")
    menu_awal()

def checkin():
    bersihlayar()

    print("<"*110)
    print("+"*48,"Check-In Tamu","+"*46)
    print(">"*110,"\n")

    with open(csv_file, mode='a', newline='') as csvfile:
        judulinput = ['Kamar', 'NIK', 'Nama', 'Jenis Kelamin', 'Check In', 'Check Out']
        ubah = csv.DictWriter(csvfile, fieldnames=judulinput)

        tamu = []

        with open(csv_file, mode="r") as csvfile:
            bacafile = csv.DictReader(csvfile)
            for i in bacafile:
                tamu.append(i)

        daftarkamar =[]
        for i in tamu:
            daftarkamar.append(i['Kamar'])

        print("Nomor Kamar yang sudah terisi : ", end='')
        for x in daftarkamar:
            print(x, end='')
            print(" ", end='')
        while True:
            kamar = input("\nMasukan Nomor Kamar :")
            if kamar in daftarkamar:
                print("Kamar sudah TERISI !!! Masukan nomor kamar lainnya!!!")
            else :
                break
        nik = input("NIK : ")
        nama = input("Nama : ")
        kelamin = input("Jenis Kelamin (P / L) : ")
        if kelamin == "P" or kelamin == "p":
            jenis_kelamin = "Perempuan"
        elif kelamin == "L" or kelamin == "l":
            jenis_kelamin = "Laki-Laki"
        check_in = datetime.datetime.now()
        check_out = "Belum Check Out"

        ubah.writerow({'Kamar': kamar, 'NIK' : nik, 'Nama': nama, 'Jenis Kelamin': jenis_kelamin, 'Check In': check_in, 'Check Out': check_out})
    print("Tamu berhasil Check-In pada kamar ", kamar)
    kembalimenu()

def cekdata():
    bersihlayar()
    tamu = []
    with open(csv_file) as csvfile:
        bacafile = csv.reader(csvfile, delimiter=",")
        for i in bacafile:
            tamu.append(i)
    tamuco = []
    with open(csvco) as csvfile:
        bacafile = csv.reader(csvfile, delimiter=",")
        for i in bacafile:
            tamuco.append(i)

        print("<"*110)
        print("+"*49,"Data Tamu","+"*50)
        print(">"*110,"\n")

    judul = tamu.pop(0)
    tamuco.pop(0)
    print(f"{judul[0]} \t {judul[1]} \t\t {judul[2]} \t {judul[3]} \t {judul[4]} \t\t\t {judul[5]}")
    print("="*110)
    for data in tamu:
        print(f"{data[0]} \t {data[1]} \t {data[2]} \t {data[3]} \t {data[4]} \t {data[5]}")
    for data in tamuco:
        print(f"{data[0]} \t {data[1]} \t {data[2]} \t {data[3]} \t {data[4]} \t {data[5]}")
    kembalimenu()

def checkout():
    bersihlayar()
    tamu = []

    with open(csv_file, mode="r") as csvfile:
        bacafile = csv.DictReader(csvfile)
        for i in bacafile:
            tamu.append(i)
    
    print("<"*110)
    print("+"*47,"Check-Out Tamu","+"*46)
    print(">"*110)

    print("\nKamar \t NIK \t\t Nama \t Jenis Kelamin \t Check In \t\t\t Check Out")
    print("="*110)

    for data in tamu:
        print(f"{data['Kamar']} \t {data['NIK']} \t {data['Nama']} \t {data['Jenis Kelamin']} \t {data['Check In']} \t {data['Check Out']}")
    
    print("+"*110)
    nik = input("Masukan NIK : ")
    check_out = datetime.datetime.now()

    daftarnik =[]
    for i in tamu:
        daftarnik.append(i['NIK'])

    if nik in daftarnik:
        tamuco = []
        indeks = 0
        for data in tamu:
            if data['NIK'] == nik:
                tamu[indeks]['Check Out'] = check_out
                tamuco.append(tamu[indeks])
            indeks += 1

        with open(csvco, mode='a', newline='') as csvfile:
            judulinput = ['Kamar', 'NIK', 'Nama', 'Jenis Kelamin', 'Check In', 'Check Out']
            ubah = csv.DictWriter(csvfile, fieldnames=judulinput)
            # ubah.writeheader()
            for databaru in tamuco:
                ubah.writerow({'Kamar': databaru['Kamar'],'NIK' : databaru['NIK'], 'Nama': databaru['Nama'], 'Jenis Kelamin': databaru['Jenis Kelamin'], 'Check In': databaru['Check In'], 'Check Out': databaru['Check Out']})
        
        indeks = 0
        for data in tamu:
            if data['NIK'] == nik:
                tamu.remove(tamu[indeks])
            indeks += 1

        with open(csv_file, mode='w', newline='') as csvfile:
            judulinput = ['Kamar', 'NIK', 'Nama', 'Jenis Kelamin', 'Check In', 'Check Out']
            ubah = csv.DictWriter(csvfile, fieldnames=judulinput)
            ubah.writeheader()
            for databaru in tamu:
                ubah.writerow({'Kamar': databaru['Kamar'],'NIK' : databaru['NIK'], 'Nama': databaru['Nama'], 'Jenis Kelamin': databaru['Jenis Kelamin'], 'Check In': databaru['Check In'], 'Check Out': databaru['Check Out']})

        print("\nTamu dengan NIK {} berhasil Check Out pada {}".format(nik, check_out))
        kembalimenu()


    else :
        print("Data tidak ditemukan!!!")
        ulang = input("Masukan data ulang? (y/n) : ")
        if ulang == "y" or ulang == "Y":
            checkout()
        else :
            menu_awal()

def ubahkamar():
    bersihlayar()
    tamu = []

    with open(csv_file, mode="r") as csvfile:
        bacafile = csv.DictReader(csvfile)
        for i in bacafile:
            tamu.append(i)
    
    print("<"*110)
    print("+"*47,"Ubah Kamar Tamu","+"*46)
    print(">"*110)

    print("\nKamar \t NIK \t\t Nama \t Jenis Kelamin \t Check In \t\t\t Check Out")
    print("="*110)

    for data in tamu:
        print(f"{data['Kamar']} \t {data['NIK']} \t {data['Nama']} \t {data['Jenis Kelamin']} \t {data['Check In']} \t {data['Check Out']}")
    
    print("+"*110)
    nik = input("Cari NIK : ")

    daftarkamar =[]
    daftarnik = []
    for i in tamu:
        daftarkamar.append(i['Kamar'])
        daftarnik.append(i['NIK'])

    if nik in daftarnik:
        ulang = False
        while not ulang :
            kamar = input("\nMasukan Nomor Kamar Baru : ")
            if kamar in daftarkamar:
                print("Kamar sudah TERISI !!! Masukan nomor kamar lainnya!!!")
                ulang = input("Masukan data ulang? (y/n) : ")
                if ulang == "y" or ulang == "Y":
                    ulang = False
                else :
                    menu_awal()
            else :
                indeks = 0
                for data in tamu:
                    if data['NIK'] == nik:
                        tamu[indeks]['Kamar'] = kamar
                    indeks += 1
                    ulang = True
    else :
        print("Data NIK tidak ada!!!")
        ulang = input("Masukan data ulang? (y/n) : ")
        if ulang == "y" or ulang == "Y":
            ubahkamar()
        else :
            menu_awal()

    with open(csv_file, mode='w', newline='') as csvfile:
        judulinput = ['Kamar', 'NIK', 'Nama', 'Jenis Kelamin', 'Check In', 'Check Out']
        ubah = csv.DictWriter(csvfile, fieldnames=judulinput)
        ubah.writeheader()
        for databaru in tamu:
            ubah.writerow({'Kamar': databaru['Kamar'],'NIK' : databaru['NIK'], 'Nama': databaru['Nama'], 'Jenis Kelamin': databaru['Jenis Kelamin'], 'Check In': databaru['Check In'], 'Check Out': databaru['Check Out']})
    print("Kamar Tamu berhasil diubah menjadi nomor ", kamar)
    kembalimenu()

def caritamu():
    bersihlayar()
    tamu = []
    with open(csv_file, mode="r") as csvfile:
        bacafile = csv.DictReader(csvfile)
        for i in bacafile:
            tamu.append(i)
    tamuco = []
    with open(csvco, mode="r") as csvfile:
        bacafile = csv.DictReader(csvfile)
        for i in bacafile:
            tamuco.append(i)
    
    print("<"*110)
    print("+"*50,"Cari Tamu","+"*49)
    print(">"*110)

    nik = input("\nCari berdasarkan NIK : ")
    
    daftarnik = []
    daftarnikco = []
    for i in tamu:
        daftarnik.append(i['NIK'])
    for i in tamuco:
        daftarnikco.append(i['NIK'])

    data_ditemukan = []
    if nik in daftarnik:
        indeks = 0
        for data in tamu:
            if data['NIK'] == nik:
                data_ditemukan = tamu[indeks]
            indeks += 1
    elif nik in daftarnikco:
        indeks = 0
        for data in tamuco:
            if data['NIK'] == nik:
                data_ditemukan = tamuco[indeks]
            indeks += 1

    if len(data_ditemukan) > 0:
        print("TAMU DITEMUKAN !!!")
        print(f"Kamar\t\t\t: {data_ditemukan['Kamar']}")
        print(f"Nama (Jenis Kelamin) \t: {data_ditemukan['Nama']} ({data_ditemukan['Jenis Kelamin']})")
        print(f"Check In \t\t: {data_ditemukan['Check In']}")
        print(f"Check Out \t\t: {data_ditemukan['Check Out']}")
        lanjut = input("\nCari Lagi? (y/n) ")
        if lanjut == "y":
            caritamu()
        else :
            menu_awal()
    else :
        print("Data Tamu TIDAK ditemukan!!!")
        lanjut = input("Cari Lagi? (y/n) ")
        if lanjut == "y":
            caritamu()
        else :
            kembalimenu()

def hapusdata():
    bersihlayar()
    tamu = []
    with open(csv_file, mode="r") as csvfile:
        bacafile = csv.DictReader(csvfile)
        for i in bacafile:
            tamu.append(i)
    tamuco = []
    with open(csvco, mode="r") as csvfile:
        bacafile = csv.DictReader(csvfile)
        for i in bacafile:
            tamuco.append(i)
    
    print("<"*110)
    print("+"*47,"Hapus Data Tamu","+"*46)
    print(">"*110)

    print("\nKamar \t NIK \t\t Nama \t Jenis Kelamin \t Check In \t\t\t Check Out")
    print("="*110)

    for data in tamu:
        print(f"{data['Kamar']} \t {data['NIK']} \t {data['Nama']} \t {data['Jenis Kelamin']} \t {data['Check In']} \t {data['Check Out']}")
    for data in tamuco:
        print(f"{data['Kamar']} \t {data['NIK']} \t {data['Nama']} \t {data['Jenis Kelamin']} \t {data['Check In']} \t {data['Check Out']}")
    
    daftarnik = []
    daftarnikco = []
    for i in tamu:
        daftarnik.append(i['NIK'])
    for i in tamuco:
        daftarnikco.append(i['NIK'])
    print("+"*110)

    nik = input("Masukan NIK : ")
    if nik in daftarnik:
        indeks = 0
        for data in tamu:
            if data['NIK'] == nik:
                tamu.remove(tamu[indeks])
            indeks += 1

        with open(csv_file, mode='w', newline='') as csvfile:
            judulinput = ['Kamar', 'NIK', 'Nama', 'Jenis Kelamin', 'Check In', 'Check Out']
            ubah = csv.DictWriter(csvfile, fieldnames=judulinput)
            ubah.writeheader()
            for databaru in tamu:
                ubah.writerow({'Kamar': databaru['Kamar'],'NIK' : databaru['NIK'], 'Nama': databaru['Nama'], 'Jenis Kelamin': databaru['Jenis Kelamin'], 'Check In': databaru['Check In'], 'Check Out': databaru['Check Out']})
        
        print("Data dengan NIK {} sudah terhapus".format(nik))
        kembalimenu()

    elif nik in daftarnikco:
        indeks = 0
        for data in tamuco:
            if data['NIK'] == nik:
                tamuco.remove(tamuco[indeks])
            indeks += 1

        with open(csvco, mode='w', newline='') as csvfile:
            judulinput = ['Kamar', 'NIK', 'Nama', 'Jenis Kelamin', 'Check In', 'Check Out']
            ubah = csv.DictWriter(csvfile, fieldnames=judulinput)
            ubah.writeheader()
            for databaru in tamuco:
                ubah.writerow({'Kamar': databaru['Kamar'],'NIK' : databaru['NIK'], 'Nama': databaru['Nama'], 'Jenis Kelamin': databaru['Jenis Kelamin'], 'Check In': databaru['Check In'], 'Check Out': databaru['Check Out']})
        
        print("Data dengan NIK {} sudah terhapus".format(nik))
        kembalimenu()
    else:
        print("NIK tidak ditemukan!!!")
        pilihan = input("Coba Lagi? (y/n) : ")
        if pilihan == 'y':
            hapusdata()
        else:
            menu_awal()

if __name__ == "__main__":
    while True:
        menu_awal()