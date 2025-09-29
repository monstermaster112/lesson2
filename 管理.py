# 简易待办清单（to-do list）管理程序
# 功能：
# 1) 添加新任务
# 2) 显示所有任务
# 3) 将任务标记为完成
# 要求：使用列表和循环实现基础功能


def show_menu():
    print("\n=== 待办清单 ===")
    print("1. 添加新任务（可用逗号一次性添加多个）")
    print("2. 显示所有任务")
    print("3. 将任务标记为完成")
    print("4. 删除任务")
    print("5. 退出")


def list_tasks(tasks):
    if not tasks:
        print("暂无任务。")
        return
    print("\n当前任务：")
    for index, task in enumerate(tasks, start=1):
        status = "✓ 已完成" if task["done"] else "✗ 未完成"
        print(f"{index}. {task['title']}  [{status}]")


def add_task(tasks):
    raw = input("请输入任务内容（可用逗号分隔多个）：").strip()
    if not raw:
        print("任务内容不能为空。")
        return
    # 支持英文逗号和中文逗号
    parts = [p.strip() for p in raw.replace("，", ",").split(",")]
    added = 0
    for title in parts:
        if title:
            tasks.append({"title": title, "done": False})
            added += 1
    if added:
        print(f"已添加 {added} 个任务！")
    else:
        print("没有有效的任务被添加。")


def complete_task(tasks):
    if not tasks:
        print("没有可以完成的任务。")
        return
    list_tasks(tasks)
    raw = input("请输入要标记完成的任务编号：").strip()
    if not raw.isdigit():
        print("请输入有效的数字编号。")
        return
    idx = int(raw)
    if 1 <= idx <= len(tasks):
        tasks[idx - 1]["done"] = True
        print("已标记为完成！")
    else:
        print("编号超出范围。")


def delete_task(tasks):
    if not tasks:
        print("没有可以删除的任务。")
        return
    list_tasks(tasks)
    raw = input("请输入要删除的任务编号：").strip()
    if not raw.isdigit():
        print("请输入有效的数字编号。")
        return
    idx = int(raw)
    if 1 <= idx <= len(tasks):
        removed = tasks.pop(idx - 1)
        print(f"已删除任务：{removed['title']}")
    else:
        print("编号超出范围。")


def main():
    # 使用列表保存任务；任务为字典，包含标题与完成状态
    tasks = []
    while True:
        show_menu()
        choice = input("请选择操作（1-5）：").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("已退出程序。")
            break
        else:
            print("无效选择，请输入 1-5。")


if __name__ == "__main__":
    main()

