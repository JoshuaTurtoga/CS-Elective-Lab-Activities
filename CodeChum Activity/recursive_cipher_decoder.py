def recursive_cipher_decoder(s):
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    while True:
        i = 0
        new_s = ""
        while i < len(s):
            if i + 1 < len(s) and s[i] in charset and s[i + 1].isdigit():
                c = s[i]
                d = int(s[i + 1])
                pos = charset.index(c)

                new_pos = (pos - d) % 36
                new_s += charset[new_pos]
                i += 2
            else:
                new_s += s[i]
                i += 1

        if new_s == s or not any(ch.isdigit() for ch in new_s):
            return new_s
        s = new_s


print("Enter string:", end=" ")
s = input().strip()
print("Result:", recursive_cipher_decoder(s))
