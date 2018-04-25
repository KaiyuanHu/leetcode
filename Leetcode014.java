class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length == 0) return "";
        if (strs.length == 1) return strs[0];
        int idx = 0;
        while( idx < strs[0].length()){
            for(int i = 0; i < strs.length-1; i++ ){
                if (idx > strs[i].length()-1 || idx > strs[i + 1].length()-1 || strs[i].charAt(idx) != strs[i+1].charAt(idx)){
                    if (idx == 0){ return "";}
                    else{ return strs[0].substring(0, idx);}
                }
            
            }
            idx++;
        
        }
        return strs[0];  
    }
}
