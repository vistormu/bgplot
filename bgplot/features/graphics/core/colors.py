from dataclasses import dataclass


@dataclass
class Colors:
    black: str = '#4d5359'
    white: str = '#f4f3ee'
    gray: str = '#8a817c'
    red: str = '#cf7171'
    green: str = '#dbe8c1'
    blue: str = '#aecdd2'
    purple: str = '#c696bc'
    pink: str = '#ffcbdb'
    yellow: str = '#fadf7f'
    cream: str = '#fff8f0'
    dark_lava: str = '#463f3a'
    isabelline: str = '#f4f3ee'
    brandy: str = '#924242'
    gamboge: str = '#de9e36'
    wintergreen: str = '#4b8f8c'
    space_cadet: str = '#2d3142'
    black_coral: str = '#4f5d75'
    manatee: str = '#8d99ae'
    raisin_black: str = '#242325'
    tea_green: str = '#DAEDBD'
    french_lilac: str = '#985F99'
    middle_blue: str = '#7DBBC3'
    spanish_pink: str = '#F4B9B2'
    popstar: str = '#B75D69'
    yellow_orange: str = '#EEA243'

    @staticmethod
    def to_rgb(hex_code: str):
        stripped_code = hex_code.lstrip('#')
        rgb_value = tuple(int(stripped_code[i:i+2], 16) for i in (0, 2, 4))

        return rgb_value
