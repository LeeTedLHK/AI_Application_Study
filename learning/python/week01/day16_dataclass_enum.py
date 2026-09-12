"""Day 16：dataclass 与 enum——先预测，再亲手补齐。

第一阶段（先在对话中回答，不运行）：
1. 预测 QueryPlan("orders") 的 repr 中会出现哪些字段和值。
2. 预测 plan = QueryPlan("orders"); plan.limit 和 plan.mode.value 的值。
3. `@dataclass` 会因为 table_name: str 自动拒绝 QueryPlan(123) 吗？

第二阶段（回答后再实现）：
补齐 QueryPlan 的三个字段和 plan_label 函数。
要求：
- QueryMode 只有 PREVIEW="preview" 与 EXECUTE="execute"；
- QueryPlan 字段依次为 table_name: str（必传）、limit: int = 100、
  mode: QueryMode = QueryMode.PREVIEW；
- plan_label(plan) 返回 `"<mode>:<table_name>:<limit>"`，例如
  `preview:orders:100`；
- 不新增运行时类型校验，不把 123 转成字符串；
- 模块导入无输出。

验收：预测准确；亲手实现后验证默认计划和 EXECUTE / 自定义 limit 计划；
能解释 dataclass 生成了什么、Enum 成员与 .value 的区别、标注为何仍不等于校验。
核心实现由学习者完成，文件不提供标准答案。
"""

from dataclasses import dataclass
from enum import Enum


class QueryMode(Enum):
    PREVIEW = "preview"
    EXECUTE = "execute"


@dataclass
class QueryPlan:
    table_name: str
    limit: int = 100
    mode: QueryMode = QueryMode.PREVIEW


def plan_label(plan: QueryPlan) -> str:
    return f"{plan.mode.value}:{plan.table_name}:{plan.limit}"

if __name__ == "__main__":
    default_plan = QueryPlan("orders")
    print(default_plan)
    print(plan_label(default_plan))

    execute_plan = QueryPlan("customers", limit=50, mode=QueryMode.EXECUTE)
    print(execute_plan)
    print(plan_label(execute_plan))
