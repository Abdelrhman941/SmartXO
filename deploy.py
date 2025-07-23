#!/usr/bin/env python3
"""
Quick deployment script for XO Game Delight
This script automatically runs the Streamlit app with optimized settings.
"""

import subprocess
import sys
import os
import webbrowser
import time
from pathlib import Path

def check_streamlit_installed():
    """Check if Streamlit is installed."""
    try:
        import streamlit
        return True
    except ImportError:
        return False

def install_streamlit():
    """Install Streamlit if it's not already installed."""
    print("📦 Streamlit not found. Installing...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Streamlit. Please install it manually:")
        print("   pip install streamlit")
        return False

def run_streamlit_app():
    """Run the Streamlit app with optimized settings."""
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    app_file = script_dir / "xo_game_streamlit.py"
    
    if not app_file.exists():
        print(f"❌ Error: {app_file} not found!")
        print("Make sure you're running this script from the project directory.")
        return False
    
    print("🚀 Starting XO Game Delight...")
    print("🌐 The game will open in your default browser")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Run streamlit with optimized settings
        cmd = [
            sys.executable, "-m", "streamlit", "run", str(app_file),
            "--server.port", "8501",
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false",
            "--server.address", "localhost"
        ]
        
        # Start the Streamlit process
        process = subprocess.Popen(cmd)
        
        # Give the server a moment to start
        time.sleep(3)
        
        # Try to open the browser
        try:
            webbrowser.open("http://localhost:8501")
        except Exception:
            print("⚠️  Could not auto-open browser. Please visit: http://localhost:8501")
        
        # Wait for the process to complete
        process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down the server...")
        try:
            process.terminate()
        except:
            pass
        return True
    except Exception as e:
        print(f"❌ Error running the app: {e}")
        return False

def main():
    """Main function to deploy the XO Game."""
    print("🎮 XO Game Delight - Quick Deploy")
    print("=" * 40)
    
    # Check if Streamlit is installed
    if not check_streamlit_installed():
        if not install_streamlit():
            sys.exit(1)
    
    # Run the app
    success = run_streamlit_app()
    
    if success:
        print("\n✅ Thanks for playing XO Game Delight!")
    else:
        print("\n❌ Failed to start the game. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
