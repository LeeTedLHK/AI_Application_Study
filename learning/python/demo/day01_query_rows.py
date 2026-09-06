"""Week 1 / Day 1: turn SQL-like rows into a department summary."""

rows = [
    {"department": "sales", "amount": 1200, "status": "paid"},
    {"department": "tech", "amount": 800, "status": "paid"},
    {"department": "sales", "amount": 500, "status": "cancelled"},
    {"department": "tech", "amount": 700, "status": "paid"},
    {"department": "sales", "amount": 300, "status": "paid"},
]


# def summarize_paid_amount(query_rows):
#     """按部门汇总已支付的金额。

#     任务要求：
#     1. 遍历参数 query_rows，不要直接读取全局变量 rows。
#     2. 只统计 status 等于 "paid" 的记录，忽略其他状态。
#     3. 按 department 累加 amount。
#     4. 返回格式为 {部门: 已支付总金额} 的字典。
#     5. 暂时假设每行都包含 department、amount 和 status。

#     当前样例的预期输出：
#     {"sales": 1500, "tech": 1500}

#     验收标准：
#     - cancelled 的 500 不得计入结果；
#     - 函数返回字典，而不是只在函数内部打印；
#     - 能解释部门第一次出现与再次出现时的累计过程。
#     """
#     # TODO: 由学习者亲手实现，先不要让 Agent 代写。
#     # dict.get() 和直接用 dict[] 最大的区别是：key 不存在时，get() 不会报错。
#     dict = {}
#     for i in query_rows:
#         if i["status"] == "paid":
#             dict[i["department"]] = dict.get(i["department"], 0) + i["amount"]
#     return dict


# result = summarize_paid_amount(rows)
# print(result)




def summarize_paid_amount(query_rows, target_status="paid"):
    """
    # 第二轮修改要求：
    # 1. 把变量 dict 改成不会遮蔽 Python 内置名称、且能表达用途的名字。
    # 2. 把循环变量 i 改成能表达“当前数据行”的名字。
    # 3. 为函数增加参数 target_status，默认值为 "paid"，不要再硬编码状态。
    # 4. 保持当前调用的输出仍为 {"sales": 1500, "tech": 1500}。
    # 5. 新增一次调用：target_status="cancelled"，预期输出为 {"sales": 500}。
    # 6. 新增空列表边界测试，预期输出为 {}。

    # 验收标准：三个结果均正确，并能解释 dict.get(key, 0) 中默认值 0 的作用。
    """
    # dict.get() 和直接用 dict[] 最大的区别是：key 不存在时，get() 不会报错。
    summary = {}
    for row in query_rows:
        if row["status"] == target_status:
            summary[row["department"]] = summary.get(row["department"], 0) + row["amount"]
    return summary


result = summarize_paid_amount(rows)
print(result)

result = summarize_paid_amount(rows, target_status="cancelled")
print(result)

result = summarize_paid_amount([])
print(result)
