from pathlib import Path
p = Path('.')
ls = list(p.glob('**/parsed_subtitles.txt'))
for id, f in enumerate(ls):
    print(ls[id])
