# Default Python Custom Actions

The template enables the Python agent by default and registers common actions in `agent/actions.py`.

中文说明见下方。

## Available Actions

### CenterClick

Clicks the center of the current recognition box.

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "CenterClick"
        }
    }
}
```

### OffsetClick

Clicks the center of the current recognition box with an offset.

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "OffsetClick",
            "custom_action_param": {
                "x": 12,
                "y": -4
            }
        }
    }
}
```

### NodeOverride

Overrides pipeline nodes at runtime.

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "NodeOverride",
            "custom_action_param": {
                "SomeNode": {
                    "next": [
                        "NoopDone"
                    ]
                }
            }
        }
    }
}
```

### DisableNode

Disables a node at runtime.

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "DisableNode",
            "custom_action_param": {
                "node_name": "SomeNode"
            }
        }
    }
}
```

## 中文说明

模板默认启用 Python agent，并在 `agent/actions.py` 中注册了几个常用 action。

### CenterClick

点击当前识别框中心。

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "CenterClick"
        }
    }
}
```

### OffsetClick

点击当前识别框中心，并增加偏移量。

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "OffsetClick",
            "custom_action_param": {
                "x": 12,
                "y": -4
            }
        }
    }
}
```

### NodeOverride

运行时覆盖 pipeline 节点。

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "NodeOverride",
            "custom_action_param": {
                "SomeNode": {
                    "next": [
                        "NoopDone"
                    ]
                }
            }
        }
    }
}
```

### DisableNode

运行时禁用某个节点。

```json
{
    "action": {
        "type": "Custom",
        "param": {
            "custom_action": "DisableNode",
            "custom_action_param": {
                "node_name": "SomeNode"
            }
        }
    }
}
```
