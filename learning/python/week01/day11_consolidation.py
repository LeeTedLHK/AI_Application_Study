"""Day 11 每日闭卷巩固：iterator、generator 与 yield。

要求：
- 不运行代码，先写出预测；
- 每题说明理由，不只写最终结果；
- 不修改本文件；
- 本组不引入自定义迭代器、生成器表达式或异步生成器。

题 1：执行预测
- 生成器函数先打印 start，再 yield "orders"，随后打印 resume 并 yield "events"。
- 创建生成器后先打印 created，再依次调用两次 next。
- 问题：准确输出顺序是什么？创建生成器时函数体是否执行？

题 2：单次消费改错
- table_iterator 是包含 orders、events 的生成器。
- 第一次 list(table_iterator) 用于预览；随后再次 for table in table_iterator。
- 问题：第二次循环为何没有内容？给出“重新创建生成器”和“保存为 list”两种修复思路及取舍。

题 3：AI 数据流选择
- 数据库有 100 万行，只需找到前 20 个匹配结果就停止。
- 问题：选择 list 还是 generator？它一定更快吗？什么条件下才能避免读取剩余数据？
"""
