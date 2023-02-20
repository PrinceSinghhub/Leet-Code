
s = list(input())
sq_open_bracket =[]
sq_close_bracket=[]

cr_open_bracket=[]
cr_close_bracket = []

pr_open_bracket=[]
pr_close_bracket = []

for i in range(len(s)):
    if s[i]=='(':
        pr_open_bracket.append(s[i])

    elif s[i]==")":
        pr_close_bracket.append(s[i])

    elif s[i]=="[":
        sq_open_bracket.append(s[i])

    elif s[i]=="]":
        sq_close_bracket.append(s[i])

    elif s[i]=="{":
        cr_open_bracket.append(s[i])

    elif s[i]=="}":
        cr_close_bracket.append(s[i])

print(pr_open_bracket)
print(pr_close_bracket)
print(sq_open_bracket)
print(sq_close_bracket)
print(cr_open_bracket)
print(cr_close_bracket)

res = []
print(len(sq_open_bracket), len(sq_close_bracket))
if len(pr_open_bracket)!=len(pr_close_bracket):
    res.append(False)

elif len(sq_open_bracket)!=len(sq_close_bracket):
    res.append(False)

elif len(cr_open_bracket)!=len(cr_close_bracket):
    res.append(False)

else:
    res.append(True)
print(res)
print(all(res))