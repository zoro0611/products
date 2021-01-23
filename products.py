products = []

while True:
	name = input("請輸入商品名稱: ")
	if name == "q":
		break
	price = input("請輸入商品價格: ")

	p = []
	p.append(name) # 9~11行這邊代表用p這個清單將商品名稱跟價格一起打包
	p.append(price) #或者一次寫完 p = [name, price]

	products.append(p) # 最後將p清單再放入products清單中
print(products)



