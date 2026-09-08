"""Day 12 每日闭卷巩固：函数装饰器基础。

要求：
- 不运行代码，先写出预测；
- 每题说明理由，不只写最终结果；
- 不修改本文件；
- 本组不引入 *args、**kwargs、functools.wraps 或带参数装饰器。

题 1：装饰时机与调用顺序

def mark(func):
    print("decorate")

    def wrapper(name):
        print("before")
        result = func(name)
        print("after")
        return result

    return wrapper


@mark
def normalize(name):
    print("body")
    return name.upper()


print("ready")
value = normalize("orders")
print(value)

问题：准确输出顺序是什么？执行到 print("ready") 时，normalize 指向谁？


题 2：返回值改错

def log_call(func):
    def wrapper(table_name):
        print("start")
        func(table_name)
        print("finish")

    return wrapper


@log_call
def load_table(table_name):
    return {"table_name": table_name}


result = load_table("events")
print(result)

问题：输出是什么？result 保存什么？只描述最小修复及其原因。


题 3：decorator 与 generator 交错

def trace(func):
    def wrapper():
        print("call")
        return func()

    return wrapper


@trace
def make_ids():
    print("body")
    yield 1


print("ready")
ids = make_ids()
print(next(ids))

问题：准确输出顺序是什么？调用 make_ids() 时，原生成器函数体是否立即执行？
"""
