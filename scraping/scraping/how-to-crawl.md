# Keywords and their examples:
- site: the whole voz.vn website. It is what you see when accessing [https://voz.vn/](voz.vn) on a browser. The site contains many forums
- forum: a forum consists of posts about a topic. Example: https://voz.vn/f/phan-cung-chung.9/
- post: a post in a forum, consisting of multiple user comments. Example: https://voz.vn/t/xe-dien-ha-noi-chuyen-cac-sp-xe-dien-xe-may-dien-new-cap-nhat-lien-tuc.2348/
- postTitle: title of a post
- postContent: the first comment of a post
- forumName: the name of the forum to which the post belongs
- postLink: the url of the post

# How to crawl:
- Install `scrapy`: pip install scrapy
- Change directory into the `scraping` directory
- Specify the urls of forums you want to crawl in the python list `forums_to_crawl` inside `forumsList.py`
- Run command: `scrapy crawl forum -O <outputFileName> --nolog`.
	- Scrapy will infer file type from the extension in `outputFileName`. For example: out.csv will generate a csv file, out.jl will generate a json lines file
	- Run `scrapy crawl -h` for information about -O and --nolog arguments, as well as other possible arguments of `scrapy crawl`
