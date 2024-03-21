// Original solution, really stupid
class Solution {
  public String reverseVowels(String s) {
    StringBuilder vowels = new StringBuilder();
    char[] chr = s.toCharArray();
    for (int i = chr.length - 1; i >= 0; i--) {
      if ((chr[i] == 'a') || (chr[i] == 'e') || (chr[i] == 'i') || (chr[i] == 'o') || (chr[i] == 'u')
          || (chr[i] == 'A') || (chr[i] == 'E') || (chr[i] == 'I') || (chr[i] == 'O') || (chr[i] == 'U')) {

        vowels.append(chr[i]);
      }
    }

    int index = 0;
    String vowelString = vowels.toString();

    for (int i = 0; i < chr.length; i++) {
      if ((chr[i] == 'a') || (chr[i] == 'e') || (chr[i] == 'i') || (chr[i] == 'o') || (chr[i] == 'u')
          || (chr[i] == 'A') || (chr[i] == 'E') || (chr[i] == 'I') || (chr[i] == 'O') || (chr[i] == 'U')) {
        chr[i] = vowels.charAt(index);
        index++;
      }
    }
    String ret = new String(chr);
    return ret;
  }
}

// Using double pointers
