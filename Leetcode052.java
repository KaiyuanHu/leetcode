// Leetcode 52 N-Queens II

class Solution {
    private int result = 0;

    public int totalNQueens(int n) {
        boolean[] col_check = new boolean[n];
        boolean[] diag_check =  new boolean[2*n];
        boolean[] anti_diag_check = new boolean[2*n];
        solver(0, col_check, diag_check, anti_diag_check);
        return result;

    }

    private void solver(int row, boolean[] col_check, boolean[] diag_check, boolean[] anti_diag_check){
        if(row == col_check.length){
            result++;
        }else{
            for(int i=0;i<col_check.length;i++){
                if(col_check[i]  || diag_check[col_check.length-(row - i)] || anti_diag_check[row + i]) continue;
                col_check[i] = true;
                diag_check[col_check.length-(row - i)] = true;
                anti_diag_check[row + i] = true;
                solver(row+1, col_check, diag_check, anti_diag_check);
                col_check[i] = false;
                diag_check[col_check.length-(row - i)] = false;
                anti_diag_check[row + i] = false;
            }
        }
    }
}
