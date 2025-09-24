import re
import random
import string

def check_password_strength(password):
    """
    檢查密碼強度。
    規則：
    1. 長度 >= 8
    2. 至少一個數字
    3. 至少一個大寫字母
    4. 至少一個小寫字母
    5. 至少一個特殊字元
    回傳：'弱'、'中等'、'強'
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中等"
    else:
        return "強"

def generate_strong_password(length=12):
    """
    生成一個隨機強密碼，長度至少8。
    密碼包含：小寫、大寫、數字、特殊字元各至少一個。
    """
    if length < 8:
        raise ValueError("密碼長度應該至少為8")
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice('!@#$%^&*(),.?":{}|<>')
    ]
    all_chars = string.ascii_letters + string.digits + '!@#$%^&*(),.?":{}|<>'
    password_chars += random.choices(all_chars, k=length - 4)
    random.shuffle(password_chars)
    return ''.join(password_chars)

if __name__ == "__main__":
    """
    命令列執行邏輯：
    - 若有參數，檢查密碼強度。
    - 無參數則生成強密碼。
    """
    import sys
    if len(sys.argv) > 1:
        password = sys.argv[1]
        strength = check_password_strength(password)
        print(f"密碼強度: {strength}")
    else:
        strong_password = generate_strong_password()
        print(f"生成的強密碼: {strong_password}")
    # ...existing code...
