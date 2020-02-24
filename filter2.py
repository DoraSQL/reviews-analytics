
data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count +=1  #count = count + 1
		if count % 1000 ==0: #如果count除以1000的餘數是0
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

print(data[0])




sum_len=0
for d in data:
	sum_len = sum_len + len(d) # sum_len是指所有留言長度總和; len(d)是指每個留言長度
print('留言平均長度是', sum_len/len(data)) #len(data)是指data的個數


#------------------------------
# 找出留言字數小於100的留言有幾筆?
new=[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


#------------------------------
#找出留言內包含good的流言有幾筆?

good=[]
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言')
print(good[0])

#------------------------------
#快寫法
good= [d for d in data if 'good' in d]
print(good)

bad= ['bad' in d for d in data]
print(bad)




#文字計數

wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] +=1
	else:
		wc[word] = 1 #新增新的key進wc字典

# print(wc)

for word in wc:
	if wc[word] > 100000: #印出出現次數>100次的字字
		print(word, wc[word]) #印出字典的字字 與 字出現次數

print(len(wc)) # 印出字典長度
print(wc['Allen']) #查找字典中是否有包含allen的字

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print( word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒出現過歐~')
	
print('感謝使用本查詢功能')

