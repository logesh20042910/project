import zipfile
zip_file = zipfile.ZipFile('temp3.zip','w')
zip_file.write('req.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()