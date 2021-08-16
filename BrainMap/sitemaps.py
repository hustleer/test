

from django.contrib.sitemaps import Sitemap
from person.models import Person
from django.shortcuts import reverse
 
 
class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = 'https'
    
    def items(self):
        return ['index', ]
    
    def location(self, item):
        return reverse(item)
    
    '''def lastmod(self, obj):
        return obj.pub_date
    
    ''def items(self):
        return Person.objects.all()

    def lastmod(self, obj):
        return obj.article_published
        
    def location(self,obj):
        return '/blog/%s' % (obj.article_slug)'''

'''changefreq=
    'always'
    'hourly'
    'daily'
    'weekly'
    'monthly'
    'yearly'
    'never'
'''

##For static sitemaps
from django.contrib.sitemaps import Sitemap
from person.models import Person
from django.urls import reverse

...


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = 'https'

    def items(self):
        return ['index', ]
    
    def location(self, item):
        return reverse(item)
