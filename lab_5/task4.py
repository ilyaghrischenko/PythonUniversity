chessboard = [["_"] * 8 for _ in range(8)]

chessboard[0][0] = "R"
chessboard[0][7] = "R"
chessboard[7][0] = "R"
chessboard[7][7] = "R"

for row in chessboard:
    print(" ".join(row))
