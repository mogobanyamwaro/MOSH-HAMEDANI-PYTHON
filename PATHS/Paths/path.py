from pathlib import Path
# for windows guys
Path(r"C:\Program Files\Microsoft") 

# for linux users

Path("/usr/local/bin")
Path()


# Path() /"ecommerce" /"__init__.py"

# Path.home()


path =Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)

