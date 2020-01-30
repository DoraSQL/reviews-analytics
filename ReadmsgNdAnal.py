
data=[]
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
print(data[0]) #印出第一筆
print('----------------------------------------')
print(data[1])
