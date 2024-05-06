// Hashmap solution
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>>  hashmap = new HashMap<>();
        for (String str: strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String strSorted = new String(chars);
            if (hashmap.containsKey(strSorted)) {
                hashmap.get(strSorted).add(str);
            } else {
                ArrayList<String> strings = new ArrayList<>();
                strings.add(str);
                hashmap.put(strSorted, strings);
            }
        }
        List<List<String>> ret = new ArrayList<>(hashmap.values());
        return ret;
    }
}

// A more concise way to write
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> m = new HashMap<>();
        for (String str: strs) {
            char[] s = str.toCharArray();
            Arrays.sort(s);
            m.computeIfAbsent(new String(s), k -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(m.values());
    }
}
