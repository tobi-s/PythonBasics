import zipfile

myzip = zipfile.ZipFile("Archive.zip")

mylist = myzip.namelist()

for m in mylist:
	print(m)


