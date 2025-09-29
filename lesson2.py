# 读取用户输入的分数（0-100），并根据区间输出评价

def classify_score(score: float) -> str:
    if score < 0 or score > 100:
        raise ValueError("分数必须在 0 到 100 之间")
    if score >= 90:
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 60:
        return "及格"
    return "不及格"


if __name__ == "__main__":
    try:
        raw = input("请输入分数（0-100）：")
        score = float(raw)
        result = classify_score(score)
        print(f"评价：{result}")
    except ValueError as e:
        print(f"输入错误：{e}")
        
    input("按下回车键退出程序")


