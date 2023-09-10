from core import *



class SearchThread(QThread):
    search_results = Signal(list)

    def __init__(self, search_query):
        super().__init__()
        self.search_query = search_query

    def run(self):
        videosSearch = VideosSearch(self.search_query + " vevo", limit=50)
        videosResult = videosSearch.result()
        
        search_results = []
        for video in videosResult['result']:
            # print all results
            print(video)
            # duration_cut = video['duration'].split(':')
            # if len(duration_cut) > 2:
            #     pass
            # else:
                
            result = {
                'link': video['link'],
                'title': video['title'],
                'thumbnail': video['thumbnails'][0]['url'],
                'duration': video['duration'],
                'view_count': video['viewCount']['short'],
                'published_time': video['publishedTime']
            }
            search_results.append(result)
        
        self.search_results.emit(search_results)


