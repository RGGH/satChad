# with open("data/mC43pZkpTec/parsed_subtitles.txt") as f:
#     d = f.readlines()
import json
d = data = [json.loads(line) for line in open('data/mC43pZkpTec/parsed_subtitles.txt', 'r')]
print(len(d))
    