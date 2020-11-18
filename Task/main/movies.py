import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
import django
django.setup()
from django.core.management import call_command

import requests
import bs4
from movie.models import TopMovie
base_url = 'https://www.imdb.com'
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')

repo = soup.find(class_='lister-list')
repo_list = repo.find_all(class_='titleColumn')

def movies_detail():
    for movie in repo_list[:50]:
        movie_name = movie.find('a').text
        year = movie.find(class_='secondaryInfo').text[1:5]
        link = movie.find('a')['href']
        next_page = requests.get(base_url+link)
        page_info = bs4.BeautifulSoup(next_page.text, 'lxml')
        rating = page_info.find(class_='ratingValue').text
        director = page_info.find(class_='credit_summary_item')
        director_name = director.find('a').text
        cast_detail = page_info.find(class_='cast_list')
        
        cast_name = []
        cast_odd = cast_detail.find_all(class_='odd')
        for name in cast_odd:
            cast_odd_name = name.find('a')
            odd_name = cast_odd_name.select('img')[0]['alt']
            cast_name.append(odd_name)

        cast_even = cast_detail.find_all(class_='even')
        for name in cast_even:
            cast_even_name = name.find('a')
            even_name = cast_even_name.select('img')[0]['alt']
            cast_name.append(even_name)
   
        TopMovie.objects.get_or_create(title=movie_name, year=int(year), 
                         rating=rating, director=director_name, cast=cast_name)


if __name__ == '__main__':
    print("Start...")
    movies_detail()
    print("End...")


