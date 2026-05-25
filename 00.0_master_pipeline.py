import subprocess
import sys
import time

def run_pipeline():
    print("🚀 INITIALIZING HYPER-CREATIVE PIPELINE 🚀")
    print("===========================================")
    
    scripts = [
        "01.0_phase1_generator.py",
        "02.0_phase2_auditor.py",
        "03.0_phase3_research.py",
        "04.0_phase4_podcast_script.py"
    ]
    
    for script in scripts:
        print(f"\n⏳ STARTING: {script}...")
        time.sleep(1) # Brief pause for readability
        
        # sys.executable ensures it uses the exact same Python environment
        result = subprocess.run([sys.executable, script])
        
        if result.returncode != 0:
            print(f"\n❌ PIPELINE HALTED: An error occurred in {script}.")
            print("Please fix the error before continuing.")
            sys.exit(1)
            
        print(f"✅ FINISHED: {script}")
        
    print("\n🎉 ALL PHASES COMPLETE! Check your folder for the final outputs.")

if __name__ == "__main__":
    run_pipeline()