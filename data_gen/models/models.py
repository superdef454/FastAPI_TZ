from enum import Enum
from typing import Optional
import uuid
from pydantic import BaseModel, constr

class Base(BaseModel):
    title: str
    direction: str
    code_direction: str
    start_year: int
    end_year: int
    
    class Config:
        orm_mode = True

class Edu_prog(Base):
    external_id: Optional[constr(max_length=6)]
    
class Edu_prog_file(BaseModel):
    organization_id: uuid.UUID
    edu_prog: list[Edu_prog]
    
class Education_form(str, Enum):
    EXTRAMURAL = 'EXTRAMURAL'
    FULL_TIME = 'FULL_TIME'
    PART_TIME = 'PART_TIME'
    SHORT_EXTRAMURAL = 'SHORT_EXTRAMURAL' 
    SHORT_FULL_TIME = 'SHORT_FULL_TIME'
    EXTERNAL = 'EXTERNAL'
    
class Up(Base):
    external_id: str
    education: Education_form
    educational_program: str
    
class Up_file(Up):
    organization_id: uuid.UUID