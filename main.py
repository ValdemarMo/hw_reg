import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

cl_str = ''
for x in contacts_list:
  cl_str += '\n'
  cx = x
  for xx in x:
    cl_str += xx + ','

cl_r = cl_str
print(f'\n<start cl>{cl_r}')

r = r'^(\w*\s*)\ (\w*\s*)\ (\w*\s*)(\,,\s*)'
s = "\\1,\\2,\\3"
cl_r = re.sub(r, s, cl_r, 0, re.MULTILINE)
r = r'(^\w*\s*)(\,\s*)(\w*\s*)(\ \s*)(\w*\s*)(\,,\s*)'
s = "\\1,\\3,\\5,"
cl_r = re.sub(r, s, cl_r, 0, re.MULTILINE)
r = r'^(\w*\s*)(\ )(\w*\s*)(\,,\s*)'
s = "\\1,\\3,"
cl_r = re.sub(r, s, cl_r, 0, re.MULTILINE)
r = r'^(\w*\s*\,\w*\s*\,)(\w*\s*\,)([\w[a-z]*\s*]*)\,((\w*|[^a-z]\s*)*)\,((\w*|[^a-z]\s*)*)\,((\w*\.*\@*)*)(\,*)$'
s = "\\1\\2\\3,\\4,\\6,\\8,"
cl_r = re.sub(r, s, cl_r, 0, re.MULTILINE)
r = r'(\+7|8)\s*\(*\s*(\d{3})\s*\-*\s*\)*\s*(\d{3})\s*-*\s*(\d{2})\s*-*\s*(\d{2})\s*'
s = "+7(\\2)\\3-\\4-\\5"
cl_r = re.sub(r, s, cl_r, 0, re.MULTILINE)
r = r'(\ *\(*)\s*(\доб)\s*\.*\s*(\d*)\s*\)*'
s = " \\2.\\3"
cl_r = re.sub(r, s, cl_r, 0, re.MULTILINE)

# print(f'\n<name and phone mod cl>\n{cl_r}')

r = r"\n"
s = ""
cl_r = re.sub(r, s, cl_r, 0, re.MULTILINE)
cl_r = cl_r.split(',')
cl_r.pop(len(cl_r)-1)

# print(f'\n<split [in]>\n{cl_r}')

c = 0
cx = 0
cl_x = []
cl_xx = []
for x in cl_r:
  cl_xx.append(x)
  if cx == 6:
    cl_x.append(cl_xx)
    cx = 0
    c += 1
    cl_xx = []
  else: cx += 1

cl_r = cl_x

# print(f'\n<split [[in]]>\n{cl_x}\n')

for xc in cl_r:
  for cc in cl_r:
    if cc != xc:
      if xc[0]==cc[0] and xc[1]==cc[1]:
        for c in range(2,7):
          if len(cc[c]) != 0:
            xc[c] = cc[c]

# print(f'\n<upd cl>\n{cl_x}')

cl_fin = []
for x in cl_x:
  if x not in cl_fin:
    cl_fin.append(x)

# print(f'\n<del dub> \n{cl_fin}')

cl_str = ''
for x in cl_fin:
  cx = x
  for xx in x:
    cl_str += xx + ','
  cl_str += '\n'

cl_r = cl_str
print(f'\n<result cl>\n{cl_r}')

with open("phonebook.csv", "w") as f:
  f.write((cl_r))
