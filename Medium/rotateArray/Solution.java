public class Solution {
	public void rotate(int[] nums, int k) {
		int len = nums.length;
	        k = k % len;
		rotateHelper(nums, 0 , len-1);
		rotateHelper(nums, 0 , len - k - 1);
		rotateHelper(nums, len - k , len-1);
	}
	public void rotateHelper(int[] nums, int l, int r) {
		while(l <= r) {
			int temp = nums[l];
			nums[l] = nums[r];
			nums[r] = temp;
			l++;
			r--;
		}
	}
}
