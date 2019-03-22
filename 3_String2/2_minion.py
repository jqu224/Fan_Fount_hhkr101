Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

Sample Input 
  BANANA
Sample Output
  Stuart 12

--------------------------------------------------


def minion_game(string):
    # your code goes here
    string = string.upper()
    stu = 0
    kev = 0
    len_s = len(string)
#     这题意思是，
# 数一下 元音开头的子string：substring有几个，
#  再数一下 辅音开头的子string有几个

# 譬如：
# baxep
# b: 辅音 kev 有 0 + baxep + baxe + bax + ba 和 b = 5
# a: 元音 stu 有 0 + axep + axe + ax + a = 4
# x: 辅音 stu 有 5 + xep + xe + x = 3
# e: 元音 stu 有 4 + ep + e = 6
# p: 辅音 kev 有 8 + p = 9
#   辅音多，kev == 9
    for i, char in enumerate(string):
        if char in "AEIOU":
            kev += len_s - i
        else:
            stu += len_s - i
    # mind the capital letters: K and S
    if stu > kev:
        print("Stuart "+str(stu))
    elif kev == stu:
        print("Draw")
    else:
        print("Kevin "+str(kev)) 

        ########################    
        # solution b 
        # time limit reached, which means it didnt work as requested
        # string = string.upper()
        # dict_consonants = {}
        # dict_vowels = {}
        # len_s = len(string)
        # for i, char in enumerate(string):
        # if char in "AEIOU":
        #     for j, _ in enumerate(string[::-1]):
        #         if string[i:i+j+1] in dict_vowels:
        #             dict_vowels[string[i:i+j+1]] += 1
        #         else:
        #             dict_vowels[string[i:i+j+1]] = 1 
        # else:
        #     for j, _ in enumerate(string[::-1]):
        #         if string[i:i+j+1] in dict_consonants:
        #             dict_consonants[string[i:i+j+1]] += 1
        #         else:
        #             dict_consonants[string[i:i+j+1]] = 1
        # # mind the capital letters: K and S
        # if sum(dict_consonants.values()) > sum(dict_vowels.values()):
        #     print("Stuart "+str(sum(dict_consonants.values())))
        # elif sum(dict_consonants.values()) == sum(dict_vowels.values()):
        #     print("Draw")
        # else:
        #     print("Kevin "+str(sum(dict_vowels.values())))




if __name__ == '__main__':
    s = input()
    minion_game(s)
