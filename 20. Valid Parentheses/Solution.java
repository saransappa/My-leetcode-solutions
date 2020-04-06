
class Solution {
    public boolean isValid(String s) {
            Stack st = new Stack();
            for(int i=0;i<s.length();i++){
                char ch= s.charAt(i);
                if(ch == '(' || ch == '[' || ch == '{'){
                    st.push(ch);
                }
                else if(ch==')' || ch == ']' || ch == '}'){
                    if(st.empty() || (((char)st.peek() != '(' && ch== ')')|| ((char)st.peek() != '[' && ch == ']')|| ((char)st.peek() != '{' && ch=='}'))){
                        return false;
                    }
                    else{
                        st.pop();
                    }
                }
            }
            if(st.empty()){
                return true;
            }
        return false;
    }
}