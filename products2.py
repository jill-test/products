#讀取檔案，strip 去空格、換行，split 切割
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        name, price = line.strip().split(',')
        #name = s[0]
        #price = s[1]
        products.append([name, price])
print(products)