"""
Semua sintaksis dasar pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

#Sekuensial
print('Ibu berkata,"pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print("Maka Budi kemudian pergi ke toko")
print("Dan mulai berbelanja")

# percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print (f"Jumlah botol susu, {jumlah_botol_susu} btl")
print(f"Jumlah telur, {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
else:
    print ("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")

