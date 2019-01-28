from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import desc
from sqlalchemy.orm import class_mapper
import json

Base = declarative_base()

class Entries(Base):
	__tablename__ = 'entries'
	rowid = Column(Integer, primary_key=True)
	story_id = Column(Integer)
	headline = Column(String)
	website_url = Column(String)
	image_url = Column(String)

	@staticmethod
	def get_next_story_id(session):
		first = session.query(class_mapper(Entries)).order_by(desc(Entries.story_id)).limit(1).all()
		if len(first) > 0:
			return first[0].story_id + 1
		else:
			return 1

	@staticmethod
	def get_stories(story_id, session):
		query = session.query(class_mapper(Entries)).filter(Entries.story_id == story_id).all()
		if len(query) > 0:
			headline_list = []
			for headline in query:
				headline_list.append(headline.get_dictionary_of_values())
			return json.dumps(headline_list)
		else:
			return 'Invalid story id'

	def get_dictionary_of_values(self):
		return {'story_id' : self.story_id,
				'headline' : self.headline,
				'website_url' : self.website_url,
				'image_url' : self.image_url}