from enum import Enum

DOMEN = 'https://stellarburgers.nomoreparties.site/'


class URL(str, Enum):
    LOGIN = f'{DOMEN}login'
    FORGOT_PASSWORD = f'{DOMEN}forgot-password'
    RESET_PASSWORD = f'{DOMEN}reset-password'
    REGISTER = f'{DOMEN}register'
    PERSONAL_AREA = f'{DOMEN}account/profile'
    FEED = f'{DOMEN}feed'


LOGIN_USER = "ooooccccppp@fff.ru"
LOGIN_PASSWORD = "ooooccccppp@fff.ru"
