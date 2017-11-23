from mongoengine import Document, EmbeddedDocument, fields


class Job(EmbeddedDocument):
    company = fields.StringField()
    title = fields.StringField()
    highlights = fields.ListField(fields.StringField())
    start_date = fields.DateTimeField()
    end_date = fields.DateTimeField()


class Degree(EmbeddedDocument):
    title = fields.StringField()
    institution = fields.StringField()
    location = fields.StringField()
    start_date = fields.DateTimeField()
    end_date = fields.DateTimeField()


class User(Document):
    name = fields.StringField(required=True)
    profession = fields.StringField()
    email = fields.EmailField()
    phone = fields.StringField()
    website = fields.URLField()
    github = fields.StringField()
    summary = fields.StringField()
    skills = fields.ListField(fields.StringField())
    career = fields.ListField(fields.EmbeddedDocumentField(Job))
    education = fields.ListField(fields.EmbeddedDocumentField(Degree))

    def __str__(self):
        return self.name