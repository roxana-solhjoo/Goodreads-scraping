import scrapy



class GoodreadsBookSpider(scrapy.Spider):
    name = 'goodreads-book'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/list/show/273.Self_development']

    def parse(self, response):
        books = response.css('table tr')
        for book in books:
            author = book.css('a.authorName ::text').get()
            rate = book.css('span.minirating ::text').get()

            yield {
                "Author": author,
                "Rate": rate

            }

            links = response.css('table td a.bookTitle a::attr(href)').getall()
            for link in links:
                yield scrapy.Request(link, callable=self.parse)











