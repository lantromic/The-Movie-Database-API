import argparse
import requests

def get_type_movie(type):
    if type == 'playing':
        params = {"api_key": 'deff05d88acd7c8151dbfd030da087f6', "language": "en-US", "page": 1}
        response = requests.get('https://api.themoviedb.org/3/movie/now_playing',params=params)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results'][:5]:
                print(movie['title'])
        else:
            print("error") 
    
    if type == 'popular':
        params = {"api_key": 'deff05d88acd7c8151dbfd030da087f6', "language": "en-US", "page": 1}
        response = requests.get('https://api.themoviedb.org/3/movie/popular',params=params)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results'][:5]:
                print(movie['title'])
        else:
            print("error") 

    if type == 'top':
        params = {"api_key": 'deff05d88acd7c8151dbfd030da087f6', "language": "en-US", "page": 1}
        response = requests.get('https://api.themoviedb.org/3/movie/top_rated',params=params)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results'][:5]:
                print(movie['title'])
        else:
            print("error") 
        
    if type == 'upcoming':
        params = {"api_key": 'deff05d88acd7c8151dbfd030da087f6', "language": "en-US", "page": 1}
        response = requests.get('https://api.themoviedb.org/3/movie/upcoming',params=params)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results'][:5]:
                print(movie['title'])
        else:
            print("error")

parser = argparse.ArgumentParser(description="TMDB API Interaction Script")

parser.add_argument('--type',help='enter category of movie to filter after --type(popular,top,upcoming,playing)')

args = parser.parse_args()

print(args.type,'\n')

if args.type == 'playing':
    get_type_movie('playing')
elif args.type == 'popular':
    get_type_movie('popular')
elif args.type == 'top':
    get_type_movie('top')
elif args.type == 'upcoming':
    get_type_movie('upcoming')
else:
    print("input correct type of movie")