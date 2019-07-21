from newspaper import Article

article = Article("https://www.myntra.com/casual-shoes/carlton-london/carlton-london-men-tan-brown-boat-shoes/1878181/buy")

# print(help(article))

# print(article.fetch_images())

download = article.download()
print(type(download))
