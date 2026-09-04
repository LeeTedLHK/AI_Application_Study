"""Week 1 / Day 4: make all business inputs explicit function parameters."""


QUERY_ROWS = [
    {"order_id": "A1001", "status": "paid", "amount": 120},
    {"order_id": "A1002", "status": "cancelled", "amount": 80},
    {"order_id": "A1003", "status": "paid", "amount": 200},
]


def filter_orders_by_status(query_rows, target_status="paid"):
    """按状态筛选订单，并返回一个新的列表。

    当前函数签名不完整，请你修改。任务要求：
    1. 增加参数 target_status，默认值为 "paid"。
    2. 遍历 query_rows，只保留 status 等于 target_status 的数据行。
    3. 返回新的 list[dict]，保持原始顺序，不修改 query_rows。
    4. 不读取任何保存“目标状态”的全局变量。
    5. 不要在函数内部 print，也不要硬编码测试案例的结果。

    输入：list[dict] query_rows，以及字符串 target_status。
    输出：满足状态条件的 list[dict]。

    验收标准：
    - 默认调用返回 A1001、A1003；
    - target_status="cancelled" 返回 A1002；
    - 空列表返回 []；
    - 三个测试均显示 passed: True。
    """
    # 输入从 query_rows 获得
    # 根据传入的 status 与 target_status 判断是否满足条件
    # 用 for 循环遍历 query_rows
    # 结果保存在一个新建的 list 中
    # 最后返回 list 

    filtered_rows = []
    for row in query_rows:
        if row["status"] == target_status:
            filtered_rows.append(row)
    return filtered_rows


def order_ids(rows):
    return [row["order_id"] for row in rows]


test_cases = [
    (filter_orders_by_status(QUERY_ROWS), ["A1001", "A1003"]),
    (filter_orders_by_status(QUERY_ROWS, target_status="cancelled"), ["A1002"]),
    (filter_orders_by_status([]), []),
]

for actual, expected_ids in test_cases:
    actual_ids = order_ids(actual)
    print(f"actual:   {actual_ids}")
    print(f"expected: {expected_ids}")
    print(f"passed:   {actual_ids == expected_ids}")
