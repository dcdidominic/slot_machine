# Display settings
DEFAULT_IMAGE_SIZE = (128,128)
FPS = 60
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 500, -300
X_OFFSET, Y_OFFSET = 10, 0

# Graphics
BG_IMAGE_PATH = 'graphics/background.png'
TOP_MASK = 'graphics/bg_top.png'
BOTTOM_MASK = 'graphics/bg_bottom.png'
STOLEN_IMG = 'graphics/stolen.png'
TAMPER_IMG = 'graphics/tamper.png'
SCALE_PWR_IMG = 'graphics/scale_power.png'
JACKPOT_IMG = 'graphics/jackpot.png'
CHICKEN_WIN_IMG = 'graphics/chicken_win.png'
BEER_WIN_IMG = 'graphics/beer_win.png'
CHANCE_WIN_IMG = 'graphics/chance_win.png'
GAME_INDICIES = [1, 2, 3] # 0 and 4 are outside the playing area
SYM_PATH = 'graphics/symbols'
SYM_SIZE = 128
symbols = {
    'beer':f'{SYM_PATH}/beer.png',
    'chance':f'{SYM_PATH}/chance.png',
    #'cherry':f'{SYM_PATH}/cherry.png',
    'seven':f'{SYM_PATH}/seven.png',
    'skis':f'{SYM_PATH}/skis.png',
    #'watermelon':f'{SYM_PATH}/watermelon.png',
    'chicken':f'{SYM_PATH}/chicken.png',
}

# Audio
PLAY_SOUND = True
MAIN_SOUND = 'audio/main_sound.mp3'
SPIN_SOUND = 'audio/spin_sound.mp3'
STOP_SOUND = 'audio/stop_sound.mp3'
JACKPOT_WIN_SOUND = 'audio/jackpot_win.mp3'
CHICKEN_SOUND = 'audio/chicken_sound.mp3'
BEER1_SOUND = 'audio/beer1.mp3'
BEER2_SOUND = 'audio/beer2.mp3'
CHANCE_SOUND = 'audio/chance.mp3'

# USB Weight Scale
VENDOR_ID = 0x0922
PRODUCT_ID = 0x8003
MAX_ATTEMPTS = 10
CHIP_WEIGHT = 10
CREDIT_VALUE_SPINS = 5

# CHEATS
SUPER_SPIN = False
CONTINUOUS_SPIN = False

