# CI 工作流

[English](ci.en.md)

## check.yml

`check.yml` 会在 push、pull request 和手动触发时运行。

它会做两件事：

- 安装 npm 依赖并运行 `npx @nekosu/maa-tools check`
- 使用 `tools/validate_schema.py` 校验 pipeline、task 和 interface JSON

这个 workflow 用来在 release 打包前发现任务导入错误、JSON 错误和 schema 错误。

schema 文件保存在 `deps/tools/*.schema.json`，因此本地检查和 CI 不需要额外 bootstrap 步骤。

## sync_schema_files.yml

`sync_schema_files.yml` 只支持手动触发。

当你想从 MaaFramework `main` 刷新 `deps/tools/*.schema.json` 时，可以在 GitHub Actions 里手动运行它。

## install.yml

`install.yml` 负责用 MaaFramework 和嵌入式 Python 打包项目。

默认构建：

- Windows x64
- macOS arm64

只有当前 ref 是 `refs/tags/v*` 时，release job 才会创建 GitHub Release。

普通分支和 pull request 构建只上传 CI artifact，不创建 GitHub Release。

## 项目变量

创建真实项目后，通常需要修改：

- `.github/workflows/install.yml` 里的 `PROJECT_ID`
- `.github/workflows/install.yml` 里的 `MAAFW_VERSION`，如果你想固定 MaaFramework 版本

资源更新 manifest 的仓库地址会由 GitHub Actions 传入 `${{ github.repository }}`。
