import re
 # Masala 1: Email Validatsiya (Oson)
# Topshiriq: Foydalanuvchi emailini tekshiruvchi regex yozing.Email qoidalari:

emails = [
    "ali@gmail.com",      # ✓ To'g'ri
    "test.user@yahoo.uz", # ✓ To'g'ri
    "invalid@",           # ✗ Noto'g'ri
    "@example.com",       # ✗ Noto'g'ri
    "user@domain"         # ✗ Noto'g'ri
]

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
for email in emails:
    if re.findall(andoza,email):
        print(f"{email} ✓ Tog'ri")
    else:
        print(f"{email} ✗ Noto'gri")



# Masala 2: Telefon Raqam Formatlash (O'rta)
# Topshiriq: O'zbekiston telefon raqamlarini topib, formatlang.O'zbekiston raqam formatlari:

text = """
Aloqa: +998901234567
Raqam: 998971234567
Tel: 901234567 (noto'g'ri)
"""
andoza = r'(?:/+998|998)(\d{9})'

tel = re.findall(andoza,text)
print(tel)
