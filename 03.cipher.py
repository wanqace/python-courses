#!/usr/bin/env python


class VigenereCipher:
    def __init__(self, key, al):
        self.key, self.al = key, al
        self.key_len, self.al_len = len(key), len(al)

    # d - direction 1 or -1
    def cipher(self, text, d=1):
        out, i = "", 0
        for s in text:
            shift = self.al.index(self.key[i % self.key_len])
            out += self.al[(self.al.index(s) + shift * d) % self.al_len]
            i += 1
        return out

    def encode(self, text):
        return self.cipher(text)

    def decode(self, text):
        return self.cipher(text, -1)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

c = VigenereCipher(key, alphabet)

print c.encode('codewars')  # returns 'rovwsoiv'
print c.decode('laxxhsj')   # returns 'waffles'
