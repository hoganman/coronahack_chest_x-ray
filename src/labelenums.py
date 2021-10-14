
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


class Label2(object):

    Key = 'Label_2_Virus_category'
    Label = 'Category #2'
    Normal = 0
    ARDS = 1
    Virus_Unknown = 2
    Virus_COVID19 = 3
    Virus_SARS = 4
    Bacteria_Streptococcus = 5
    Bacteria_Unknown = 6

    def __init__(self):

        self.labels: Dict[int, str] = {
            self.Normal: 'Normal',
            self.ARDS: 'ARDS',
            self.Virus_Unknown: 'Virus (Unknown)',
            self.Virus_COVID19: 'COVID-19',
            self.Virus_SARS: 'SARS',
            self.Bacteria_Unknown: 'Bacteria (Unknown)',
            self.Bacteria_Streptococcus: 'Streptococcus'
        }

