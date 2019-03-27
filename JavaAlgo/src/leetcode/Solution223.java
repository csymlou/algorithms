package leetcode;

/**
 * Rectangle Area
 */
public class Solution223 {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int ac = Math.abs(A-C);
        int eg = Math.abs(E-G);
        int ag = Math.max(Math.abs(A-G), Math.abs(E-C));
        int s  = Math.max(ac+eg-ag, 0);
        int bd = Math.abs(B-D);
        int fh = Math.abs(F-H);
        int df = Math.max(Math.abs(D-F), Math.abs(B-H));
        int t  = Math.max(bd+fh-df, 0);
        int s1 = ac * bd;
        int s2 = eg * fh;
        if(s1 == 0) return s2;
        if(s2 == 0) return s1;
        return s1 + s2 - s * t;
    }

    public static void main(String[] args) {
        int[] a ={3,0,1};
        System.out.println(new Solution223().computeArea(-2,-2,2,2,-1,-1,1,1));
    }
}
