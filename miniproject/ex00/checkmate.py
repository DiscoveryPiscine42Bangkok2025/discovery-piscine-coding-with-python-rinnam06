def checkmate(board_str: str):

    rows = board_str.splitlines()
    board = [list(row.upper()) for row in rows]
    size = len(board)

    # เช็คว่าเป็นกระดานจตุรัสมั้ย
    for row in board:
        if len(row) != size:
            print("Fail")
            print("Board must be square")
            return
    
    # เช็คว่ากระดานต้องไม่ว่าง
    has_piece = any(cell != "." for row in board for cell in row)
    if not has_piece:
        print("Fail")
        print("Board must not be empty")
        return

    # เช็คว่าตัวอักษรถูกต้อง
    valid_chars = {"P", "B", "R", "Q", "K", "."}
    for row in board:
        for cell in row:
            if cell not in valid_chars:
                print("Fail")
                print(f"Invalid character found: '{cell}'")
                return

    # หา King
    king_positions = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == "K":
                king_positions.append((i, j))

    if len(king_positions) == 0:
        print("Fail")
        print("King not found")
        return
    elif len(king_positions) > 1:
        print("Fail")
        print("Multiple Kings found")
        return

    kx, ky = king_positions[0]
    # เช็ค Pawn
    pawn_moves = [(1, -1), (1, 1)]
    for dx, dy in pawn_moves:
        x = kx + dx
        y = ky + dy
        if 0 <= x < size and 0 <= y < size:
            if board[x][y] == "P":
                print("Success")
                return

    # เช็ค Bishop / Queen (ทแยง)
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in diagonal_dirs:
        x = kx + dx
        y = ky + dy
        while 0 <= x < size and 0 <= y < size:
            if board[x][y] != ".":
                if board[x][y] in ["B", "Q"]:
                    print("Success")
                    return
                else:
                    break
            x += dx
            y += dy

    # เช็ค Rook / Queen (ตรง)
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in straight_dirs:
        x = kx + dx
        y = ky + dy
        while 0 <= x < size and 0 <= y < size:
            if board[x][y] != ".":
                if board[x][y] in ["R", "Q"]:
                    print("Success")
                    return
                else:
                    break
            x += dx
            y += dy

    # ถ้าไม่มีตัวไหนโจมตีได้
    print("Fail")