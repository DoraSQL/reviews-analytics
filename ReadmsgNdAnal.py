
data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1  #count = count + 1
		if count % 1000 ==0: #如果count除以1000的餘數是0
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
sum_len=0
for d in data:
	sum_len = sum_len + len(d) # sum_len是指所有留言長度總和; len(d)是指每個留言長度
print('留言平均長度是', sum_len/len(data)) #len(data)是指data的個數


# print(data[0]) #印出第一筆
# print('----------------------------------------')
# print(data[1])
