class Solution {
  public String mergeAlternately(String word1, String word2) {
    int minLen = Math.min(word1.length, word2.length);
    StringBuilder sb = new StringBuilder("");

    for (int i = 0; i < minLen; i++) {
      sb.append(word1.charAt(i)).append(word2.charAt(i));
    }

    return sb.append(word1.substring(minLen)).append(word2.substring(minlen)).toString();
  }
}
