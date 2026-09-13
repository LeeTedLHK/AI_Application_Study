# 2026-09-13 学习记录

## Day 17 开场

- 承接 Day 16 的 Enum 成员 / `.value` 间隔复测。学习者先答错了显式传入的模式，反馈后准确改为 `job.mode = Mode.FAST`（类型 `Mode`）与 `job.mode.value = "fast"`（类型 `str`）。
- 进入 Pydantic v2：当前环境版本为 2.13.4；已查阅官方模型与字段文档。
- 核心心智模型：外部字典 → `BaseModel.model_validate` → 运行时解析/校验 → 已验证模型 → `model_dump()`。
- 已创建 Day 17 讲义、速查和练习脚手架；等待学习者完成四个调用的闭卷预测，再独立实现核心模型。


## Day 17 预测、实现与验收

- 四个阅读预测 4/4：默认 `limit=100`；`"20"` 解析为 `20`（`int`）；`-1` 因 `ge=0` 失败；缺少 `table_name` 失败。
- 学习者独立补齐 `QueryInput` 与 `normalize_query`，使用 `Field(default=100, ge=0, le=1000)` 和 `QueryInput.model_validate(data)`；没有在函数内重复手写范围判断。
- 自动断言通过：默认值、字符串数字转换、`0/1000` 合法、`-1/1001` 失败、缺少必填字段失败、`"abc"` 解析失败、`model_dump()` 结构正确、模块导入静默。
- 学习者把演示中的宽泛 `except Exception` 改为精确 `except ValidationError`；`normalize_query` 保持传播异常。学习者自行选择将主程序中的 `"abc"` 演示行注释，保留函数层面的异常传播由独立断言验证；直接运行因此退出码为 0。

## Day 17 原理、面试与巩固

- 原理反馈评分 8.5/10：准确解释默认非严格模式会先尝试合理转换，范围由 `ge/le` 约束；补充后能区分普通类型标注、dataclass 与 BaseModel 的运行时行为，并定位 API/Tool 输入适配层负责转换错误响应。
- 面试题：Agent Tool 收到 `limit="20"` 时选择自动转换还是严格模式。评分 8/10；学习者能按数据来源和业务契约权衡，补充强调严格模式适用于不稳定 LLM/用户输入和高风险 SQL 参数；类型转换不能替代范围、权限、只读和 SQL guardrail。
- 闭卷巩固 3/3：`0` 是合法 `int`；`1001` 超出 `le=1000` 失败；返回 `{}` 会破坏 `QueryInput` 返回契约并把错误延迟为属性访问处的 `AttributeError`。
- Day 17 限定范围达到 Modified-It：学习者能独立建模、验证、修改异常处理并解释边界，可复用到 FastAPI 请求模型和 Agent Tool 输入边界。
## Tracker 补全维护

- 学习者指出 `progress/ai-learning-tracker.md` 到 Day 17 后存在遗漏。已对照全部 session notes、`learning/python/` 练习/测试文件和 Git 历史核对 Day 1～17。
- tracker 新增“章节索引”和“每日巩固索引”，补入 Day 12～17 的 Week 1 总结，并明确 Day 1～5 随早期基线提交保存、Day 6 起的章节提交哈希。
- 原有 Python 细粒度主题、Knowledge Gaps、Weekly Interview Performance 和历史记录保留不删。