# src/utils.py

def extract_domain(email: str) -> str:
     """从邮箱中提取域名，如 'user@gmail.com' → 'gmail.com'"""
     if "@" not in email:
         return ""
     return email.split("@")[1]
     
     