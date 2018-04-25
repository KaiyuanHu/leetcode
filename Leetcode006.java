// leetcode 06 ZigZag Conversion

class Solution {
    public String convert(String s, int numRows) {
        if(numRows<=1)return s;
        String[] result = new String[numRows];

        for(int i = 0; i < numRows; i++){
            result[i] = "";
        }
        int step = 0, indicate = 0;

        for (int i = 0; i<s.length(); i++){
            result[step] += s.charAt(i);
            if(step == 0){indicate = 1 ;}
            if(step == (numRows - 1)){indicate = -1; }
            step += indicate;
        }

        String final_result = "";

        for(int i = 0; i < numRows; i++){
            final_result += result[i];
        }

        return final_result;
    }
}
