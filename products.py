products = []

while True:
	name = input("請輸入商品名稱: ")
	if name == "q":
		break
	price = input("請輸入商品價格: ")
	products.append([name, price]) # 一次寫完省略之前三行寫法
print(products)

for p in products:
	print(p[0], "的價格是", p[1])
	




