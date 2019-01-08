import java.util.HashSet;

import javax.swing.tree.TreeNode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isUnivalTree(TreeNode root) {
    	Set<Integer> s = new HashSet<Integer>();
    	
    if(root.isLeaf()) 
    	return true;
    
    for(root:root.child){
    	
    }
    	
        
    }
}