import scrapy

class forumSpider(scrapy.Spider):
    name = 'forum'

    start_urls = ["https://voz.vn/f/xe-cac-loai.77/"]

    def parse(self, response):
        postLinks = response.css("div.structItem-title").xpath(".//a[@class='']")
        yield from response.follow_all(postLinks, callback=self.parse_post)
        next_forum_page = response.css("a.pageNav-jump.pageNav-jump--next::attr(href)").get()
        if next_forum_page is not None:
            print('we have next page')
            yield response.follow(next_forum_page, callback=self.parse)

    def parse_post(self, response):
        postContent = response.css("div.bbWrapper:first-child::text").get()
        forumName = response.css("ul.p-breadcrumbs li:last-child a span::text").get()
        yield {
            'postCotent': postContent,
            'forumName': forumName,
            'postLink': response.url,

        }

