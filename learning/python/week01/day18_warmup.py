"""Day 18 开场复测：Pydantic 默认值、转换与校验边界（约 2 分钟）。

沿用 Day 17 QueryInput，当前环境 Pydantic 2.13.4，默认非严格模式。
输入：下方三个独立调用；每个调用单独考虑，不受前一个是否失败影响。
任务：先不运行、不查讲义，在聊天中回答每次调用得到的 limit 值及类型，
或是否抛出 ValidationError；解释为什么第三个调用会或不会改用默认值 100。
约束：不修改模型，不添加捕获异常后返回默认值的逻辑。
验收：能区分缺失字段、可转换的输入和范围校验失败，再进入 .env 配置管理。

1. QueryInput.model_validate({"table_name": "reports"})
2. QueryInput.model_validate({"table_name": "reports", "limit": "0"})
3. QueryInput.model_validate({"table_name": "reports", "limit": "1001"})

复测只保存题面，不自动执行，以免提前展示答案。
参考：https://docs.pydantic.dev/latest/concepts/models/
"""

from day17_pydantic_basemodel import QueryInput
