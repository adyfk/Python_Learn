# LIst atau Array

thislist = ["apple", "banana", "cherry"]
# sama seperti dengan string


thislist[-1]
# untuk mencari item paling terakhir

thislist[2:5]
# untuk mencari dari index 2 hingga index sebeluh 5

thislist[:4]
# untuk mencari index sebelum 4

"apple" in thislist
# check item berada di dalam array

thislist.append("melon")
# menambahkan item pada array

thislist.index("coconut", 1)
# menyisipkan item pada index tertentu

thislist.remove("apple")
# mengahpus item dari array

thislist.pop()
# mengapus 1 item array dari belakang

del thislist[0]
# menghapus item array pada index tertentu

thislist.clear()
# mengahapus semua item array

thislist.copy()
# untuk clone array
# atau dengan cara
list(thislist)

thislist.sort()
# untuk sorting(mengurutkan) item array
