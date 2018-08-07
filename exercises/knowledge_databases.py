from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
# v =Knowledge(name,wiki,topic,rating)
def add_article(name,wiki_article,topic,rating):
    knowledge_object = Knowledge(
        name=name,
        wiki_article=wiki_article,
        topic=topic,
        rating =rating,
        )
    session.add(knowledge_object)
    session.commit()
    
def query_all_articles():
    k = session.query(Knowledge).all()
    return k
def query_article_by_topic(their_topic):
    know = session.query(
    Knowledge).filter_by(
    topic=their_topic).first()
    return know

def delete_article_by_topic(the_topic):
   session.query(Knowledge).filter_by(
       topic=the_topic).delete()
   session.commit()

def delete_all_articles():
    session.query(Knowledge).delete()
    session.commit()

def edit_article_rating(update_rating,article_name):
    know = session.query(
    Knowledge).filter_by(
    wiki_article=article_name).first()
    know.rating = update_rating
    session.commit()

add_article("vivi","canada wiki","canada",8)

add_article("noam","music wiki","music",9)
#delete_article_by_topic("canada")
#delete_all_articles()
#print(query_article_by_topic("music"))
edit_article_rating(5,"canada wiki")
print(query_all_articles())
