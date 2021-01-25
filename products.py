# 讀取檔案
products = []
with open("products.csv", 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',') #每一行 只要遇到"," 就切割
		products.append([name, price])

print(products)

while True:
	name = input("請輸入商品名稱: ")
	if name == "q":
		break
	price = input("請輸入商品價格: ")
	price = int(price)
	products.append([name, price]) # 一次寫完省略之前三行寫法
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], "的價格是", p[1])
	
#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

