from resources import setting, get


class TvInformation(object):
	def __init__ (self, show_name, show_year):
		self.show_name = show_name
		self.show_year = show_year


	def tv_search(self):
		search_url  =  setting.search_url.format(base_url=setting.base_url, api_key=setting.api, tv_title=self.show_name.replace(' ', '+'), tv_year=self.show_year)
		results = get.GetRequest.request(search_url)
		for i in range(len(results.get('results'))):
			if self.show_name.lower() in results['results'][i]['name'].lower() and str(self.show_year) in results['results'][i]['first_air_date']:
				self.search_dict = results['results'][i]

		tv_url = setting.season_query_url.format(base_url=setting.base_url, tv_id=self.search_dict['id'], api_key=setting.api)
		self.results = get.GetRequest.request(tv_url)
		





tv = TvInformation('The walking dead', 2010)
tv.tv_search()