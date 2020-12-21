class KeyInput:
    word = str
    status: [bool] = None
    definition: [str]

    def build_definition(self)->str:
        return '\n'.join(self.definition)


