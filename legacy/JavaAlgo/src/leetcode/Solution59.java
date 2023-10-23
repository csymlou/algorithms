package leetcode;

import java.util.Arrays;

/**
 * Spiral Matrix II
 */
public class Solution59 {

    public int[][] generateMatrix(int n) {
        Walker walker = new Walker(n);
        while (walker.walk()) {
        }
        return walker.flip();
    }

    public static void main(String[] args) {
        int[][] m = new Solution59().generateMatrix(10);
        for (int[] row : m) {
            System.out.println(Arrays.toString(row));
        }
    }


    static class Walker {
        enum Direction {EAST, SOUTH, WEST, NORTH}

        private int n;
        private int[][] matrix;
        private int x, y;
        private int num = 1;
        private Direction cur = Direction.EAST;

        public Walker(int n) {
            this.n = n;
            matrix = new int[n][n];
            x = y = 0;
        }

        public Direction next() {
            if (cur == Direction.EAST) {
                if (check(x + 1, y)) return Direction.EAST;
                else if (check(x, y + 1)) return Direction.SOUTH;
            } else if (cur == Direction.SOUTH) {
                if (check(x, y + 1)) return Direction.SOUTH;
                else if (check(x - 1, y)) return Direction.WEST;
            } else if (cur == Direction.WEST) {
                if (check(x - 1, y)) return Direction.WEST;
                else if (check(x, y - 1)) return Direction.NORTH;
            } else if (cur == Direction.NORTH) {
                if (check(x, y - 1)) return Direction.NORTH;
                else if (check(x + 1, y)) return Direction.EAST;
            }
            return null;
        }

        public boolean walk() {
            matrix[x][y] = num++;
            Direction next = next();
            if (next == null) return false;
            switch (next) {
                case EAST:
                    x++;
                    break;
                case SOUTH:
                    y++;
                    break;
                case WEST:
                    x--;
                    break;
                case NORTH:
                    y--;
                    break;
            }
            if (check(x, y)) {
                cur = next;
                return true;
            } else {
                return false;
            }
        }

        private boolean check(int x, int y) {
            return 0 <= x && x < n && 0 <= y && y < n && matrix[x][y] == 0;
        }

        public int[][] flip() {
            for (int i = 0; i < n; i++) {
                for (int j = i; j < n; j++) {
                    int t = matrix[j][i];
                    matrix[j][i] = matrix[i][j];
                    matrix[i][j] = t;
                }
            }
            return matrix;
        }

        public void print() {
            for (int[] row : matrix) {
                System.out.println(Arrays.toString(row));
            }
        }
    }

}
