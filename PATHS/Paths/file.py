from time import ctime
path = Path("ecommerce/__init__.py")




print(ctime(path.stat().st_ctime))


path.read_text()
path.write_text('....')


import shutil

