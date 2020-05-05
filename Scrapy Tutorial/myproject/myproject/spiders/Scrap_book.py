import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bookss"
    
    def start_requests(self):
        
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
        ]
        
        #Generator Function
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        #with open("book.csv", "w") as file:
            #header = ",".join(["image_url","book_title","product_price"]) + "\n"
            #file.write(header)
            
        for q in response.css('article.product_pod'):
            img = q.css('div.image_container img ::attr(src)').get()
            book_title = q.css('div.image_container img ::attr(alt)').get()
            product_price = q.css('div.product_price p ::text').get()
            #books = ",".join([str(image_url),str(book_title),str(product_price)]) + "\n"
            #file.write(books)
            
            
            yield {
                'image_url':img,
                'book_title':book_title,
                'product_price':product_price,
            
            
            
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
        