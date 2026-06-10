# Add a Task

[中文](add-task.md)

A visible task usually needs two files:

- A pipeline file under `assets/resource/pipeline/`
- A task wrapper under `assets/resource/tasks/`

## 1. Add the Pipeline

Create a pipeline entry, for example `assets/resource/pipeline/daily_login.json`:

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

## 2. Add the Task Wrapper

Create `assets/resource/tasks/example/daily_login_task.json`:

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

## 3. Import the Task

Add the wrapper path to `assets/interface.json`:

```json
"import": [
    "resource/tasks/system/startup_task.json",
    "resource/tasks/example/example_task.json",
    "resource/tasks/example/daily_login_task.json"
]
```

## 4. Validate

Run:

```bash
python tools/dev.py check
```

Or run the lower-level commands manually:

```bash
npx @nekosu/maa-tools check
python tools/validate_schema.py \
  --schema-dir deps/tools \
  --resource-dirs assets/resource/pipeline \
  --interface-files assets/interface.json \
  --task-dirs assets/resource/tasks
```

The template also includes common Python custom actions such as `CenterClick` and `OffsetClick`. See [Default Python Custom Actions](custom-actions.en.md).
