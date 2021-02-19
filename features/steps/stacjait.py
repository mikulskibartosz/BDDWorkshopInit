from behave import *
import re
import requests as r


@when(u'workshop website is retrieved')
def request_the_website(context):
    response = r.get('https://stacja.it/produkt/behavior-driven-development-w-pythonie-z-uzyciem-biblioteki-behave/')
    context.website_html = response.content


@then(u'the title contains "{text}"')
def match_title_element(context, text):
    website_title = re.search(r'<title>(.*?)</title>', str(context.website_html))
    print(website_title)
    assert text in website_title.group(1)
