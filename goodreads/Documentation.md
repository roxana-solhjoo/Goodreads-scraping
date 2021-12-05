#Goodreads.com web scraping 

##Task:
Developing an Automated application that:
- Scraps goodreads.com, selfdevelopment books and getting a list of atleast 100 authors with their rats.
- Save the data in csv file 
- Save the top five rated authors data in csv file and upload it on google drive. 
- Create a google form with five authors as multi choices question.
- Send the form to the list of email (defined in csv file) weekly.


Here we are using Python 3.7 and Scrapy farmework.
##Dependencies Installation
###Python Installation on Mac 

####Install Brew
1.Open the terminal
2.Run the command below 
<pre><code>curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
</code></pre>

####Install Python3 with Brew
1.Enter brew command into terminal
<pre><code>brew install python3</code></pre>

####Installing Scrapy
Most of the dependencies will automatically get installed. They're available for Python 2.7+.
<pre><code>pip install Scrapy</code></pre>
####Or
<pre><code>pip install Scrapy</code></pre>
##Creating a new Scrapy project
Before you start scraping, you will have to set up a new Scrapy project. Enter a directory where you’d like to store your code and run:</br>
<pre><code>scrapy startproject goodreads </code></pre>
This will create a "goodreads" folder. </br>
And then we need to genrate spider in our project, so in goodreas dirctory run
<pre><code>scrapy genspider goodreads-book goodreads.com</code></pre>
Which `goodreads-book` is simply creates `goodreads-book.py` file and `goodread.com` is the website we would like to scrape.

- Open the goodreads-book.py, here is the code included in file:
<pre><code>import scrapy

class GoodreadsBookSpider(scrapy.Spider):
    name = 'goodreads-book'
    allowed_domains = ['goodreads.com']
    start_urls = ['goodreads.com']

    def parse(self, response):
      pass
</code></pre>
In oredr to run this file use:
<pre><code>scrapy crawl goodreads-book</code></pre>
 First we need to change start_urls to url of the page we would like to scrape which is:
<pre><code>start_urls = ['https://www.goodreads.com/list/show/273.Self_development']</code></pre>
And then we need to open the Url on our brownser, inspect the page and find corresponding css tag to the list of book that we would like to scrape, we are basically looking for the containers which include Author's name and Rates of each book. 
And then by using responce object we would be able to crawl the webpage:
<pre><code>  
   def parse(self, response):
        books = response.css('table tr')
        for book in books:
            author = book.css('a.authorName ::text').get()
            rate = book.css('span.minirating ::text').get()

            yield {
                "Author": author,
                "Rate": rate}
</code></pre>
 It mentioned in requirments that the application need to crawl atleast 100 pages, adding the codes below to the end of  `def parse()`would take take care of that:
<pre><code>            links = response.css('table td a.bookTitle a::attr(href)').getall()
            for link in links:
                yield scrapy.Request(link, callable=self.parse)
</code></pre>

#How to set up and run the project on new environment:
####Download the project file 
Go to project directory 
<pre><code> cd goodreads </code></pre> <br>
<pre><code>scrapy crawl goodreads-book</code></pre>
And you must be able to crawl the webpage by here.<br>
####Create .csv file (of gathered data)
<pre><code>scrapy crawl goodreads-book -t csv -o goodreads-book.csv </code></pre>
Open file `topFiveRated.py` and run it. (This file will generate the top five rated Athors and write them to the new .csv file)<br>
Code in topFiveRated.py is as below :
<pre><code>import csv


with open ('goodreads-book.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    with open("/Users/roxana/Desktop/Automation/Drive/topFiveRatedAuthors.csv", 'w') as new_file:
        for line in csv_reader:
            rate = line[1]
            rate = rate[19:-8]
            if str(rate) == '':
                pass
            else:
                rate = int(rate.replace(',', ''))

            if int(rate) > 178875:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(line)</code></pre>
##Drive folder 
This folder includes the Google drive API set up, you may get more information regarding this here:<br>
(https://developers.google.com/drive/api/v3/quickstart/python), <br>
**drive.py** is included all the configuration codes. <br>
**credential.json** includes credentials which was created on (https://console.cloud.google.com/).
Drive folder basically handeling  the upload of csv file(generated in topFiveRated.py) to google drive.<br>
**Note**: Remove the token.json before running this file.<br>
And in order to run, go to Drive directory and:
<pre><code> python drive.py</code></pre><br>
this must upload a csv file of topFiveAothors.csv on your google drive.

##goodreads.json
Includes the json file from Google Apps script. you may set up your own project from here(https://script.google.com).<br>
This file is basically creates a Google form and add those five top authors as multiple choices and send email
to the list of emails defined in email.csv.<br>
This application scheduled to repeat the same process weekly on monday between 9 to 10 am. (You may change thins setting on trigger window).











