import json

class Article_jclass(object):

    def __init__(self):
        self.author = ""
        self.title = ""
        self.description = ""
        self.url = ""
        self.urlToImage = ""
        self.publishedAt = ""
        self.publisher_code = ""

    def classify(self, json_string):
        result_info = []
        parsed_json = json.loads(json_string)

        if(type(parsed_json["author"]) == str):
            self.author = parsed_json["author"]
        else:
            result_info.append("Incorrect type: author")

        if(type(parsed_json["title"]) == str):
            self.title = parsed_json["title"]
        else:
            result_info.append("Incorrect type: title")

        if(type(parsed_json["description"]) == str):
            self.description = parsed_json["description"]
        else:
            result_info.append("Incorrect type: description")

        if(type(parsed_json["url"]) == str):
            self.url = parsed_json["url"]
        else:
            result_info.append("Incorrect type: url")

        if(type(parsed_json["urlToImage"]) == str):
            self.urlToImage = parsed_json["urlToImage"]
        else:
            result_info.append("Incorrect type: urlToImage")

        if(type(parsed_json["publishedAt"]) == str):
            self.publishedAt = parsed_json["publishedAt"]
        else:
            result_info.append("Incorrect type: publishedAt")

        return result_info

    def unclassify(self):
        myself = dict()

        myself["author"] = self.author
        myself["title"] = self.title
        myself["description"] = self.description
        myself["url"] = self.url
        myself["urlToImage"] = self.urlToImage
        myself["publishedAt"] = self.publishedAt

        return json.dumps(myself, indent = 3)
