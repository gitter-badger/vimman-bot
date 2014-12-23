# -*- coding: utf-8 -*-
from bpmappers import Mapper, RawField, DelegateField, ListDelegateField
class OperationMapper(Mapper):
    id = RawField()
    username = RawField()
    state = RawField()
    created_at = RawField()
    updated_at = RawField()

class ListOperationMapper(Mapper):
    result = ListDelegateField(OperationMapper)

class AnswerMapper(Mapper):
    id = RawField()
    question_id = RawField()
    content = RawField()
    state = RawField()
    created_by = RawField()
    updated_by = RawField()
    created_at = RawField()
    updated_at = RawField()

class ListAnswerMapper(Mapper):
    pass

class QuestionMapper(Mapper):
    id = RawField()
    content = RawField()
    state = RawField()
    created_by = RawField()
    updated_by = RawField()
    created_at = RawField()
    updated_at = RawField()

    answers = ListDelegateField(AnswerMapper)

class ListQuestionMapper(Mapper):
    #question_list = ListDelegateField(QuestionMapper)
    result = ListDelegateField(QuestionMapper)


class InformationMapper(Mapper):
    id = RawField()
    content = RawField()
    state = RawField()
    created_by = RawField()
    updated_by = RawField()
    created_at = RawField()
    updated_at = RawField()

class ListInformationMapper(Mapper):
    result = ListDelegateField(InformationMapper)

class TweetMapper(Mapper):
    id = RawField()
    type = RawField()
    tweet_id = RawField()
    content = RawField()
    created_by = RawField()
    updated_by = RawField()
    created_at = RawField()
    updated_at = RawField()

class ListTweetMapper(Mapper):
    result = ListDelegateField(TweetMapper)

class ResponseMapper(Mapper):
    id = RawField()
    type = RawField()
    content = RawField()
    state = RawField()
    created_by = RawField()
    updated_by = RawField()
    created_at = RawField()
    updated_at = RawField()

class ListResponseMapper(Mapper):
    result = ListDelegateField(ResponseMapper)
