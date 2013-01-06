#!/usr/bin/python

from xml.etree.ElementTree import fromstring
import dateutil.parser
from json import JSONEncoder

class HackyJsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

# see this http://data.stackexchange.com/stackoverflow/query/69572
POST_TYPE_ID_QUESTION = 1
POST_TYPE_ID_ANSWER = 2
# 3  Wiki                
# 4  TagWikiExcerpt      
# 5  TagWiki             
# 6  ModeratorNomination 
# 7  WikiPlaceholder     
# 8  PrivilegeWiki  

ACCEPTED_ANSWER_ID = 'AcceptedAnswerId'
CREATION_DATE = 'CreationDate'

# http://stackoverflow.com/questions/127803/how-to-parse-iso-formatted-date-in-python
def split_tags(tags_str):
    return tags_str.replace('<', ' ').replace('>', ' ').split()

class QuestionPost(object):
    def __init__(self, attributes_dict):
        self.tags = split_tags(attributes_dict['Tags'])
        self.answer_count = int(attributes_dict.get('AnswerCount', '0'))
        self.accepted_answer_id = int(attributes_dict[ACCEPTED_ANSWER_ID], '0')
        self.creation_time_str = attributes_dict[CREATION_DATE]
        self.accepted_latency_seconds = -1

    def merge_accepted_response(self, accepted_post_attribss):
        this_post_time = dateutil.parser.parse(self.creation_time_str)
        self.accepted_latency_seconds = int((accepted_post_time - this_post_time
                                             ).total_seconds())

    def creation_time(self):
        return dateutil.parser.parse(self.creation_time_str)

class AnswerPost(object):
    def __init__(self, attib):
        self.answer_id = int(attrib['Id'])
        self.answer_time = dateutil.parser.parse(accepted_post_attrs[CREATION_DATE])

    def creation_time(self):
        return self.answer_time

def post_from_line(line):
    attrib = fromstring(line.strip()).attrib
    posttypeid = int(attrib['PostTypeId'])    
    if posttypeid == POST_TYPE_ID_QUESTION:
        return QuestionPost(attrib)
    else:
        return AnswerPost(attrib)

def main():
    questions_needing_answers = {}
    for idx, line in enumerate(open('/home/rrenaud/SE_Dump/Content/posts.xml')):
        if idx <= 1:
            continue
        post = post_from_line(line)
        if type(post) == QuestionPost:
            if question_post.answer_id:
                questions_needing_answers[question_post.accepted_answer_id] = \
                    question_post
            else:
                
        elif type(post) == AnswerPost:
            if answer_id in questions_needing_answers:
                questions_needing_answers[answer_id].merge_accepted_response(attrib)
        
                

if __name__ == '__main__':
    main()
