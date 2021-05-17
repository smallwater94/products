import os #operating system

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue    #strip() : 將\n去掉
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('清輸入商品價格: ')
		products.append([name, price])
	print(products)#products[0][0] #二維清單
	return products

#列印出購買紀錄
def print_products(products):
	for p in products:
		print(p[0],'的價格是',p[1])

#寫入檔案
def write_file(filename, products):
	with open (filename,'w') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

#程式進入點 主函式
def main(filename):
	if os.path.isfile(filename): #檢查檔案在不在
		print('yeah! 找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案.....')
	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main('products.csv')