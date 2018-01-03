import gets
import api

class TvInfo(object):   ####Get Meta Data info by search
    def __init__(self, tv_title, tv_year):
        self.name = tv_title   ###Sets Tv name name as string
        self.year = tv_year   ###Sets Year as String
        self.base_url = 'https://api.themoviedb.org/3/'   ###TMDB API base URL
        self.api_key = api.api   ####Set Custom Api Here######
        self.search_url = '{base_url}search/tv?api_key={api_key}&query={tv_title}&year{tv_year}'.format(base_url=self.base_url, 
                            api_key=self.api_key, tv_title=self.name.replace(' ', '+'), tv_year=self.year)
        self.image_base_url = 'https://image.tmdb.org/t/p/original'   ###Base URL from TMDB for images
        self.meta = gets.GetMeta.meta(self.search_url, self.name, self.year)  ###Stores Meta relevant for Movie in Dict form
        self.poster = self.image_base_url + gets.GetPoster.poster(self.meta)   ###Gets Poster image path
        self.backdrop = self.image_base_url + gets.GetBackdrop.backdrop(self.meta)   ###Gets Backdrop image path
        self.original_title = gets.GetTitle.actual_name(self.meta)
        self.imdb = gets.GetImdb.imdb(self.original_title, self.year) 
        self.id = gets.GetId.id(self.meta)


class TvSeasons(TvInfo):   ####Gets number of season for parsing episodes
    def __init__(self, tv_title, tv_year):
        super(TvSeasons, self).__init__(tv_title, tv_year)
        self.season_query_string = '{base_url}tv/{tv_id}?api_key={api_key}'.format(base_url=self.base_url, 
                                    tv_id=self.id, api_key=self.api_key)
        self.season_meta_raw = gets.GetRequest.request(self.season_query_string)
        self.num_of_seasons = self.season_meta_raw.get('number_of_seasons')


class TvEpisodes(TvSeasons):   ####Will return a dict of all data for all seasons and episodes
    def __init__(self, tv_title, tv_year):
        super(TvEpisodes, self).__init__(tv_title, tv_year)
        self.full_tv_dict = {}
        for i in range(self.num_of_seasons):
            self.episode_query_string = '{base_url}tv/{tv_id}/season/{season_number}?api_key={api_key}'.format(base_url=self.base_url,
                                         tv_id=self.id, season_number=(i+1), api_key=self.api_key)
            # self.season_info = TvSeasons.metas(self.season_query_string)
            self.episode_meta_raw = gets.GetRequest.request(self.episode_query_string)
            self.full_tv_dict['season_' + str(i + 1)] = self.episode_meta_raw
        
    def episode_info_list(self): ####Returns a dict of all seasons with all episode names and poster art.
        self.episode_dict = {}
        # self.episode_dict['poster_path'] = (self.season_meta_raw.get('poster_path'))
        for s in range(len(self.full_tv_dict)):
            self.episode_dict['season_' + str(s+1)] = {}
            self.episode_dict['season_' + str(s+1)]['poster_path'] = self.image_base_url + self.full_tv_dict.get('season_' + str(s+1)).get('poster_path')
            for i in range(len(self.full_tv_dict.get('season_' + str(s+1)).get('episodes'))):
                self.episode_dict['season_' + str(s + 1)]['episode_' + str(i+1)] = self.full_tv_dict.get('season_'+ str(s+1)).get('episodes')[i].get('name')


