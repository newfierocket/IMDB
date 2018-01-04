from resources import movie, tv, gets

class XmlTemplate(object):
    
    @staticmethod
    def template(show, show_type):	

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
    def template_seasons(show, show_type, file_name):
        for i in range(len(show.episode_dict)):
            season = 'Season' + ' ' + str(i+1)
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
    <link></link>
    <animated_thumbnail></animated_thumbnail>
    <thumbnail>{Poster}</thumbnail>
    <animated_fanart></animated_fanart>
    <fanart>{Backdrop}</fanart>
</dir> \n\n\n'''.format(Title=show.original_title, Year=show.year, Backdrop=show.backdrop, Poster=show.episode_dict['season_' + str(i+1)]['poster_path'], Season=season)
            print 'Writing File....'
            gets.WriteFile.write(string_to_write, file_name)
            print 'Done writing.'

        return

    @staticmethod
    def template_episodes(show, show_type, file_name):
        for s in range(len(show.episode_dict)):
            season = 'Season ' + str(s+1)
            print season
            for i in range(len(show.episode_dict['season_' + str(s+1)])-1):
                episode_number = 'Episode ' + str(i+1)
                episode = show.episode_dict['season_' + str(s+1)]['episode_' + str(i+1)]
                
                string_to_write = '''
<item>
        <title>{Title}</title>
        <meta>
                <content>episode</content>
                <imdb></imdb>
                <tvdb></tvdb>
                <tvshowtitle>{Episode}</tvshowtitle>
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
        <thumbnail></thumbnail>
        <animated_fanart></animated_fanart>
        <fanart></fanart>
</item> \n\n\n'''.format(Title=show.original_title, Year=show.year,Episode_Number=episode_number, Backdrop=show.backdrop, Poster=show.episode_dict['season_' + str(s+1)]['poster_path'], Episode=episode, Season=season)
                print 'Writing File....'
                gets.WriteFile.write(string_to_write, file_name)
                print 'Done writing.'

        return





