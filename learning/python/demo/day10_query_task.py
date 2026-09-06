"""Day 10 亲手练习：用 class 表达一个查询任务。

业务目标：
后端或 Agent 需要保存一个查询任务的表名和返回条数，并把当前任务状态
转换成可交给 API / Tool 调用的 Python 字典。

输入：
- table_name：要查询的表名，例如 "orders"；
- limit：返回条数；0 也是有效值，必须原样保留。

输出契约：
- QueryTask(table_name, limit) 创建一个拥有独立状态的实例；
- task.to_payload() 返回：
  {"table_name": <当前实例的 table_name>, "limit": <当前实例的 limit>}。

约束：
- 使用 __init__ 把两个参数保存为实例属性；
- 使用 self 读取当前实例的状态；
- to_payload 返回 Python dict，不返回 JSON 字符串；
- 不使用全局变量或 class 共享变量保存 table_name / limit；
- 本课暂不增加类型校验、继承、dataclass 或 Pydantic。

动手顺序：
1. 先用三行伪代码写出“创建实例 → 保存状态 → 生成 payload”；
2. 替换两个方法中的占位实现；
3. 运行 test_day10_query_task.py；
4. 增加 update_limit(new_limit)，只更新当前实例并隐式返回 None。

验收：
初始三个测试和 update_limit 需求修改测试全部通过；能解释 self、参数与实例属性的区别，以及为什么两个
实例的状态互不影响。
"""

# 创建实例
class QueryTask:
    def __init__(self, table_name, limit):
        """保存一个查询任务的初始状态。"""
        # 保存状态
        self.table_name = table_name
        self.limit = limit

    # 生成 payload
    def to_payload(self):
        """返回当前实例状态对应的 Python 字典。"""
        return {"table_name": self.table_name, "limit": self.limit}

    def update_limit(self, new_limit):
        """更新当前实例的 limit。"""
        self.limit = new_limit
