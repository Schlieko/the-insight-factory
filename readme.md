# 🧠 Creative Idea Pipeline

An autonomous, multi-agent AI pipeline that takes a raw, fuzzy idea and mathematically expands it into a comprehensive deep research report and a conversational podcast script.

Powered by Google's new `google-genai` SDK, utilizing the `gemini-3.1-pro-preview` and `gemini-3.5-flash` models.

## 🚀 The Pipeline Architecture

This repository is broken into four distinct automation phases, all managed by a master script:

1. **Phase 1: The Generator (`01.0_phase1_generator.py`)**
   Reads a raw prompt (`idea.md`) and expands it into a massive, highly structured conceptual master document.

2. **Phase 2: The Auditor (`02.0_phase2_auditor.py`)**
   Acts as a "Red Team" to aggressively attack the Phase 1 concept, exposing logical flaws, market vulnerabilities, and conceptual debt.

3. **Phase 3: The Deep Researcher (`03.0_phase3_research.py`)**
   Uses an outline-driven loop to write a comprehensive, 20-page Deep Research Report (`.docx`), complete with professional formatting and executive styling. It also generates a fallback prompt for manual Deep Research.

4. **Phase 4: The Podcast Producer (`04.0_phase4_podcast.py`)**
   Converts the research into a conversational two-host podcast script and generates highly-optimized Custom Instructions for NotebookLM's Audio Overview feature.

## 🛠️ Setup & Installation

This project is OS-agnostic and runs perfectly on Windows, Mac, Linux, or directly inside GitHub Codespaces.

1. Clone this repository to your local machine (or open it in GitHub Codespaces).
2. Install the lightweight dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Authentication

* **Local Run:** Create a `.env` file in the root directory and add your Google Gemini API key:
  ```env
  GEMINI_API_KEY="your_api_key_here"
  ```

* **GitHub Codespaces:** Go to your repository settings > Secrets and variables > Codespaces, and add a new secret named `GEMINI_API_KEY`. The scripts will automatically detect it!

## 🏃‍♂️ How to Run

1. Open the `idea.md` file. This is your single source of truth. Delete the placeholder text and write your raw concept.
2. Execute the master pipeline script:
   ```bash
   python 00.0_master_pipeline.py
   ```
3. Sit back and watch as the AI automatically generates your master document, audit, research report, and podcast assets right into the folder.

## 🔒 Privacy Note

Thanks to the included `.gitignore` file, your `.env` API keys and generated output files (like the Word doc and scripts) are completely invisible to Git. They will safely stay in your local folder or private Codespace session until overwritten, and will never be uploaded or synced to the public repository.

## 🎧 Audio Generation (NotebookLM)

To generate hyper-realistic, conversational audio for your podcast:

1. Go to Google NotebookLM.
2. Upload the newly generated `Deep_Research_Report.docx` (or `master_output.md`) as your source.
3. Copy the text inside `NotebookLM_Custom_Instructions.txt` and paste it into the Audio Overview configuration menu.
4. Hit generate and enjoy your custom show!
