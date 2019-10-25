import java.util.Stack;
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack();
        for(String ch : tokens){
            if(!ch.equals("+") && !ch.equals("-") && !ch.equals("*") && !ch.equals("/")){
                s.push(Integer.parseInt(ch));
            }
            else if(ch.equals("+")){
                int k = s.pop();
                int l = s.pop();
                s.push(k+l);
            }
            else if(ch.equals("-")){
                int k = (int)s.pop();
                int l = (int)s.pop();
                s.push(l-k);
            }
            else if(ch.equals("*")){
                int k = (int)s.pop();
                int l = (int)s.pop();
                s.push(k*l);
            }
            else if(ch.equals("/")){
                int k = (int)s.pop();
                int l = (int)s.pop();
                s.push(l/k);
            }
        }
        return s.pop();
    }
}