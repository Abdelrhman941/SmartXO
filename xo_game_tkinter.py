import tkinter as tk
from tkinter import ttk, messagebox
import time
from typing import Dict, List, Optional, Literal

class XOGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XO Game Delight")
        self.root.geometry("700x800")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(True, True)
        self.root.minsize(500, 600)
        
        # Game state
        self.board = {i: '' for i in range(1, 10)}
        self.current_player = 'X'
        self.game_mode = 'human_vs_human'  # 'human_vs_human' or 'human_vs_ai'
        self.player_symbol = 'X'
        self.ai_symbol = 'O'
        self.game_active = True
        
        # Score tracking
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        
        # Win cases
        self.win_cases = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
            (1, 5, 9), (3, 5, 7)              # Diagonals
        ]
        
        # UI Components
        self.buttons = {}
        self.score_labels = {}
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="XO Game Delight", 
            font=('Arial', 28, 'bold'),
            bg='#1a1a1a',
            fg='#ffffff'
        )
        title_label.pack(pady=(10, 20))
        
        # Game mode selection
        self.setup_mode_selection(main_frame)
        
        # Score display
        self.setup_score_display(main_frame)
        
        # Game board
        self.setup_game_board(main_frame)
        
        # Control buttons
        self.setup_control_buttons(main_frame)
        
    def setup_mode_selection(self, parent):
        """Set up game mode selection"""
        mode_frame = tk.Frame(parent, bg='#1a1a1a')
        mode_frame.pack(pady=10)
        
        tk.Label(
            mode_frame, 
            text="Select Game Mode:", 
            font=('Arial', 14, 'bold'),
            bg='#1a1a1a',
            fg='#ffffff'
        ).pack(pady=5)
        
        button_frame = tk.Frame(mode_frame, bg='#1a1a1a')
        button_frame.pack()
        
        # Human vs Human button
        self.hvh_button = tk.Button(
            button_frame,
            text="Human vs Human",
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=10,
            relief='raised',
            command=lambda: self.set_game_mode('human_vs_human')
        )
        self.hvh_button.pack(side='left', padx=5)
        
        # Human vs AI button
        self.hvai_button = tk.Button(
            button_frame,
            text="Human vs AI",
            font=('Arial', 12, 'bold'),
            bg='#2196F3',
            fg='white',
            padx=20,
            pady=10,
            relief='flat',
            command=lambda: self.set_game_mode('human_vs_ai')
        )
        self.hvai_button.pack(side='left', padx=5)
        
    def setup_score_display(self, parent):
        """Set up score display"""
        score_frame = tk.Frame(parent, bg='#1a1a1a')
        score_frame.pack(pady=15)
        
        tk.Label(
            score_frame, 
            text="Score Board", 
            font=('Arial', 16, 'bold'),
            bg='#1a1a1a',
            fg='#ffffff'
        ).pack(pady=(0, 10))
        
        scores_container = tk.Frame(score_frame, bg='#1a1a1a')
        scores_container.pack()
        
        # X wins
        x_frame = tk.Frame(scores_container, bg='#dc3545', relief='raised', bd=2)
        x_frame.pack(side='left', padx=10, pady=5)
        tk.Label(x_frame, text="X Wins", font=('Arial', 12, 'bold'), bg='#dc3545', fg='white').pack(pady=5)
        self.score_labels['X'] = tk.Label(x_frame, text="0", font=('Arial', 18, 'bold'), bg='#dc3545', fg='white')
        self.score_labels['X'].pack(pady=2)
        
        # Draws
        draw_frame = tk.Frame(scores_container, bg='#ffc107', relief='raised', bd=2)
        draw_frame.pack(side='left', padx=10, pady=5)
        tk.Label(draw_frame, text="Draws", font=('Arial', 12, 'bold'), bg='#ffc107', fg='black').pack(pady=5)
        self.score_labels['Draw'] = tk.Label(draw_frame, text="0", font=('Arial', 18, 'bold'), bg='#ffc107', fg='black')
        self.score_labels['Draw'].pack(pady=2)
        
        # O wins
        o_frame = tk.Frame(scores_container, bg='#007bff', relief='raised', bd=2)
        o_frame.pack(side='left', padx=10, pady=5)
        tk.Label(o_frame, text="O Wins", font=('Arial', 12, 'bold'), bg='#007bff', fg='white').pack(pady=5)
        self.score_labels['O'] = tk.Label(o_frame, text="0", font=('Arial', 18, 'bold'), bg='#007bff', fg='white')
        self.score_labels['O'].pack(pady=2)
        
    def setup_game_board(self, parent):
        """Set up the 3x3 game board"""
        board_frame = tk.Frame(parent, bg='#1a1a1a')
        board_frame.pack(pady=20, expand=True)
        
        # Current player indicator
        self.player_indicator = tk.Label(
            board_frame,
            text=f"Current Player: {self.current_player}",
            font=('Arial', 16, 'bold'),
            bg='#1a1a1a',
            fg='#ffffff'
        )
        self.player_indicator.pack(pady=(0, 15))
        
        # Game grid
        grid_frame = tk.Frame(board_frame, bg='#2d2d2d')
        grid_frame.pack(expand=True)
        
        # Configure grid weights for responsive design
        for i in range(3):
            grid_frame.grid_rowconfigure(i, weight=1)
            grid_frame.grid_columnconfigure(i, weight=1)
        
        for i in range(3):
            for j in range(3):
                position = i * 3 + j + 1
                button = tk.Button(
                    grid_frame,
                    text="",
                    font=('Arial', 28, 'bold'),
                    width=5,
                    height=2,
                    bg='#404040',
                    fg='#ffffff',
                    activebackground='#505050',
                    activeforeground='#ffffff',
                    relief='raised',
                    bd=3,
                    command=lambda pos=position: self.make_move(pos)
                )
                button.grid(row=i, column=j, padx=3, pady=3, sticky='nsew')
                self.buttons[position] = button
                
                # Add hover effects
                button.bind("<Enter>", lambda e, btn=button: self.on_button_hover(btn, True))
                button.bind("<Leave>", lambda e, btn=button: self.on_button_hover(btn, False))
                
    def setup_control_buttons(self, parent):
        """Set up control buttons"""
        control_frame = tk.Frame(parent, bg='#1a1a1a')
        control_frame.pack(pady=20)
        
        # New Game button
        new_game_btn = tk.Button(
            control_frame,
            text="New Game",
            font=('Arial', 14, 'bold'),
            bg='#FF9800',
            fg='white',
            activebackground='#e68900',
            activeforeground='white',
            padx=25,
            pady=12,
            relief='raised',
            command=self.new_game
        )
        new_game_btn.pack(side='left', padx=10)
        
        # Reset Scores button
        reset_scores_btn = tk.Button(
            control_frame,
            text="Reset Scores",
            font=('Arial', 14, 'bold'),
            bg='#9C27B0',
            fg='white',
            activebackground='#8e24aa',
            activeforeground='white',
            padx=25,
            pady=12,
            relief='raised',
            command=self.reset_scores
        )
        reset_scores_btn.pack(side='left', padx=10)
        
    def on_button_hover(self, button, entering):
        """Handle button hover effects"""
        if button['text'] == '' and self.game_active:
            if entering:
                button.configure(bg='#555555', relief='sunken')
            else:
                button.configure(bg='#404040', relief='raised')
                
    def set_game_mode(self, mode):
        """Set the game mode"""
        self.game_mode = mode
        if mode == 'human_vs_human':
            self.hvh_button.configure(relief='raised', bg='#4CAF50')
            self.hvai_button.configure(relief='flat', bg='#2196F3')
        else:
            self.hvh_button.configure(relief='flat', bg='#4CAF50')
            self.hvai_button.configure(relief='raised', bg='#2196F3')
        
        self.new_game()
        
    def make_move(self, position):
        """Handle player move"""
        if not self.game_active or self.board[position] != '':
            return
            
        # Make the move
        self.board[position] = self.current_player
        self.buttons[position].configure(
            text=self.current_player,
            bg='#dc3545' if self.current_player == 'X' else '#007bff',
            fg='white',
            relief='sunken'
        )
        
        # Check for game end
        if self.check_win(self.current_player):
            self.end_game(f"Player {self.current_player} wins!")
            self.scores[self.current_player] += 1
            self.update_scores()
            return
        elif self.check_draw():
            self.end_game("It's a draw!")
            self.scores['Draw'] += 1
            self.update_scores()
            return
            
        # Switch player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_player_indicator()
        
        # AI move if in AI mode
        if self.game_mode == 'human_vs_ai' and self.current_player == self.ai_symbol:
            self.root.after(500, self.ai_move)  # Small delay for better UX
            
    def ai_move(self):
        """Make AI move using minimax algorithm"""
        if not self.game_active:
            return
            
        best_score = -float('inf')
        best_move = None
        
        for position in range(1, 10):
            if self.board[position] == '':
                # Try this move
                self.board[position] = self.ai_symbol
                score = self.minimax(self.board, False, -float('inf'), float('inf'))
                self.board[position] = ''
                
                if score > best_score:
                    best_score = score
                    best_move = position
                    
        if best_move:
            self.make_move(best_move)
            
    def minimax(self, board, is_maximizing, alpha, beta):
        """Minimax algorithm with alpha-beta pruning"""
        if self.check_win(self.ai_symbol):
            return 1
        elif self.check_win(self.player_symbol):
            return -1
        elif self.check_draw():
            return 0
            
        if is_maximizing:
            max_score = -float('inf')
            for position in range(1, 10):
                if board[position] == '':
                    board[position] = self.ai_symbol
                    score = self.minimax(board, False, alpha, beta)
                    board[position] = ''
                    max_score = max(score, max_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return max_score
        else:
            min_score = float('inf')
            for position in range(1, 10):
                if board[position] == '':
                    board[position] = self.player_symbol
                    score = self.minimax(board, True, alpha, beta)
                    board[position] = ''
                    min_score = min(score, min_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return min_score
            
    def check_win(self, player):
        """Check if a player has won"""
        for case in self.win_cases:
            if all(self.board[pos] == player for pos in case):
                return True
        return False
        
    def check_draw(self):
        """Check if the game is a draw"""
        return all(self.board[pos] != '' for pos in range(1, 10))
        
    def end_game(self, message):
        """End the game and show result"""
        self.game_active = False
        
        # Highlight winning combination
        self.highlight_winner()
        
        # Show message after a short delay
        self.root.after(1000, lambda: messagebox.showinfo("Game Over", message))
        
    def highlight_winner(self):
        """Highlight winning combination"""
        for case in self.win_cases:
            if all(self.board[pos] != '' and self.board[pos] == self.board[case[0]] for pos in case):
                for pos in case:
                    self.buttons[pos].configure(bg='#28a745', fg='white')
                break
                
    def update_player_indicator(self):
        """Update current player indicator"""
        mode_text = "AI's turn" if (self.game_mode == 'human_vs_ai' and 
                                   self.current_player == self.ai_symbol) else f"Player {self.current_player}'s turn"
        self.player_indicator.configure(text=f"Current Turn: {mode_text}")
        
    def update_scores(self):
        """Update score display"""
        for key, label in self.score_labels.items():
            label.configure(text=str(self.scores[key]))
            
    def new_game(self):
        """Start a new game"""
        self.board = {i: '' for i in range(1, 10)}
        self.current_player = 'X'
        self.game_active = True
        
        # Reset board buttons
        for button in self.buttons.values():
            button.configure(text='', bg='#404040', fg='#ffffff', relief='raised')
            
        self.update_player_indicator()
        
    def reset_scores(self):
        """Reset all scores"""
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        self.update_scores()
        
    def run(self):
        """Start the game"""
        self.root.mainloop()

if __name__ == "__main__":
    game = XOGame()
    game.run()