import requests
import json
from article import Article_jclass

class Newsapi_articles(object):

    def __init__(self):
        self.status = "ok"
        self.source = "abc-news-au"
        self.sortBy = "top"
        self.articles = []

    def classify(self, json_string):
        result_info = []
        parsed_json = json.loads(json_string)

        if(type(parsed_json["status"]) == str):
            self.status = parsed_json["status"]
        else:
            result_info.append("Incorrect type: status")

        if(type(parsed_json["source"]) == str):
            self.source = parsed_json["source"]
        else:
            result_info.append("Incorrect type: source")

        if(type(parsed_json["sortBy"]) == str):
            self.sortBy = parsed_json["sortBy"]
        else:
            result_info.append("Incorrect type: sortBy")

        self.articles = []
        if(type(parsed_json["articles"]) == list):
            for each in parsed_json["articles"]:
                article = Article_jclass()
                if len(article.classify(json.dumps(each))) == 0:
                    article.publisher_code = self.source
                    self.articles.append(article)
                else:
                    result_info.append("Articles in unexpected format")
        else:
            result_info.append("Incorrect type: articles")

        return result_info

    def unclassify(self):
        myself = dict()

        myself["status"] = self.status
        myself["source"] = self.source
        myself["sortBy"] = self.sortBy

        myself["articles"] = []
        for article in self.articles:
            myself["articles"].append(json.loads(article.unclassify()))

        return json.dumps(myself, indent=3)

    def get_news(self, url):
        full_response = requests.get(url)
        if full_response.status_code == 200:
            self.classify(full_response.text)
            return True
        return False


if __name__ == '__main__':
    api_key = '<insert API key here>'
    news_url = 'https://newsapi.org/v1/articles?apiKey=' + api_key + '&source='

    news = Newsapi_articles()
    if news.get_news(news_url + 'al-jazeera-english'):
        print(news.unclassify())
    else:
        print("Bad news today")


