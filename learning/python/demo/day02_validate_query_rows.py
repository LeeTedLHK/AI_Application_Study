"""Week 1 / Day 2: validate one SQL/JSON-style row before processing."""

REQUIRED_FIELDS = ("department", "amount", "status")
VALID_STATUSES = {"paid", "cancelled", "pending"}


def validate_query_row(row, required_fields=REQUIRED_FIELDS):
    """返回当前数据行的全部校验错误。

    任务要求：
    1. 返回 list[str]；合法数据返回空列表 []。
    2. 遍历 required_fields，缺少字段时追加："missing field: 字段名"。
    3. 字段存在时再校验值，不能因缺失字段抛出 KeyError。
    4. department 必须是非空字符串，否则追加：
       "department must be a non-empty string"。
    5. amount 必须是 int 或 float 且大于 0，否则追加：
       "amount must be greater than 0"。
    6. status 必须属于 VALID_STATUSES，否则追加：
       "status must be one of: paid, cancelled, pending"。
    7. 一次返回全部错误，不要遇到第一个错误就 return。
    8. 不使用 try/except；练习通过成员检查安全访问字典。

    验收标准：
    - 下方三个案例的 actual 都等于 expected；
    - 缺少 amount 的案例只报告字段缺失，不抛 KeyError；
    - 能解释为什么 required_fields 使用 tuple、VALID_STATUSES 使用 set。
    """
    # TODO: 由学习者亲手实现，建议控制在 15～25 行。
    errors = []
    for field in required_fields:
        if field not in row:
            errors.append(f"missing field: {field}")
        else:
            value = row[field]
            if field == "department":
                if isinstance(value, str) and value.strip():
                    pass
                else:
                    errors.append("department must be a non-empty string")
            elif field == "amount":
                if isinstance(value, (int, float)) and value > 0:
                    pass
                else:
                    errors.append("amount must be greater than 0")
            elif field == "status":
                if value in VALID_STATUSES:
                    pass
                else:
                    errors.append("status must be one of: paid, cancelled, pending")
    return errors


test_cases = [
    (
        {"department": "sales", "amount": 1200, "status": "paid"},
        [],
    ),
    (
        {"department": "sales", "status": "paid"},
        ["missing field: amount"],
    ),
    (
        {"department": "", "amount": -50, "status": "refunded"},
        [
            "department must be a non-empty string",
            "amount must be greater than 0",
            "status must be one of: paid, cancelled, pending",
        ],
    ),
]

for test_row, expected in test_cases:
    actual = validate_query_row(test_row)
    print(f"actual:   {actual}")
    print(f"expected: {expected}")
    print(f"passed:   {actual == expected}")

