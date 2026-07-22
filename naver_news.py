"""네이버 뉴스 기사에서 제목과 본문을 추출하는 기능을 제공합니다."""

from __future__ import annotations

import re

import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def get_naver_news_article_body(url: str) -> tuple[str | None, str | None]:
    """기사 URL에서 제목과 본문을 추출합니다.

    추출에 실패하면 ``(None, None)``을 반환합니다.
    """
    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None, None

    soup = BeautifulSoup(response.text, "lxml")
    article_body = soup.find("div", id="dic_area") or soup.find(
        "div", class_="_article_body"
    )
    if article_body is None:
        return None, None

    for element in article_body.select(
        "script, style, figure, figcaption, .byline, .util_art, .text_guide, "
        ".img_center, .img_viewer, .img_desc"
    ):
        element.decompose()

    paragraphs = [
        paragraph.get_text(" ", strip=True)
        for paragraph in article_body.find_all("p")
        if paragraph.get_text(strip=True)
    ]
    body = "\n\n".join(paragraphs) if paragraphs else article_body.get_text("\n", strip=True)
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    title_tag = soup.find("h2", id="title_area")
    title = title_tag.get_text(" ", strip=True) if title_tag else "제목 없음"
    return title, body or None
