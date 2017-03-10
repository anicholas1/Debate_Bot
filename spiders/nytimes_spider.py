import random
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from super_web.items import SuperWebItem
from scrapy.selector import Selector



class NYSpider(CrawlSpider):
    name = "derp"
    allowed_domains = ["www.nytimes.com"]
    start_urls = ['https://www.nytimes.com/pages/politics/index.html']

    rules = [
        Rule(LinkExtractor(
            # allow has html patter \d for all digits and \w for alphanumeric
            # this follows reddit pattern for its pages as the
            allow=['/r/pics/\?count=\d*&after=\w*', '/\d/\d/\d/us/politics', '/pages/politics']),
            callback='parse_item',
            follow=True)
    ]


# //*[@id="main"]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/h2/a - heading
#


    # rules = [
    #     # Traverse the in the /r/pics subreddit. When you don't pass
    #     # callback then follow=True by default.
    #     # It's also important to NOT override the parse method
    #     # the parse method is used by the CrawlSpider continuously extract links
    #     Rule(LinkExtractor(
    #     	allow=['/r/pics/\?count=\d*&after=\w*']),
    #     	callback='parse_item',
    #     	follow=True),
    # ]


    # Goes through each callback which is an html page I believe, and searches for all


    def parse_item(self, response):

        headlines = Selector(response).xpath('//div[@class="storyHeader"]/h2')
        stories = Selector(response).xpath('//div[@class="story"]/h3')
        news_item = SuperWebItem()

        for story in stories:
            story_item = SuperWebItem()
            story_item['story_title'] = story.xpath('a/text()').extract()[0]
            story_item['story_url'] = story.xpath('a/@href').extract()[0]
            yield story_item

        '''for headline in headlines:
            news_item['headline_title'] = headline.xpath(
                'a/text()').extract()[0]
            news_item['headline_url'] = headline.xpath(
                'a/@href').extract()[0]
            yield news_item'''





        '''selector_list = response.css('div.thing')

        for selector in selector_list:
            item = SuperWebItem()
            item['images'] = selector.xpath('//div[@class="image"]/img').extract()
            item['title'] = selector.xpath('//div[@class="storyHeader"]/h2/a').extract()
            item['url'] = selector.xpath('//div[@class="storyHeader"]/a/@href').extract()
            item['summary'] = selector.xpath()
            yield item '''


