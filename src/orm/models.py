from pymodm import fields, MongoModel, EmbeddedMongoModel


class Champion(MongoModel):
    riot_id = fields.IntegerField()
    key = fields.CharField()
    name = fields.CharField()
    title = fields.CharField()


class Item(MongoModel):
    riot_id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    plaintext = fields.CharField()


class Map(MongoModel):
    riot_id = fields.IntegerField()
    name = fields.CharField()


class ReforgedRunePath(MongoModel):
    riot_id = fields.IntegerField()
    name = fields.CharField()
    key = fields.CharField()
    icon = fields.CharField()


class ReforgedRune(MongoModel):
    riot_id = fields.IntegerField()
    name = fields.CharField()
    key = fields.CharField()
    short_desc = fields.CharField()
    long_desc = fields.CharField()
    icon = fields.CharField()


class SummonerSpell(MongoModel):
    riot_id = fields.IntegerField()
    name = fields.CharField()
    key = fields.CharField()
    description = fields.CharField()
    summoner_level = fields.IntegerField()


class ProfileIcon(MongoModel):
    riot_id = fields.IntegerField()
    image = fields.EmbeddedDocumentField('Image')


"""Embedded model fields"""


class Image(EmbeddedMongoModel):
    full = fields.CharField()
    sprite = fields.CharField()
