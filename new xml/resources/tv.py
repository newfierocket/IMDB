from resources import setting, get


class TvInformation(object):
    def __init__ (self, show_name, show_year):
        self.episodes = {}
        self.show_name = show_name
        self.show_year = show_year
# def tv_search(self):
        search_url  =  setting.search_url.format(base_url=setting.base_url, api_key=setting.api, tv_title=self.show_name.replace(' ', '+'), tv_year=self.show_year)
        results = get.GetRequest.request(search_url)
        
        for i in range(len(results.get('results'))):
            if self.show_name.lower() in results['results'][i]['name'].lower() and str(self.show_year) in results['results'][i]['first_air_date']:
                self.search_dict = results['results'][i]
        season_url = setting.season_query_url.format(base_url=setting.base_url, tv_id=self.search_dict['id'], api_key=setting.api)
        self.season = get.GetRequest.request(season_url)
        num_of_seasons = self.season['number_of_seasons']
    
        for i in range(num_of_seasons):
            episode_query_string = setting.episode_query_string.format(base_url=setting.base_url, tv_id=self.search_dict['id'], season_number=(i+1), api_key=setting.api)
            # self.season_info = TvSeasons.metas(self.season_query_string)
            episode_meta_raw = get.GetRequest.request(episode_query_string)
            self.episodes['season_' + str(i + 1)] = episode_meta_raw





        # episode_url = setting.episode_query_string = '{base_url}tv/{tv_id}/season/{season_number}?api_key={api_key}'.format(base_url=setting.base_url,tv_id=self.search_dict['id'], api_key=setting.api)
        # self.episode = get.GetRequest.request(episode_url)

