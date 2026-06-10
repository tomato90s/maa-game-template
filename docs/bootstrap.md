# 项目初始化清单

[English](bootstrap.en.md)

通过 GitHub **Use this template** 创建新仓库后，按这个清单整理项目。

模板不会生成或改写 `interface.json`。请根据 Maa ProjectInterface 协议和你的项目需求自行实现。

## 1. 项目元数据

编辑 `assets/interface.json`：

- `name`：机器可读的项目 id，例如 `maa-example-game`
- `title`：显示名称，例如 `MAA Example Game`
- `description`：项目简介
- `github`：你的仓库地址
- `welcome`：兼容启动器显示的首次欢迎信息

## 2. CI 项目名

编辑 `.github/workflows/install.yml`：

```yaml
env:
  PROJECT_ID: MaaGameTemplate
```

`PROJECT_ID` 是 CI artifact 和 release 包名的前缀。真实项目里建议改成自己的项目名，例如 `MaaExampleGame`。

## 3. README

编辑 `README.md`：

- 替换模板描述为你的游戏项目说明
- 说明支持的模拟器、分辨率、语言和登录前提
- 删除不适合你项目的示例说明

## 4. 示例任务

`assets/resource/pipeline/startup.json` 和 `assets/resource/pipeline/example.json` 都只是示例。

不是所有项目都需要自动启动游戏。如果不需要，可以删除示例启动任务，或把它替换为“确认游戏已打开”的节点。

## 5. 资源文件

截图和模板图放在：

```text
assets/resource/image/
```

OCR 模型放在：

```text
assets/resource/model/ocr/
```

模板默认不包含 OCR 模型文件。需要 OCR 时，可以加入自己的模型，或从 Maa common assets 复制。

## 6. Schema 文件

模板把 MaaFramework JSON schema 文件保存在：

```text
deps/tools/
```

升级 MaaFramework schema 版本时，可以刷新这些文件。
