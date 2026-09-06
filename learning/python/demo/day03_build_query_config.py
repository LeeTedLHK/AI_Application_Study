"""Week 1 / Day 3: practice required parameters, defaults, and return values."""


def build_query_config(table_name, limit=100):
    """构造供查询工具使用的配置字典。

    任务要求：
    1. table_name 是必传参数，limit 的默认值是 100。
    2. 返回 {"table_name": table_name, "limit": limit}。
    3. 函数内部不要 print；结果必须通过 return 交给调用方。
    4. 不要直接返回某个测试案例的固定值。
    """
    config = {"table_name": table_name, "limit": limit}
    return config 

test_cases = [
    (
        build_query_config("orders"),
        {"table_name": "orders", "limit": 100},
    ),
    (
        build_query_config("customers", 20),
        {"table_name": "customers", "limit": 20},
    ),
    (
        build_query_config(table_name="events", limit=0),
        {"table_name": "events", "limit": 0},
    ),
]

for actual, expected in test_cases:
    print(f"actual:   {actual}")
    print(f"expected: {expected}")
    print(f"passed:   {actual == expected}")
