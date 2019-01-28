import json

class Headline_jclass(object):

	def __init__(self):
		self.headline = ""
		self.stories_id = 0
		self.percentage = 0
		self.agencies = []

	def classify(self, json_string):
		result_info = []
		parsed_json = json.loads(json_string)

		if(type(parsed_json["headline"]) == str):
			self.headline = parsed_json["headline"]
		else:
			result_info.append("Incorrect type: headline")

		if((type(parsed_json["percentage"]) == int) or (type(parsed_json["percentage"]) == float)):
			self.percentage = parsed_json["percentage"]
		else:
			result_info.append("Incorrect type: percentage")

		self.agencies = []
		if(type(parsed_json["agencies"]) == list):
			for each in parsed_json["agencies"]:
				if(type(each) == list):
					self.agencies.append(each)
				else:
					result_info.append("Incorrect type in list: agencies")
		else:
			result_info.append("Incorrect type: agencies")

		return result_info

	def unclassify(self):
		myself = {}

		myself["headline"] = self.headline
		myself["percentage"] = self.percentage
		myself["agencies"] = self.agencies
		myself["stories_id"] = self.stories_id

		return json.dumps(myself, indent = 3)

