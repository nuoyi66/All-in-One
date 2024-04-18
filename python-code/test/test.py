import re
def identify_operator(phone_number: str) -> str:
    patterns = {
        "中国移动": r"^((13[4-9]|147|15[0-27-9]|178|18[2-478]|198)\d{8}|(170[5-9]|16[57])\d{7})$",
        "中国联通": r"^((13[01]|145|15[56]|171|175|18[56]|196)\d{8}|(170[012]|166)\d{7})$",
        "中国电信": r"^((133|153|173|177|18[019]|19[19])\d{8}|170[34]\d{7})$",
    }

    for operator, pattern in patterns.items():
        if re.match(pattern, phone_number):
            return operator

    return "输入的号码有"

# 测试示例
print(identify_operator(input("请输入手机号码：\n")))