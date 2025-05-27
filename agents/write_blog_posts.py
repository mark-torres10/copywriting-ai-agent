import os
import json
from datetime import datetime
from pathlib import Path

from agents.summarize_articles import load_articles
from agents.article_writer import load_latest_writing_style, load_article_summaries
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from agents.prompts import article_writer_prompt
from lib.load_env_vars import CLAUDE_API_KEY

# Output directory and timestamped filename
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "written_blog_posts")
os.makedirs(output_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_fp = os.path.join(output_dir, f"precomputed_blog_posts_{timestamp}.json")

# LLM setup
llm = ChatAnthropic(model="claude-3-7-sonnet-20250219", temperature=0, anthropic_api_key=CLAUDE_API_KEY)


def main():
    print("Loading articles and summaries...")
    articles = load_articles()
    article_summaries = load_article_summaries()
    writing_style = load_latest_writing_style()
    results = {}
    total = len(articles)
    for i, article in enumerate(articles):
        url = article["metadata"]["source"]
        meta = article["metadata"]
        summary = article_summaries[url]["summary"] if url in article_summaries else None
        if not summary:
            print(f"[SKIP] No summary for {url}")
            continue
        print(f"[{i+1}/{total}] Generating blog post for: {meta.get('title', url)}")
        prompt = ChatPromptTemplate.from_template(article_writer_prompt)
        chain = prompt | llm | StrOutputParser()
        generated_text = chain.invoke({"writing_style": writing_style, "summary": summary})
        results[url] = {
            "metadata": meta,
            "generated_text": generated_text,
        }
    print(f"Saving {len(results)} blog posts to {output_fp}")
    with open(output_fp, "w") as f:
        json.dump(results, f, indent=2)
    print("DONE.")

if __name__ == "__main__":
    main() 