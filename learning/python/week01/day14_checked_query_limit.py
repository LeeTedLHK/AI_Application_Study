"""Day 14：查询条数校验——先给思路，再亲手实现。

业务目标：给查询函数明确类型约定，并实际拒绝不合法的条数。
任务：补齐 checked_query_limit 的参数和返回值标注，以及函数体。
参数 limit 期望 int，默认值 10；返回值期望 int。
规则：
1. 非整数抛出 TypeError，信息为 'limit must be an integer'。
2. 整数小于 0 时抛出 ValueError，信息为 'limit must be non-negative'。
3. 合法整数原样返回；0 合法，不能替换为默认值。
输入范围：本题只考整数（不含 bool）、字符串和 None。
约束：不将字符串转换为整数，不捕获并吞掉异常；核心逻辑自己写。
验收案例：
  checked_query_limit() -> 10
  checked_query_limit(0) -> 0
  checked_query_limit(25) -> 25
  checked_query_limit(-1) -> ValueError
  checked_query_limit('25') -> TypeError
  checked_query_limit(None) -> TypeError
验收还包括：标注准确、默认值保留、模块导入无输出；解释标注与校验的分工。
开始前：在对话中说明校验顺序与原因，不必先写代码。
完成后：可在 __main__ 保护中自行验证，也可从其他脚本导入调用。
"""


def checked_query_limit(limit:int=10) -> int:
    if not isinstance(limit, int):
        raise TypeError('limit must be an integer')
    if limit < 0:
        raise ValueError('limit must be non-negative')
    return limit


if __name__ == "__main__":
    # 可在此处自行验证，也可从其他脚本导入调用。
    print(checked_query_limit())      # 10
    print(checked_query_limit(0))     # 0
    print(checked_query_limit(25))    # 25
    try:
        checked_query_limit(-1)        # ValueError
    except ValueError as e:
        print(e)
    try:
        checked_query_limit('25')      # TypeError
    except TypeError as e:
        print(e)
    try:
        checked_query_limit(None)       # TypeError
    except TypeError as e:
        print(e)