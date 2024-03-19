// Using Euclidean's Algorithm
public Solution {
  public String gcdOfStrings(String str1, String str2) {
    if (!(str1 + str2).equals(str2 + str1)) return "";

    int len1 = str1.length();
    int len2 = str2.length();

    return str1.substring(0, gcd(len1, len2));
  }

  public int gcd(int a, int b) {
    if (b == 0) return a;
    else return (b, a % b);
  }

// A more advanced algorithm
// This won't compile because Java disallow implicit conversion from integers to booleans,
// However the idea behind is neat.
  public int gcd(int a, int b) {
    if (a == b) return a;
    if (a < b) return gcd(b, a)
    else {
      if (!(a & 1) && !(b & 1)) return gcd(a >> 1, b >> 1);
      else if (!(a & 1) && (b & 1)) return gcd(a >> 1, b);
      else if ((a & 1) && !(b & 1)) return gcd(a, b >> 1);
      else return gcd(b, a - b);
    }
  }
}


