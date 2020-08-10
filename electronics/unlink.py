import re

with open("D:\GoogleDrive\Projects\Falmo\electronics\Circuit\scene.phn", "r", encoding="utf-8") as f:
    lines = list(f.readlines())

i = 0
lines_modified = []

for line in lines:
    if m := re.match(r"(\s*body := )\d+(;.*)", line):
        i += 1
        lines_modified.append(f"{m.groups()[0]}{i}{m.groups()[1]}")
    else:
        lines_modified.append(line)

with open("D:\GoogleDrive\Projects\Falmo\electronics\Circuit\scene_m.phn", "w", encoding="utf-8") as f:
    f.writelines(lines_modified)