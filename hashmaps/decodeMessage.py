"""
2325 - decode the message
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message."""
class Solution(object):
    def decodeMessage(self, key, message):
        new_alphabet = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_key = key.replace(" ", "")

        used_chars = set()
        decoded_message = ""

        index = 0

        for char in new_key:
            if char not in used_chars:
                new_alphabet[char] = alphabet[index]
                used_chars.add(char)
                index += 1
                if index >= 26:
                    break

        for i in range(len(message)):
            if message[i] == " ":
                decoded_message += " "
            else:
                decoded_message += new_alphabet.get(message[i], message[i])
                
        return decoded_message
