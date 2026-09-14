"""Day 18 编码练习：.env 加载 → 环境读取 → Pydantic 校验。

业务背景：智能取数服务从外部配置读取表名和查询行数上限。
已有知识：os.getenv 读到字符串或 None；load_dotenv(path, override=False)
只填充缺失的进程变量；Day 17 的 QueryInput.model_validate 负责转换和范围校验。

先在聊天中写三步设计，再亲手实现 load_query_config(dotenv_path: str) -> QueryInput。
输入：一个存在的 .env 文件路径；本章的 day18_config/.env.example 包含
DAY18_TABLE_NAME=reports 和 DAY18_QUERY_LIMIT=25，均为无密钥演示值。

需求：
1. 在函数内显式 load_dotenv(dotenv_path, override=False)，保留已有环境变量。
2. 用 os.getenv 读取 DAY18_TABLE_NAME、DAY18_QUERY_LIMIT。
3. 把读取值交给 Day 17 的 QueryInput.model_validate；函数返回 QueryInput 模型。
4. table_name 必填，缺失时报 ValidationError；不要伪造表名。
5. limit 缺失时，让 QueryInput 自己提供默认值 100；不要传入 None 代替缺失。
6. limit="0" 可以转换并通过；limit="1001" 或 "abc" 应传播 ValidationError。
7. 不手写 int 转换或范围 if，也不要捕获并吞掉 ValidationError。
8. 导入本模块时无输出，不加载 .env；演示调用放入 __main__ 保护块。

边界提示：Pydantic 仅在字段缺失时使用默认值；字典里有 limit=None
表示提供了一个值，需要校验。先决定输入字典里什么时候应加入 limit 键。
约束：不访问真实密钥、不连接数据库；约 10～30 行核心代码。
验收：文件值生效、已有环境变量优先、缺失 limit 使用模型默认值、
非法 limit 传播 ValidationError、导入静默。最后解释加载与校验的职责。
运行与测试将在实现后进行。本文件不提供核心答案。
"""

# 请先写三步设计，再在这里实现函数。
import os
from pydantic import BaseModel, Field, ValidationError
import dotenv
from day17_pydantic_basemodel import QueryInput  # 假设 QueryInput 在同一目录下的 day17_pydantic_basemodel.py 中定义


def load_query_config(dotenv_path: str) -> "QueryInput":
    """加载 .env 配置，读取环境变量，返回已验证的 QueryInput 模型。"""
    # Step 1: Load the .env file without overriding existing environment variables
    dotenv.load_dotenv(dotenv_path, override=False)

    # Step 2: Read the environment variables for table name and limit
    table_name = os.getenv("DAY18_TABLE_NAME")
    limit_str = os.getenv("DAY18_QUERY_LIMIT")

    # Step 3: Prepare the data dictionary for validation
    data = {"table_name": table_name}
    if limit_str is not None:
        data["limit"] = limit_str
    return QueryInput.model_validate(data)

if __name__ == "__main__":
    # 测试加载配置
    try:
        config = load_query_config("learning/python/week01/day18_config/.env.example")
        print(config.model_dump())
    except ValidationError as e:
        print(type(e).__name__, e)