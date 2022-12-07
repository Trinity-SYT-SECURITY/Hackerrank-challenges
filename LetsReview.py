for test in range(int(input())):
    s = input()
    even = [s[i] for i in range(len(s)) if i % 2 == 0]
    odd = [s[i] for i in range(len(s)) if i % 2 != 0]
    print("".join(even), "".join(odd))  # "" 字與字中間不插入任何咚咚，.join將even符合條件的輸出
