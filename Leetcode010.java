// leetcode 10 Regular Expression Matching

class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] f = new boolean[s.length() + 1][p.length() + 1];
        for (int i = 0; i <= s.length(); i++) {
          for (int j = 0; j <= p.length(); j++) {
            f[i][j] = false;
          }
        }
        f[0][0] = true;
        for (int i = 0; i <= s.length(); i++) {
          for (int j = 1; j <= p.length(); j++) {
            if (i > 0 && (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '.')) {
              f[i][j] = f[i - 1][j - 1];
            }
            if (p.charAt(j - 1) == '*') {
              if (i == 0 || (s.charAt(i - 1) != p.charAt(j - 2) && p.charAt(j - 2) != '.')) {
                f[i][j] = f[i][j - 2];
              } else {
                f[i][j] = f[i - 1][j] || f[i][j - 1] || f[i][j - 2];
              }
            }
          }
        }
        return f[s.length()][p.length()];
    }
}
