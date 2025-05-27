# 🧠 PRD: Brand Voice AI Agent – Content Generation Platform

## 🎯 Objective

Build a Streamlit-based AI system that:

- Learns a brand's tone and style from existing published content (URLs or raw text)
- Generates new content (e.g. blog posts, opinion pieces, product copy) on custom topics in that voice
- Optionally scores the generated copy using an LLM-based judge for tone and content quality
- Allows the user to export final copy to Google Docs (via pre-integrated Google API auth)
- Allows users to submit feedback on generated drafts to improve future generations

## 🧩 Key Features

- Brand Voice Ingestion
  - Input: URLs or pasted raw text of brand content
  - Process: Clean extraction of text; summarize tone, style, and rhetorical devices
  - Output: Structured "voice profile" used in future prompt templates

- Trend or Topic Input
  - Input: Manually typed, pasted, or URL-based input of a current topic or trend
  - Optional: Integrate trending topic scrapers (e.g., Reddit, Google News APIs)

- Voice-Driven Content Generation
  - Compose content in the ingested brand voice using the selected topic
  - Adjustable formats: blog, headline, opinion, product copy
  - Prompt includes voice profile + content objective

- LLM Judge Module (Optional)
  - Evaluates tone fit, content quality, brand alignment
  - Provides structured ratings + freeform feedback
  - Output visible in UI for QA/debugging

- Interactive Streamlit UI
  - Input brand URLs or text
  - Provide topic or paste link
  - Show generated content with side-by-side original copy
  - LLM scoring results
  - Export to Google Docs
  - Feedback: Includes a text box below the generated draft. Users can submit feedback on the generation . Submissions are saved as JSON records (includes prompt, draft, and feedback). These records are used to ground future prompts for improved tuning.

- Google Docs Export
  - Uses existing OAuth integration
  - Pushes generated output to user-selected Google Drive folder.

Proposed file structure:
```
ai_brand_voice_agent/
├── app.py                       # Streamlit entry point
├── interface/
│   ├── input_interface.py             # Collect brand content URLs/text
│   ├── topic_interface.py             # Input custom topic or trend
│   ├── generate_interface.py          # Generation interface
│   ├── judge_interface.py             # QA + rating viewer (Optional)
│   ├── export_interface.py            # Google Docs integration
│   ├── feedback_interface.py          # User feedback form and submission
├── modules/
│   ├── extractor.py             # URL/text content cleaning
│   ├── voice_profiler.py        # Style extraction from text
│   ├── generator.py             # LLM-based content generator
│   ├── judge.py                 # LLM judge scoring logic
│   ├── google_docs.py           # Google API exporter
│   ├── feedback_handler.py      # Save feedback as JSON and prepare tuning prompts
├── data/
│   ├── samples/                 # Sample input/output examples
│   ├── temp/                    # Temp logs / evaluations
│   └── feedback_logs/           # Saved feedback JSON entries
├── config/
│   └── prompts.yaml             # Prompt templates per task
├── requirements.txt
└── README.md
```

Proposed Streamlit layout:

- Single-page
- Series of interfaces

