merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000

harga_merchandise = [merchandise_1, merchandise_2, merchandise_3,
                     merchandise_4, merchandise_5, merchandise_6]

biaya_kado = 7500

total_harga = (merchandise_1 + merchandise_2 + merchandise_3 +
               merchandise_4 + merchandise_5 + merchandise_6 + biaya_kado)

rata_rata = total_harga / len(harga_merchandise)

nim = 105

bolean = nim > rata_rata

kurs_usd = 16500
total_harga_usd = total_harga / kurs_usd

barang_2_sampai_4 = harga_merchandise[-5:-2]

print("merchandise_1 =", merchandise_1)
print("merchandise_2 =", merchandise_2)
print("merchandise_3 =", merchandise_3)
print("merchandise_4 =", merchandise_4)
print("merchandise_5 =", merchandise_5)
print("merchandise_6 =", merchandise_6)
print("harga_merchandise =", harga_merchandise)
print("biaya_kado =", biaya_kado)
print("total_harga =", total_harga)
print("rata_rata =", rata_rata)
print("nim =", nim)
print("bolean =", bolean)
print("total_harga_usd =", total_harga_usd)
print("barang_2 sampai barang_4 =", barang_2_sampai_4)