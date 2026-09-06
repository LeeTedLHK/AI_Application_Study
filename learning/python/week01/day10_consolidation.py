"""Day 10 每日闭卷巩固：class、实例状态与异常传播。

首次作答要求：不运行代码，写出预测并说明理由。

题 1：两个 QueryTask 实例中，只对 task_b 调用 update_limit(3)。预测
task_a.limit、task_b.limit 和调用返回值。区分对象状态与方法返回值。

题 2：RetrievalTask.__init__ 保存 self.query，但 to_payload 使用裸变量
query。定位失败操作、异常类型，并只修改一个位置修复。

题 3：ConfigTask.load 抛出 FileNotFoundError，外层只捕获
json.JSONDecodeError。判断异常分支、result 赋值、后续 print 与最终传播。

实际题面、首次答案、反馈与新数据复测结果记录在当日 session notes。
"""
