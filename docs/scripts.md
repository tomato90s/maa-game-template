# 脚本和命令说明

日常使用优先记住一个入口：

```bash
python tools/dev.py <command>
```

底层脚本仍然保留，主要给 CI 和高级调试使用。

[English](scripts.en.md)

## 常用命令

### 从模板创建新项目

用于把当前模板复制成一个新的 Maa 游戏项目，并替换项目名、仓库地址、包名和 CI artifact 名称。

```bash
python tools/dev.py bootstrap \
  --output ../maa-demo-game \
  --project-name maa-demo-game \
  --title "MAA Demo Game" \
  --github-repo owner/maa-demo-game \
  --package com.example.game \
  --project-id MaaDemoGame \
  --yes
```

底层脚本是：

```bash
python tools/bootstrap_project.py ...
```

### 运行本地检查

用于提交前检查资源、schema 和 Maa 项目结构。

```bash
python tools/dev.py check
```

它会依次运行：

```bash
npm ci
npx @nekosu/maa-tools check
python tools/validate_schema.py \
  --schema-dir deps/tools \
  --resource-dirs assets/resource/pipeline \
  --interface-files assets/interface.json \
  --task-dirs assets/resource/tasks
```

第一次运行 `maa-tools` 时，可能需要网络来准备 MaaFramework 检查运行时。

### 本地生成 install 目录

用于在本地模拟 CI 打包流程，输出 `install/`。

Apple Silicon Mac 示例：

```bash
python tools/dev.py package \
  --version v0.0.0 \
  --os macos \
  --arch aarch64
```

Intel Mac 示例：

```bash
python tools/dev.py package \
  --version v0.0.0 \
  --os macos \
  --arch x86_64
```

Windows x64 示例：

```bash
python tools/dev.py package \
  --version v0.0.0 \
  --os win \
  --arch x86_64
```

这个命令要求你已经准备好本地 MaaFramework 文件：

```text
deps/
  bin/
  share/MaaAgentBinary/
```

### 生成资源更新包

通常由 CI release 使用。本地排查 release 问题时可以手动运行。

```bash
python tools/dev.py update-package \
  --version v0.0.0 \
  --github-repo owner/repo \
  --root install
```

输出文件：

```text
resource-manifest.json
resource-update-v0.0.0.zip
```

## 脚本分类

### 日常入口

`tools/dev.py`

开发者日常使用的统一入口。优先用它，而不是记住所有底层脚本。

### 项目初始化

`tools/bootstrap_project.py`

从模板复制新项目并替换元数据。通常通过 `tools/dev.py bootstrap` 调用。

### 本地和 CI 打包

`tools/install.py`

从 `assets/`、`agent/` 和本地 `deps/` 生成 `install/`。CI 会直接调用它，本地建议通过 `tools/dev.py package` 调用。

`tools/configure.py`

`install.py` 内部调用。如果存在 `assets/MaaCommonAssets/OCR`，它会把默认 OCR 模型复制到 `assets/resource/model/ocr`。

### 校验

`tools/validate_schema.py`

校验 pipeline、task 和 interface JSON。通常由 `tools/dev.py check` 或 CI 调用。

### Release 资源更新

`tools/generate_update.py`

生成资源更新 zip 和 manifest。通常由 release workflow 调用，本地建议通过 `tools/dev.py update-package` 调用。

### CI 嵌入式 Python

这些脚本只给 CI 使用，日常不需要手动运行：

```text
ci/setup_embed_python.sh
ci/setup_embed_python.ps1
ci/setup_pip.py
```

### 运行时 Agent

这些不是开发命令，由 MaaFramework 运行时使用：

```text
agent/main.py
agent/actions.py
```

`agent/main.py` 启动 Python AgentServer。

`agent/actions.py` 注册默认自定义动作，例如 `CenterClick`、`OffsetClick`、`NodeOverride`、`DisableNode`。

## 本地 MaaFramework 文件如何管理

本地调试和打包用的 MaaFramework 运行库放在：

```text
deps/
  bin/
  share/MaaAgentBinary/
```

这些运行库会被 Git 忽略，不应该提交。

仓库只提交：

```text
deps/tools/*.schema.json
```

这些 schema 文件用于本地和 CI 的 JSON 校验。
