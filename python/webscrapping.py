from bs4 import BeautifulSoup
import requests
import csv
import shutil
import os

base_url_import = 'https://news.google.com/search?q=importation&hl=fr&gl=MA&ceid=MA%3Afr&start='
base_url_export = 'https://news.google.com/search?q=exportation&hl=fr&gl=MA&ceid=MA%3Afr'
news_data_import = []
news_data_export = []

#import
for page_number in range(0, 3):  # Increase by 10 for each page
    url = base_url_import + str(page_number)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Specify the appropriate class for the news articles
    review_elements_import = soup.find_all('a', class_='JtKRv')

    for review_element in review_elements_import:
        review_text = review_element.get_text(strip=True)
        link = 'https://news.google.com' + review_element.get('href', '')
        news_data_import.append({'Review': review_text, 'Link': link})

with open('import.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Review', 'Link']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerows(news_data_import)

# Determine the path to the public directory in the React app
react_public_path = os.path.join(os.path.dirname(__file__), '..', 'react', 'public')

# Move the CSV file to the public directory
shutil.move('import.csv', os.path.join(react_public_path, 'import.csv'))


#export
for page_number in range(0, 3):  # Increase by 10 for each page
    url = base_url_export + str(page_number)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Specify the appropriate class for the news articles
    review_elements_export = soup.find_all('a', class_='JtKRv')

    for review_element in review_elements_export:
        review_text = review_element.get_text(strip=True)
        link = 'https://news.google.com' + review_element.get('href', '')
        news_data_export.append({'Review': review_text, 'Link': link})

with open('export.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Review', 'Link']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerows(news_data_export)

# Move the CSV file to the public directory
shutil.move('export.csv', os.path.join(react_public_path, 'exports.csv'))



