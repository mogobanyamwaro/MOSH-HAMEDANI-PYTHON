import json
from pathlib import Path
movies = [
    {"id":1,"title":'hello'},
    {"id":1,"title":'mogoba'},
]

data = json.dumps(movies)

Path('text.json').write_text(data)

data = Path('text.json').read_text()
movies = json.loads(data)
print(movies)