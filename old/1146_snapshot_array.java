import java.util.TreeMap;

class SnapshotArray {
    int snap_cnt = 0;
    TreeMap<Integer, Integer>[] historyRecords;

    public SnapshotArray(int length) {
        historyRecords = new TreeMap[length];
        for (int i = 0; i < length; i++) {
            historyRecords[i] = new TreeMap<>();
            historyRecords[i].put(0, 0);
        }
    }

    public void set(int index, int val) {
        historyRecords[index].push(snap_id, val);
    }

    public int snap() {
        return snap_cnt++;
    }

    public int get(int index, int snap_id) {
        return historyRecords[index].floorEntry(snap_cnt).getValue();
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */

