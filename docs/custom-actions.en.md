# Default Python Custom Actions

[中文](custom-actions.md)

The template enables the Python agent by default and registers common actions in `agent/actions.py`.

## CenterClick

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

## OffsetClick

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

## NodeOverride

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

## DisableNode

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
