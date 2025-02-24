
with open ('customers.xml','r') as f:
    lines=f.readlines()
ll = len(lines)
print (ll)
for index, line in enumerate(lines):
    srch='word_margin'
    if 'word_margin' in line:
        id=line.index(srch)
        print (index,id)
        break
