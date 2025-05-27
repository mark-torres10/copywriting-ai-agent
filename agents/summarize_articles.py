"""Summarizes the articles in the data/news_articles directory."""
from datetime import datetime
import json
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic

from data.news_articles.copy import articles
from lib.load_env_vars import CLAUDE_API_KEY
from prompts import summarizer_prompt

current_dir = os.path.dirname(os.path.abspath(__file__))
root_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
agent_dir = os.path.join(root_project_dir, "agents")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
export_fp = os.path.join(current_dir, "summaries", f"article_summaries_{timestamp}.json")

llm = ChatAnthropic(model="claude-3-7-sonnet-20250219", temperature=0, anthropic_api_key=CLAUDE_API_KEY)

def load_articles() -> list[dict]:
    return articles

def summarize_article(article: str) -> str:
    prompt = ChatPromptTemplate.from_template(summarizer_prompt)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"article": article})


def summarize_articles(articles: list[str]) -> dict:
    """Summarizes a series of articles.
    
    Returns a dictionary of article summaries.
    """
    article_to_summary = {}
    total_articles = len(articles)
    for i, article in enumerate(articles):
        print(f"Summarizing article {i+1} of {total_articles}...")
        metadata = article["metadata"]
        title = metadata["title"]
        source = metadata["source"]
        text = article["text"]
        summary = summarize_article(text)
        article_to_summary[source] = {
            "metadata": metadata,
            "original_text": text,
            "summary": summary,
        }
        print(f"Summarized article {title} (Article {i+1} of {total_articles}).")
    return article_to_summary


def export_summaries(summaries: dict) -> None:
    """Exports the summaries to a JSON file."""
    with open(export_fp, "w") as f:
        json.dump(summaries, f)


if __name__ == "__main__":
    articles = load_articles()
    summaries = summarize_articles(articles)
    export_summaries(summaries)
