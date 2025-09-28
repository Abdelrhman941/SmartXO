#!/usr/bin/env python3
"""
XO Game Tkinter Demo
This script demonstrates the key features of the Tkinter XO Game.
"""

import subprocess
import sys
import os

def main():
    print("🎮 XO Game Delight - Tkinter Version")
    print("=" * 50)
    print()
    print("✨ Features:")
    print("  👥 Human vs Human mode")
    print("  🤖 AI Opponent with minimax algorithm")
    print("  📊 Score tracking (X wins, O wins, Draws)")
    print("  🎨 Beautiful UI with hover effects")
    print("  🏆 Win highlighting")
    print("  🔄 Game controls (New Game, Reset Scores)")
    print()
    print("🚀 Starting the game...")
    print()
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    game_file = os.path.join(current_dir, "xo_game_tkinter.py")
    
    try:
        # Launch the game
        subprocess.run([sys.executable, game_file], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error: Could not start the game.")
        print("   Make sure Python and Tkinter are properly installed.")
    except FileNotFoundError:
        print("❌ Error: xo_game_tkinter.py not found.")
        print("   Make sure you're running this from the correct directory.")
    except KeyboardInterrupt:
        print("\n👋 Game closed by user.")

if __name__ == "__main__":
    main()