def s2_in_s1(s1='',s2=''):
    s1=s1.lower()
    s2=s2.lower()
    if s2 in s1:
        return "Yes"
    else:
        return "No"
print(s2_in_s1("macbook","book"))