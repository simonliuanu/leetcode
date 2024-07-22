// Official solution
class Solution {
    public int maximumDetonation(int[][] bombs) {
        int n = bombs.length;
        Map<Integer, List<Integer>> edges = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && isConnected(bombs, i, j)) {
                    edges.putIfAbsent(i, new ArrayList<Integer>());
                    edges.get(i).add(j);
                }
            }
        }
        int ret = 0;
        for (int i = 0; i < n; i++) {
            boolean[] visited = new boolean[n];
            int cnt = 1;
            Queue<Integer> queue = new ArrayDeque<Integer>();
            queue.offer(i);
            visited[i] = true;
            while(!queue.isEmpty()) {
                int current = queue.poll();
                for (int next : edges.getOrDefault(current, new ArrayList<Integer>())) {
                    if (visited[next]) continue;
                    cnt++;
                    queue.offer(next);
                    visited[next] = true;
                }
            }
            ret = Math.max(ret, cnt);
        }
        return ret;
    }

    public boolean isConnected(int[][] arr, int u, int v) {
        long dx = arr[u][0] - arr[v][0];
        long dy = arr[u][1] - arr[v][1];
        return (long) arr[u][2] * arr[u][2] >= dx * dx + dy * dy;
    }
}
