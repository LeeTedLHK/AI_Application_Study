'''Day 8 练习：先读 traceback，再考虑修改代码。

要求：先不运行，在聊天中阅读讲义给出的真实 traceback 并回答。
本文件仅保存题面，不执行文件读取。
用途：AI 后端读取配置、模型文件或评测数据失败时，先定位根因，
      避免只看见一大段红字就盲目修改代码。

已知 day08_file_not_found_demo.py 的调用关系：
    main()
      -> load_config("missing-config.json")
          -> open(path, ...)

问题：
1. 异常类型是什么？错误详情说明缺少哪个路径？
2. traceback 中哪一行是程序最初发起 load_config 调用的位置？
3. 哪一行是真正执行失败操作的位置？
4. 为什么 after load 不会被打印？

验收：用“异常类型、错误详情、调用位置、失败位置”四项完整作答。
不要求背英文报错，也不要求现在写 try / except。
'''
