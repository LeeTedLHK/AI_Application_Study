"""Day 16 闭卷巩固，约 10～15 分钟。

任务：不看讲义、不运行代码，先在对话中按 Q1/Q2/Q3 回答。
约束：只使用 dataclass、Enum、默认字段、位置参数与 .value。
验收：Q1 字段值/类型准确；Q2 能区分枚举成员和值；Q3 能指出字段顺序和校验边界。
首次作答后再运行核对；本文件不提供标准答案。

Q1（3 分）：

    class Mode(Enum):
        FAST = "fast"
        SAFE = "safe"

    @dataclass
    class Job:
        name: str
        retries: int = 2
        mode: Mode = Mode.SAFE

    job = Job("embed")

    写出 job 的三个字段值及类型；写出 job.mode.value。

Q2（3 分）：`job.mode` 与 `job.mode.value` 哪个是 Enum 成员，哪个是字符串？
如果把 `mode` 改成字符串并写成 `"saef"`，可能产生什么问题？

Q3（4 分）：下面的 dataclass 定义为什么会在类定义阶段出错？如何调整字段顺序？

    @dataclass
    class BadPlan:
        limit: int = 100
        table_name: str

    另外，`@dataclass` 会自动检查 `table_name` 必须是字符串、`limit` 必须非负吗？
"""
