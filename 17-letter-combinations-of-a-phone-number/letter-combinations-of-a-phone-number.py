class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        s_map = {2: ["a","b","c"], 3: ["d","e","f"], 4:["g","h","i"], 5: ["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        ans = []
        def backtrack(digits, cur_word, start_idx):
            if start_idx > len(digits):
                return
            if start_idx == len(digits):
                ans.append(cur_word)
                return
            
            for letter in s_map[int(digits[start_idx])]:
                cur_word+=letter
                backtrack(digits, cur_word, start_idx + 1)
                cur_word = cur_word[:len(cur_word)-1]
        
        backtrack(digits, "", 0)
        return ans
