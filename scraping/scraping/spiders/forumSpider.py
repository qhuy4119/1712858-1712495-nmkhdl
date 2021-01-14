import scrapy
from .. import forumsList

class forumSpider(scrapy.Spider):
    name = 'forum'
    start_urls = forumsList.forums_to_crawl 

    #Parse a forum page. Example of a forum: https://voz.vn/f/phan-cung-chung.9/
    def parse(self, response):
        postLinks = response.css("div.structItem-title").xpath(".//a[@class='']")
        yield from response.follow_all(postLinks, callback=self.parse_post)
        forumTitle = response.css("h1.p-title-value::text").get()
        next_forum_page = response.css("a.pageNav-jump.pageNav-jump--next::attr(href)").get()
        if next_forum_page is not None:
            print('Crawling next forum page. URL: ', response.urljoin(next_forum_page))
            yield response.follow(next_forum_page, callback=self.parse)
        else:
            print(f"There's no next page of {forumTitle} to crawl")

    #Parse a post page. Example of a post: https://voz.vn/t/xiaomi-mi-11-ve-viet-nam-gia-hon-15-trieu-dong.208165/
    def parse_post(self, response):
        postTitle = response.css("h1.p-title-value::text").get()
        postContent = response.xpath("(//div[@class='bbWrapper'])[1]/text()[normalize-space()]").getall()
        postContent = ''.join(postContent)
        forumName = response.css("ul.p-breadcrumbs li:last-child a span::text").get()
        postDateOfCreation = response.css("time.u-dt::attr(data-date-string)").get()
        yield {
            'postTitle': postTitle,
            'postCotent': postContent,
            'forumName': forumName,
            'postLink': response.url,
            'postDateOfCreation': postDateOfCreation,
        }

