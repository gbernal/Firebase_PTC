import scrapy
from ..items import ImagegetterItem

class ImgSpider(scrapy.spiders.Spider):
    name = "img_spider"
    start_urls = ["https://rubikscode.net/"]

    def parse(self, response):
        image = ImagegetterItem()
        img_urls = []

        for img in response.css(".entry-featured-image-url img::attr(src)").extract():
            img_urls.append(img)

        image["image_urls"] = img_urls

        return image
