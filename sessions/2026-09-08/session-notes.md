# Learning Session

## Meta

- Date: 2026-09-08
- Mode: Study
- Week / Phase: Week 1 / Python Core / Day 11
- Domain: iterator / generator / yield
- 说明：本章于 2026-09-07 开始，跨日继续。

## Starting Point

- Day 10 class 最小对象模型已归档。
- 开场复测对象状态修改与隐式返回 None；随后进入 iterator / generator。

## Day 10 Spaced Retrieval

- 首次新变体准确判断方法隐式返回 None、修改目标为 task_a，但误判 task_a.limit 仍为旧值 5。
- 经参数求值链纠错后，能说明 self 指向点号左边的 task_a，new_limit 接收 task_b.limit 当时求出的值 2。
- 新变体中准确预测 first 后续改为 1、second 保留首次接收的 9、received 为 None。缺口关闭。

## Iterator / Generator Learning

- iterator 预测正确：for 自动把 StopIteration 当作迭代结束。
- generator 首次执行顺序混淆 resume 与 yield 20 的先后；反馈后准确给出 resume、20、before-last、end。
- 独立实现 iter_active_table_names：按顺序遍历配置、筛选 active=True、逐个 yield table_name。
- 初始三个测试通过：顺序筛选、同一生成器 next 后从原位置继续、空输入不产出。
- 延迟执行检查中首次认为创建生成器就会遍历；反馈后补准创建时读取 0 个配置，第一次 next 为找到 orders 检查两个配置。
- 能解释同一生成器耗尽后再次 list 得到空列表；若需重读必须重新创建，或在数据量可控且需要反复遍历时保存为 list。

## Interview Check

- 问题：RAG 服务从 100 万个文档块中找到前 100 个结果后停止，为什么 generator 可能更合适；是否一定更快；反复遍历三次如何选择。
- 学习者正确覆盖峰值内存、generator 单次消费和 list 可重复遍历，但误认为 generator 一定更快。
- 评分：7/10。标准答案在首次作答后追加到 docs/interview_answer.md。

## Current Gap

- generator 只提供按需执行机制，不保证速度更快；只有上游也按需读取且调用方提前停止，才可能避免剩余 I/O 与计算。

## Next

- 完成三题每日闭卷巩固、清理过期注释、最终验证与章节归档。

## Daily Consolidation

- 三题首次闭卷 9/10。
- 题 1 准确预测 created、start、orders、middle、resume、events，并说明创建生成器时函数体不执行。
- 题 2 准确判断 preview = list(tables) 耗尽生成器；提出重新创建生成器和遍历已物化 preview 两种可运行修复。补准取舍：前者重复读取数据源，后者不重复读取但完整列表常驻内存。
- 题 3 准确预测 0、[3]、3，并判断 update_limit(3) 在 remaining = list(limits) 恢复生成器时执行。
- 巩固分数不自动升级掌握等级；结合独立实现、解释、空输入边界和变体表现，当前等级为 Modified-It。

## Review

- 学习者按 Review 反馈删除已失效的占位实现注释，核心函数只保留实际逻辑。
- 当前工作区另有 test.py 修改，与 Day 11 无关，章节归档时明确排除。

## Next Single Priority

- 先确认并修复最新 demo 目录迁移留下的旧 week01 路径，再用约 2 分钟复测“generator 不保证更快、耗尽后不能自动重用”，随后进入 decorator。

## Final Verification

- Day 11 三个测试全部通过：顺序筛选、同一生成器继续消费、空输入。
- 新进程导入 day11_active_table_generator 与 day11_consolidation，无 stdout / stderr。
- 扩展回归首次在 week01 运行时找不到 Day 7～10 测试；系统化诊断确认最新提交 8e5c839 已把这些文件移动到 learning/python/demo。
- 在正确的 demo 目录重跑：Day 7、9、10 测试通过；Day 8 因 day08_debug_challenge.py 仍硬编码旧 week01/data 路径而失败。合计 10/11 通过。
- 搜索发现 demo 内多个运行说明和三个脚本仍引用旧 week01 路径。该问题由先前目录迁移产生，不修改、不混入 Day 11 提交。
- 当前工作区另有 test.py 修改，明确排除。

## Git

- 章节提交信息：learn(week01-day11): iterator generator yield。
- 只纳入 Day 11 讲义、速查、练习、测试、巩固及 tracker、session、面试记录；不推送远程。
