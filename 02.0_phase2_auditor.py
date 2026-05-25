import os
from dotenv import load_dotenv
from google import genai

# --- OS-AGNOSTIC PATHING ---
target_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(target_dir, ".env")
input_filepath = os.path.join(target_dir, "master_output.md")
output_filepath = os.path.join(target_dir, "audit_report.md")

# --- AUTHENTICATION ---
load_dotenv(os.path.join(target_dir, ".env"))
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file.")
    exit()

client = genai.Client(api_key=api_key)
model_id = 'gemini-3.1-pro-preview'

def main():
    print("📂 Loading Master Document for auditing...")
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            master_doc = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Could not find '{input_filepath}'. Run Phase 1 first.")
        return

    print(f"🔍 Executing Conceptual Audit using {model_id}...")
    
    prompt = f"""
    You are a ruthless "Red Team" auditor and risk analyst. 
    Review the following master document and aggressively attack the concept.
    Identify logical flaws, hidden conceptual debt, market vulnerabilities, and systemic fragility.
    Be brutally honest but constructive.
    
    MASTER DOCUMENT:
    {master_doc}
    """

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=prompt
        )
        
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(response.text.strip())
            
        print(f"✅ Success! Audit report saved to 'audit_report.md'")
        
    except Exception as e:
        print(f"❌ Error generating audit: {e}")

if __name__ == "__main__":
    main()