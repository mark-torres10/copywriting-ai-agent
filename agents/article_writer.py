"""Agent for writing articles."""
import json
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic

from lib.load_env_vars import CLAUDE_API_KEY
from prompts import article_writer_prompt

current_dir = os.path.dirname(os.path.abspath(__file__))
writing_styles_dir = os.path.join(current_dir, "writing_styles")

llm = ChatAnthropic(model="claude-3-7-sonnet-20250219", temperature=0, anthropic_api_key=CLAUDE_API_KEY)


def load_latest_writing_style() -> str:
    """Loads the latest writing style from the writing_styles directory."""
    writing_styles = os.listdir(writing_styles_dir)
    latest_writing_style = max(writing_styles)
    with open(os.path.join(writing_styles_dir, latest_writing_style), "r") as f:
        return f.read()


def load_article_summaries() -> dict:
    """Loads the article summaries from the summaries directory."""
    summaries_dir = os.path.join(current_dir, "summaries")
    summaries = os.listdir(summaries_dir)
    latest_summary = max(summaries)
    with open(os.path.join(summaries_dir, latest_summary), "r") as f:
        return json.load(f)

article_summaries = load_article_summaries()

def write_blog_post_about_article(article_url: str) -> str:
    """Writes a blog post about an article."""
    writing_style = load_latest_writing_style()
    article_summary = article_summaries[article_url]
    prompt = ChatPromptTemplate.from_template(article_writer_prompt)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"writing_style": writing_style, "summary": article_summary})


if __name__ == "__main__":
    article_url = "https://themarijuanaherald.com/2025/05/texas-house-of-representatives-approves-ban-on-hemp-derived-thc/"
    blog_post = write_blog_post_about_article(article_url)
    print(blog_post)
    print("FINISHED!")
