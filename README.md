# MAA Game Template

中文 | [English](README.en.md)

一个用于创建 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 游戏自动化项目的公开模板仓库。

当你需要一个小而完整的 Maa 项目骨架时，可以使用这个模板。它包含：

- `assets/interface.json` 中的 ProjectInterface v2 元数据
- `assets/resource/tasks/` 下的示例任务包装文件
- `assets/resource/pipeline/` 下的示例 pipeline 文件
- `agent/` 下的可选 Python agent 入口
- 用于资源检查和 release 打包的 GitHub Actions

## 快速开始

1. 在 GitHub 上点击 **Use this template**，或克隆这个仓库。
2. 根据 Maa ProjectInterface 协议实现或修改 `assets/interface.json`：
   - `name`
   - `title`
   - `description`
   - `github`
   - `welcome`
3. 将 `assets/resource/pipeline/example.json` 中的示例任务替换成真实的识别和操作节点。
4. 运行本地检查：

```bash
python tools/dev.py check
```

更多脚本用途见 [脚本和命令说明](docs/scripts.md)。

## 仓库结构

```text
assets/
  interface.json
  resource/
    pipeline/
    tasks/
agent/
ci/
tools/
.github/workflows/
docs/
```

## 文档

- [项目初始化清单](docs/bootstrap.md)
- [新增任务](docs/add-task.md)
- [默认 Python 自定义动作](docs/custom-actions.md)
- [脚本和命令说明](docs/scripts.md)
- [CI 工作流](docs/ci.md)
- [Release 打包](docs/release.md)

## Release

推送一个 `v*` tag 即可创建 GitHub Release：

```bash
git tag v0.1.0
git push origin v0.1.0
```

普通分支和 pull request 构建只会生成 CI artifact。只有 `v*` tag 会创建 GitHub Release。

## License

本模板使用 MIT License。真实项目如果需要其他许可证，可以自行替换。
