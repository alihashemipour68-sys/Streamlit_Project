import requests
from deep_translator import GoogleTranslator

PROXIES = {
    'http': '//10.232.225.170:8080',
    'https': '//10.232.225.170:8080'
}


def get_movei_info(movie_id):
    url=f"http://moviesapi.ir/api/v1/movies/{movie_id}"
    response=requests.get(url,proxies=PROXIES,verify=False)
    if response.status_code !=200:
        return "Eroor"
    else:

        response = response.json()
        imdb_rate=response['imdb_rating']
        title=response['title']
        year=response['year']
        country=response['country']
        awards=response['awards']
        genres=response['genres']
        plot=response['plot']
        plot=translator(plot)
        poster=response['poster']
        return title,imdb_rate,year,country,awards,genres[0],plot,poster

def translator(user_input):
     try:
          translated_text = GoogleTranslator(source='en', target='fa').translate(user_input)
          return translated_text
     except:
          return None
     
if __name__=='__main__':
        movie_id=input('Enter movei id: ')
        result=get_movei_info(movie_id)
        print(result)
        print("#------------------------------------------------#")

