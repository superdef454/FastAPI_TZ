import uvicorn
import argparse
import enum

from .settings import settings

class Schema(str, enum.Enum):
    edu_prog = 'edu-prog'
    up = 'up'

parser = argparse.ArgumentParser(description='T3')
parser.add_argument('-schema', type=Schema, help='Выбранная схема скрипта (edu_prog / up)')
parser.add_argument('--size', type=int, help='Необязательное число фейковых словарей')
args = parser.parse_args()
print(args)

uvicorn.run(
    'data_gen.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)