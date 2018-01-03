

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
