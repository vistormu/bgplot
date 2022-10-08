from dataclasses import dataclass


@dataclass
class Colors:
    black: str = '#4d5359'
    white: str = '#f4f3ee'
    gray: str = '#8a817c'
    red: str = '#cf7171'
    green: str = '#dbe8c1'
    blue: str = '#aecdd2'
    purple: str = '#aecdd2'
    pink: str = '#ffcbdb'
    yellow: str = '#fadf7f'
    cream: str = '#fff8f0'

    def to_rgb(hex_code: str):
        stripped_code = hex_code.lstrip('#')
        rgb_value = tuple(int(stripped_code[i:i+2], 16) for i in (0, 2, 4))

        return rgb_value
