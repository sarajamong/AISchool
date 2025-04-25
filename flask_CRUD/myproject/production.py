from dotenv import load_dotenv
import os
from urllib.parse import quote # URL 인코딩을 위한 모듈


BASE_DIR=os.path.dirname(__file__)  # 현재 파일의 디렉토리 경로를 BASE_DIR에 저장
load_dotenv(os.path.join(BASE_DIR,'.env'))  # .env 파일을 읽어옴

SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=quote(os.getenv('DB_PASSWORD')),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY= b'0HiqEMjAQW4jTAxbGfE9dliu0I_jGY2sXJ6VG9i5CKig2cvHDWpX3MFUGIIiWzbeuNea8HKfi1H9WUzusM33Zg'  # 비밀키를 설정

#token_urlsafe(64) : 64바이트 길이의 랜덤한 문자열을 생성하는 메서드