# Display settings
DEFAULT_IMAGE_SIZE = (128,128)
FPS = 240
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 500, -300
X_OFFSET, Y_OFFSET = 10, 0

# Graphics
BG_IMAGE_PATH = 'graphics/background.png'
TOP_MASK = 'graphics/bg_top.png'
BOTTOM_MASK = 'graphics/bg_bottom.png'
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
PLAY_SOUND = False
MAIN_SOUND = 'audio/main_sound.mp3'

# USB Weight Scale
VENDOR_ID = 0x0922
PRODUCT_ID = 0x8003
MAX_ATTEMPTS = 10
CHIP_WEIGHT = 12
CREDIT_VALUE_SPINS = 5

