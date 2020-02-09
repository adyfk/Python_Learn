# Set
# Anda tidak dapat mengakses item dalam set dengan merujuk pada indeks,
# karena set tidak diurutkan, item tidak memiliki indeks

thistuple = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}


thistuple.add("strip")
# menambahkan pada set

thistuple.update(["test1", "test2", "test3"])
# menambahkan multiple item

thistuple.discard("apple")
# menghapus item set

thistuple.pop()
# menghapus item array terakhir

thistuple.clear()
# Menghapus semua isi set
