class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let col = board[0].length;
        let row = board.length;

        // Check rows
        for (let i = 0; i < row; i++) {
            let rowSet = new Set();
            for (let j = 0; j < col; j++) {
                if (board[i][j] !== '.' && rowSet.has(board[i][j])) {
                    return false;
                }
                rowSet.add(board[i][j]);
            }
        }

        // Check columns
        for (let j = 0; j < col; j++) {
            let colSet = new Set();
            for (let i = 0; i < row; i++) {
                if (board[i][j] !== '.' && colSet.has(board[i][j])) {
                    return false;
                }
                colSet.add(board[i][j]);
            }
        }

        // Check subgrids (3x3)
        for (let startRow = 0; startRow < row; startRow += 3) {
            for (let startCol = 0; startCol < col; startCol += 3) {
                let subgridSet = new Set();
                for (let i = 0; i < 3; i++) {
                    for (let j = 0; j < 3; j++) {
                        let current = board[startRow + i][startCol + j];
                        if (current !== '.' && subgridSet.has(current)) {
                            return false;
                        }
                        subgridSet.add(current);
                    }
                }
            }
        }

        return true;
    }
}
