products = []
while True :
	name = input('請輸入商品名稱: ')
	if name =='q': # q = quit
		break
	price = input('請輸入價格: ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])


with open('products.csv', 'w' , encoding = 'utf-8') as f: 
# with (離開 with 自動close 這個程式碼)
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')