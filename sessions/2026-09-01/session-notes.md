# Learning Session

## Meta

- Date: 2026-09-01
- Available time: 工作日约 1 小时
- Mode: Study
- Week / Phase: Week 1 / Python Core
- Domain: Python

## Goal

本次唯一主要目标：建立 `list / tuple / set / dict` 的最小选择模型，再理解 Day 2 输入校验代码。

## Starting Point

- 已有理解：能使用 `list`、`dict`、循环和函数完成汇总；对 `tuple`、`set` 的用途缺乏系统认识。
- 上次未完成：Day 2 输入校验的理解与验收。
- 相关代码：`learning/python/week01/day02_validate_query_rows.py`

## What Was Built / Changed

- 学习者反馈教学跨度过大；已调整为先讲知识、再读例子、最后编码。
- 已创建四种常用容器的最小知识讲义。
- 已关闭字典读取与赋值副作用的理解缺口，开始 Day 3 函数基础。
- 已完成 Day 3 函数执行预测：默认参数、显式覆盖和 `return` 理解正确；f-string 分隔符阅读有一次疏漏。
- 已创建 Day 3 最小编码练习，核心函数待学习者实现。
- 学习者已实现 `build_query_config` 且三个测试通过；Review 发现 `return` 后仍残留不可达的 `raise`，待亲手清理。
- 学习者已亲手删除过期 TODO 和不可达 `raise`，复测三个案例通过。
- 对 `raise` 的解释存在偏差：误认为它是报错说明；需确认它是主动抛出异常的控制流语句。
- 已通过最小执行预测纠正上述偏差：能准确说明 `raise` 中断函数，后续 `return` 与调用方 `print` 均不会执行。
- 已进入 Day 4，创建函数作用域短讲义和速查表；等待学习者完成执行预测。
- Day 4 作用域执行预测四题全部正确，进入无全局业务依赖的编码练习。
- 学习者已实现 Day 4 筛选函数，默认状态、指定状态和空列表三个测试通过；Review 待补全伪代码判断条件并清理过期脚手架。
- Day 4 最终验收通过：伪代码已补充筛选条件，旧 TODO / 异常脚手架已移除，三个案例复测通过。
- 根据学习证据决定在 Day 5 前增加一次 15～20 分钟闭卷巩固门槛；已创建“校验 → 筛选 → 汇总”综合题。
- 学习者闭卷完成综合题：五个案例全部通过；Review 确认校验、筛选、汇总、边界和输入不变性均正确，等待累计过程解释后评定 `Built-It`。
- 学习者准确解释 `sales` 首次走 `else` 写入 1200、再次走 `if` 累加 300 得到 1500；综合能力评定为 `Built-It`。
- 已进入 Day 5，创建 module、import 与 `__main__` 的短讲义和速查表；等待执行预测。
- Day 5 首次预测经纠正后，已能准确区分入口模块与被导入模块的 `__name__`，并给出精确输出；进入双文件模块化练习。
- 学习者完成双文件模块化：直接运行模块、运行消费端和纯 import 三项验收通过，import 无演示副作用。
- 学习者选择今天先做一次闭卷巩固再结束，不进入 Day 6；安排 3 题函数、作用域与模块化交错检索。
- 闭卷巩固评分 7/10：作用域题全对；参数题误多写默认值输出；模块题能判断顶层连接会执行，但对副作用应移动到函数体或保护块的表达不精确。
- 学习者明确教学偏好：以后每个学习日都要像今天一样预留巩固时间；已将固定机制写入根规则和 learning 专项规则。
- 学习者要求建立独立 Git 仓库，并在每个章节完成后记录一次提交；已添加 `.gitignore` 和持久提交规则，等待配置本仓库作者身份后创建基线提交。
- Day 5 首次预测理解入口保护不在导入时执行，但将被导入模块的 `__name__` 写成 `"__main__"`，且遗漏 `lower()` 的小写转换；待纠正。

## Learner-Written Core Code

- 学习者已实现 Day 2 校验函数，等待运行和理解验收。

## Understanding Check

- Explain: 正确说明 list 的有序可变、set 的去重与成员判断、dict 的 key-value、tuple 的结构固定；需校准 tuple 的主要选择依据
- Modify: 待完成
- Edge case: 缺少 `amount` 时只记录缺失错误，不触发 `KeyError`
- Result: Day 2 三个运行案例通过；缺失字段执行路径解释正确
- Explain（金额校验）: 正确解释 `isinstance` 判断失败后，`and` 会短路且不执行字符串与数字比较
- Explain（函数）: 正确解释必传参数、默认参数覆盖以及 `return` 与 `print` 的区别；需提高输出字符预测精度
- Modify（函数）: 已正确构造并返回配置字典；需删除 `return` 后的不可达代码才能完成验收
- Modify（函数）: 不可达代码已清理，三个测试复验通过
- Explain（异常）: 待区分 `raise` 主动抛异常与 `return` 结束函数
- Explain（作用域）: 正确区分同名全局变量、函数参数和函数局部变量，知道局部名字不能在函数外直接访问
- Explain（模块）: 纠正后能准确解释直接运行与 import 时 `__name__` 的区别，以及入口保护为何不在导入时执行
- End-of-day retrieval: 作用域稳定；显式参数覆盖和入口保护的缩进边界需下次做 2 分钟复测
- Modify（作用域）: 已将目标状态设计为显式参数，函数不读取全局业务状态；代码清理尚未完成
- Modify（作用域）: 代码清理完成，函数显式接收业务输入并通过三个案例

## Mastery Changes

| Topic | Before | After | Evidence |
|---|---|---|---|
| list / tuple / set / dict 选择 | Need-Practice | Understood-It | 四个场景选择全部正确，并给出基本理由 |
| isinstance / and 短路求值 | Need-Practice | Understood-It | 正确完成字符串金额的三步执行预测 |
| 函数参数 / 字典输入校验 | Need-Practice | Modified-It | 独立实现校验函数，运行通过并解释缺失字段分支 |
| 函数必传参数 / 默认参数 / return | Need-Practice | Modified-It | 独立实现函数、通过 3 个测试、清理不可达代码并解释控制流 |
| `raise` / `return` 执行顺序 | Need-Practice | Understood-It | 正确预测主动抛出异常后，函数与调用方后续语句均不执行 |
| 函数局部 / 全局作用域 | Need-Practice | Modified-It | 四个预测正确；独立实现无全局业务依赖的筛选函数并通过三个案例 |
| 校验 / 筛选 / 汇总综合能力 | Modified-It | Built-It | 闭卷独立实现综合函数，5 项测试通过并解释首次与再次累计过程 |
| module / import / `__main__` | Need-Practice | Understood-It | 两种运行方式的执行预测经一次纠正后全部准确 |
| module / import / `__main__` 编码 | Understood-It | Modified-It | 独立迁移业务函数、编写消费者，并正确添加两个入口保护 |

## Next Single Priority

下次先复测显式参数覆盖和导入副作用位置，再进入 Day 6 JSON。

## Session Close

- Day 2 输入校验：代码与三个测试通过，掌握等级 `Modified-It`。
- 容器选择：能根据顺序、可变性、成员判断和 key-value 选择类型，掌握等级 `Understood-It`。
- `isinstance` / `and` 短路：阅读预测通过，掌握等级 `Understood-It`。
- 字典读取与赋值：已能区分 `dict[key]`、`dict.get()` 和 `dict[key] = value`。
- 面试追问：7/10，标准回答已写入 `docs/interview_answer.md`。
- Day 3：函数代码预测已完成；进入最小编码练习。
- Day 4：闭卷综合题达到 `Built-It`。
- Day 5：双文件模块化达到 `Modified-It`，面试追问 9/10。
- 当日闭卷巩固：7/10，暴露两个次日复测点。

## Interview Follow-up

### Q1

- Question: 为什么输入校验通常先判断字段存在，再校验字段值？顺序反过来有什么问题？
- Learner answer: 正确指出反过来等于默认字段存在；误认为 `dict.get("key") = 120` 会创建 key。
- Score: 7/10
- Gap: `dict.get()` 只读取且不会创建 key；`dict[key] = value` 才执行赋值。

### Q2

- Question: 一个函数只 `print` 配置而没有显式 `return` 时，两次输出是什么、调用结果保存什么，为什么这种设计不适合作为 AI Tool 或后端业务函数？
- Learner answer: 正确预测字典和 `None`，说明 `print` 没有把业务数据交给调用变量，应改用 `return`。
- Score: 9/10
- Gap: 应精确表述为 `result` 明确保存了隐式返回值 `None`，而不是“没有保存任何东西”。

### Q3

- Question: 为什么应把 `target_status` 设计成函数参数，而不是让函数直接读取全局变量？至少说明两个工程影响。
- Learner answer: 正确指出全局变量可能在调用前被其他代码改变，参数化让行为更可控。
- Learner follow-up: 正确说明共享全局状态会让 A/B 请求都使用同一个筛选条件，而参数让每次调用保持独立。
- Score: 9/10
- Gap: 首次只覆盖全局状态不可预测性；经 A/B 请求变体后，已补充并发调用互相污染的风险。

### Q4

- Question: 入口保护是否意味着模块被 import 时整个文件都不执行？哪些内容仍执行，哪些不执行？
- Learner answer: 正确指出 DEMO_ROWS 会绑定、两个函数会被创建，保护块中的 main() 调用不执行。
- Score: 9/10
- Gap: “函数生成”应精确表达为执行 `def` 并创建函数对象；函数体尚未执行，`if` 条件本身仍会求值。

## Files Updated

- `learning/python/AGENTS.md`
- `learning/python/lessons/0002-choose-container-types.html`
- `learning/python/lessons/0003-function-input-output.html`
- `learning/python/week01/day03_build_query_config.py`
- `learning/python/lessons/0004-function-scope.html`
- `learning/python/reference/function-scope-quick-reference.html`
- `learning/python/week01/day04_filter_orders_by_status.py`
- `learning/python/week01/day04_consolidation_challenge.py`
- `learning/python/lessons/0005-modules-import-main.html`
- `learning/python/reference/modules-import-main-quick-reference.html`
- `learning/python/week01/day05_modules/order_summary.py`
- `learning/python/week01/day05_modules/use_order_summary.py`
- `sessions/2026-09-01/session-notes.md`
- `progress/ai-learning-tracker.md`
- `AGENTS.md`
- `learning/AGENTS.md`
- `.gitignore`
