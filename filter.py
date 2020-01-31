
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



