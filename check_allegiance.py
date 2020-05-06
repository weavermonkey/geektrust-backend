class CheckAllegiance:
    def __init__(self,destination_kingdom,decrypted_message):
        self.required_counts = self.character_count(destination_kingdom.emblem)
        self.actual_counts = self.character_count(decrypted_message)
        if self.compare_counts(self.actual_counts,self.required_counts):
            destination_kingdom.is_ally = True

    def character_count(self,decrypted_message):
        character_count = {}
        for curr_char in decrypted_message:
            if curr_char in character_count:
                character_count[curr_char] += 1
            else:
                character_count[curr_char] = 1
        return character_count

    def compare_counts(self,actual_counts,required_counts):
        letters_match = 0
        for curr_key in required_counts:
            if curr_key in actual_counts:
                if actual_counts[curr_key] >= required_counts[curr_key]:
                    letters_match += 1
        if letters_match == len(required_counts):
            return True
        return False