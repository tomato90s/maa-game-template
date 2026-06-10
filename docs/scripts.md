# Scripts and Commands

Use `tools/dev.py` for daily work. The lower-level scripts are kept for CI and advanced debugging.

中文说明见下方。

## Daily Commands

| Task | Command | Notes |
| --- | --- | --- |
| Create a project from this template | `python tools/dev.py bootstrap --output ../maa-demo-game --project-name maa-demo-game --title "MAA Demo Game" --github-repo owner/maa-demo-game --package com.example.game --project-id MaaDemoGame --yes` | Copies the template and replaces core project fields. |
| Run local checks | `python tools/dev.py check` | Runs `npm ci`, `maa-tools check`, and schema validation. Requires network the first time Maa tools prepare their runtime. |
| Build local install directory | `python tools/dev.py package --version v0.0.0 --os macos --arch aarch64` | Requires MaaFramework already extracted under `deps/`. Outputs `install/`. |
| Generate resource update package | `python tools/dev.py update-package --version v0.0.0 --github-repo owner/repo --root install` | Usually used by CI release, but useful for local release debugging. |

## Lower-Level Scripts

| Script | Used by | Purpose | Run directly? |
| --- | --- | --- | --- |
| `tools/dev.py` | Humans | Unified command wrapper for common local workflows. | Yes |
| `tools/bootstrap_project.py` | `tools/dev.py`, humans | Copy this template into a new project directory and replace metadata. | Yes |
| `tools/install.py` | CI, `tools/dev.py` | Build `install/` from `assets/`, `agent/`, and local `deps/`. | Sometimes |
| `tools/validate_schema.py` | CI, `tools/dev.py` | Validate pipeline, task, and interface JSON files. | Sometimes |
| `tools/generate_update.py` | CI release, `tools/dev.py` | Create resource update zip and manifest. | Rarely |
| `tools/configure.py` | `tools/install.py` | Copy OCR model files from `assets/MaaCommonAssets` when present. | Rarely |
| `ci/setup_embed_python.sh` | CI | Install embedded Python on macOS/Linux. | No |
| `ci/setup_embed_python.ps1` | CI | Install embedded Python on Windows. | No |
| `ci/setup_pip.py` | CI setup scripts | Install pip into embedded Python. | No |
| `agent/main.py` | MaaFramework runtime | Start the Python AgentServer. | No |
| `agent/actions.py` | `agent/main.py` | Register default custom actions such as `CenterClick`. | No |

## Local MaaFramework Dependencies

`tools/dev.py package` and `tools/install.py` require local MaaFramework files:

```text
deps/
  bin/
  share/MaaAgentBinary/
```

These runtime files are ignored by Git. Only `deps/tools/*.schema.json` is committed for local schema validation.

## 中文说明

日常使用优先记住 `tools/dev.py`。底层脚本保留给 CI 和高级调试。

## 常用命令

| 任务 | 命令 | 说明 |
| --- | --- | --- |
| 从模板创建项目 | `python tools/dev.py bootstrap --output ../maa-demo-game --project-name maa-demo-game --title "MAA Demo Game" --github-repo owner/maa-demo-game --package com.example.game --project-id MaaDemoGame --yes` | 复制模板并替换核心项目字段。 |
| 运行本地检查 | `python tools/dev.py check` | 运行 `npm ci`、`maa-tools check` 和 schema 校验。第一次运行 maa-tools 可能需要网络准备运行时。 |
| 本地生成 `install/` | `python tools/dev.py package --version v0.0.0 --os macos --arch aarch64` | 需要先把 MaaFramework 解压到 `deps/`。 |
| 生成资源更新包 | `python tools/dev.py update-package --version v0.0.0 --github-repo owner/repo --root install` | 通常由 CI release 使用，本地排查 release 问题时也可以用。 |

## 底层脚本

| 脚本 | 谁使用 | 用途 | 是否直接运行 |
| --- | --- | --- | --- |
| `tools/dev.py` | 开发者 | 常用本地工作流统一入口。 | 是 |
| `tools/bootstrap_project.py` | `tools/dev.py`、开发者 | 从模板复制新项目并替换元数据。 | 可以 |
| `tools/install.py` | CI、`tools/dev.py` | 从 `assets/`、`agent/` 和本地 `deps/` 生成 `install/`。 | 偶尔 |
| `tools/validate_schema.py` | CI、`tools/dev.py` | 校验 pipeline、task、interface JSON。 | 偶尔 |
| `tools/generate_update.py` | CI release、`tools/dev.py` | 生成资源更新 zip 和 manifest。 | 很少 |
| `tools/configure.py` | `tools/install.py` | 如果存在 `assets/MaaCommonAssets`，复制 OCR 模型。 | 很少 |
| `ci/setup_embed_python.sh` | CI | macOS/Linux 安装嵌入式 Python。 | 否 |
| `ci/setup_embed_python.ps1` | CI | Windows 安装嵌入式 Python。 | 否 |
| `ci/setup_pip.py` | CI setup 脚本 | 给嵌入式 Python 安装 pip。 | 否 |
| `agent/main.py` | MaaFramework 运行时 | 启动 Python AgentServer。 | 否 |
| `agent/actions.py` | `agent/main.py` | 注册 `CenterClick` 等默认自定义动作。 | 否 |

## 本地 MaaFramework 依赖

`tools/dev.py package` 和 `tools/install.py` 需要本地 MaaFramework 文件：

```text
deps/
  bin/
  share/MaaAgentBinary/
```

这些运行库文件会被 Git 忽略。仓库只提交 `deps/tools/*.schema.json`，用于本地 schema 校验。
