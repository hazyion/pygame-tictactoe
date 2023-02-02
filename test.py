import ttt

game = ttt.TTT()
game.place(4, 1)
game.place(2, 2)
game.place(3, 1)
game.display()
print(game.end(game.state, 1), game.end(game.state, 2))
print(game.lossFunction(game.state, 1))
print(game.lossFunction(game.state, 2))