# Streamlit App Plan: Brand Voice AI Agent – Content Generation Platform

## 1. Project Overview

**Goal:** Build a demo Streamlit app that showcases an AI agent capable of learning a brand's voice and generating high-quality, on-brand content. The app should be visually impressive, intuitive, and clearly communicate value to marketing professionals.

---

## 2. User Experience (UX) Flow

### a. Landing & Introduction
- **Welcome section**: Brief, visually engaging intro explaining the app's value (AI-powered copywriting in your brand voice).
- **How it works**: 3-step visual guide (Ingest Brand Voice → Select Topic → Generate & Refine Content).

### b. Brand Voice Ingestion
- **Input options**: 
  - Paste URLs of existing brand content
  - Paste raw text
- **UI feedback**: Show progress, success/failure, and a summary of the extracted brand voice (tone, style, rhetorical devices) in a visually appealing card.

### c. Article Selection & Preview
- **Article list**: Display saved articles as clickable cards/buttons with title previews.
- **On click**: Show AI-generated summary of the article in a side panel or modal.

### d. Content Generation
- **Prompt area**: Button to "Write a custom AI-generated blog post about this article".
- **Generation feedback**: Show loading animation/spinner while generating.
- **Display**: Show generated article in a clean, readable format, side-by-side with the original if available.

### e. Feedback & Export
- **Feedback box**: Text area for free-form feedback, thumbs up/down buttons, and a submit button.
- **Feedback confirmation**: Show a toast or modal confirming feedback/export success.

---

## 3. UI/Design Principles
- **Modern, minimal, and brand-neutral color palette**
- **Clear visual hierarchy**: Use cards, sections, and whitespace for clarity
- **Responsive layout**: Works on desktop and tablet
- **Accessible fonts and contrast**
- **Microinteractions**: Subtle animations for loading, button clicks, and feedback
- **Consistent iconography**: Use icons for steps, feedback, and export

---

## 4. Technical Modules & Steps

### a. Streamlit App Structure
- Single-page app with sectioned layout (using `st.sidebar` and main area)
- Modular code: separate files for UI, logic, and integrations

### b. Brand Voice Ingestion
- Text extraction from URLs (web scraping/boilerplate removal)
- Text cleaning and summarization (tone/style extraction)
- Store structured voice profile in session state

### c. Article Management
- Load and display saved articles (from local or cloud storage)
- Generate previews and summaries

### d. Content Generation
- Prompt construction using voice profile and selected topic/article
- Call LLM API (OpenAI or similar) for content generation
- Display results with clear formatting

### e. Feedback & Export
- Collect feedback (text, thumbs up/down)
- Save feedback as JSON in `data/tmp/{session_timestamp}/`

### f. Session & State Management
- Use Streamlit session state for user progress, selections, and temporary data

---

## 5. Implementation Steps

1. **Set up Streamlit project structure**
2. **Design landing and onboarding UI**
3. **Implement brand voice ingestion (UI + backend)**
4. **Build article list and preview interface**
5. **Integrate content generation logic and display**
6. **Implement feedback collection and JSON saving**
7. **Polish UI/UX: colors, spacing, icons, animations**
8. **Test end-to-end flow and demo with sample data**

---

## 6. Demo & Value Communication
- **Highlight ease of use**: Minimal steps, clear calls to action
- **Emphasize feedback loop**: How user feedback improves future generations

---

## 7. Success Criteria
- Non-technical users can ingest brand voice, generate, and export content in <5 minutes
- UI is visually impressive and intuitive
- Feedback and export features work seamlessly
- Demo leaves marketing audience confident in AI copywriting value 