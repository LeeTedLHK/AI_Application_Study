# 2026-09-17 学习记录｜Day 19 logging

> 最终状态：Day 19 已完成；掌握等级 Modified-It。面试 7/10；每日巩固首次 9/10，纠错通过。下一步先复测 logging 职责边界，再进入 pytest。

## 开场复测

- 能判断 `override=False` 保留已有进程变量，缺失时由 `.env` 填充。
- 初答只说把加载与打印放入函数；补写后能使用 `main()` 与 `if __name__ == "__main__":` 避免导入副作用。
- 主动实测 `from query_service import run_query` 与 `import query_service` 的名称绑定区别：后者必须通过 `query_service.run_query()` 调用，继续写裸 `run_query()` 会触发 `NameError`。

## logging 基础

- 准确判断 INFO 门槛过滤 DEBUG，DEBUG 门槛输出 DEBUG / INFO / WARNING。
- 补准日志格式包含 levelname、logger name 与 message，不应把日志调用表述成 print。
- 能解释应用入口统一 `basicConfig`，业务模块使用 `getLogger(__name__)`。
- 独立完成 `run_query`：100 路径 INFO → INFO；500/600 路径 INFO → WARNING → INFO；返回字典、参数化日志和导入静默通过。

## 异常日志

- 能区分 `logger.error()` 与 `logger.exception()`：后者在 except 中附带 traceback。
- 能区分捕获、记录和重新传播；明确 `logger.exception()` 不等于 `raise`。
- 独立完成 `parse_query_limit`：正常、0、空字符串和 abc 行为断言通过，非法输入记录 traceback 并返回 None，调用方继续执行。
- 根据 Review 将 try 缩小到仅包含 `int(raw_limit)`，成功日志和 return 移到 try/except 之后；复验 4/4 通过。

## 面试

- 得分：7/10。
- 正确：traceback 差异；根据 `int | None` 与 `int` 契约选择返回 None 或 raise。
- 缺口：未完整说明 logging 的级别、格式和路由价值；日志上下文只指出排除 API Key，遗漏应保留的 request_id、table_name、失败 limit；初答错误地用测试和内存占用解释控制流选择。
- 标准回答已追加到 `docs/interview_answer.md`。

## 每日巩固

- Q1 正确筛选出 WARNING 与 ERROR，但首次遗漏格式中的级别前缀，对门槛的解释也不够精确。
- Q2 准确判断 `logger.exception` 记录 ERROR 与 traceback，`raise` 继续传播，`done` 不执行且 `limit` 不完成赋值。
- Q3 准确判断仅导入不执行函数体；保留 request_id、table_name、limit，排除 API Key；由应用入口统一配置 `basicConfig`。
- 首次得分 9/10。纠错后准确说明 WARNING 是最低门槛，DEBUG / INFO 被过滤，WARNING 及以上可输出。

## 最终验证与结论

- 巩固 Q1 实际输出为 WARNING、ERROR；Q2 实际记录 ERROR 与 traceback，进程退出码为 1。
- 查询与解析行为断言 6/6 通过；所有 Week 2 Python 文件逐一编译通过；模块导入静默。
- 仓库完整回归 24/24 通过。
- 掌握等级：Modified-It。实现、修改、失败路径、解释和变体均有证据；安全上下文与 `None` / `raise` 决策的首次表达仍不稳定，不升级为 Built-It。
- 项目复用：后续 RAG、Tool、SQL 与 Agent 请求可统一记录模块、请求上下文与异常 traceback；敏感字段必须排除。
- 下一步唯一优先任务：约 2 分钟复测 `basicConfig`、`getLogger`、`logger.exception`、`raise` 的职责，再进入 pytest。
