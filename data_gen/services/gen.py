from datetime import datetime
import json
import random
from time import time
from typing import List
import uuid
import faker

from ..models.models import Edu_prog, Edu_prog_file, Education_form, Up, Up_file

class GenService:
    def __init__(self) -> None:
        faker.Faker.seed(int(time()))
        self.fake = faker.Faker(locale='ru_RU')
    
    def get_edu_prog(self, size: int = 1) -> List[Edu_prog]:
        return_list = []
        for _ in range(size):
            data = {
                'title': self.fake.word(),
                'direction': self.fake.word(),
                'code_direction':self.fake.phone_number().replace(" ", ""),
                'start_year': int(self.fake.date(pattern= '%Y')),
                'end_year': int(self.fake.date(pattern= '%Y')),
                'external_id': str(self.fake.pyint(100000, 999999))
            }
            add_object = Edu_prog(**data)
            return_list.append(add_object)
        self.get_up(1)
        return return_list
    
    def get_up(self, size: int = 1) -> List[Up]:
        return_list = []
        for _ in range(size):
            data = {
                'title': self.fake.word(),
                'direction': self.fake.word(),
                'code_direction':self.fake.phone_number().replace(" ", ""),
                'start_year': int(self.fake.date(pattern= '%Y')),
                'end_year': int(self.fake.date(pattern= '%Y')),
                'external_id': str(uuid.uuid4()),
                'educational_program': str(uuid.uuid4()),
                'education': random.choice(list(Education_form))
            }
            add_object = Up(**data)
            return_list.append(add_object)
        return return_list
    
    def create_json_file(self, json, name_file: str) -> str:
        file = open(name_file, 'w')
        file.write(json)
        file.close()
        return name_file
    
    def json_edu_prog(self, data: Edu_prog_file) -> str:
        jsondata = data.json()
        # json
        return self.create_json_file(jsondata, f'edu_prog_at_{datetime.now().strftime("%H_%M_%S")}.json')
    
    def json_up(self, data: Up_file) -> str:
        jsondata = data.json(models_as_dict=False)
        return self.create_json_file(jsondata, f'up_at_{datetime.now().strftime("%H_%M_%S")}.json')