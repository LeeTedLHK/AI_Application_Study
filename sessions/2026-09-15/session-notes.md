# 2026-09-15 学习记录｜Day 18

> 最终状态：Day 18 已完成并提交 `1b7db14`；掌握等级 Modified-It。面试 8/10；每日巩固首次 8/10，纠错通过。下次先用约 2 分钟复测配置优先级、空字符串的 `int_parsing` 与缺失键默认值，完成 Week 1 周测，再进入 Week 2 logging。以下保留学习过程中的阶段性“待完成”记录，以最终状态为准。

## Day 18 继续学习

- 承接 9 月 14 日已回答的开场复测：100/int、0/int、ValidationError，超范围不采用默认值，全部正确。上次工具中断未能及时保存，此处补记，不重复复测。
- 继续 os.environ / os.getenv 第一小节，尚未完成 .env 加载、编码、面试或每日巩固。
- 已补建 day18_env_reading.py 与 0018-env-configuration.html；只使用进程内演示变量，不读取密钥。
- 下一步唯一任务：完成变量为 "0"、不存在、空字符串的三个独立状态预测。
- 工具：普通入口仍因 .sandbox-bin ACL 错误无法启动；此次沙箱外审批恢复可用，用于仓库内教学文件操作，未修复普通入口。

## 环境变量读取复测与 .env 加载

- 学习者准确回答 "0"/str、"100"/str，以及空字符串不触发默认值，读取预测 3/3 通过。
- 开始显式 load_dotenv(path, override=False)：已有环境变量优先、缺失时从文件填充；配置加载不负责校验。
- 创建 day18_config/.env.example 与被忽略的 .env，仅含 DAY18_QUERY_LIMIT=25，无密钥；添加 day18_dotenv_demo.py 并更新讲义。
- 课堂示例预设进程值 "60"，文件值 25；待核对输出。下一步完成优先级三种输入预测，再由学习者设计配置函数。

## .env 优先级预测与编码题

- 三题首次作答：环境 "0" → "0"/str 正确；环境缺失 → 文件值 25 正确，但误判类型 int；环境 "abc" 不被文件 25 覆盖正确。
- 用当前 python-dotenv 1.2.2 运行独立变体：分别为 '0'/str、'25'/str、'abc'/str。补准加载文件值仍为文本，不自动变成 int。
- 模板和本地演示文件增加无密钥 DAY18_TABLE_NAME=reports；创建 day18_query_config.py 题面，要求学习者先说加载、读取、校验三步，再实现核心函数。
- 关键边界：limit 键缺失时由 QueryInput 默认 100；显式 None 并不等于缺失。尚未验收代码、面试或收尾巩固。

## 学习者实现与首次 Debug

- 学习者指出缺失 limit 不加入校验字典才会触发默认值，并在 day18_query_config.py 实现加载、读取、条件加入 limit、model_validate 的主路径。
- 首次运行失败：第 33 行 import QueryInput 导致 ModuleNotFoundError: No module named 'QueryInput'。目前还未运行到配置校验，不能宣称代码验收通过。
- 先让学习者根据 traceback 区分模块文件名与模块内部的类名，并亲手修正导入；随后再测正常与失败路径。

## 修复后行为验收

- 学习者将导入修正为 from day17_pydantic_basemodel import QueryInput；直接运行得到 {'table_name': 'reports', 'limit': 25}。
- Agent 用临时无密钥配置和隔离的进程环境验证六类行为：导入静默；文件值 reports/25；已有环境覆盖为 orders/0；缺失 limit 使用 100；非法 abc 和 1001 均传播 ValidationError；缺失 table_name 也传播 ValidationError。均通过。
- 核心数据流正确，暂未评分掌握等级。小范围维护建议：未使用的 BaseModel、Field 导入可清理；当前演示相对路径要求从仓库根目录运行。
- 下一步先进行面试主问题与一层追问，再做当天闭卷巩固；此时不创建完成提交。

## Day 18 面试过程（已完成）

- 主问题：智能取数服务的环境变量 DAY18_QUERY_LIMIT="abc"，本地 .env 写 DAY18_QUERY_LIMIT=25，程序用 load_dotenv(override=False)，然后交给你写的 QueryInput 校验。最终采用哪个原始值、会发生什么？为什么不能认为“加载配置成功”就代表“配置有效”？
- 标准答案只在学习者首次回答并完成追问评分后记录到 docs/interview_answer.md。
- 首次面试回答：最终读取 abc，报 ValidationError，因为 override=False。配置优先级与异常类型判断正确；尚未明确区分加载文本成功和后续类型/范围校验成功。
- 一层追问（待答）：如果环境变量 DAY18_QUERY_LIMIT 已存在但值为 ""，.env 仍为 25，override=False；你的函数最终会使用默认 100、文件值 25，还是报 ValidationError？解释每一步。
- 面试追问回答：环境变量空字符串保留，最终报 ValidationError；把失败原因描述成超出范围。实际隔离验证为 ValidationError，错误 type=int_parsing、loc=('limit',)，发生在整数解析阶段。
- 面试评分 8/10：优先级、空值与失败结果正确；需区分无法解析整数与整数越界。题目和标准答案已追加 docs/interview_answer.md。

## 每日巩固过程（已完成）

- 题目见 learning/python/week01/day18_consolidation.py：已有 "0" 的来源与类型、缺失 limit 的字典构建改错、配置校验失败与上下文管理器清理交错题。
- 下一步唯一任务：学习者闭卷完成三题并解释；核对后更新掌握等级与本章状态。首次答案前不展示标准结果。
- 每日巩固首次回答：Q1 "0"/str → 0/int 正确；Q2 正确判断字典含 limit=None 会触发 ValidationError，但建议 os.getenv(..., "100")，结果虽为 100，却让读取层提供默认值，未满足“由模型默认值生效、不伪造 100”的题目要求；Q3 正确判断 only True、会话关闭、done 不执行。
- Agent 隔离运行核对：Q1 '0'/str 与 0/int；Q2 含 None 的错误类型 int_type，显式 getenv 默认值虽能得到 100，但来源是读取层；Q3 仅打印 True。
- 首次巩固暂评 8/10；第 2 题需纠错：学习者沿用自己已写的 load_query_config 条件加入键的思路，口述并写出 2～3 行最小修改。纠错前不标记今日完成或创建章节提交。
- 第 2 题首次纠错尝试：建议把 os.getenv("DAY18_QUERY_LIMIT") 改为 os.getenv("DAY18_QUERY_LIMIT", None)。这两种调用在变量缺失时等价，均返回 None；若 data 字典仍包含 limit=None，Pydantic 仍报 int_type。
- 下一步改用局部骨架提示：先构建仅含 table_name 的 data，再在 raw 非 None 时加入 limit；学习者亲手补齐条件体。首次巩固 8/10 保留，尚未完成纠错。

## Day 18 收尾与章节验收

- 学习者在局部骨架提示后补出 data["limit"] = raw，确认仅在 raw 非 None 的分支执行；缺失时字典不含 limit，QueryInput 使用默认 100。纠错通过，首次巩固 8/10 保留。
- 核心实现由学习者完成，因首次 import QueryInput 错误曾启动失败；学习者亲手修正后独立行为六类通过。正常演示、dotenv 优先级和 os.getenv 示例均运行通过。
- 面试 8/10；能解释环境值优先和配置非法触发 ValidationError，空字符串错误类型 int_parsing 经实际运行补准。
- 掌握等级 Modified-It；近期仍需提示才能稳定区分 getenv 默认值、传入 None 与模型字段缺失，不升级为 Built-It。
- 可复用结论：该模式适用于 AI 服务/Agent 的本地配置读取及输入边界；示例只有无密钥演示值，没有真实连接、模型调用或密钥加载。
- 下次唯一优先任务：约 2 分钟间隔复测来源优先级、空字符串的解析失败及缺失键默认值；随后完成 Week 1 周测，再进入 Week 2 logging。
- 章节归档：仅提交 Day 18 讲义、示例、无密钥 .env.example、核心练习、巩固题、已评分面试记录、tracker 与本次 session notes；不纳入 test.py 或被忽略的 .env，不推送远程。提交信息 learn(week01-day18): env configuration and validation，哈希以 Git 日志为准。
- 已补充 Day 18 配置速查，并修正讲义中的阶段措辞；只整理教学资料，不改变学习者核心实现。
