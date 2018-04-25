class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> ro = new HashMap<Character, Integer>();
        ro.put('M', 1000);
        ro.put('D', 500);
        ro.put('C', 100);
        ro.put('L', 50);
        ro.put('X', 10);
        ro.put('V', 5);
        ro.put('I', 1);
        int result = 0;
        for(int i = 0; i < s.length(); i++){
            if(i != s.length()-1 && (ro.get(s.charAt(i))) < ro.get(s.charAt(i+1))){
                result -= ro.get(s.charAt(i));
            }else{
                result += ro.get(s.charAt(i));
            }
        }
        
        return result;
        
    }
}
