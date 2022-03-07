v=7228
def su(v):
    s=0
    for i in str(v):
        s+=int(i)
    return s
s=su(v)
while s>9:
    s=su(s)
print(s)