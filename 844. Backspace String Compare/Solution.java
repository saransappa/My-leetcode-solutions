import java.util.*;
class Solution {
    public boolean backspaceCompare(String S, String T) {
        Stack s = new Stack();
        Stack t = new Stack();
        for(int i=0;i<S.length();i++){
            char ch = S.charAt(i);
            if(ch!= '#'){
                s.push(ch);
            }
            else if(!s.empty()){
                s.pop();
            }
        }
        for(int i=0;i<T.length();i++){
            char ch = T.charAt(i);
            if(ch!= '#'){
                t.push(ch);
            }
            else if(!t.empty()){
                t.pop();
            }
        }
        String s1 = "";
        while(!s.empty()){
            s1=s1+s.pop();
        }
        String s2 = "";
        while(!t.empty()){
            s2=s2+t.pop();
        }
        if(s1.length()!=s2.length()){
            return false;
        }
        else{
            for(int i=0;i<s1.length();i++){
                if(s1.charAt(i)!=s2.charAt(i)){
                    return false;
                }
            }
            return true;
        }
    }
}