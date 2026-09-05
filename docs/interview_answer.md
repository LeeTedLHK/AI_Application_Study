# 面试问题与标准回答

> 用于沉淀日常学习追问、周测和 Mock Interview 中出现的问题。
> 标准回答用于答题后的复盘，不替代先独立作答。

## 2026-08-31 — Python `dict`

### 问题 1：`dict.get(key, 0)` 中的 `0` 有什么作用？部门第一次出现和再次出现时，累计过程分别是什么？

**标准回答：**

`0` 是 key 不存在时使用的默认值。部门第一次出现时，字典中还没有该 key，`get(key, 0)` 返回 `0`，再加上当前金额并写入字典。部门再次出现时，`get(key, 0)` 返回已经累计的金额，而不是默认值 `0`，再加上当前金额。例如 `sales` 第一次是 `0 + 1200 = 1200`，再次出现是 `1200 + 300 = 1500`。

### 问题 2：如果直接执行 `summary[row["department"]] += row["amount"]`，第一次遇到某个部门时会发生什么？为什么？

**标准回答：**

会立即抛出 `KeyError`。`+=` 需要先读取左侧 key 的现有值，但第一次遇到该部门时，字典中还没有这个 key；`dict[key]` 对缺失 key 不会返回 `None`，而是直接抛出 `KeyError`，所以加法和赋值都不会执行。可以先初始化该 key，或者使用 `summary.get(key, 0) + amount`。

## 2026-09-01 — Python 输入校验

### 问题 1：设计 API 或 Tool Calling 参数校验时，为什么通常要先判断字段是否存在，再校验字段值？如果顺序反过来，可能出现什么问题？

**标准回答：**

字段存在性和字段值合法性是两个不同层次的校验。应先确认字段存在，再读取并检查其类型、范围或枚举值；否则直接使用 `data[key]` 读取缺失字段会抛出 `KeyError`，使校验流程中断，也无法返回清晰的“字段缺失”错误。`data.get(key)` 不会创建字段，它在字段缺失时返回 `None` 或指定默认值；只有执行 `data[key] = value` 才会创建或更新字段。

## 2026-09-01 — Python 函数返回值

### 问题 1：以下函数的两次输出依次是什么，`result` 保存了什么，为什么只在函数内部 `print` 不适合作为 AI Tool 或后端业务函数的设计？

```python
def build_config():
    print({"limit": 100})


result = build_config()
print(result)
```

**标准回答：**

第一次输出是 `{'limit': 100}`，第二次输出是 `None`。函数没有显式执行 `return` 时，会隐式返回 `None`，因此 `result` 保存的是 `None`。`print` 只是把内容写到标准输出，属于输出副作用，调用方无法获得该字典并继续校验、组合或序列化；可复用的业务函数应通过 `return` 把结果交给调用方，由外层决定是否打印、记录日志或返回给 API 客户端。

## 2026-09-01 — Python 函数作用域

### 问题 1：在 `filter_orders_by_status` 中，为什么应把 `target_status` 设计成函数参数，而不是让函数直接读取一个全局变量 `TARGET_STATUS`？请说明至少两个工程影响。

**标准回答：**

全局变量是隐藏依赖：只看函数签名无法知道完整输入，而且它可能在调用前被其他代码修改，使相同显式输入产生不同结果，降低可读性和可测试性。全局可变状态还会让并发请求互相干扰，例如请求 A 需要 `paid`、请求 B 需要 `cancelled` 时，共享的 `TARGET_STATUS` 只能保存一个当前值，可能导致某个请求使用另一个请求的条件。把 `target_status` 作为参数后，每次调用都携带自己的业务输入，函数更容易复用、独立测试和安全地并发调用。

## 2026-09-01 — Python 模块与入口保护

### 问题 1：`if __name__ == "__main__"` 是否意味着模块被 `import` 时整个文件都不会执行？结合 `order_summary.py` 说明导入时哪些内容仍会执行，哪些不会执行。

**标准回答：**

不是。导入模块时，Python 会执行模块的顶层代码：模块常量会被绑定，`def` 语句会执行并创建函数对象，顶层的其他语句也会执行；函数体仅在函数被调用时执行。入口保护的 `if` 条件同样会被求值，但被导入模块的 `__name__` 是模块名而不是 `"__main__"`，所以保护块中的 `main()` 调用不会执行。入口保护只隔离放在该代码块中的启动或演示逻辑，无法阻止保护块之外的数据库连接、模型加载或 API 请求在导入时运行。

## 2026-09-02 — Python 对象、JSON 文本与返回约定

本轮评分：9/10。类型路径与变体错误定位正确；首次理由侧重测试检查，追问后能从调用方的类型要求解释。

### 问题 1：你的函数中，输入 `json_text`、解析后的 `data`、最终返回值，分别是什么类型？

**标准回答：**

本题输入是 JSON object 文本，因此输入为 str，经 json.loads 解析得到 dict，再经 json.dumps 编码返回 str。JSON 文本与 Python 字典不是同一种类型。

### 问题 2：如果调用方要求 JSON 文本，把 `return json.dumps(data)` 改成 `return data`，还满足要求吗？为什么？

**标准回答：**

不满足。本题约定返回承载合法 JSON 文本的 str，而 return data 返回 dict。测试检查的是这个既定约定，不是因为测试存在才需要返回字符串；即使没有测试，调用方仍可能因类型不匹配而失败。若另一个接口明确要求 dict，则返回 dict 可以是正确设计，不能把所有函数都统一规定为返回 JSON 文本。

### 追问：假设没有测试，调用方这样使用你的函数。如果函数改成 `return data`，上面哪一行会出问题？为什么？

```python
result = update_query_limit('{"limit": 100}', 20)
config = json.loads(result)
```

**标准回答：**

第一行能正常接收 dict，但第二行 json.loads(result) 会抛出 TypeError，因为已经解析过的 Python 字典不是该函数接受的 JSON 输入。原接口要求 str，应通过 json.dumps(data) 返回 JSON 文本。本课以 str 为例；标准库 loads 也支持承载 JSON 的 bytes、bytearray，但不接受 dict。

## 2026-09-04 — JSON 文件读取与资源生命周期

本轮评分：7/10。原题正确；变体中混淆文件文本与文件对象，并遗漏了文件已经关闭的状态。已反馈，待独立纠错复述。

后续复测：学习者已正确复述返回 dict 可继续使用、返回已关闭文件对象不能继续读取；另补准关闭时机为调用方获得返回值之前。原评分保留，待交错巩固和跨日复测检验稳定性。

当日收尾：三题交错巩固及学习者亲手修正缩进均通过，巩固另计 10/10，不改写首次面试评分；下次进行间隔复测。

### 问题 1：return 位于 with 内部时，调用方获得结果前文件是否关闭？继续读取 result["limit"] 是否还需要文件打开？为什么？

```python
def load_query_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

result = load_query_config(path)
```

**标准回答：**

文件已关闭，也不需要为了访问 result["limit"] 保持打开。return 先求值 json.load(f)，在文件仍打开时读取并解析 JSON；本题顶层 JSON object 被解析为内存中的 dict。随后离开 with 时关闭文件，调用方获得返回的字典。关闭文件不会销毁已解析的字典，后续读取字典不需要再次读取文件。

### 追问：仅将 return json.load(f) 改成 return f：调用方获得什么对象？再执行 json.load(result) 是否成功，为什么？

**标准回答：**

调用方获得的是已经关闭的文件对象，不是文件中的文本，也不是解析后的字典。return f 只确定要返回哪个对象，不读取或解析文件；离开 with 时仍会执行关闭操作。json.load(result) 需要读取该文件对象，但文件已关闭，因此失败。本地实际运行得到 ValueError: I/O operation on closed file.。关键不是背异常名，而是区分“文件对象仍存在”与“文件仍然打开、可以读取”。

### 当日巩固 1：文件内容为 {"active": false, "label": "false", "limit": 0}，经 json.load 解析后依次打印三个字段。三行输出依次是什么？三个字段值分别是什么 Python 类型？

**标准回答：** 输出依次为 False、false、0；对应类型为 bool、str、int。JSON 的 false 是布尔值，带双引号的 "false" 是字符串；print 显示字符串内容时不加引号。

### 当日巩固 2：以下代码停止前会打印什么？哪一行出错，原因是什么？只调整缩进让调用方拿到解析后的数据，保留两条 print。

```python
def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        print("opened")
    return json.load(f)

config = load_config(path)
print("done")
```

**标准回答：** 假设文件存在且包含合法 JSON，原题先打印 opened，随后 return json.load(f) 读取已关闭的文件而失败，不会打印 done。将 return json.load(f) 向内缩进一级，放入 with 块，与 print("opened") 同级，即可在关闭文件之前完成读取解析。调用方拿到的是字典，修正后依次打印 opened、done。学习者已亲手完成这项修改并经执行验证。

### 当日巩固 3：config_tools 顶层打印 loading，build_config(limit=100) 只 print(limit)，入口保护中调用 build_config()。app 导入函数后执行 result = build_config(0) 和 print(result)。精确输出顺序是什么？result 保存什么？默认值 100 会打印吗，为什么？

**标准回答：** 新进程执行 app 时依次输出 loading、0、None。导入会执行模块顶层 print，但入口保护中的调用不执行；app 显式传入 0，覆盖默认值 100。build_config 没有显式 return，隐式返回 None，所以 result 保存 None，100 不会打印。

## 2026-09-05 — 异常与 traceback 阅读

本轮评分：8/10。能先识别最后一行异常类型，正确区分 FileNotFoundError 与 JSONDecodeError 的修复方向，也知道不应修改标准库；变体中需要补准“先看最近的自己代码失败行，再向上追调用和输入”。

### 问题 1：AI 后端启动时加载 JSON 配置失败，traceback 中既有自己的代码，也有多行 Python 标准库代码。你会按照什么顺序阅读 traceback？怎样区分应该修复文件路径，还是修复 JSON 内容？

**标准回答：**

先读 traceback 最后一行，确认异常类型和详情。若是 FileNotFoundError，重点核对失败的 open 操作、实际 path、当前工作目录及文件是否存在；若是 JSONDecodeError，说明文件通常已打开并进入解析阶段，应根据异常给出的 JSON 行列检查文本语法。然后从靠近底部的自己代码 frame 开始，确认直接失败的操作，再向上追调用链和输入来源。修改后必须重新运行并核对实际结果与预期，不能把“不再抛异常”当作完成。

### 追问：最后一行是 JSONDecodeError，上方先是多行 json/decoder.py，再往上是 config_loader.py 第 8 行 return json.load(f)，app.py 第 20 行 config = load_config(path)。是否修改 json/decoder.py？自己的两行先检查哪一行？如何追到有问题的 JSON 输入？

**标准回答：**

不修改 Python 标准库的 json/decoder.py；它只是异常传播过程中显示的内部调用。先检查最靠近异常的自己代码 config_loader.py 第 8 行，确认失败操作是 json.load(f)，由此知道问题发生在读取到的 JSON 内容解析阶段。再向上检查 app.py 第 20 行传入的 path，追到具体文件，结合 JSONDecodeError 的文本行列检查该文件。修复后重新运行测试，并比较解析结果是否符合业务预期。

## 2026-09-05 — 精确异常捕获

本轮评分：9/10。学习者能解释宽泛捕获会把其他根因错误标记为 invalid_json，导致无法精确定位并误导开发人员排查；补充影响是调用方和监控也可能基于错误分类采取错误动作。

### 问题：如果 load_query_config 内部的程序错误抛出 NameError，而代码使用 except Exception 并统一返回 invalid_json，会产生什么工程问题？为什么 AI 后端不应把所有异常都当成 invalid_json？

**标准回答：**

except Exception 会同时捕获 JSON 格式错误、权限问题、程序缺陷等许多不同异常。统一返回 invalid_json 会掩盖原始异常类型和 traceback，使开发人员误查 JSON 文件，调用方也可能错误地提示用户修改配置或执行不合适的恢复动作，日志和监控还会得到失真的错误分类。应只捕获当前层明确知道如何恢复或转换的异常；例如分别处理 FileNotFoundError 和 json.JSONDecodeError，让 NameError 等未知异常保留原类型继续传播，以便尽快暴露并修复代码缺陷。
