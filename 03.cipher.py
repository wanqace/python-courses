#!/usr/bin/env python


class VigenereCipher:
    def __init__(self, key, al):
        self.key, self.al = key, al
        self.key_len, self.al_len = len(key), len(al)

    # d - direction 1 or -1
    def cipher(self, text, d=1):
        print('key: {0}, text: {1}'.format(self.key, text))
        out = ""
        for i, s in enumerate(text):
            if s not in self.al:
                out += s
                continue
            shift = self.al.index(self.key[i % self.key_len])
            out += self.al[(self.al.index(s) +
                            self.al_len + shift * d) % self.al_len]
        return out

    def encode(self, text):
        return self.cipher(text)

    def decode(self, text):
        return self.cipher(text, -1)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

c = VigenereCipher(key, alphabet)

print c.encode('codewars ')  # returns 'rovwsoiv'
print c.decode('laxxhsj')   # returns 'waffles'
