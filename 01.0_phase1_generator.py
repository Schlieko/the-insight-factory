import os
from dotenv import load_dotenv
from google import genai

# --- OS-AGNOSTIC PATHING ---
# This dynamically finds the folder this script is sitting in, no matter the OS!
target_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(target_dir, ".env")
input_filepath = os.path.join(target_dir, "idea.md")
output_filepath = os.path.join(target_dir, "master_output.md")

# --- AUTHENTICATION ---
load_dotenv(os.path.join(target_dir, ".env"))
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file.")
    exit()

# Initialize the modern GenAI SDK
client = genai.Client(api_key=api_key)
model_id = 'gemini-3.1-pro-preview'

def main():
    print("📂 Loading raw idea...")
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            raw_idea = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Could not find '{input_filepath}'. Please create 'idea.md' first.")
        return

    print(f"🧠 Generating Master Concept Document using {model_id}...")
    
    prompt = f"""
    You are an expert strategic consultant and creative director. 
    Take the following raw concept and expand it into a comprehensive, highly structured master document.
    Explore the target audience, core mechanics, potential business models, and immediate next steps.
    
    RAW CONCEPT:
    {raw_idea}
    """

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=prompt
        )
        
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(response.text.strip())
            
        print(f"✅ Success! Master document saved to 'master_output.md'")
        
    except Exception as e:
        print(f"❌ Error generating document: {e}")

if __name__ == "__main__":
    main()