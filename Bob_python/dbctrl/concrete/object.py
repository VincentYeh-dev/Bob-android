import json
from typing import List, TextIO

from dbctrl.framework.data import Data, DataParser


class Language:
    def __init__(self, code: str, tr_name: str, tr_sentence: str):
        self.tr_sentence = tr_sentence
        self.tr_name = tr_name
        self.code = code


class Object(Data):
    def __init__(self, name: str, group: str, sentence: str, action: str, languages: List[Language]):
        self.languages = languages
        self.action = action
        self.sentence = sentence
        self.group = group
        self.name = name

    def getSpecifyLanguage(self, code: str) -> Language:
        for language in self.languages:
            if language.code is code:
                return language

        raise Exception()

    def getQueryId(self):
        return self.name


class JSONObjectParser(DataParser):

    def __init__(self):
        super().__init__()

    def parse(self, content: TextIO) -> List[Object]:
        objectList: List[Object] = []
        json_array = json.load(content)

        for json_object in json_array:
            languages: List[Language] = []
            json_languages_array = json_object['languages']
            for lan in json_languages_array:
                languages.append(Language(lan['code'], lan['tr_name'], lan['tr_sentence']))

            objectList.append(
                Object(json_object['name'], json_object['group'], json_object['sentence'], json_object['action'],
                       languages))
        return objectList
