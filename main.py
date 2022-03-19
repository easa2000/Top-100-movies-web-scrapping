import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com" \
      "/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
webpage = response.text

movie_list = []
soup = BeautifulSoup(webpage, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
for movie in movie_titles:
    movie_list.append(movie.getText())
movie_list = movie_list[::-1]

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(movie + "\n")
    print("movie.text file created go and check have fun 🤩🤩🥳👍")
