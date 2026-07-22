"""네이버 뉴스 본문 추출 명령줄 인터페이스입니다."""

from __future__ import annotations

import argparse

from naver_news import get_naver_news_article_body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="네이버 뉴스 기사 제목과 본문을 추출합니다.")
    parser.add_argument("url", nargs="?", help="네이버 뉴스 기사 URL")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    url = args.url or input("네이버 뉴스 기사 URL을 입력하세요: ").strip()
    if not url:
        print("뉴스 기사 URL을 입력해야 합니다.")
        return 2

    title, body = get_naver_news_article_body(url)
    if title is None or body is None:
        print("기사 본문을 추출하지 못했습니다.")
        return 1

    print(f"\n--- 기사 제목 ---\n{title}\n")
    print(f"--- 기사 본문 ({len(body)}자) ---\n{body}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
