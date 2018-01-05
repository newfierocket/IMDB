from resources import get
import setting

class MovieInfo(object):
    def __init__(self, movie_name, movie_year):
        self.name = movie_name   ###Sets Movie name as string
        self.year = movie_year   ###Sets Year as String
        self.base_url = 'https://api.themoviedb.org/3/'   ###TMDB API base URL
        self.api_key = setting.api   ####Set Custom Api Here######
        self.search_url = '{base_url}search/movie?api_key={api_key}&query={movie_title}&year{movie_year}'.format(base_url=self.base_url, api_key=self.api_key, movie_title=self.name.replace(' ', '+'), movie_year=self.year)
        self.image_base_url = 'https://image.tmdb.org/t/p/original'   ###Base URL from TMDB for images
        self.meta = get.GetMeta.meta(self.search_url, self.name, self.year)  ###Stores Meta relevant for Movie in Dict form
        self.poster = self.image_base_url + get.GetPoster.poster(self.meta)   ###Gets Poster image path
        self.backdrop = self.image_base_url + get.GetBackdrop.backdrop(self.meta)   ###Gets Backdrop image path
        self.original_title = get.GetTitle.actual_name(self.meta)
        self.imdb = get.GetImdb.imdb(self.original_title, self.year)   ####Gets IMDB number using regex, can produce incorrect data

