class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        set <string> s;
        string alpha[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        for(string t : words){
            string p ="";
            for(int i=0;i<t.size();i++){
                p+= alpha[t[i]-'a'];
            }
            s.insert(p);
        }
        return s.size();
    }
};