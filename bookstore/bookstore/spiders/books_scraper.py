import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('li.col-xs-6'):
            item = {
                'name': book.css('h3 a::text').get(),
                'price': book.css('p.price_color::text').get(),
                'url': response.urljoin(book.css('h3 a::attr(href)').get())
            }
            yield item
        
        next_page = response.css('ul.pager li.next a::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
        
def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(BooksSpider)
    process.start()

if __name__ == '__main__':
    main()