from pathlib import Path
from typing import Tuple

import pygame as pg
from pydantic import BaseSettings

from crygeen.controls import cntrl, Control, allowed_keys
from crygeen.main_menu.states import Status


class Settings(BaseSettings):
    # general setup _________________________________________________________________________________
    SCREEN_WIDTH: int = 1280
    SCREEN_HEIGHT: int = 760
    FLAGS: int = pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE
    BIT_PER_PIXEL: int = 32
    BASE_PATH: Path = Path(__file__).parent.resolve()
    STD_BUTTON_COLOR: Tuple[int, int, int] = (255, 255, 255)  # white
    STD_BUTTON_ALPHA: int = 200
    STD_BUTTON_OPACITY_OFFSET: int = 1
    GAME_TITLE: str = "Crygeen"
    GAME_ICO: Path = BASE_PATH.joinpath('assets', 'graphics', 'game_ico.png')
    MENU_FPS: int = 40
    GAME_FPS: int = 60

    SAVE_LOAD_BASE_PATH: Path = BASE_PATH.joinpath('data')
    CONTROL_DATA_PATH: Path = SAVE_LOAD_BASE_PATH.joinpath('control', 'control_data.json')

    # main main_menu setup _______________________________________________________________________________
    MAIN_MENU_LIST: dict = {
        'New Game': {'status': Status.NEW_GAME, 'state': 'game.state = State.GAME'},  # todo fix game.state
        'Load game': {'status': Status.MAIN_MENU},  # todo while testing
        'Settings': {'status': Status.SETTINGS,
                     'start_time': 'main_menu.settings_menu.dropdown_start_time = pg.time.get_ticks()'},
        'Exit': {'status': Status.EXIT,
                 'start_time': 'main_menu.exit_menu.dropdown_start_time = pg.time.get_ticks();'
                               'main_menu.exit_menu.animation_start_time = pg.time.get_ticks()'}
    }
    MAIN_MENU_FONT: Path = BASE_PATH.joinpath('assets', 'graphics', 'font', 'AlumniSansInlineOne-italic.ttf')
    MAIN_MENU_POSITION: str = 'topleft'
    MAIN_MENU_X: int = 150
    MAIN_MENU_Y: int = 100
    MAIN_MENU_Y_OFFSET: int = 100
    MAIN_MENU_BUTTON_OPACITY_OFFSET: int = 10
    MAIN_MENU_ALPHA: int = 128
    MAIN_MENU_DROPDOWN_ANIMATION: int = 2000
    MAIN_MENU_FONT_SIZE: int = 50
    MAIN_MENU_FONT_COLOR: Tuple[int, int, int] = (255, 255, 255)  # white

    # screensaver setup _____________________________________________________________________________
    # SCREENSAVER_PATH: Path = BASE_PATH.joinpath('assets', 'graphics', 'screensaver')
    SCREENSAVER_PATH: Path = BASE_PATH.joinpath('assets', 'graphics', 'main')
    # SCREENSAVER_PATH: Path = BASE_PATH.joinpath('assets', 'graphics', 'gametest')
    SCREENSAVER_ALPHA_OFFSET: float = .5
    SCREENSAVER_FONT: Path = BASE_PATH.joinpath('assets', 'graphics', 'font', 'AlumniSansInlineOne-italic.ttf')
    SCREENSAVER_FONT_SIZE: int = 45
    SCREENSAVER_FONT_COLOR: Tuple[int, int, int] = (255, 255, 255)  # white
    SCREENSAVER_SURF_COLOR: Tuple[int, int, int] = (0, 0, 0)  # black
    SCREENSAVER_ALPHA_VANISH_DURATION: int = 10000
    SCREENSAVER_START_ALPHA_VANISH: int = 255
    SCREENSAVER_TEXT: str = 'Press any key to continue...'
    SCREENSAVER_TEXT_X: int = SCREEN_WIDTH // 2
    SCREENSAVER_TEXT_Y: int = SCREEN_HEIGHT - SCREEN_HEIGHT // 8
    SCREENSAVER_ALPHA_TEXT_DURATION: int = 7000
    SCREENSAVER_START_TEXT_ALPHA: Tuple[int, int] = (0, 255)

    # exit setup ____________________________________________________________________________________
    EXIT_LIST: dict = {'No': {'status': Status.MAIN_MENU,
                              'start_time': 'main_menu.menu.dropdown_start_time = pg.time.get_ticks();'
                                            'main_menu.exit_menu.animation_start_time = pg.time.get_ticks();'
                              },
                       'Yes': {'action': 'pg.quit(); exit()'}}
    EXIT_BUTTON_START_Y: int = 1000
    EXIT_BUTTON_DEST_Y: list[int] = [500, 500]
    EXIT_BUTTON_X: tuple[int, int] = (SCREEN_WIDTH // 2 - 200, SCREEN_WIDTH // 2 + 200)
    EXIT_BUTTON_POSITION: str = 'center'
    EXIT_ALPHA_VANISH_DURATION: int = 1000
    EXIT_START_ALPHA_VANISH: int = 0
    EXIT_END_ALPHA_VANISH: int = 255
    EXIT_TEXT_X: int = SCREEN_WIDTH // 2
    EXIT_TEXT_Y: int = SCREEN_HEIGHT // 2
    EXIT_TEXT: str = 'Are you sure you want to exit?'
    EXIT_DROPDOWN_DURATION: int = 2000

    # settings setup ________________________________________________________________________________
    SETTINGS_ALPHA_VANISH_DURATION: int = 1000
    SETTINGS_DEST_ALPHA_VANISH: int = 128

    # control section
    CONTROL_TITLE: str = 'Control Setup'
    CONTROL_ALPHA: int = 228
    CONTROL_SELECT_COLOR: tuple = (255, 0, 0)  # red
    CONTROL_X: int = SCREEN_WIDTH // 2 or 2.5
    CONTROL_Y: int = SCREEN_HEIGHT // 10
    CONTROL_BUTTONS_POSITION: str = 'topleft'
    CONTROL_Y_OFFSET: int = 10 + MAIN_MENU_FONT_SIZE
    CONTROL_FONT_SIZE: int = 30
    CONTROL_BOTTOM_BOUNDARY: int = SCREEN_HEIGHT - SCREEN_HEIGHT // 4
    CONTROL_TOP_BOUNDARY: int = SCREEN_HEIGHT // 4
    CONTROL_SCROLL_OFFSET: int = 9
    CONTROL_ANIMATION_DURATION: int = 1000
    CONTROL: Control = cntrl
    CONTROL_ALLOWED_KEYS: dict[int, str] = allowed_keys


settings: Settings = Settings()
