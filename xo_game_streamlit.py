import streamlit as st
import time
from typing import Dict, List, Optional, Literal
################################ Set up the page configuration #################################
st.set_page_config(
    page_title            = "XO Game Delight",
    page_icon             = "🎮",
    layout                = "centered",
    initial_sidebar_state = "collapsed"
)
################################ Custom CSS for styling #################################
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa, #000000);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .stApp {
        background: linear-gradient(135deg, #2e6552 0%, #2e6552 50%, #DAF7A6 100%);
        color: #ffffff;
    /*---------- Title styling ----------*/
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(145deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
    }
    
    .game-title {
        font-size: 2.5rem; 
        font-weight: 800;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(to right, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    
    .game-subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #4b5563;
        margin-bottom: 2rem;
    }
    
    .centered-text {
        text-align: center;
    }
    
    .badge {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.875rem;
        margin-right: 8px;
    }
    
    .badge-blue {
        background-color: #dbeafe;
        color: #1e40af;
    }
    
    .badge-red {
        background-color: #fee2e2;
        color: #b91c1c;
    }
    
    .badge-gray {
        background-color: #f3f4f6;
        color: #1f2937;
    }
    /*---------- Game status styling ----------*/
    .game-status {
        text-align: center;
        margin: 20px 0;
        padding: 15px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .status-win {
        background: linear-gradient(145deg, rgba(46, 204, 113, 0.3), rgba(39, 174, 96, 0.3));
        border-color: #2ecc71;
        animation: winCelebration 2s ease-in-out;
    }
    
    .status-win-ai {
        background: linear-gradient(145deg, rgba(231, 76, 60, 0.4), rgba(192, 57, 43, 0.4));
        border: 3px solid #e74c3c;
        animation: winCelebration 2s ease-in-out;
        color: #ffffff !important;
        box-shadow: 0 0 25px rgba(231, 76, 60, 0.5);
    }
    
    .status-win-ai h2 {
        color: #e74c3c !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        font-weight: bold;
    }
    
    .status-win-ai p {
        color: #ffffff !important;
    }
    
    .status-win-human {
        background: linear-gradient(145deg, rgba(52, 152, 219, 0.4), rgba(41, 128, 185, 0.4));
        border: 3px solid #3498db;
        animation: winCelebration 2s ease-in-out;
        color: #ffffff !important;
        box-shadow: 0 0 25px rgba(52, 152, 219, 0.5);
    }
    
    .status-win-human h2 {
        color: #3498db !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        font-weight: bold;
    }
    
    .status-win-human p {
        color: #ffffff !important;
    }
    
    .status-draw {
        background: linear-gradient(145deg, rgba(255, 193, 7, 0.3), rgba(255, 152, 0, 0.3));
        border-color: #ffc107;
    }
    
    .status-message {
        font-size: 1.5rem;
        font-weight: 600;
        text-align: center;
        color: #1f2937;
        margin-bottom: 1rem;
        padding: 0.5rem;
    }
    
    .stButton > button {
        height: 80px;
        font-size: 2rem;
        font-weight: bold;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.2s;
    }
    
    .cell-x > button {
        background-color: #dbeafe !important;
        border: 2px solid #93c5fd !important;
        color: #1e40af !important;
    }
    
    .cell-o > button {
        background-color: #fee2e2 !important;
        border: 2px solid #fca5a5 !important;
        color: #b91c1c !important;
    }
    
    .cell-empty > button {
        background-color: white !important;
        border: 2px solid #d1d5db !important;
        color: #6b7280 !important;
    }
    
    .cell-empty > button:hover {
        background-color: #f3f4f6 !important;
        transform: scale(1.05);
    }
    
    div[data-testid="stHorizontalBlock"] {
        gap: 10px !important;
    }
    
    @keyframes winCelebration {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        function styleButtons() {
            const buttons = document.querySelectorAll('button[data-testid*="cell"]');
            buttons.forEach(button => {
                const text = button.textContent.trim();
                if (text === 'X') {
                    button.style.color = '#e74c3c';
                    button.style.textShadow = '3px 3px 6px rgba(0, 0, 0, 0.4)';
                    button.style.background = '#ecf0f1';
                } else if (text === 'O') {
                    button.style.color = '#3498db';
                    button.style.textShadow = '3px 3px 6px rgba(0, 0, 0, 0.4)';
                    button.style.background = '#ecf0f1';
                }
            });
        }
        
        // Style buttons initially and on any changes
        styleButtons();
        const observer = new MutationObserver(styleButtons);
        observer.observe(document.body, { childList: true, subtree: true });
    });
</script>""", unsafe_allow_html=True)
################################ Game Types and Constants #################################
Player     = Literal["X", "O"]
CellValue  = Optional[Player]
GameMode   = Literal["menu", "human-vs-human", "human-vs-ai"]
GameStatus = Literal["playing", "won", "draw"]

WIN_CASES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
    [1, 5, 9], [3, 5, 7]              # Diagonals
]

# Game Logic Functions
def check_win(board: Dict[int, CellValue], player: Player) -> bool:
    """Check if a player has won the game."""
    return any(all(board[position] == player for position in combo) for combo in WIN_CASES)

def check_draw(board: Dict[int, CellValue]) -> bool:
    """Check if the game is a draw."""
    return all(cell is not None for cell in board.values())

def space_is_free(board: Dict[int, CellValue], position: int) -> bool:
    """Check if a position on the board is free."""
    return board[position] is None

def get_available_moves(board: Dict[int, CellValue]) -> List[int]:
    """Get all available moves on the board."""
    return [i for i in range(1, 10) if space_is_free(board, i)]

def minimax(board: Dict[int, CellValue], is_maximizing: bool, computer: Player = "O", player: Player = "X") -> int:
    """Minimax algorithm for AI decision making."""
    if check_win(board, computer):
        return 1
    elif check_win(board, player):
        return -1
    elif check_draw(board):
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        available_moves = get_available_moves(board)
        
        for move in available_moves:
            board[move] = computer
            score = minimax(board, False, computer, player)
            board[move] = None
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        available_moves = get_available_moves(board)
        
        for move in available_moves:
            board[move] = player
            score = minimax(board, True, computer, player)
            board[move] = None
            best_score = min(score, best_score)
        return best_score

def get_best_move(board: Dict[int, CellValue]) -> Optional[int]:
    """Get the best move for the AI using minimax algorithm."""
    best_score = float('-inf')
    best_move  = None
    computer   = "O"
    player     = "X"
    
    available_moves = get_available_moves(board)
    
    for move in available_moves:
        board[move] = computer
        score = minimax(board, False, computer, player)
        board[move] = None
        
        if score > best_score:
            best_score = score
            best_move  = move
    
    return best_move

# Initialize Session State
def initialize_state():
    """Initialize or reset the game state."""
    if 'game_mode' not in st.session_state:
        st.session_state.game_mode = "menu"
    
    if 'board' not in st.session_state:
        st.session_state.board = {i: None for i in range(1, 10)}
    
    if 'current_player' not in st.session_state:
        st.session_state.current_player = "X"
    
    if 'game_status' not in st.session_state:
        st.session_state.game_status = "playing"
    
    if 'winner' not in st.session_state:
        st.session_state.winner = None
    
    if 'scores' not in st.session_state:
        st.session_state.scores = {"X": 0, "O": 0, "draws": 0}
        
    # Flag to track if we need to process the AI move
    if 'process_ai_move' not in st.session_state:
        st.session_state.process_ai_move = False

def reset_game():
    """Reset the game board and status."""
    st.session_state.board = {i: None for i in range(1, 10)}
    st.session_state.current_player = "X"
    st.session_state.game_status = "playing"
    st.session_state.winner = None
    st.session_state.process_ai_move = False

def back_to_menu():
    """Return to the main menu and reset all game data."""
    st.session_state.game_mode = "menu"
    reset_game()
    st.session_state.scores = {"X": 0, "O": 0, "draws": 0}

# Cell click handler - respond to cell clicks
def handle_cell_click(position):
    """Handle a cell click and make a move."""
    make_move(position)
    
    # If it's now AI's turn, set flag to process AI move
    if (st.session_state.game_mode == "human-vs-ai" and st.session_state.current_player == "O" and st.session_state.game_status == "playing"):
        st.session_state.process_ai_move = True

def make_move(position: int):
    """Make a move and update the game state."""
    # If the cell is already occupied or the game is over, do nothing
    if st.session_state.board[position] is not None or st.session_state.game_status != "playing":
        return
    
    # Update the board with the player's move
    st.session_state.board[position] = st.session_state.current_player
    
    # Check for win or draw
    if check_win(st.session_state.board, st.session_state.current_player):
        st.session_state.game_status = "won"
        st.session_state.winner = st.session_state.current_player
        st.session_state.scores[st.session_state.current_player] += 1
        return
    
    if check_draw(st.session_state.board):
        st.session_state.game_status = "draw"
        st.session_state.scores["draws"] += 1
        return
    
    # Switch player
    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

def get_status_message() -> str:
    """Get the status message based on current game state."""
    if st.session_state.game_status == "won":
        if st.session_state.game_mode == "human-vs-ai":
            return "You Win! 🎉" if st.session_state.winner == "X" else "AI Wins! 🤖"
        return f"Player {st.session_state.winner} Wins! 🏆"
    
    if st.session_state.game_status == "draw":
        return "It's a Draw! 🤝"
    
    if st.session_state.game_mode == "human-vs-ai":
        return "Your Turn" if st.session_state.current_player == "X" else "AI Thinking..."
    
    return f"Player {st.session_state.current_player}'s Turn"

def render_cell(position: int):
    """Render a game cell with appropriate styling."""
    value = st.session_state.board[position]
    
    # Determine the cell class based on its value
    if value == "X":
        cell_class = "cell-x"
        label = "X"
    elif value == "O":
        cell_class = "cell-o"
        label = "O"
    else:
        cell_class = "cell-empty"
        label = " "
    
    # Determine if the button should be disabled
    disabled = (value is not None or (st.session_state.current_player == "O" and st.session_state.game_mode == "human-vs-ai" and st.session_state.game_status == "playing"))
    
    # Create a div with the appropriate class and a button inside
    col_html = f'<div class="{cell_class}">'
    st.markdown(col_html, unsafe_allow_html=True)
    
    if st.button(label, key=f"cell_{position}", use_container_width=True, disabled=disabled):
        make_move(position)
    
    st.markdown('</div>', unsafe_allow_html=True)

def ai_move():
    """Make a move for the AI."""
    if (st.session_state.game_mode == "human-vs-ai" and st.session_state.current_player == "O" and st.session_state.game_status == "playing"):
        
        # Get the best move for the AI
        move = get_best_move(st.session_state.board)
        if move:
            # Update the board with the AI's move
            st.session_state.board[move] = "O"
            
            # Check for win or draw
            if check_win(st.session_state.board, "O"):
                st.session_state.game_status = "won"
                st.session_state.winner = "O"
                st.session_state.scores["O"] += 1
            elif check_draw(st.session_state.board):
                st.session_state.game_status = "draw"
                st.session_state.scores["draws"] += 1
            else:
                # Switch back to the human player
                st.session_state.current_player = "X"
        
        # Reset the process_ai_move flag
        st.session_state.process_ai_move = False

def render_game_board():
    """Render the entire game board using Streamlit columns."""
    # Create a 3x3 grid of buttons
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            position = row * 3 + col + 1
            with cols[col]:
                value = st.session_state.board[position]
                
                # Determine the cell class based on its value
                if value == "X":
                    cell_class = "cell-x"
                    label = "X"
                elif value == "O":
                    cell_class = "cell-o"
                    label = "O"
                else:
                    cell_class = "cell-empty"
                    label = " "
                
                # Determine if the button should be disabled
                disabled = (value is not None or (st.session_state.current_player == "O" and st.session_state.game_mode == "human-vs-ai" and st.session_state.game_status == "playing"))
                
                # Create a div with the appropriate class for styling
                st.markdown(f'<div class="{cell_class}">', unsafe_allow_html=True)
                
                # Create a button for each cell with a unique key
                # The on_click parameter enables single-click response
                st.button(
                    label,
                    key=f"cell_{position}",
                    on_click=handle_cell_click,
                    args=(position,),
                    use_container_width=True,
                    disabled=disabled)
                
                st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main function to render the game UI."""
    # Initialize the game state
    initialize_state()
    
    # Process AI move if needed (this will happen after human click)
    if st.session_state.process_ai_move:
        time.sleep(0.5)  # Small delay for AI "thinking"
        ai_move()
    
    # Display the game title with enhanced styling
    st.markdown('<h1 class="main-title">XO Game Delight</h1>', unsafe_allow_html=True)
    
    # Main Menu Screen
    if st.session_state.game_mode == "menu":
        st.markdown('<p class="game-subtitle">Choose your game mode</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.button("👥 Human vs Human",  key="hvh_button",  on_click=lambda: setattr(st.session_state, 'game_mode', "human-vs-human"), use_container_width=True)
        
        with col2:
            st.button("🤖 Human vs AI",  key="hvai_button",  on_click=lambda: setattr(st.session_state, 'game_mode', "human-vs-ai"), use_container_width=True)
        
        # Reset game when selecting a mode
        if st.session_state.game_mode != "menu":
            reset_game()
    
    # Game Screen
    else:
        # Game mode indicator and back button
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            st.button("← Menu", key="back_button", on_click=back_to_menu)
        
        with col2:
            game_mode_display = "🤖 vs 👤" if st.session_state.game_mode == "human-vs-ai" else "👤 vs 👤"
            st.markdown(f'<div class="centered-text">{game_mode_display}</div>', unsafe_allow_html=True)
        
        # Status message with enhanced styling
        status_class = "game-status"
        if st.session_state.game_status == "won":
            if st.session_state.game_mode == "human-vs-ai":
                status_class += " status-win-human" if st.session_state.winner == "X" else " status-win-ai"
            else:
                status_class += " status-win"
        elif st.session_state.game_status == "draw":
            status_class += " status-draw"
            
        st.markdown(f'<div class="{status_class}"><div class="status-message">{get_status_message()}</div></div>', unsafe_allow_html=True)
        
        # Scores
        score_display = f"""
        <div class="centered-text">
            <span class="badge badge-blue">X: {st.session_state.scores["X"]}</span>
            <span class="badge badge-red">O: {st.session_state.scores["O"]}</span>
            <span class="badge badge-gray">Draws: {st.session_state.scores["draws"]}</span>
        </div>
        """
        st.markdown(score_display, unsafe_allow_html=True)
        
        # Game board - wrapped in a styled container
        st.markdown("<div style='background: linear-gradient(to bottom right, #dbeafe, #ede9fe); padding: 20px; border-radius: 12px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.05); margin: 20px 0;'>", unsafe_allow_html=True)
        render_game_board()
        st.markdown("</div>", unsafe_allow_html=True)
        
        # New Game button
        st.button("🔄 New Game", key="new_game", on_click=reset_game, use_container_width=True)
        
        # The AI moves are now handled by the process_ai_move flag
        # This makes the UX smoother and avoids explicit rerun calls

if __name__ == "__main__":
    main()