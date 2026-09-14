"""Day 18 每日闭卷巩固（约 10～15 分钟）。

先独立回答，不运行，不查讲义；题目只覆盖本日与近期已学内容。
每题给出输出或异常类型，并用一句话解释执行顺序。三个情形互相独立。
验收：能分清环境值优先、Pydantic 默认值和异常时的资源清理。

Q1 配置来源与类型：
.env 中 DAY18_QUERY_LIMIT=25，进程环境已有 DAY18_QUERY_LIMIT="0"。
代码用 load_dotenv(path, override=False)，再执行：
    raw = os.getenv("DAY18_QUERY_LIMIT", "100")
    model = QueryInput.model_validate({"table_name": "reports", "limit": raw})
分别写出 raw 的值/类型，以及 model.limit 的值/类型。

Q2 微型改错：
假设 .env 和进程环境都没有 DAY18_QUERY_LIMIT，但 table_name="reports"。
有人写：
    data = {"table_name": "reports", "limit": os.getenv("DAY18_QUERY_LIMIT")}
    result = QueryInput.model_validate(data)
是得到默认值 100，还是抛出 ValidationError？只修改 data 构建逻辑，
怎样让模型默认值生效？请写伪代码或最小 Python 片段，不能伪造 100。

Q3 交错复习 context manager：
沿用 Day 13 的 QuerySession；环境变量 limit="abc"，.env 仍写 25，
load_query_config(path) 会抛 ValidationError。预测打印内容，解释会话状态：
    session = QuerySession()
    try:
        with session:
            load_query_config(path)
        print("done")
    except ValidationError:
        print(session.closed)

首次作答后再运行变体验证，不在本文件展示答案。
"""
