"""Day 5 reusable module: order summary business logic.

你的任务：
1. 把上一题已经验证通过的 summarize_valid_orders 函数迁移到本文件。
2. 函数必须继续使用参数 query_rows、target_status="paid"、min_amount=0。
3. 不要让函数读取其他文件的数据，也不要在函数内部 print。
4. 编写 main()，用 DEMO_ROWS 调用函数并打印：
   module demo: {'sales': 120}
5. 添加入口保护，使 main() 只在直接运行本文件时执行。

约束：
- 模块被 import 时，不得自动打印演示结果；
- 不要从旧文件 import 函数，本题要把可复用逻辑迁入当前模块；
- 删除完成后的 TODO 和 NotImplementedError。

验收命令：
python learning/python/week01/day05_modules/order_summary.py

直接运行时必须只输出一行：
module demo: {'sales': 120}
"""


DEMO_ROWS = [
    {"department": "sales", "amount": 120, "status": "paid"},
    {"department": "sales", "amount": 50, "status": "cancelled"},
]


def summarize_valid_orders(query_rows, target_status="paid", min_amount=0):
    result_list = []
    for row in query_rows:
        if row.get("status") == target_status:
            if isinstance(row.get("department"),str) and row.get("department").strip():
                if isinstance(row.get("amount"), (int, float)) and row.get("amount") > 0:
                    if row.get("amount") >= min_amount:
                        result_list.append(row)

    summary = {}
    for row in result_list:
        dept = row["department"]
        amount = row["amount"]
        if dept in summary:
            summary[dept] += amount
        else:
            summary[dept] = amount

    return summary


def main():
    print(f"module demo: {summarize_valid_orders(DEMO_ROWS)}")


if __name__ == "__main__":
    main()