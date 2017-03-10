# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SuperWebItem(Item):
    images = Field()
    story_title = Field()
    story_url = Field()
    summary = Field()
    headline_title = Field()
    headline_url = Field()

# class ShowerThoughtItem(Item):
#     image_urls = Field()
#     images = Field()
#     title = Field()
#     url = Field()