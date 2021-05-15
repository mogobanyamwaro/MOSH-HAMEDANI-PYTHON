from pathlib import Path
from zipfile import ZipExtFile

with  ZipExtFile("files.zip", "w") as zip:
    for path in Path('ecommerce').rglob("*.*"):
        zip.write(path)



with ZipExtFile("files.zip") as zip:
    # get all the zip files
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extact")