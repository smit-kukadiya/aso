from typing import Dict, Any

from aso.main import ASO

class TrendKeywords:

    def __init__(self, store: str) -> None:
        self.aso_instance = ASO(store)

    def tread_keywords(self, keyword: str, lang: str = "en", country: str = "us") -> Dict[str, Any]:
        """
        Get the trend keywords of the keyword
        :param keyword: the keyword
        :param lang: the language of the keyword
        :param country: the country of the keyword

        :return: the trend keywords of the keyword
        """
        try:

            suggests = self.aso_instance.suggest(keyword, country=country)
            if suggests == []:
                return {"error": "No data found"}
            suggests.pop(0)
            list1 = []
            map = {}
            map_popularity = {}

            map[keyword] = True
            map_popularity[keyword] = 100

            minus = 0
            for s in suggests:
                list1.append(s)
                map[s] = False
                map_popularity[s] = 100 - minus
                minus += 2

            def google_suggests(lst, level):

                res = []
                for sug in lst:
            
                    if map.get(sug, False) == False:
                        suggests = self.aso_instance.suggest(sug, country=country)
                        if suggests == []:
                            continue
                        suggests.pop(0)
                        map[sug] = True

                        minus = 0
                        for s in suggests:
                            if map.get(s, None) == None:
                                res.append(s)
                                map[s] = False
                                if map_popularity.get(s, None) == None:
                                    map_popularity[s] = level - minus
                            minus += 2   

                return res

            list2 = google_suggests(list1, 70)
            list3 = google_suggests(list2, 50)
            list4 = google_suggests(list3, 20)
            # list5 = google_suggests(list4, 15)

            data = []

            for item in map_popularity.items():
                data.append({"keyword": item[0], "number": item[1]})

            data = sorted(data, key=lambda k: k['number'], reverse=True)

            return data
        except Exception as e:
            return {"error": str(e)}