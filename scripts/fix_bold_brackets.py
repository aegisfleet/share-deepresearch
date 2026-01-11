import sys
import re
import os

def fix_bold_brackets(content):
    # 1. **「 または \*\*「 または \\**「 を <strong>「 に置換
    content = re.sub(r'[\*\\]+「', r'<strong>「', content)
    # 2. 」** または 」\*\* または 」\\** を 」</strong> に置換
    content = re.sub(r'」[\*\\]+', r'」</strong>', content)
    
    # 重複してしまった場合のクリーンアップ (例: <strong><strong> )
    content = content.replace('<strong><strong>', '<strong>')
    content = content.replace('</strong></strong>', '</strong>')
    
    # 万が一 ** だけ残ってしまった場合の救済 (強引ですが)
    # <strong>「システム」</strong>** -> <strong>「システム」</strong>
    content = re.sub(r'(<\/strong>)[\*\\]+', r'\1', content)
    content = re.sub(r'[\*\\]+(<strong>)', r'\1', content)
    
    return content

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
