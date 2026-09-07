"""Day 5 consumer: import and reuse order_summary without import side effects.

你的任务：
1. 使用 `import order_summary` 导入同目录模块。
2. 编写 main()，把 QUERY_ROWS 传给：
   order_summary.summarize_valid_orders(...)
3. 打印格式必须为：
   consumer result: {'tech': 200}
4. 添加入口保护，使 main() 只在直接运行本文件时执行。

验收命令：
python learning/python/demo/day05_modules/use_order_summary.py

必须只输出一行 consumer result；如果同时出现 module demo，说明
order_summary.py 的演示代码没有被入口保护正确隔离。
"""


QUERY_ROWS = [
    {"department": "tech", "amount": 200, "status": "paid"},
    {"department": "tech", "amount": 90, "status": "cancelled"},
]


import order_summary

def main():
    print(f"consumer result: {order_summary.summarize_valid_orders(QUERY_ROWS)}")


if __name__ == "__main__":
    main()
