public class Codec {
    public String encode(List<String> strs) {
        if (strs.isEmpty()) return Character.toString((char)258);
        StringBuilder sb = new StringBuilder();
        for (String s: strs) {
            sb.append(s);
            sb.append(Character.toString((char)257));
        }
        sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }

    public List<String> decode(String s) {
        if (s.equals(Character.toString((char)258))) return new ArrayList();
        return Arrays.asList(s.split(Character.toString((char)257), -1));
    }
}
