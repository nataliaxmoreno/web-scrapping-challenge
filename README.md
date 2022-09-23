# web-scrapping-challenge
In this assignment, the task was to build a web application that scrapes various websites for data related to the Mission to Mars and display the information in a HTML page, the challenge had two parts:

Step 1: Scraping
Step 2: MongoDB and Flask Application

# Step 1: Scraping
scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter:

NASA Mars News Site:

The latest news title
The latest news paragraph text
Featured Space Image: The image url for the current Featured Space image

Mars tables:

the Mars facts table: Pandas was used to convert the data to a HTML table string

USGS Astrogeology:
The full-resolution image url of each hemisphere
The title of the hemisphere name

# Step 2: MongoDB and Flask Application
MongoDB with Flask templating was used to create a new HTML page that displays all of the information that was scraped from the URLs above. 

