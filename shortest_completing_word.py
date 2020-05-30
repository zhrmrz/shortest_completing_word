class Sol:
    def shortest_completing_word(self,arr):
        arr.sort(key=lambda x:len(x))
        ans=arr[0]
        for word in arr:
            if len(word)>len(ans):
                for i,letter in enumerate(word):
                    if letter not in arr[0]:
                        break
                    else:
                        if i==len(word)-1:
                            ans = word
        return ans
if __name__ == '__main__':
    p=Sol()
    print(p.shortest_completing_word(["step", "steps", "stripe", "stepple"]))
    print(p.shortest_completing_word(['sara','stew']))
