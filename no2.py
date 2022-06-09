age=int(input("enter age"))
sex=input("enter number")
marital=input("enter marital")
if sex=="f":
    if age>=18 and age<=60 or marital=="yes":
        print("she will work only urban area")
    else:
        print("none")
elif sex=="m":
    if age>=20 and age<=40 or marital=="yes":
        print("he may work in anywhere")
    elif age>=40 and age<=60 or marital=="yes":
        print("he may work in urban area")
    else:
        print("not")
else:
    print("error")