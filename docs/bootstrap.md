# 创建新游戏项目

[English](bootstrap.en.md)

建议先完成最小改名，再逐步替换真实游戏资源。

## 初始化脚本

在模板仓库中运行：

```bash
python tools/dev.py bootstrap \
  --output ../maa-demo-game \
  --project-name maa-demo-game \
  --title "MAA Demo Game" \
  --github-repo your-name/maa-demo-game \
  --package com.example.game \
  --project-id MaaDemoGame \
  --yes
```

脚本会复制模板到输出目录，跳过本地构建/运行产物，并替换主要项目字段。

## 维护者说明：开启 GitHub Template 模式

如果你维护的是模板仓库本身，推送到 GitHub 后可以开启模板模式：

1. 打开 GitHub 仓库页面。
2. 进入 **Settings**。
3. 启用 **Template repository**。
4. 回到仓库首页，使用 **Use this template** 创建新项目。

通过模板创建的新仓库会拥有全新的 Git 历史。它不是 fork，也不会自动接收模板仓库后续更新。

## 必改字段

编辑 `assets/interface.json`：

- `name`：机器可读的项目 id，例如 `maa-example-game`
- `title`：显示名称，例如 `MAA Example Game`
- `description`：项目简介
- `github`：你的仓库地址
- `welcome`：兼容启动器显示的首次欢迎信息

编辑 `.github/workflows/install.yml`：

- `PROJECT_ID`：CI 和 GitHub Release 使用的 artifact 前缀

编辑 `README.md`：

- 替换模板描述为你的游戏项目说明
- 说明支持的模拟器、分辨率、语言和登录前提

## 启动包名

替换 `assets/resource/pipeline/startup.json` 中的占位包名：

```json
"package": "com.example.game"
```

如果你的项目不需要自动启动游戏，可以把 `StartApp` 替换为“确认游戏已打开”的节点。

## 资源文件

截图和模板图放在：

```text
assets/resource/image/
```

OCR 模型放在：

```text
assets/resource/model/ocr/
```

模板默认不包含 OCR 模型文件。需要 OCR 时，可以加入自己的模型，或从 Maa common assets 复制。

## Schema 文件

模板把 MaaFramework JSON schema 文件保存在：

```text
deps/tools/
```

升级 MaaFramework schema 版本时，可以刷新这些文件。
