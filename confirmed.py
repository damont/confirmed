from pprint import pprint
import json
from headline import Headline_jclass
from newsapi_articles import Newsapi_articles
from entries import Entries
from apikey import newsapi_key

news_list = ['al-jazeera-english',
             'abc-news-au',
             'associated-press',
             'bbc-news',
             'buzzfeed',
             'cnbc',
             'cnn',
             'newsweek',
             'new-york-magazine',
             'reuters',
             'the-huffington-post',
             'the-new-york-times',
             'the-washington-post',
             'usa-today']
news_url = 'https://newsapi.org/v1/articles?apiKey=' + newsapi_key + '&source='


def get_headlines():
    """
    Loop through over our list of news agencies and return the headlines

    :return: A list of Newsapi_articles
    """
    headline_lists = []
    for news_agency in news_list:
        news = Newsapi_articles()
        if news.get_news(news_url + news_agency):
            headline_lists.append(news)
    return headline_lists

def structure_json_formatted_output(matches):
    """
    Once we get to this point we have the matches that we want. Therefore, we need to save off the matches
    to our sql database and
    :param matches:
    :return:
    """
    # conn = SQLConn()
    matched_output = []
    for match in matches:
        headline = Headline_jclass()
        headline.headline = match[0].title
        headline.percentage = float(len(match))/float(len(news_list))
        headline.stories_id = 1#Entries().get_next_story_id(conn.s)
        for article in match:
            headline.agencies.append(article.publisher_code)
            ent = Entries()
            ent.story_id = headline.stories_id
            ent.headline = article.title
            ent.image_url = article.urlToImage
            ent.website_url = article.url
        #     conn.s.add(ent)
        # conn.s.commit()
        matched_output.append(headline)
    # Return the matches in the correct order.
    ranked_match_output = []
    for match in matched_output:
        if len(ranked_match_output) == 0:
            ranked_match_output.append(match)
        else:
            for index in range(len(ranked_match_output)):
                if match.percentage > ranked_match_output[index].percentage:
                    ranked_match_output.insert(index, match)
                    break
                elif index == (len(ranked_match_output) - 1):
                    ranked_match_output.append(match)
    return_matches = []
    for match in ranked_match_output:
        return_matches.append(json.loads(match.unclassify()))
    return json.dumps(return_matches)

def find_match(headline1, headline2):
    string_list = headline1.split()
    filtered_string_list = [string for string in string_list if len(string) > 4]
    match = []
    for string in filtered_string_list:
        if string in headline2.split():
            match.append(string)
    return set(match)

def get_article_list(headline_list):
    # for headline in headline_list['headlines']:
    #     for heady in headline:
    #         print(heady.title)
    match_list = []
    for index in range(len(headline_list) - 1):
        current_headline_list = headline_list[index]
        for current_article in current_headline_list.articles:
            agencies_excluding_current = headline_list[index + 1:]
            headline_match = []
            for not_current_agency in agencies_excluding_current:
                for compared_arcticle in not_current_agency.articles:
                    matches = find_match(current_article.description, compared_arcticle.description)
                    if len(matches) > 3:
                        if len(headline_match) == 0:
                            headline_match.append(current_article)
                        headline_match.append(compared_arcticle)
            if len(headline_match) > 0:
                match_list.append(headline_match)
    return match_list

# def get_stories(story_id):
#     # conn = SQLConn()
#     return Entries.get_stories(story_id, conn.s)

if __name__ == '__main__':
    pprint(structure_json_formatted_output(get_article_list(get_headlines())))


