// Leetcode 51 N-Queens

class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        int[] position = new int[n];
        for(int i=0;i<n;i++) position[i] = -1;
        solver(result, 0, position);
        return result;
    }

    private boolean isValid(int[] position, int row, int col){
        for(int i=0;i<row;i++){
            if(position[i] == col || Math.abs(i-row) == Math.abs(col-position[i])){
                return false;
            }
        }
        return true;
    }

    private void solver(List<List<String>> result, int row, int[] position){
        int n = position.length;
        if(row == n){
            List<String> temp = new ArrayList<>();
            for(int i=0;i<n;i++){
                StringBuilder sb = new StringBuilder();
                for(int j=0;j<n;j++){sb.append('.');}
                sb.setCharAt(position[i], 'Q');
                temp.add(sb.toString());
            }
            result.add(new ArrayList<String>(temp));
        }else{
            for(int i=0;i<n;i++){
                if(isValid(position, row, i)){
                    position[row] = i;
                    solver(result, row+1, position);
                    position[row] = -1;
                }
            }
        }
    }

}
