import os
from dotenv import load_dotenv
from google import genai

# --- 1. CONFIGURATION & AUTHENTICATION ---
# OS-Agnostic pathing (Works on Windows, Mac, Linux, and GitHub Codespaces)
target_dir = os.path.dirname(os.path.abspath(__file__))
input_filepath = os.path.join(target_dir, "master_output.md")

load_dotenv(os.path.join(target_dir, ".env"))
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file (or GitHub Secrets).")
    exit()

client = genai.Client(api_key=api_key)
model_id = "gemini-3.1-pro-preview"

def main():
    # --- 2. LOAD THE SOURCE DOCUMENT ---
    print("📂 Loading source document: master_output.md...")
    try:
        with open(input_filepath, "r", encoding="utf-8") as f:
            document_text = f.read()
    except FileNotFoundError:
        print(f"❌ ERROR: Could not find '{input_filepath}'. Make sure Phase 1 has run.")
        return

    # --- 3. GENERATE PRIMARY PODCAST SCRIPT ---
    print(f"🎙️ Generating Primary Podcast Script using {model_id}...")

    podcast_prompt = f"""
    You are an expert podcast producer and scriptwriter. 
    Turn the following research document into an engaging, conversational podcast script between two hosts (Host A and Host B).
    Make it dynamic, insightful, and accessible to a general audience.
    
    Keep the dialogue continuous, alternating, and do not include long monologues.

    DOCUMENT TEXT:
    {document_text}
    """

    try:
        podcast_response = client.models.generate_content(
            model=model_id,
            contents=podcast_prompt,
        )
        
        podcast_script = podcast_response.text.strip()
        
        podcast_filepath = os.path.join(target_dir, "Generated_Podcast_Script.txt")
        with open(podcast_filepath, "w", encoding="utf-8") as f:
            f.write(podcast_script)
            
        print("✅ Saved primary podcast script to 'Generated_Podcast_Script.txt'")

    except Exception as e:
        print(f"❌ Error generating podcast script: {e}")
        return

    # --- 4. GENERATE NOTEBOOKLM FALLBACK INSTRUCTIONS ---
    print("🧠 Generating NotebookLM Custom Instructions fallback...")

    notebook_system_prompt = f"""
    You are an expert podcast producer and Prompt Engineer. 
    Based on the provided document, write a highly optimized 'Custom Instruction' for Google NotebookLM's Audio Overview feature.

    The instruction must speak directly to the two AI hosts and tell them:
    1. The primary thesis and target audience.
    2. The specific tone they should adopt (e.g., highly technical, balanced, enthusiastic).
    3. 2-3 specific data points, metaphors, or concepts they absolutely must highlight.
    4. What to avoid.

    Keep the instruction punchy, directive, and under 3000 characters. Output ONLY the instruction text.

    DOCUMENT TEXT:
    {document_text}
    """

    try:
        notebook_response = client.models.generate_content(
            model=model_id,
            contents=notebook_system_prompt,
        )
        
        notebook_instructions = notebook_response.text.strip()
        
        instructions_filepath = os.path.join(target_dir, "NotebookLM_Custom_Instructions.txt")
        with open(instructions_filepath, "w", encoding="utf-8") as f:
            f.write("--- COPY AND PASTE THIS INTO NOTEBOOKLM'S AUDIO OVERVIEW CUSTOM INSTRUCTIONS ---\n\n")
            f.write(notebook_instructions)
            
        print("✅ Saved NotebookLM instructions to 'NotebookLM_Custom_Instructions.txt'")

    except Exception as e:
        print(f"❌ Error generating NotebookLM instructions: {e}")

    print("\n🎉 Phase 4 Complete! Text and Prompts are ready for NotebookLM.")

if __name__ == "__main__":
    main()