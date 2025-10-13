class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        decoded = ''
        number = ''

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                decoded = ''
                while stack[-1] != '[':
                    ch_popped = stack.pop()
                    decoded = ch_popped + decoded
                stack.pop()
                number = ''
                while stack and stack[-1].isdigit():
                    ch_popped = stack.pop()
                    number = ch_popped + number

                decoded = int(number) * decoded
                stack.append(decoded)
        return ''.join(stack)
