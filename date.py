import datetime


def date():
	x = datetime.datetime.now()
	if(x.month >=8):
		a = "1/8/"
		date = a+str(x.year)
	else:
		a="1/1/"
		date = a+str(x.year)
	return date


print(date())

