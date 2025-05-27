"""Trains the article writer agent on the style that it should
write in.

Returns the details of the style and tone the agent should write in.
"""

import os
from datetime import datetime

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from data.samples.website.blogposts import blogposts
from data.samples.website.copy import copy
from prompts import writing_style_learner_prompt

# hacky solution, direnv isn't working.
root_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
agent_dir = os.path.join(root_project_dir, "agents")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

export_fp = os.path.join(agent_dir, "writing_styles")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"writing_style_{timestamp}.md"
export_fp = os.path.join(export_fp, filename)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)


def load_training_data() -> list[dict]:
    return copy + blogposts


def load_text_from_training_data(training_data: list[dict]) -> list[str]:
    return [item["text"] for item in training_data]


def train_agent(training_data: list[str]) -> str:
    joined_texts = [
        "[TEXT {i}]\n{text}\n\n".format(i=i, text=text)
        for i, text in enumerate(training_data)
    ]
    joined_texts = "\n".join(joined_texts)
    prompt = ChatPromptTemplate.from_template(writing_style_learner_prompt)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"texts": joined_texts})


if __name__ == "__main__":
    training_data: list[dict] = load_training_data()
    print(f"Loaded {len(training_data)} training data items.")
    texts: str = load_text_from_training_data(training_data)
    print(f"Loaded {len(texts)} training texts.")
    writing_style: str = train_agent(texts)
    print(f"Trained agent on {len(texts)} training texts.")
    with open(export_fp, "w") as f:
        f.write(writing_style)
        print(f"Wrote writing style to {export_fp}")
    print(f"Writing style: {writing_style}")
    print("FINISHED!")
