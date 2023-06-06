# List of menu that user choose

def らめん():
    print("\nらめん？ りょかい！")
    価格 = 900
    額 = int(input("何個買いたいですか？: "))
    合計 = 価格 * 額
    print("\nだから費用がかかる: ", 合計, "￥")

def うどん():
    print("\nうどん？ りょかい！")
    価格 = 700
    額 = int(input("何個買いたいですか？: "))
    合計 = 価格 * 額
    print("\nだから費用がかかる: ", 合計, "￥")

def すし():
    print("\nすし？ りょかい！")
    価格 = 800
    額 = int(input("何個買いたいですか？: "))
    合計 = 価格 * 額
    print("\nだから費用がかかる: ", 合計, "￥")

def おちゃ():
    print("\nおちゃ？ りょかい！")
    価格 = 465
    額 = int(input("何個買いたいですか？: "))
    合計 = 価格 * 額
    print("\nだから費用がかかる: ", 合計, "￥")

# User ordering menu

while True:
    print("\nこれメヌわどうぞ: \n 1. らめん\n 2. うどん\n 3. すし\n 4. おちゃ\n")
    メヌ = int(input("どう？ どれを買いたいですか？: "))

    if メヌ == 1:
        らめん()
    elif メヌ == 2:
        うどん()
    elif メヌ == 3:
        すし()
    elif メヌ == 4:
        おちゃ()
    else:
        print("なんだよ？")
    break

