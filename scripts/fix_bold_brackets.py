import sys
import re
import os

def fix_bold_brackets(content):
    # 行頭の見出しシンボル（#）で始まる行は、見出し全体の太字処理を避けるために除外する処理を検討。
    # ここでは、単純な置換ではなく、行ごとに処理を行うか、より具体的なパターンを使用する。
    
    new_lines = []
    for line in content.splitlines():
        # 見出し行（#で始まる）の場合は、冒頭と末尾の**のみを置換対象にするなど慎重に処理
        if line.strip().startswith('#'):
            # 見出し全体の太字 **Title** を <strong>Title</strong> にしたいケースもあるが、
            # 今回の問題は **5. ... </strong> のようにマッピングが壊れること。
            # 見出し行は Markdown パーサーに任せるのが安全なので、ここでは「 」が含まれる場合のみに限定するか、
            # あるいは見出し行の置換自体をスキップする。
            # ユーザーの要望は「5. ...」の表示異常の解決なので、見出し行での置換を制限する。
            
            # 見出し行に「 」が含まれる場合のみ置換を試みるが、
            # 「**5. 形式」のようなケースで壊れないよう、開始と終了がセットでない場合は置換しない。
            pass
        else:
            # 1. **「 または \*\*「 または \\**「 を <strong>「 に置換
            line = re.sub(r'[\*\\]+「', r'<strong>「', line)
            # 2. 」** または 」\*\* または 」\\** を 」</strong> に置換
            line = re.sub(r'」[\*\\]+', r'」</strong>', line)
            
            # 重複クリーンアップ
            line = line.replace('<strong><strong>', '<strong>')
            line = line.replace('</strong></strong>', '</strong>')
        
        new_lines.append(line)
    
    return '\n'.join(new_lines) + ('\n' if content.endswith('\n') else '')

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            with open(arg, 'r', encoding='utf-8') as f:
                old_content = f.read()
            new_content = fix_bold_brackets(old_content)
            if old_content != new_content:
                with open(arg, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {arg}")
        elif os.path.isdir(arg):
            for root, dirs, files in os.walk(arg):
                for file in files:
                    if file.endswith(".md"):
                        path = os.path.join(root, file)
                        with open(path, 'r', encoding='utf-8') as f:
                            old_content = f.read()
                        new_content = fix_bold_brackets(old_content)
                        if old_content != new_content:
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"Fixed: {path}")
