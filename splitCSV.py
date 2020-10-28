import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

import sys
args = sys.argv
full_name = "C:\\Users\\Admin\\Desktop\\MRI-20200701-20200731\\MRI_IN_202007__detail.csv" #file location
count = 3 #how many splits do you want
log_mark_line_count = 10000
if len(args) >= 4:
    log_mark_line_count = int(args[3])
suffix = ''
splited_name = str.split(full_name, '.')
name = splited_name[0]
if len(splited_name) > 1:
    suffix = splited_name[1]
files = []
for i in range(0, count):
    splited_file_name = name + "-P" + str(i)
    if len(suffix) > 0:
        splited_file_name += "." + suffix
    f = open(splited_file_name, "w")
    files.append(f)
with open(full_name) as f:
    index = 0
    line = f.readline()
    for line in f:
        if index % log_mark_line_count == 0:
            print('splited', index, 'lines')
        files[index % count].write(line)
        index += 1
for i in range(0, count):
    files[i].close()
print('split over!')