products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('清輸入商品價格: ')
	products.append([name, price])
print(products)

#products[0][0] #二維清單

for p in products:
	print(p[0],'的價格是',p[1])

with open ('products.csv','w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') 