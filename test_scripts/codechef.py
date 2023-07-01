import requests
import bs4
import regex as re

id="abhishek_2509"
response= requests.get(f"https://www.codechef.com/users/{id}")
soup=bs4.BeautifulSoup(response.text,'html.parser')
soup=soup.find_all('section',class_='rating-data-section problems-solved')
h5= soup[0].find_all('h5')[0].getText()
questionVal= int(re.search(r"\d+", h5).group())

