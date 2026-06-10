# 默认 Python 自定义动作

[English](custom-actions.en.md)

模板默认启用 Python agent，并在 `agent/actions.py` 中注册几个常用 action。

## CenterClick

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

## OffsetClick

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

## NodeOverride

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

## DisableNode

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
