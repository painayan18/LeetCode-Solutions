def main():
    s1 = "3[a]2[bc]"
    s2 = "3[a2[c]]"
    s3 = "2[abc]3[cd]ef"

    print("input:", s1, "output:", decode_string(s1))
    print("input:", s2, "output:", decode_string(s2))
    print("input:", s3, "output:", decode_string(s3))


def decode_string(s: str) -> str:
    stack = []
    current_str = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)

        elif char == "[":
            stack.append(current_num)
            stack.append(current_str)
            current_num = 0
            current_str = ""

        elif char == "]":
            prev_str = stack.pop()
            prev_num = stack.pop()
            current_str = prev_str + current_str * prev_num

        else:
            current_str += char

    while stack:
        current_str = stack.pop() + current_str

    return current_str


main()




















