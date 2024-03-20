import sys

rlt = {}
N = int(sys.stdin.readline())
for _ in range(N) :
    file = sys.stdin.readline().strip()
    index = file.index('.')
    extension = file[index + 1:]
    if (rlt.get(extension)) :
        rlt[extension] += 1
    else :
        rlt[extension] = 1

extension_list = list(rlt.keys())
extension_list.sort()

for i in range(len(extension_list)) :
    exts = extension_list[i]
    print(f"{exts} {rlt[exts]}")