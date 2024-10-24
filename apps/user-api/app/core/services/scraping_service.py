# import os
import re

import html2text
import requests
from bs4 import BeautifulSoup

# from langchain_community.document_loaders import PyPDFLoader

tags_to_remove = [
    "script",
    "style",
    "noscript",
    "footer",
    "header",
    "nav",
    "aside",
    "button",
]


def html_to_markdown(html_content):
    """
    htmlをmarkdownに変換
    """
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(html_content)

    # 整形
    markdown_content = markdown_content.replace("ページのトップへ戻る", "")
    markdown_content = markdown_content.replace(" ", "")
    markdown_content = re.sub(
        r"(^#+)([^\s#])", r"\1 \2", markdown_content, flags=re.MULTILINE
    )
    # markdown_content = re.sub(r"\n+", "\n", markdown_content)
    # markdown_content = markdown_content.rstrip("\n")

    return markdown_content


def html_of_web_page(url):
    """
    urlからhtmlを取得する
    """

    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in tags_to_remove:
        for element in soup.find_all(tag):
            element.decompose()

    # 画像タグを削除
    for img_tag in soup.find_all("img"):
        img_tag.decompose()

    # # aタグを削除し、そのテキストを埋め込む
    # for a_tag in soup.find_all("a"):
    #     a_tag.replace_with(a_tag.get_text())

    if soup.find(id="main") is not None:
        contents = soup.find(id="contents").find(id="main")
    else:
        contents = soup.find(id="contents")

    html = contents.prettify()
    return html


# def scraping_pdf(url):
#     temp_path = "data/temp/temp_document.pdf"

#     # PDFファイルをダウンロード
#     response = requests.get(url)
#     pdf_content = response.content

#     # PDFファイルを一時ファイルに保存
#     with open(temp_path, "wb") as f:
#         f.write(pdf_content)

#     # PyPDFLoaderを使用してPDFを読み込む
#     loader = PyPDFLoader(temp_path)
#     pages = loader.load_and_split()

#     os.remove(temp_path)

#     content = "\n".join([page.page_content for page in pages])

#     return content
