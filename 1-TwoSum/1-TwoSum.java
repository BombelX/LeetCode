// Last updated: 23.04.2026, 15:39:39
1class Solution {
2    public int[] twoSum(int[] nums, int target) {
3        Map<Integer,Integer> comps = new HashMap<>();
4
5        for(int i = 0;i<nums.length ;i++){
6            
7            int comp = target - nums[i];
8            if (comps.containsKey(comp)){
9                return new int[]{comps.get(comp), i};
10            }
11            comps.put(nums[i], i);
12            
13        }
14
15        return new int[0];
16
17    }
18}