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
def top_article():
    max=0
    ls = session.query(Knowledge).all()
    for i in range(5):
        if(ls[i].rating>max):
                max=ls[i].rating
    return max 
def top_3_articles():
    ma=[top_article(),0,0]
    ls = session.query(Knowledge).all()
    for i in range(5):
        if(ls[i].rating>ma[1] and ls[i].rating!=top_article()):
            ma[1]=ls[i].rating
    for i in range(5):
        if(ls[i].rating>ma[2] and ls[i].rating!=top_article()and ls[i]!=ma[1].rating):
            ma[2]=ls[i].rating
    return ma
add_article("vivi","canada wiki","canada",8)
add_article("leen","art wiki","art",10)
add_article("gilad","robotics wiki","robotics",5)
add_article("alice","phone wiki","phones",7)
add_article("noam","music wiki","music",9)
#delete_article_by_topic("canada")
#delete_all_articles()
#print(query_article_by_topic("music"))
edit_article_rating(5,"canada wiki")
print(query_all_articles())
print(top_article())
print(top_3_articles())