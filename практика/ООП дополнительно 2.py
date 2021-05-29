class Tomato():
    states={
        1:"отсутствует",
        2:"цветение",
        3:"зеленый",
        4:"красный"
    }
    value = list(states.values())
    def __init__(self,_index,_state=value[0]):
        self._index=_index
        self._state=_state
    def grow(self,_state=value[1]):
        self._state=_state



