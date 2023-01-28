import tkinter as tk

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic-Tac-Toe")

        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(self, width=5, height=2, command=lambda row=i, col=j: self.button_clicked(row, col))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)

        self.player = "X"
        self.game_over = False

    def button_clicked(self, row, col):
        if self.game_over or self.buttons[row][col]['text'] != "":
            return

        self.buttons[row][col].config(text=self.player)
        self.check_game_over()
        self.player = "0" if self.player == "X" else "X"

    def check_game_over(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                self.game_over = True
                self.end_game(self.buttons[i][0]['text'])
                return
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                self.game_over = True
                self.end_game(self.buttons[0][i]['text'])
                return
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.game_over = True
            self.end_game(self.buttons[0][0]['text'])
            return
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.game_over = True
            self.end_game(self.buttons[0][2]['text'])
            return
        if all(self.buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
            self.game_over = True
            self.end_game("Tie")

    def end_game(self, winner):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)
                message = tk.Label(self, text="Player-{} wins!".format(winner))
        message.grid(row=3, column=0, columnspan=3)

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()