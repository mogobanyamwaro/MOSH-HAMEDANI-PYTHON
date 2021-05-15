from pathlib import Path
path = Path('ecommerce')
path.exists()
path.mkdir()
path.rmdir()
path.rename("eccomerce2")
# to get the list of files and directories
print(path.iterdir())

for p in path.iterdir():
    print(p)

# glob u can use the pattern

paths  = [p for p in path.glob("*.py")]