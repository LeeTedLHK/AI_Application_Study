"""Day 11 亲手练习：用生成器逐个产出启用的表名。

业务目标：
AI 后端读取多份查询配置时，只把 active=True 的 table_name 逐个交给
后续处理。调用方既可以使用 next() 取一个，也可以使用 for / list 消费。

输入：
- configs：由配置字典组成的 list；
- 每个字典都包含 table_name（str）和 active（bool）。

输出契约：
- 按输入顺序逐个 yield active=True 的 table_name；
- active=False 的配置不产出值；
- 空 list 不产出任何值，生成器自然结束。

约束：
- 使用 for、if 和 yield；
- 不创建结果 list，不使用 append，不 return 一个完整容器；
- 不打印，不修改输入 configs；
- 本课暂不编写自定义 __iter__ / __next__，也不引入异步生成器。

动手顺序：
1. 先写三行伪代码：遍历 → 判断 active → 产出 table_name；
2. 删除函数中的占位产出，完成核心逻辑；
3. 运行 test_day11_active_table_generator.py。

验收：
三个测试全部通过；能解释调用生成器函数、第一次 next、yield 暂停和耗尽
时 StopIteration 的执行顺序。
"""


def iter_active_table_names(configs):
    """按输入顺序逐个产出启用配置的表名。"""
    for config in configs:
        if config["active"]:
            yield config["table_name"]
