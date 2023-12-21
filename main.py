import subprocess
import sys
from othello_py import *



if sys.argv[1] == 'cui':
    
    # AIの手番の選択
    try:
        ai_player = int(input('AIの手番 0: 黒(先手) 1: 白(後手) : '))
    except:
        print('0か1を入力してください')
        exit()
    if ai_player != 0 and ai_player != 1:
        print('0か1を入力してください')
        exit()
    
    ai_exe = subprocess.Popen('./ai.out'.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ai_exe.stdin.write((str(ai_player) + '\n').encode('utf-8'))
    ai_exe.stdin.flush()
    
    o = othello()

    print()

    def ai():
        alph = ["A", "B", "C", "D", "E", "F", "G", "H"]
        grid_str = ''
        for i in range(hw):
            for j in range(hw):
                grid_str += '0' if o.grid[i][j] == 0 else '1' if o.grid[i][j] == 1 else '.'
        grid_str += '\n'
        print(grid_str)
        ai_exe.stdin.write(grid_str.encode('utf-8'))
        ai_exe.stdin.flush()
        y, x = [int(elem) for elem in ai_exe.stdout.readline().decode().split()]
        # print(y, x)
        print(f"AI 着手({o.sequence_num+1}手目)：", y+1, x+1, f"({alph[x]} {y+1})")
        o.move(y, x)
    

    while True:
        
        # 合法手生成とパス判定
        if not o.check_legal():
            o.player = 1 - o.player
            
            # 終局
            if not o.check_legal():
                break
        
        print(f"現在の手番：{o.sequence_num}手目")
        o.print_info()
        if o.player == ai_player:
            ai()
        else:
            o.move_stdin()
else:
    message = '''
使い方

【実行方法】
    python main.py cui
    
    '''
    print(message)