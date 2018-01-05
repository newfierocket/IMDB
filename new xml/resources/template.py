from resources import movie, tv, get, setting

class XmlTemplate(object):
    
    @staticmethod
    def movie(show, show_type):	

	   string_to_write = '''	
<item>
	<title>{Title} ({Year})</title>
    <meta>
    	<content>{Type}</content>
    	<imdb>{IMDB}</imdb>
    	<title>{Title} ({Year})</title>
    	<year>{Year}</year>
    </meta>
    <link>
    	<sublink>search</sublink>
    	<sublink>searchsd</sublink>
    </link>
    <animated_thumbnail></animated_thumbnail>
    <thumbnail>{Poster}</thumbnail>
    <animated_fanart></animated_fanart>
    <fanart>{Backdrop}</fanart>
</item>\n\n\n'''.format(Title=show.original_title, Year=show.year, Backdrop=show.backdrop, Type=show_type, Poster=show.poster, IMDB=show.imdb)
	
	   return string_to_write

    

    @staticmethod
    def seasons(show, show_type, file_name):
        title = show.search_dict['name']
        backdrop = setting.image_base_url + show.search_dict['backdrop_path']
        for i in range(len(show.season['seasons']) - 1):
            poster = setting.image_base_url + show.season['seasons'][i+1]['poster_path']
            season = 'Season ' + str(i+1)
            year = show.season['seasons'][i+1]['air_date'][:4]
            link = setting.base_host_url + file_name + '/seasons/season' + str(i+1) + '.xml'
            string_to_write = '''
<dir>
    <name>{Title}-{Season}</name>
    <meta>
        <content>season</content>
        <imdb></imdb>
        <tvdb></tvdb>
        <tvshowtitle>{Season}</tvshowtitle>
        <year>{Year}</year>
        <season>{Season}</season>
    </meta>
    <link>{Link}</link>
    <animated_thumbnail></animated_thumbnail>
    <thumbnail>{Poster}</thumbnail>
    <animated_fanart></animated_fanart>
    <fanart>{Backdrop}</fanart>
</dir> \n\n\n'''.format(Title=title, Year=year, Link=link, Backdrop=backdrop, Poster=poster, Season=season)
            print 'Writing File....'
            get.WriteFile.write(string_to_write, file_name)
            print 'Done writing.'

        return

    

    @staticmethod
    def episodes(show, show_type, file_name):
        for s in range(len(show.episodes)):
            season = 'Season ' + str(s+1)
            for e in range(len(show.episodes['season_' + str(s+1)]['episodes'])):
                season_dict = show.episodes['season_' + str(s+1)]['episodes'][e]
                if season_dict:
                    episode = 'Episode ' + str(e+1).encode('utf-8')
                    name = season_dict['name']
                    backdrop = setting.image_base_url + season_dict['still_path']
                    air_date = season_dict['air_date']
                    episode_number = 'Episode ' + str(e+1).encode('utf-8')
                    season_number = 'Season ' + str(season_dict['season_number']).encode('utf-8')
            

                    string_to_write = '''
<item>
        <title>{Title}</title>
        <meta>
                <content>episode</content>
                <imdb></imdb>
                <tvdb></tvdb>
                <tvshowtitle>{Title}</tvshowtitle>
                <year>{Year}</year>
                <title>{Title}</title>
                <premiered>{Year}</premiered>
                <season>{Season}</season>
                <episode>{Episode_Number}</episode>
        </meta>
        <link>
                <sublink>search</sublink>
                <sublink>searchsd</sublink>
        </link>
        <animated_thumbnail></animated_thumbnail>
        <thumbnail>{Backdrop}</thumbnail>
        <animated_fanart></animated_fanart>
        <fanart>{Backdrop}</fanart>
</item> \n\n\n'''.format(Title=name, Year=air_date, Episode_Number=episode_number, Backdrop=backdrop, Episode=episode, Season=season)
                    print 'Writing File....'
                    get.WriteFile.write(string_to_write, file_name + 'season'+ str(s+1) + '.xml')
                    print 'Done writing.'
                else:
                    print 'No Data in season'
        return





