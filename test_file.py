from wed import wea

app=wea("Delhi")
print(app.find_data())
data = app.find_data()
for value in data.values():
	print(value)