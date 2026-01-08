#!/usr/bin/env python3
"""
Simple Course Quality Check

Just run this script to see what's missing or needs attention in your courses.
"""

import subprocess
import sys
from pathlib import Path

def main():
    script_dir = Path(__file__).parent
    analyzer_script = script_dir / "course_analyzer.py"
    
    if not analyzer_script.exists():
        print("❌ course_analyzer.py not found")
        return
    
    print("🔍 Checking course quality...")
    print("="*50)
    
    try:
        # Run the main analyzer
        result = subprocess.run([
            sys.executable, str(analyzer_script), 
            "--courses-dir", "../Courses"
        ], text=True)
        
        if result.returncode != 0:
            print("❌ Error running analysis")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()