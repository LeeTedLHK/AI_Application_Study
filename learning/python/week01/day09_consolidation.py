"""Day 9 每日巩固：精确异常捕获与近期知识交错。

要求：
- 闭卷作答，不运行代码后再猜；
- 写出精确输出或返回值，并说明关键控制流；
- 不修改本文件，也不引入 else、finally 或新的异常类型；
- 预计用时 10～15 分钟。

题目 1：执行预测
----------------

    import json

    print("start")
    try:
        config = json.loads('{"limit": 0,}')
        print("loaded")
    except FileNotFoundError:
        print("missing")
    except json.JSONDecodeError:
        print("invalid")
    print("finish")

请写出精确输出顺序，并说明 config 是否完成赋值、哪个 except 执行。

题目 2：区分两个失败阶段
----------------------

函数依次执行 open(path) 和 json.load(f)。请分别回答：

A. path 对应的文件不存在时，哪个异常分支执行？
B. 文件存在但内容是 {"active": false,} 时，哪个异常分支执行？
C. 为什么不能把这两种情况都写成 error="invalid_json"？

题目 3：交错复习 return、with 与未匹配异常
----------------------------------------

    def load(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return None

    result = load("missing.json")
    print(result)

假设 missing.json 不存在：

1. result 能否完成赋值？
2. print(result) 是否执行？
3. FileNotFoundError 最终怎样处理？

验收标准：
- 三题都区分成功路径、匹配分支和未匹配异常传播；
- 不把“语句开始执行”误写成“赋值已经完成”；
- 能解释精确错误分类对 AI 后端调用方的价值。

作答后复盘
----------

1. 精确输出为 start、invalid、finish。json.loads 抛出异常时，config
   赋值未完成，loaded 不打印；FileNotFoundError 分支不匹配，
   json.JSONDecodeError 分支执行。
2. 文件不存在进入 FileNotFoundError；文件存在但文本非法进入
   json.JSONDecodeError。统一标记 invalid_json 会掩盖失败阶段和根因，
   误导调用方、开发人员与监控系统。
3. open 抛出的 FileNotFoundError 不匹配唯一的 JSONDecodeError 分支，
   因此 load 没有返回值，result 赋值不完成，print(result) 不执行，
   FileNotFoundError 保留原类型继续传播。

结果：
- 首次闭卷：7/10。第 1、2 题正确，第 3 题误认为未匹配异常会返回 None。
- 纠错复述：3/3。已能说明赋值不完成、后续 print 不执行、异常继续传播。
- 下次先用新场景做约 2 分钟间隔复测，不把即时纠错等同于稳定掌握。
"""
