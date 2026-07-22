# get-naver-news-article-body

네이버 뉴스 기사 URL에서 제목과 본문을 추출하는 작은 Python 도구입니다.

## 설치

```bash
pip install -r requirements.txt
```

## CLI 사용법

프로젝트 디렉터리에서 URL을 인수로 전달합니다.

```bash
python main.py "https://n.news.naver.com/mnews/article/..."
```

URL을 생략하면 대화형으로 입력할 수 있습니다.

```bash
python main.py
```

## Python에서 사용하기

```python
from naver_news import get_naver_news_article_body

title, body = get_naver_news_article_body("https://n.news.naver.com/mnews/article/...")
if title and body:
    print(title)
    print(body)
```

추출에 실패하면 함수는 `(None, None)`을 반환합니다.

## 구성

- `naver_news.py`: `get_naver_news_article_body` 함수
- `main.py`: URL 입력과 결과 출력용 CLI
- `get_naver_news_article_body.ipynb`: 사용 예시와 실험용 노트북
