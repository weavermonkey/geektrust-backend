from current_emblem import EmblemMapping


class Kingdom(EmblemMapping):
    def __init__(self, kingdom):
        self.kingdom = kingdom
        self.emblem = EmblemMapping.emblem_mapping[kingdom]
        self.cipher_key = len(self.emblem)
        self.is_ally = False
