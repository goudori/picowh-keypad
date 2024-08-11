# 4*4のkeypad
from machine import Pin  # type: ignore
from time import sleep

# keypadキーが離された状態
KEY_UP = const(0)  # type: ignore
# keypadキーが押された状態
KEY_DOWN = const(1)  # type: ignore

# keypadキーのキーの配列(keypadの配置)
keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"],
]

# Pin number
rows = [2, 3, 4, 5]
cols = [6, 7, 8, 9]

# 行のPinを出力に設定
row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]

# 列のPinを入力に設定
col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]


def init():
    for row in range(0, 4):
        for col in range(0, 4):
            row_pins[row].low()


def scan(row, col):
    """scan the keypad"""

    # set the current column to high
    row_pins[row].high()
    key = None

    # キーイベントの確認
    if col_pins[col].value() == KEY_DOWN:
        key = KEY_DOWN
    if col_pins[col].value() == KEY_UP:
        key = KEY_UP
    row_pins[row].low()

    # return the key state
    return key


print("starting")

# 全ての列をlowにする(デフォルトリセット)
init()

while True:
    # 行のループ
    for row in range(4):
        # 列のループ
        for col in range(4):
            key = scan(row, col)
            if key == KEY_DOWN:
                print("Key Pressed", keys[row][col])
                last_key_press = keys[row][col]
                sleep(0.2)
