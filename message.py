class TransmitMessage:
    def __init__(self,destination_kingdom,encrypted_message):
        self.deciphered_message = self.decipher_message(destination_kingdom,encrypted_message)

    def decipher_message(self,destination_kingdom,encrypted_message):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        decrypted_message = []
        for curr_char in encrypted_message:
            curr_index = alphabet.find(curr_char)
            curr_decoded_char = alphabet[ curr_index - destination_kingdom.cipher_key]
            decrypted_message.append(curr_decoded_char)
        return ''.join(decrypted_message)