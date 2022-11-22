# ANGGIT GENTO YUWONO
# PROJECT MODUL 1 
# PURWADHIKA - JCDSOL-008-042
# GUDANG - DATA STOCK

menu = ['1. Report Data Stok Gudang',
        '2. Menambahkan Data Stok Gudang',
        '3. Mengubah Data Stok Gudang',
        '4. Menghapus Data Stok Gudang', 
        '5. Keluar']

stok = [ {'Kode' : 'Wkwk1', 'Nama' : 'AC-DAIKIN', 'Spesifikasi' : '2PK', 
           'Quantity' : 15, 'Lokasi' : 'A01'}
        {'Kode' : 'Wkwk2', 'Nama' : 'Pipa Refrigerant', 'Spesifikasi' : '3 Meter', 
           'Quantity' : 5 Batang, 'Lokasi' : 'A02'}
        {'Kode' : 'Wkwk3', 'Nama' : 'Refrigerant', 'Spesifikasi' : 'R407', 
           'Quantity' : 10 Kaleng, 'Lokasi' : 'A03'} ]
           


def Main_Menu () : 
    MainMenu = True 
    while MainMenu != '5' : 
        print ('\n======= Data Record Stok Gudang =======\n')
        for i in menu :
            print(i)
            Main_Menu = input('Silahkan pilih Main_Menu [1-5] : ')
            if MainMenu == '1' :
               Report_Menu()
            elif MainMenu == '2' :
                Create_Menu()
            elif MainMenu == '3' :
                Update_Menu()
            elif  Main_Menu == '4' :
                Delete_Menu()
            elif Main_Menu == '5' : 
                print ('\nTerima kasih dan sampai jumpa!!!')
            break




def Report_Menu () : 
    ReportMenu = True
    while ReportMenu != '3' :
        print ('n\++++++ Report data stok gudang ++++++')
        print ('1. Report seluruh stok gudang')
        print ('2. Report stok gudang tertentu')
        print ('3. Kembali ke Menu Utama')
        ReportMenu = input('Silahkan pilih Sub Menu Report Data [1-3] : ')

        if ReportMenu == '1':
           if len(stok) !=0 :
                print ('\nDaftar stok gudang :')
                for j, i in enumerate (stok) :
                    print (f"{j+1}. Kode : {i['Kode']}, Spesifikasi : {i['Spesifikasi']}") 

                
                else : 
                 print ( '\n******* Stok gudang tidak ada *******')
                 continue

    

        elif ReportMenu == '2' :
            if len(stok) !=0 :
                 std = input ('Masukan kode stok gudang : ').upper()
                 print (f"Data Stok gudang dengan kode : {std}")
                 for j, i in enumerate(stok):
                     if i ['Kode'] == std : 
                        print (f"{j+1}"). Kode : {i['Kode']}, Nama : {i['Nama']}, Spesifikasi : {i['Spesifikasi']}
                        break
        else : 
            print ('\n******* Stok gudang tidak terdaftar *******')
    
def create_Menu () :
    while True :
        print ('\n+++++++ Menambah data Stok gudang +++++++')
        print ('1. Tambah data stok gudang')
        print ('2. Kembali ke Menu utama')
        Createmenu = input ('Silahkan pilih sub menu create data [1-2] : ')

        if Createmenu == '1':
            if len(stok) !=0 :
                addkode = input ('Masukan kode stok gudang').upper ()
                for j, i in enumerate (stok):
                    if addkode == i ['Kode'] :
                        print ('stok gudang sudah ada')
                        break
                    
                else :
                    addNama = input ('Masukan nama barang :').upper ()
                    addSpek = input ('Masukan spesifikasi barang :').upper ()
                    addQty = input ('Masukan quantity barang :').upper ()
                    addLoc = input ('Masukan lokasi barang : ').upper ()

                    tambahan = {
                        'Kode' : '{}'.format(addkode),
                        'Nama' : '{}'.format(addNama),
                        'Spesifikasi' : '{}'.format(addSpek),
                        'Quantity' : '{}'.format(addQty),
                        'Lokasi' : '{}'.format(addLoc),
                    }
                    print('\nStok gudang yang ditambahkan adalah : ',tambahan)
                    checkerCreate = input ('n\Apakah sudah benar? (Y/N) : ').upper()
                    if checkerCreate == 'Y':
                        stok.append(tambahan)
                        print('\n--- Stok gudang berhasil ditambahkan ---')
                    elif checkerCreate == 'N':
                        print('n\--- Stok gudan tidak berhasil ditambahkan ---')
                    else:
                        continue
            
        
        elif Createmenu == '2':
            break

        else :
            print ('\n******* Pilihan menu tidak ada *******')

def Update_Menu () :
    Updatemenu = True
    while Updatemenu != '2' :
        print ('\n+++++++ Mengubah data stok gudang +++++++')
        print ('1. ubah data stok gudang')
        print ('2. kembli ke menu utama')
        Updatemenu = input('Silahkan pilih sub menu update data [1-2] :')

        if Updatemenu == '1':
            if len(stok) !=0 :
                updatekode = input('Masukan kode stok gudang : ').upper ()

                for i in range (len(stok)):
                    if updatekode == stok [i] ['Kode'] :
                        print ('Stok gudang yang ingin diubah adalah : ', stok [i])
                        nameupdate = input ('n\Masukan kolom yang ingin diubah :').lower()

                        if nameupdate == 'Kode' :
                            Ubahkode = input('\nUpdate kode :').upper()
                            confkode = input('\nApakah data akan diubah? [Y/N] :').lower()
                            if confkode == 'y' :
                                stok[i]['Kode'] = Ubahkode
                                print('\nData berhasil diubah')
                                break
                            elif confkode == 'n':
                                print ('\nData tidak diubah')
                        if nameupdate == 'Nama' :
                            Ubahnama = input('\nUpdate Nama :').upper()
                            confnama = input('\nApakah data akan diubah? [Y/N] :').lower()
                            if confnama == 'y' :
                                stok[i]['Nama'] = Ubahnama
                                print('\nData berhasil diubah')
                                break
                            elif confnama == 'n' :
                                print ('\nData tidak diubah')
                        if nameupdate == 'Spesifikasi' :
                            Ubahspek = input('\nUpdate Spesifikasi :').upper()
                            confspek = input('\nApakah data akan diubah? [Y/N] :').lower()
                            if confspek == 'y' :
                                stok[i]['Spesifikasi'] = Ubahspek
                                print('\nData berhasil diubah')
                                break
                            elif confspek == 'n' :
                                print ('\nData tidak diubah')
                        if nameupdate == 'Quantity' :
                            Ubahqty = input('\nUpdate Quantity :').upper()
                            confqty = input('\nApakah data akan diubah? [Y/N] :').lower()
                            if confqty == 'y' :
                                stok[i]['Quantity'] = Ubahqty
                                print('\nData berhasil diubah')
                                break
                            elif confqty == 'n' :
                                print ('\nData tidak diubah')
                        if nameupdate == 'Lokasi' :
                            Ubahlok = input('\nUpdate Lokasi :').upper()
                            conflok = input('\nApakah data akan diubah? [Y/N] :').lower()
                            if conflok == 'y' :
                                stok[i]['Lokasi'] = Ubahlok
                                print('\nData berhasil diubah')
                                break
                            elif conflok == 'n' :
                                print ('\nData tidak diubah')
                else :
                    print ('\n******* Pilihan menu tidak ada *******')

def Delete_Menu () :
    DeleteMenu = True
    while DeleteMenu != '2' :
        print ('\n+++++++ Delete data stok gudang +++++++')
        print ('1. Hapus stok gudang')
        print ('2. Kembali ke menu utama')
        DeleteMenu = input('silahkan pilih sub menu report data  [1-3] : ')

        if DeleteMenu == '1' :
            if len(stok) !=0 :
                delCode = input ('\nMasukan kode stok gudang yang ingin dihapus : ').upper()
                for i in range (len(stok)):
                    if delCode == stok [i] ['Kode'] :
                        print ('\nStok gudang yang ingin dihapus adalah : ', stok[i])
                        confDel = input ('\nApakah yakin ingin menghapus data ini (Y/N) :').lower ()
                        if confDel == 'y':
                            del stok[i]
                            print('\nStok gudang yang berhasil dihapus')
                            break
                        elif confDel == 'n':
                            print('\nStok gudang tidak terhapus')
                            break
                        else :
                            print('\nMenu yang anda masukan salah')
                            break
                    else :
                        print ('\nStok gudang tidak ditemukan')
                        break
                else:
                    print ('\nStok gudang sudah tidak ada stok')
            elif DeleteMenu == '2' :
                break
            else: 
                print ('\n******* Pilihan menu tidak ada *******')

Main_Menu()





                