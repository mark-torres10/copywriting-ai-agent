"""Summarizes the articles in the data/news_articles directory."""
from datetime import datetime
import json
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from data.news_articles.copy import articles
from prompts import summarizer_prompt

current_dir = os.path.dirname(os.path.abspath(__file__))
root_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
agent_dir = os.path.join(root_project_dir, "agents")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
export_fp = os.path.join(current_dir, f"article_summaries_{timestamp}.json")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

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
        text = article["text"]
        summary = summarize_article(text)
        article_to_summary[title] = {
            "metadata": metadata,
            "original_text": text,
            "timestamp": article["timestamp"],
            "summary": summary,
        }
        print(f"Summarized article {title} (Article {i+1} of {total_articles}).")
    return article_to_summary


def export_summaries(summaries: dict) -> None:
    """Exports the summaries to a JSON file."""
    with open("summaries.json", "w") as f:
        json.dump(summaries, f)


if __name__ == "__main__":
    articles = load_articles()
    summaries = summarize_articles(articles)
    export_summaries(summaries)
