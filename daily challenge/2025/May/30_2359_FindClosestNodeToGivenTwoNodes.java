class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int n = edges.length;
        int[] dist1 = calcDist(edges, node1);
        int[] dist2 = calcDist(edges, node2);

        int ans = -1, minDist = n;

        for (int i = 0; i < n; i++) {
            if (dist1[i] < 0 || dist2[i] < 0) continue;
            int cand = Math.max(dist1[i], dist2[i]);
            if (cand < minDist) {
                minDist = cand;
                ans = i;
            }
        }

        return ans;
    }

    private int[] calcDist(int[] edges, int node) {
        int n = edges.length;
        int[] ret = new int[n];
        Arrays.fill(ret, -1);
        int curr = node, dist = 0;
        while (curr != -1 && ret[curr] == -1) {
            ret[curr] = dist++;
            curr = edges[curr];
        }
        return ret;
    }
}
