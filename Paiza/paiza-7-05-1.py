
'''
演習課題「RPGの攻撃シーン」
右のコードには、RPGの攻撃シーンを表示するプログラムで、teamのメンバーが順番にattack関数を呼び出します。さらに、teamのメンバーが攻撃した後に、敵の体力(enemy_hp)を表示するようになっています。敵の最初の体力は標準入力によって入力されます。

ここに、teamのメンバーが攻撃した分だけ、敵の体力をマイナスするコードを追加してください。
teamのメンバーの攻撃力は、あらかじめteamに定義されています。
敵の体力は、450以上とします。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 入力される値
730

 標準入力からの値取得方法はこちらをご確認ください

 期待する出力値
勇者はスライムを攻撃した
敵のHPは残り530です
戦士はスライムを攻撃した
敵のHPは残り380です
魔法使いはスライムを攻撃した
敵のHPは残り280です
'''

# RPGの攻撃シーン

def attack(person):
    print(person + "はスライムを攻撃した")

def output_ememy_hp(enemy_hp):
    print("敵のHPは残り" + str(enemy_hp) + "です")

enemy_hp = int(input())
team = {"勇者" : 200, "戦士" : 150, "魔法使い" : 100}

for person, power in team.items():
    attack(person)
    # 以下に、敵の体力を減少させるコードを書く
    enemy_hp = enemy_hp-power
    output_ememy_hp(enemy_hp)
