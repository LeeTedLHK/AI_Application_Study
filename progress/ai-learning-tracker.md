# AI Application Engineer Learning Tracker

> 全局唯一学习进度来源。

## 当前状态

- 当前日期：2026-09-03（Day 6 归档维护；未开展新课）
- 当前 Week：Week 1
- 当前 Phase：Python Core
- 当前主目标：Day 6 JSON 代码、解释、面试与每日巩固已验收
- 下一步唯一优先任务：下次先用约 2 分钟闭卷复测 JSON 严格语法与返回类型，再进入 JSON 文件读写
- 上次周测日期：
- 上次阶段 Mock：

## 12 周路线

| Week | 主题 | 状态 | 主要产物 |
|---|---|---|---|
| 1 | Python Core | 进行中 | Day 1～4 综合能力 `Built-It`；Day 5 模块化通过；Day 6 JSON 代码、解释与巩固通过 |
| 2 | Python Engineering / Async | 未开始 | |
| 3 | FastAPI / Backend | 未开始 | |
| 4 | LLM API / Tool Calling | 未开始 | |
| 5 | Baseline RAG | 未开始 | |
| 6 | Retrieval Engineering | 未开始 | |
| 7 | RAG Evaluation | 未开始 | |
| 8 | Hand-written Agent Loop | 未开始 | |
| 9 | OpenAI Agents SDK | 未开始 | |
| 10 | MCP / Agent Engineering | 未开始 | |
| 11 | Intelligent Query Agent | 未开始 | |
| 12 | Project / Interview | 未开始 | |

## 掌握等级

- Need-Practice
- Understood-It
- Modified-It
- Built-It
- Interview-Ready

## Python

| Topic | Level | Evidence | Gap / Next |
|---|---|---|---|
| list / dict / for / if / function | Modified-It | 独立完成 `day01_query_rows.py`，通过 paid、cancelled、空列表案例 | 巩固 `dict.get` 找到已有 key 时返回累计值，而非默认值 |
| 函数参数 / 字典输入校验 | Modified-It | 独立实现 `day02_validate_query_rows.py`，三个案例通过并正确解释缺失字段控制流 | 完成面试表达；后续增加一个新边界情况 |
| list / tuple / set / dict 选择 | Understood-It | 正确完成四个场景判断并给出基本理由 | tuple 的关键选择依据是固定、有序，而非允许重复 |
| isinstance / and 短路求值 | Understood-It | 正确判断字符串金额使左侧为 False、右侧不执行、整体为 False | 在后续输入校验中继续运用 |
| 函数必传参数 / 默认参数 / return | Modified-It | 已实现函数；9 月 2 日复测准确预测显式 20 覆盖默认值，隐式返回 None | 后续任务中继续间隔复习 |
| 函数局部 / 全局作用域 | Modified-It | 独立实现显式接收状态参数的筛选函数，3 个测试通过；面试追问能解释隐藏依赖和并发请求污染 | 后续在 FastAPI / Agent Tool 中继续验证 |
| 校验 / 筛选 / 汇总综合能力 | Built-It | 闭卷独立实现 `summarize_valid_orders`，5 项测试通过；准确解释部门首次写入与再次累计的分支和数值变化 | 后续在模块化与真实项目中复用 |
| module / import / `__main__` | Modified-It | 已完成双文件模块化；9 月 2 日复测准确区分函数体与模块顶层调用 | 后续任务中继续复用 |
| Python 对象 / JSON 文本 | Modified-It | 学习者实现 update_query_limit，收尾复跑 3 个测试通过；解释类型路径及调用方类型错误；交错巩固 3/3 正确；9 月 3 日已自行修正注释 | 保持 Modified-It，不以同日满分代替长期掌握；下次先复测 |

## Backend

| Topic | Level | Evidence | Gap / Next |
|---|---|---|---|

## LLM Application

| Topic | Level | Evidence | Gap / Next |
|---|---|---|---|

## RAG

| Topic | Level | Evidence | Gap / Next |
|---|---|---|---|

## Agent / MCP

| Topic | Level | Evidence | Gap / Next |
|---|---|---|---|

## Project A — Enterprise Data Knowledge Assistant

- Current milestone:
- Last demo:
- Current blockers:
- Eval status:

## Project B — Intelligent Query Agent

- Current milestone:
- Last demo:
- Current blockers:
- Eval status:

## Knowledge Gaps

### Blocker

### Significant

### Minor

- 本次巩固未暴露新的概念缺口；JSON 大小写与引号两项已通过当日独立复测，仍需跨日提取验证。

## Latest Daily Consolidation

- 2026-09-02：三道交错题全部正确，10/10；覆盖 JSON / Python 值、合法文本、模块导入、显式 0、隐式返回 None。
- 未用巩固满分自动升级掌握等级；下次先用新数据复测严格 JSON 语法与返回类型。
- 2026-09-03 归档维护：用户指定的作者身份已写入本仓库；仅使用针对本仓库的命令级信任例外，未更改全局配置。三个测试复跑通过，注释已由学习者修正。
- 本章归档标识：`learn(week01-day06): JSON serialization and query config`；提交记录以 Git 日志为准。仅归档本章文件和必要的忽略规则，其他未跟踪文件保留原样。


## Weekly Interview Performance

| Date | Scope | Score | Weakness | Follow-up |
|---|---|---:|---|---|
| 2026-09-01 | Python 输入校验 | 7/10 | 误认为 `dict.get()` 会创建 key | 用最小例子区分读取与赋值 |
| 2026-09-01 | Python 函数返回值 | 9/10 | 对“`result` 保存 `None`”的表达可更精确 | Day 4 继续训练函数作用域与低耦合设计 |
| 2026-09-01 | Python 函数作用域 | 9/10 | 首次回答只覆盖一个工程影响 | 通过并发请求变体补全共享状态污染风险 |
| 2026-09-01 | Python 模块与入口保护 | 9/10 | “函数生成”术语不够精确 | 用“执行 def 并创建函数对象，函数体未调用”表达 |
| 2026-09-02 | JSON 返回类型与调用约定 | 9/10 | 首次解释侧重测试要求 | 追问已准确解释调用方 loads 不接受 dict；后续从接口约定直接作答 |

## Recently Resolved Gaps

| Date | Gap | Evidence |
|---|---|---|
| 2026-08-31 | 理解 `dict.get(key, default)` 的默认值只在 key 缺失时生效 | 能正确判断直接累计缺失 key 会失败，并完成三个运行案例 |
| 2026-09-01 | 区分字典缺失读取、`get()` 和赋值的副作用 | 正确预测 `get()` 返回 None 且不修改字典，赋值后才创建 key |
| 2026-09-01 | 区分 `raise` 主动抛出异常与 `return` 结束函数 | 正确预测 `raise` 后的 `return` 和调用方 `print` 均不会执行 |
| 2026-09-01 | 区分函数内部 `print` 与向调用方 `return` | 正确预测隐式返回 `None`，并说明业务结果应通过 `return` 传递 |
| 2026-09-01 | 解释参数化相对全局业务状态的工程价值 | 能说明隐藏状态可能被修改，并通过 A/B 请求变体解释并发污染 |
| 2026-09-01 | 验证 Day 1～4 知识的独立提取能力 | 闭卷完成校验、筛选、汇总综合题，5 项测试通过并解释累计过程 |
| 2026-09-01 | 区分直接运行与被导入模块的 `__name__` | 纠正后能准确给出两种运行方式的模块名、入口保护行为和输出顺序 |
| 2026-09-01 | 理解入口保护的作用边界 | 能说明 import 仍绑定常量并创建函数对象，只有保护块内的 `main()` 调用不执行 |
| 2026-09-02 | 显式参数覆盖与导入副作用位置的次日提取 | 准确预测 20 / None，并说明模块顶层连接与 main 函数体连接的差别 |
| 2026-09-02 | JSON 大小写、双引号及返回值的当日独立提取 | 巩固准确预测 True / None 与 JSON true / null；逐一解释单引号 key 和 False 非法；综合题准确预测 loaded、limit 0、None |
