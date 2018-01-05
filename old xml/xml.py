from resources import movie, tv, gets, template
import sys

def main(show_name, show_year):
	if show_type == 'movie':
		movie = movie.MovieInfo(show_name, show_year)
		string_to_write = template.XmlTemplate.template(movie, show_type)
		print 'Writing File....\n'
		gets.WriteFile.write(string_to_write, file_name)
		print 'Done writing\n'
		
		return raw_input('Please Enter another Show name: -->')
	elif show_type == 'tvshow':
		tvshow = tv.TvInfo(show_name, show_year)
		string_to_write = template.XmlTemplate.template(tvshow, show_type)
		print 'Writing File....\n'
		gets.WriteFile.write(string_to_write, file_name)
		print 'Done writing\n'
		return raw_input('Please Enter another Show name: -->')
	elif show_type == 'season':
		tvshow = tv.TvEpisodes(show_name, show_year)
		template.XmlTemplate.template_seasons(tvshow, show_type, file_name)
		# print 'Writing File....\n'
		# gets.WriteFile.write(string_to_write, file_name)
		# print 'Done writing\n'
		return raw_input('Please Enter another Show name: -->')
	elif show_type == 'episode':
		tvshow = tv.TvEpisodes(show_name, show_year)
		template.XmlTemplate.template_episodes(tvshow, show_type, file_name)
		# print 'Writing File....\n'
		# gets.WriteFile.write(string_to_write, file_name)
		# print 'Done writing\n'
		return raw_input('Please Enter another Show name: -->')


if __name__ == '__main__':
	
	
	print '''
##########################################NOTICE###########################################################
##       This script is used to download Meta Data and create an XML for JEN addon.                      ##
##       Please ensure you have a TMDB API set in the resource folder. You can change the file to write  ##
##       by typing in "--set file" instead of a movie name. Typing exit will also exit script.           ##
###########################################################################################################
			'''



	args = sys.argv[1:]
	

	if not args:
		args = []
		global show_type
		show_type = raw_input('Please Enter tvshow, movie, season, episode, for XML type')
		get_info = raw_input('Please Enter Search Params: Movie Title\Tv Show + Year:-->')
		for item in get_info.split(' '):
			args.append(item)

	global file_name
	file_name = raw_input('Please Enter the file name to write to:-->')

	while args[-1] != 'exit':
		
		if ' '.join(args[:]).lower() == '--set file'.lower():
			# global file_name
			file_name = raw_input('Please Enter the file name to write to:-->') 
			re_use = raw_input('Please Enter Search Params: Movie Title\Tv Show + Year-->')
			args = []
			for item in re_use.split(' '):
				args.append(item)

		else:
			show_name = ' '.join(args[:-1])
			show_year  = ''.join(args[-1])
			print show_name + ' ' + show_year
			re_use = main(show_name, show_year)
			args = []
			for item in re_use.split(' '):
				args.append(item)
			
	else:
		sys.exit(1)