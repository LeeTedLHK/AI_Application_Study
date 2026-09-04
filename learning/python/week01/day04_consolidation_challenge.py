"""Week 1 consolidation gate: validate, filter, and aggregate SQL-like rows."""


QUERY_ROWS = [
    {"department": "sales", "amount": 1200, "status": "paid"},
    {"department": "tech", "amount": 800, "status": "paid"},
    {"department": "sales", "amount": 500, "status": "cancelled"},
    {"department": "tech", "amount": 700, "status": "paid"},
    {"department": "sales", "amount": 300, "status": "paid"},
    {"department": "ops", "status": "paid"},
    {"department": "", "amount": 200, "status": "paid"},
    {"department": "ops", "amount": "900", "status": "paid"},
]


def summarize_valid_orders(query_rows, target_status="paid", min_amount=0):
    """校验、筛选并按部门汇总订单金额。

    业务需求：
    SQL 查询结果中可能混有缺失字段或非法值。只汇总合法且符合筛选条件的行，
    返回格式为 {部门: 汇总金额}。

    输入：
    - query_rows: list[dict]，不得直接读取全局 QUERY_ROWS。
    - target_status: 目标状态，默认 "paid"。
    - min_amount: 最低金额，默认 0；金额等于阈值时应计入。

    一行数据同时满足以下条件才可汇总：
    1. 包含 department、amount、status 三个字段；
    2. department 是去除首尾空格后仍非空的字符串；
    3. amount 是 int 或 float，并且大于 0；
    4. status 等于 target_status；
    5. amount 大于或等于 min_amount。

    约束：
    - 非法行直接忽略，本题暂不返回错误详情；
    - 按 department 累加 amount，使用原始 department 值作为结果 key；
    - 不修改 query_rows；不使用全局业务状态；函数内部不 print；
    - 不查看 Day 1～4 的实现，不硬编码测试答案；
    - 只使用已经学过的变量、list、dict、for、if、isinstance、参数和 return。

    学习者必须亲手完成：
    1. 先在 TODO 下写 4～6 行中文伪代码；
    2. 再实现核心逻辑；
    3. 运行文件并解释一个部门首次出现和再次出现时的累计过程。

    验收标准：文件末尾 5 个案例全部显示 passed: True。
    """
    # 从 query_rows 获取数据
    # 根据 target_status 和 min_amount 筛选数据
    # department 和 amount 要做字段校验
    # 满足所有条件的行进行汇总
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



def run_case(name, actual, expected):
    print(f"{name}: {actual == expected}")
    print(f"  actual:   {actual}")
    print(f"  expected: {expected}")


snapshot = [row.copy() for row in QUERY_ROWS]

run_case(
    "default paid",
    summarize_valid_orders(QUERY_ROWS),
    {"sales": 1500, "tech": 1500},
)
run_case(
    "cancelled",
    summarize_valid_orders(QUERY_ROWS, target_status="cancelled"),
    {"sales": 500},
)
run_case(
    "minimum 700",
    summarize_valid_orders(QUERY_ROWS, min_amount=700),
    {"sales": 1200, "tech": 1500},
)
run_case("empty rows", summarize_valid_orders([]), {})
run_case("input unchanged", QUERY_ROWS, snapshot)
