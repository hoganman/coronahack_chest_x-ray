
from collections import UserDict
from typing import Dict


class Label(UserDict):

    Key = 'Label'
    Label = 'Symptom'
    Normal = 0
    Pnemonia = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data: Dict[str, int] = {
            'Normal': self.Normal,
            '': self.Normal,
            'Pnemonia': self.Pnemonia
        }
        # The quasi-inverse mapping for labels
        self.label: Dict[int, str] = {
            self.Normal: '',
            self.Pnemonia: 'Pnemonia'
        }


class Label1(UserDict):

    Key = 'Label_1_Virus_category'
    Label = 'Category #1'
    Normal = 0
    Virus = 1
    Bacteria = 2
    Unknown = 3

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data: Dict[str, int] = {
            'Normal': self.Normal,
            '': self.Normal,
            'Virus': self.Virus,
            'bacteria': self.Bacteria,
            'Stress-Smoking': self.Unknown
        }

        self.labels: Dict[int, str] = {
            self.Normal: 'Normal',
            self.Virus: 'Virus',
            self.Bacteria: 'Bacteria',
            self.Unknown: 'Unknown'
        }

    @staticmethod
    def is_normal(label: str) -> bool:
        return label.lower() == 'normal' or len(label) == 0


class Label2(UserDict):

    Key = 'Label_2_Virus_category'
    Label = 'Category #2'
    Normal = 0
    ARDS = 10
    Streptococcus = 25
    COVID19 = 50
    SARS = 60
    Unknown = 1000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data: Dict[str, int] = {
            'Normal': self.Normal,
            'ARDS': self.ARDS,
            'Unknown': self.Unknown,
            'COVID-19': self.COVID19,
            'SARS': self.SARS,
            'Streptococcus': self.Streptococcus
        }

        self.labels: Dict[int, str] = {
            self.Normal: 'Normal',
            self.ARDS: 'ARDS',
            self.Unknown: 'Unknown',
            self.COVID19: 'COVID-19',
            self.SARS: 'SARS',
            self.Streptococcus: 'Streptococcus'
        }


