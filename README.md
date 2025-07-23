# XO Game Delight

A beautiful and interactive Tic-Tac-Toe game built with Streamlit, featuring both human vs. human and human vs. AI gameplay modes.


## ✨ Features

- **Two Game Modes**:
  - 👥 **Human vs. Human**: Play against a friend on the same device
  - 🤖 **AI Opponent**: Challenge an unbeatable AI powered by the minimax algorithm
- **Beautiful UI**: Elegant design with smooth animations and visual feedback
- **Score Tracking**: Keep track of X wins, O wins, and draws
- **Responsive Design**: Works well on desktop and mobile devices

## 🚀 How to Run

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start (Recommended)

1. **Clone or download this repository**

2. **Navigate to the project directory**

3. **Run the deployment script**
   ```bash
   python deploy.py
   ```
   
   The script will:
   - ✅ Automatically install Streamlit if needed
   - 🚀 Start the game server
   - 🌐 Open your browser automatically
   - 🎮 Ready to play!

### Manual Installation

If you prefer to run manually:

1. **Install required packages**
   ```bash
   pip install streamlit
   ```

2. **Run the game**
   ```bash
   streamlit run xo_game_streamlit.py
   ```

3. **Your browser should automatically open with the game running**
   - If not, open a browser and go to: http://localhost:8501

## 🎮 How to Play

1. **Choose a game mode** from the main menu:
   - Human vs. Human
   - Human vs. AI

2. **Playing the Game**:
   - The board is a 3x3 grid
   - Players take turns placing their mark (X or O) in empty cells
   - X always goes first
   - In AI mode, you play as X against the computer (O)

3. **Winning the Game**:
   - Get three of your marks in a horizontal, vertical, or diagonal row
   - If all cells are filled and no player has three in a row, the game is a draw

4. **Game Controls**:
   - Click on any empty cell to place your mark
   - Use the "New Game" button to start a new round with the same mode
   - Use the "Menu" button to return to the mode selection screen

## 🧠 AI Opponent

The AI uses the minimax algorithm to make optimal moves, making it essentially unbeatable. At best, you can force a draw against it!

## 💻 Technical Details

- Built with [Streamlit](https://streamlit.io/), a Python framework for data apps
- Uses session state to maintain game state between interactions
- Features custom CSS and animations for an enhanced user experience
- Implements the minimax algorithm for perfect AI play
- Includes `deploy.py` for one-click deployment with automatic dependency management

### Files Structure
- `xo_game_streamlit.py` - Main game application
- `deploy.py` - Quick deployment script
- `thecode.py` - Additional game logic (if any)
- `README.md` - This documentation

## 📝 License

This project is open source and available for personal and educational use.

---

Enjoy the game! 🎮
