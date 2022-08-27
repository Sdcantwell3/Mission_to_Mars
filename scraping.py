#!/usr/bin/env python
# coding: utf-8



# Import Splinter and BeautifulSoup

from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd 
from webdriver_manager.chrome import ChromeDriverManager




#this activates the splinter instance allowing me to watch the script work through a given website(s).

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)




# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)




# Now to set up HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')





# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title





# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)





# Find and click the full image button - to varify it was valid to use the 'button' tag we searched it and found that 
#there were only 3 instances of this tag and felt safe to procede.The index number tellt he code to hit the second button

full_image_elem = browser.find_by_tag('button')[1]

full_image_elem.click()





# Parse the resulting html with soup (each time we change pages we need to re-parse)
html = browser.html
img_soup = soup(html, 'html.parser')





# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel





# Use the base URL to create an absolute URL 
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


### Mars Facts

#Importing a data table from an html website as a pandas DataFrame.

#Creating a new DataFrame from the HTML table.  "0" tells the script to pull the first table it encounters.
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

#This line assigns column to data in the DataFrame
df.columns=['Description', 'Mars', 'Earth']

#this turns the 'Description' column into the df index
df.set_index('Description', inplace=True)

df





#Pandas has a way to easily convert our DataFrame back into HTML-ready 
#code using the 'to_html() function.' Add this line to the next cell in your 
#notebook and then run the code.

df.to_html()


browser.quit()






