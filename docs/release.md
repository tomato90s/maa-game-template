# Release 打包

[English](release.en.md)

## 创建 Release

推送一个 `v*` tag：

```bash
git tag v0.1.0
git push origin v0.1.0
```

`install.yml` workflow 会执行：

1. 下载 MaaFramework。
2. 设置嵌入式 Python。
3. 复制 `assets/resource`、`assets/interface.json` 和 `agent`。
4. 安装 Python 依赖。
5. 上传平台 artifact。
6. 为 tag 创建 GitHub Release。
7. 生成资源更新包和 manifest。

## 手动测试打包

在 GitHub Actions 中手动运行 `install.yml`，可以生成 artifact，但不会创建 GitHub Release。

## 资源更新包

release workflow 默认把这些路径加入资源更新包：

```text
agent/**/*.py
resource/**/*.json
resource/image/**/*
resource/model/**/*
interface.json
```

如果项目还需要更新其他资源，可以在 `.github/workflows/install.yml` 中添加更多 include pattern。
