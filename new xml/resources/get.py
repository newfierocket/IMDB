import re, requests, sys, urllib2


class GetRequest(object):  ###pulls data from TMDB api
    @staticmethod
    def request(search_url):
        payload = {}
        response = requests.request("GET", search_url, data=payload)
        print 'Getting MetaData...'
        return response.json()
               
class GetMeta(object):  ####gets meta data relevent to movie
    @staticmethod
    def meta(search_url, show_name, show_year):
        meta_dict = GetRequest.request(search_url)
        if 'title' in meta_dict.get('results')[0].keys():
            title = 'title'
            year = 'release_date'
        elif 'name' in meta_dict.get('results')[0].keys():
            title = 'name'
            year = 'first_air_date'
        else:
            print '####ERROR ->> Unable to Fetch Meta Data....PLease ensure Title and Year is correct!!!'
            sys.exit(1)   

        for i in range(len(meta_dict.get('results'))):
            # print meta_dict.get('results')[i]
            # raw_input('Enter to continue')
            if show_name.lower() == meta_dict.get('results')[i].get(title).lower() and str(show_year) in meta_dict.get('results')[i].get(year):
                return meta_dict.get('results')[i]
            # else:
            #     print '####ERROR ->> Unable to Fetch Meta Data....PLease ensure Title and Year is correct!!!'
            #     sys.exit(1)
        
class GetPoster(object):  ###Get Poster art URL
    @staticmethod
    def poster(meta):
        try:
            if not meta:
                return ''
            else:
                print 'Retrieving Poster Art URL...'
                return meta.get('poster_path')
        except AttributeError:
            print "###ERROR Please ensure data is correct###"

class GetBackdrop(object):  ####Gets Background art URL
    @staticmethod
    def backdrop(meta):
        try:
            if not meta:
                return ''
            else:
                print 'Retrieving Background Art URL...'
                return meta.get('backdrop_path')
        except:
            return ''

class GetId(object):
    @staticmethod
    def id(meta):
        print 'Getting show ID...'
        return meta.get('id')

class GetTitle(object):  ####Gets the original title for the movie
    @staticmethod
    def actual_name(meta):
        try:
            if 'original_title' in meta.keys():
                print 'Getting Original Title info...'
                return meta.get('original_title')
            elif 'original_name' in meta.keys():
                print 'getting Original Title info...'
                return meta.get('original_name')
            else:
                return ''
        except:
            print '######Meta Data Error ensure name is correct...#####'
            return ''

class WriteFile(object):  ###Takes a filename and string to write
    @staticmethod
    def write(string, filename):
        with open(filename + '.xml', 'a') as f:
            f.write(string)

class GetImdb(object):   ####gets imdb number....movie name needs to be close to exact to get correct results. Will
    @staticmethod        ####return None value if not found.
    def imdb(movie_name, movie_year):
        try:
            movie_name_clean = movie_name.replace('&', '%26')
            search_term = movie_name_clean.replace(' ', '+') + '+' + str(movie_year)
            search_url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q=%s&s=all' % search_term
            html = urllib2.urlopen(search_url)
            html = html.read()
            regex_string = "\/title\/(\w+)\/.\w+.\w+.\s>{movie_name}.+?<\/a>\W\({movie_year}\)".format(movie_name=movie_name, movie_year=movie_year)
            imdb = re.search(regex_string, html, re.IGNORECASE)
            print 'Getting IMDB number...'
            return imdb.group(1)

        except:
            print "\n\n\n#######Please ensure you have typed the movie name correctly.###############"
            print       "#######If results are incomplete a manual update might be nescessary.#######"
            print       "#######Imdb number could not be found, please update manually.##############\n\n"
            return ''
