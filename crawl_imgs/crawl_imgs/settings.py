# Scrapy settings for crawl_imgs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawl_imgs'

SPIDER_MODULES = ['crawl_imgs.spiders']
NEWSPIDER_MODULE = 'crawl_imgs.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawl_imgs (+http://www.yourdomain.com)'
