from .lazy import LazyListField
from .verbs import Gettable

from jsonmodels import models, fields


class Topic(models.Base):
    topic = fields.StringField()
    topicId = fields.StringField()
    url = fields.StringField()


class Author(Gettable, models.Base):
    aliases = fields.ListField([str])
    authorId = fields.StringField()
    citationVelocity = fields.IntField()
    influentialCitationCount = fields.IntField()
    name = fields.StringField()
    papers = LazyListField(['Paper'])
    url = fields.StringField()

    def can_get(self):
        return self.authorId is not None

    def endpoint(self):
        return '/author/{authorId}'.format(authorId=self.authorId)


class Paper(Gettable, models.Base):
    arxivId = fields.StringField()
    authors = LazyListField(['Author'])
    citationVelocity = fields.IntField()
    citations = LazyListField(['Paper'])
    doi = fields.StringField()
    influentialCitationCount = fields.IntField()
    paperId = fields.StringField()
    references = LazyListField(['Paper'])
    title = fields.StringField()
    topics = fields.ListField([Topic])
    url = fields.StringField()
    venue = fields.StringField()
    year = fields.IntField()

    def can_get(self):
        return self.paperId is not None

    def endpoint(self):
        return '/paper/{paperId}'.format(paperId=self.paperId)
