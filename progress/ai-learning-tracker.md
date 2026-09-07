# AI Application Engineer Learning Tracker

> 全局唯一学习进度来源。

## 当前状态

- 当前日期：2026-09-08
- 当前 Week：Week 1
- 当前 Phase：Python Core
- 当前主目标：Day 11 iterator / generator / yield 已完成；Day 1～10 的长期目录已确认为 `learning/python/demo`，迁移路径维护完成
- 下一步唯一优先任务：用约 2 分钟复测 generator 性能条件与单次消费，随后进入 decorator
- 上次周测日期：
- 上次阶段 Mock：

## 12 周路线

远程归档：2026-09-03 已创建私有仓库 https://github.com/LeeTedLHK/AI_Application_Study ，origin/main 已验证与本地 Day 6 提交 feebccb3a74ca73027960a3bd43392ae4553458d 一致。Day 7 本地提交为 7375edd，Day 8 为 ae8eb97；Day 9 本轮只创建本地章节提交，不自动推送。其他未跟踪文件不纳入。

| Week | 主题 | 状态 | 主要产物 |
|---|---|---|---|
| 1 | Python Core | 进行中 | Day 1～4 综合能力 `Built-It`；Day 5～7 模块、JSON、文件读取通过；Day 8～11 traceback、精确异常捕获、class、generator 与巩固通过，`Modified-It` |
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
| Python 对象 / JSON 文本 | Modified-It | Day 6 实现、测试与解释通过；9 月 3 日补测准确回答 False / False、bool / str，区分相同显示与不同类型 | 字符串 / 布尔值经反馈后提取正确，保留收尾及跨日复测，不据此升级 |
| JSON 文件读取 / open / with | Modified-It | 学习者实现 load_query_config，9 月 4 日复跑 3 个测试通过、导入静默；亲手修正巩固题缩进并经实际运行验证；三题巩固 10/10 | 已能实现、解释并修改失败变体；不据当日表现判定长期掌握，下次复测关闭时机与返回对象区别 |
| exception / traceback | Modified-It | 9 月 5 日独立分两轮修复 challenge 的路径与 JSON；准确解释解析器在读到下一行右花括号时才确认尾随逗号后缺少字段；最终输出正确，Day 8 测试 1/1、Day 7 回归 3/3 通过 | 面试追问曾先检查上层调用行；下次间隔复测“最后一行 → 最近的自己代码 → 向上追输入”的顺序，再进入最小异常处理 |
| specific try / except | Modified-It | 独立实现成功、文件不存在、JSON 非法三条结构化返回路径；Day 9 测试 3/3、Day 7 回归 3/3 通过；面试能解释宽泛捕获掩盖根因 | 完成当日交错巩固；下次复测未匹配异常传播，不提前扩展 finally |

| class / instance / self | Modified-It | 独立实现 QueryTask 的 __init__、to_payload、update_limit；Day 10 测试 4/4，通过实例隔离与 limit=0 边界；面试 9/10 | Day 11 开场变体最终准确解释参数求值、self 绑定、实例状态与隐式返回值，跨日缺口关闭 |
| iterator / generator / yield | Modified-It | 独立实现 iter_active_table_names；顺序筛选、消费位置、空输入测试 3/3；能解释延迟执行、yield 暂停与单次消费 | 面试误认为 generator 一定更快；下次复测上游惰性、提前停止与重复读取的条件 |

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

- 知识层面暂无 Significant 缺口。Day 8 的入口、调用、失败操作与 JSON 文本检测位置已在反馈和巩固中补准，保留跨日复测。

### Minor

- 2026-09-08 Day 11：面试中一度认为 generator 一定更快。已补准 generator 只保证按需产出；只有上游也延迟读取且调用方提前停止，才可能避免剩余 I/O 与计算。下次用新场景间隔复测。
- 2026-09-07 Day 10：首次巩固把 update_limit 修改后的实例属性与方法返回值混淆；经实际输出和逐步解释后，能说明 self.limit 更新为新值，而无显式 return 只使调用结果为 None。下次用新数据间隔复测。
- 2026-09-05 Day 9：巩固变体中一度认为不匹配的 FileNotFoundError 会由 JSONDecodeError 分支返回 None；即时纠错已通过，下次用新数据复测传播、赋值与后续语句三者关系。
- 2026-09-05 Day 8：一度把 path 改到业务内容不匹配的 day08_invalid_config.json；根据输出契约重新选择 challenge 配置后已解决。巩固中已补充“无异常还要比较 actual / expected 并运行测试”。
- 2026-09-05 Day 8：面试变体中先选择检查 app.py 上层调用行；标准顺序应先看最靠近底部的自己代码 return json.load(f)，再向上追到调用方提供的 path。下次做两分钟间隔复测。
- 2026-09-04：已完成返回对象纠错与 with 外读取失败的改错；关闭时机补准为“调用方拿到返回值前”。下次仍做两分钟间隔复测，不将当天通过等同于稳定掌握。
- 2026-09-03 曾误把 "false" 视为 bool；9 月 4 日交错题准确区分 False / bool 与 false / str。9 月 3 日完整收尾未开展，不追溯补记完成。

## Latest Daily Consolidation

- 2026-09-08 工程维护：学习者确认 `learning/python/demo` 是 Day 1～10 的长期目录。修复 demo 内 16 处旧 `week01` 路径引用；旧路径搜索清零，Day 1～10 回归 14/14、Day 11 回归 3/3 通过，无效 JSON 示例恢复为预期 `JSONDecodeError`。
- 2026-09-08 Day 11：三题首次闭卷 9/10。生成器执行顺序与 class 交错题正确；单次消费原因和两种修复均正确，内存与重复读取取舍表达需补准。面试 7/10，主要缺口是误认为 generator 一定更快。
- Day 11 最终验证：本章测试 3/3 通过，业务模块与巩固模块导入静默。扩展回归在最新 demo 目录中 10/11 通过；唯一失败来自先前目录迁移未更新 Day 8 硬编码数据路径，不属于 Day 11 代码，本轮未修改。
- Day 11 章节归档信息：learn(week01-day11): iterator generator yield；只纳入本章讲义、速查、练习、测试、巩固和相关记录，明确排除 test.py 与目录迁移修复，不推送远程。
- 2026-09-07 Day 10：三题首次闭卷 7/10。实例状态题误判输出，混淆属性更新与方法返回值；参数 / 实例属性改错和未匹配异常传播判断正确。反馈后借助真实输出补准，新数据 update_limit(0) 复测准确给出属性 0、调用结果 None。首次评分保留，下次间隔复测。
- Day 10 最终验证：本章测试 4/4、Day 9 回归 3/3、Day 8 回归 1/1、Day 7 回归 3/3，共 11/11 通过；Day 10 业务模块与巩固模块导入静默。掌握等级为 Modified-It。
- Day 10 章节归档信息：learn(week01-day10): class instance state；只纳入本章讲义、速查、练习、测试、巩固和相关记录，不推送远程。
- 2026-09-05 Day 9：三题首次闭卷 7/10。成功路径与两个精确异常分支判断正确；未匹配异常题误认为会返回 None。反馈后纠错 3/3，能说明 result 不赋值、后续 print 不执行、FileNotFoundError 原样传播。首次评分保留，下次间隔复测。
- Day 9 最终验证：本章 3/3、Day 8 回归 1/1、Day 7 回归 3/3 通过；三个 Day 9 模块导入静默；临时 NameError 传播探针显示原类型与信息均未被吞掉。掌握等级保持 Modified-It。
- Day 9 章节归档信息：learn(week01-day09): specific exception handling；只纳入本章讲义、速查、练习、测试与相关记录，不推送远程。
- 2026-09-05：Day 8 三题闭卷巩固完成，9/10。能从 traceback 底部开始、预测 start 后抛出 FileNotFoundError 且 finish 不执行，并判断改路径后无异常仍需核对结果和测试。表达补准：输出是 start；完整顺序先读最后一行异常，再看最近的自己代码，最后向上追调用与输入。
- Day 8 面试 8/10，巩固 9/10；综合独立分步 Debug、解释和测试证据，掌握等级提升为 Modified-It，不据即时高分升级为长期稳定掌握。
- Day 8 章节归档信息：learn(week01-day08): exception and traceback debugging；只纳入本章代码、数据、讲义、测试及相关学习记录，不纳入 Day 6 修改和其他未跟踪文件，本次不推送远程。
- 2026-09-04：day07_consolidation.py 三题巩固完成，10/10。准确预测 False / false / 0 及 bool / str / int；定位 with 外读取失败并亲手修正缩进；准确预测 loading / 0 / None 与显式参数覆盖。
- 本次复核：Day 7 三个测试通过；从题面提取已修改代码在临时配置上执行，Q1～Q3 均符合预期；业务模块导入无输出。掌握等级根据实现、解释和实际改错共同提升至 Modified-It，并非仅凭巩固分数。
- Day 7 章节归档信息：`learn(week01-day07): JSON file reading and resource lifetime`；具体提交哈希以 Git 日志为准。本章文件外的 Day 6 改动和旧章节未跟踪文件不纳入。
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
| 2026-09-04 | JSON 文件读取与资源生命周期 | 7/10 | 原题正确；首次变体遗漏已关闭状态 | 原面试评分保留；后续纠错、实际改错和三题巩固通过（巩固另计 10/10），下次间隔复测 |
| 2026-09-05 | 异常与 traceback 阅读 | 8/10 | 变体中先检查上层 app 调用行，而非最近的自己代码失败行 | 下次复测“异常详情 → 最近的自己代码 → 向上追输入”，再学习最小异常处理 |
| 2026-09-05 | 精确异常捕获 | 9/10 | 核心风险解释完整；可进一步从调用方动作和监控分类说明影响 | 巩固未匹配异常传播；后续在 API 错误映射中复用 |
| 2026-09-07 | class、实例与状态 | 9/10 | 一度认为普通字典无法同时表示多个对象 | 补准字典可有多份；class 的优势是为明确领域概念集中状态与行为 |
| 2026-09-08 | iterator、generator 与 yield | 7/10 | 误认为 generator 一定更快 | 复测上游惰性、提前停止、峰值内存与重复读取成本的条件 |

## Recently Resolved Gaps

| Date | Gap | Evidence |
|---|---|---|
| 2026-09-08 | Day 1～10 移入长期 `demo` 目录后仍残留旧 `week01` 路径 | 修复 16 处代码与运行说明引用；旧路径搜索清零，Day 1～10 14/14、Day 11 3/3 测试通过 |
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
| 2026-09-05 | 区分 traceback 的入口、调用、失败操作与 JSON 检测位置 | 能复述入口调用 main、main 调用加载函数、json.load 触发解析；并解释解析器在读到右花括号时才确认前一行尾随逗号导致语法无法继续 |
| 2026-09-07 | 区分异常未匹配、向上传播与顶层 traceback | 新变体准确预测上层捕获 FileNotFoundError 后输出 missing、finish，无 traceback，config 与 result 赋值均未完成 |
| 2026-09-08 | 区分实例状态修改、参数求值与方法返回值 | 新变体准确预测 first 改为 1、second 保留调用时接收的 9、received 为 None，并说明参数接收的是当时求出的值 |
