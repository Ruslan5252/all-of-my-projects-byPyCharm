def exist_tr(a,b,c):
    if a<b+c and b<c+a and c<b+a:
        return "Yes"
    else:
        return "No"
print(exist_tr(3,6,2))