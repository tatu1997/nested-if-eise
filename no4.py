day=input("enter day")
meal_time=input("enter meal time")
if day=="monday":
    if meal_time=="breakfast":
        print("pri sabzi")
    elif meal_time=="linch":
        print("sambhar rice")
    elif meal_time=="dinner":
        print("chicken rice")
    else:
        print("none")
elif day=="tuedays":
    if meal_time=="breakfast":
        print("poha")
    elif meal_time=="lunch":
        print("rajma rice")
    elif meal_time=="dinner":
        print("roti sabji")
    else:
        print("not")
else:
    print("error")