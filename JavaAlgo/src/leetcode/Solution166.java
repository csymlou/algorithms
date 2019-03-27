package leetcode;

import java.math.BigDecimal;
import java.math.MathContext;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Fraction to Recurring Decimal
 */
public class Solution166 {
    public String fractionToDecimal(int numerator, int denominator) {
        BigDecimal d = BigDecimal.valueOf(numerator).divide(BigDecimal.valueOf(denominator), new MathContext(100));
        System.out.println(d);
        if (numerator == 0) {
            return "0";
        }
        StringBuilder res = new StringBuilder();
        // "+" or "-"
        res.append(((numerator > 0) ^ (denominator > 0)) ? "-" : "");
        long num = Math.abs((long)numerator);
        long den = Math.abs((long)denominator);

        // integral part
        res.append(num / den);
        num %= den;
        if (num == 0) {
            return res.toString();
        }

        // fractional part
        res.append(".");
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();
        map.put(num, res.length());
        while (num != 0) {
            num *= 10;
            res.append(num / den);
            num %= den;
            if (map.containsKey(num)) {
                int index = map.get(num);
                res.insert(index, "(");
                res.append(")");
                break;
            }
            else {
                map.put(num, res.length());
            }
        }
        return res.toString();
    }

    public static void main(String[] args) {
        Solution166 so = new Solution166();
        String s = so.fractionToDecimal(2, 3);
//        System.out.println(s);
        so.fractionToDecimal(2, 1);
        so.fractionToDecimal(1, 25);
        so.fractionToDecimal(15, 56);
        so.fractionToDecimal(105, 26);
        so.fractionToDecimal(404, 999);
    }
}
