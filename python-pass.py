

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        palindromic = ''

        # loop through the input string
        for i in range(len(s)):

            # loop backwards through the input string
            for j in range(len(s), i, -1):

                # Break if out of range
                if len(palindromic) >= j-i:
                    break

                # Update variable if matches
                elif s[i:j] == s[i:j][::-1]:
                    palindromic = s[i:j]
                    break

        return palindromic


# test command: 
print(Solution.longest_palindromic('babad')) # >> bab
print(Solution.longest_palindromic('cbbd'))  # >> bb
print(Solution.longest_palindromic('a'))     # >> a
print(Solution.longest_palindromic('ac'))    # >> a



