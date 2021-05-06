def weekday_dutch(date):
    import datetime
    day_name = {"Monday": "maandag", "Tuesday": "dinsdag", "Wednesday": "woensdag", "Thursday": "donderdag",
                "Friday": "vrijdag", "Saturday": "zaterdag", "Sunday": "zondag"}
    day = datetime.datetime.strptime(date, '%d %m %Y').strftime("%A")
    return day_name[day]

print (weekday_dutch("21 9 1970"))
print (weekday_dutch("2 9 1945"))
print (weekday_dutch("9 11 2001"))