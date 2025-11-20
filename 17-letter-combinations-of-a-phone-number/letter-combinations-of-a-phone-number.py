class Solution:
    
    def add_digits(self,digits):
        if len(digits)>1:
            self.add_digits(digits[1:])
        else:
            for c in self.s_map[int(digits)]:
                self.out.append(c)
            return
        digit = int(digits[0])
        new_out = []
        for out in self.out:
            for c in self.s_map[digit]:
                print(c)
                new_out.append(c+out)
        self.out = new_out

    def letterCombinations(self, digits: str) -> List[str]:
        self.s_map = {2: ["a","b","c"], 3: ["d","e","f"], 4:["g","h","i"], 5: ["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}

        self.out = []
        self.add_digits(digits)
        return self.out
