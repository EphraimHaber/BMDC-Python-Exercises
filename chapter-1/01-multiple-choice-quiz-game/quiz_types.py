from typing import Dict, Literal, TypedDict

OptionLetter = Literal['A', 'B', 'C', 'D']


class Question(TypedDict):
    question: str
    options: Dict[OptionLetter, str]
    answer: OptionLetter
