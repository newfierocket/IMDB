from resources import tv, movie, get, template
import sys

def main(show_name, show_year):
	if 'movie' in show_type:
		show = movie.MovieInfo(show_name, show_year)
		string_to_write = template.XmlTemplate.movie(show, show_type)
		print 'Writing File....\n'
		get.WriteFile.write(string_to_write, file_name)
		print 'Done writing\n'
	elif 'season' in show_type:
		show = tv.TvInformation(show_name, show_year)
		string_to_write = template.XmlTemplate.seasons(show, show_type, file_name)
	elif 'episode' in show_type:
		show = tv.TvInformation(show_name, show_year)
		string_to_write = template.XmlTemplate.episodes(show, show_type, file_name)
	else:
		print 'Incorrect show type selected...Retry Please..'
		sys.exit(1)
		
	return raw_input('Please enter a new show-->')


if __name__ == '__main__':

	args = sys.argv[1:]
	

	if not args:
		args = []
		global show_type
		show_type = raw_input('Please Enter tvshow, movie, season, episode, for XML type-->')
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
