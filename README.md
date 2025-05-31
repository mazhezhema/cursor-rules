# Lokibble - AI换脸社交App（MVP阶段）

本项目是 Lokibble 的核心文档库，涵盖产品定义、架构设计、开发状态、数据埋点、支付逻辑等所有模块。
我们使用 `anchor.yaml` 作为项目唯一锚点，结合 `changelog` 实现多轮会话、多人协作对齐。

## 📁 项目结构说明

- `anchor.yaml`：系统锚点，唯一可信的主线定义，每次重大决策需同步此处
- `changelog/`：按日期记录的每日变更日志，记录讨论重点与分支演化
- `doc/`：存放产品原型、UX稿、接口定义、API协议、研发文档等内容
- `rules/`：Cursor 等自动生成代码的结构规范（如 rules.mdt、约束规范等）

## ✅ 使用方法

1. 每轮 GPT 对话结束后，补充更新 `changelog/yyy-mm-dd.md`
2. 若涉及主结构调整，同步更新 `anchor.yaml`
3. 所有核心文件均应 git 提交，作为长期演化基线