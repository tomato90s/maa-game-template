# 新增任务

[English](add-task.en.md)

一个会出现在界面里的任务通常需要两个文件：

- pipeline 文件：放在 `assets/resource/pipeline/`
- task wrapper 文件：放在 `assets/resource/tasks/`

## 1. 新增 pipeline

例如创建 `assets/resource/pipeline/daily_login.json`：

```json
{
    "DailyLogin": {
        "recognition": {
            "type": "OCR",
            "param": {
                "expected": [
                    "Login"
                ]
            }
        },
        "action": {
            "type": "Click"
        },
        "next": [
            "NoopDone"
        ]
    }
}
```

## 2. 新增 task wrapper

例如创建 `assets/resource/tasks/example/daily_login_task.json`：

```json
{
    "task": [
        {
            "name": "Daily Login",
            "entry": "DailyLogin",
            "group": [
                "example"
            ],
            "label": "Daily Login",
            "description": "Claim the daily login reward."
        }
    ],
    "option": {}
}
```

## 3. 导入任务

把 task wrapper 路径加入 `assets/interface.json`：

```json
"import": [
    "resource/tasks/system/startup_task.json",
    "resource/tasks/example/example_task.json",
    "resource/tasks/example/daily_login_task.json"
]
```

## 4. 校验

运行：

```bash
python tools/dev.py check
```

也可以手动运行底层命令：

```bash
npx @nekosu/maa-tools check
python tools/validate_schema.py \
  --schema-dir deps/tools \
  --resource-dirs assets/resource/pipeline \
  --interface-files assets/interface.json \
  --task-dirs assets/resource/tasks
```

模板还内置了 `CenterClick`、`OffsetClick` 等常用 Python 自定义动作，详见 [默认 Python 自定义动作](custom-actions.md)。
