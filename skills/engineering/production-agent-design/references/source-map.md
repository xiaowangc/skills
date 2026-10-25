# 白皮书知识来源映射

## 用途

本文件说明技能知识如何由五份 Google 白皮书重组，便于追溯概念和避免把产品示例误当成通用原则。页码指 PDF 印刷页主题范围，具体引用时以原 PDF 为准。

## 1. Introduction to Agents

来源：`/Users/yongchiwang/work/chi_opc/白皮书/2025_Day_1_Rewrite_v1_IntroductionToAgents.pdf`，54 页，Updated May 2026。

主要吸收：

- Agent = Model + Tools + Orchestration + Deployment/Runtime；
- Mission → Scene → Think → Act → Observe 的循环；
- 从模型能力、工具增强、策略规划、多智能体到自演化的能力层次；
- 模型按业务质量、延迟和成本选择；
- 确定性工作流与 LM 自治的连续谱；
- 多智能体协调、顺序、迭代改进和 HITL 模式；
- AgentOps、业务 KPI、LM Judge、Trace 和反馈闭环；
- Agent Identity、最小权限、Gateway/Registry 和纵深防御；
- 学习、自演化和离线 Agent Gym 的受控方式。

映射到：`SKILL.md` 核心立场与自治流程、`architecture-and-orchestration.md`、`production-agentops.md`。

## 2. Agent Tools & Interoperability with MCP

来源：`/Users/yongchiwang/work/chi_opc/白皮书/2025_Day_2_Rewrite_v1_AgentTools.pdf`，56 页，Updated May 2026。

主要吸收：

- Function/Built-in/Agent Tool 分类；
- 工具文档、任务化、粒度、简洁输出、Schema 校验和描述性错误；
- MCP Host/Client/Server、Tool/Resource/Prompt/Sampling/Elicitation/Roots；
- MCP 的动态发现、可组合性和上下文膨胀；
- 企业级身份、授权、观测缺口；
- 动态能力注入、工具影子、恶意描述/内容、敏感信息泄漏、粗粒度授权和 Confused Deputy；
- 白名单、版本固定、Gateway、净化、污点/敏感标注、短期 Scope 凭证与 HITL。

映射到：`tools-interoperability-security.md`。

## 3. Context Engineering: Sessions, Memory

来源：`/Users/yongchiwang/work/chi_opc/白皮书/2025_Day_3_Rewrite_v1_ContextEngineering.pdf`，73 页，Updated May 2026。

主要吸收：

- 上下文工程的动态 Fetch/Prepare/Invoke/Upload 生命周期；
- Session 的事件与状态、共享/独立多 Agent 历史；
- 长上下文成本、延迟、质量及截断/摘要/事件驱动压缩；
- Memory 与 RAG 的职责差异；
- 记忆类型、范围、组织、存储与多模态来源；
- Extraction/Consolidation/Storage/Retrieval、来源谱系、置信度和遗忘；
- 主动预载与 Memory-as-a-Tool；
- 异步生成、并发、一致性、失败处理、隔离、删除与投毒防护；
- 记忆生成、检索和端到端任务评测。

映射到：`context-session-memory.md`。

## 4. Agent Quality

来源：`/Users/yongchiwang/work/chi_opc/白皮书/2025_Day_4_Rewrite_v1_AgentQuality.pdf`，52 页，Updated May 2026。

主要吸收：

- 质量是架构支柱，Trajectory is the Truth；
- Effectiveness、Efficiency、Robustness、Safety 四类质量；
- Outside-In：端到端黑盒评测后进入轨迹玻璃盒分析；
- 规划、工具、观察、RAG、效率和多 Agent 动态的轨迹评测；
- 自动指标、LLM-as-a-Judge、Agent-as-a-Judge、HITL 与用户反馈；
- 日志、Trace、系统指标与质量指标；
- 动态采样、PII 清理和 Agent Quality Flywheel。

映射到：`quality-evaluation-observability.md`。

## 5. Prototype to Production

来源：`/Users/yongchiwang/work/chi_opc/白皮书/2025_Day_5_Rewrite_v1_Prototype.pdf`，41 页，Updated May 2026。

主要吸收：

- 生产差距主要在基础设施、安全和验证；
- 人员责任与 Evaluation-Gated Deployment；
- CI、Staging、人工批准生产的三阶段流水线；
- Canary、Blue-Green、A/B、Feature Flag 和全资产版本化；
- 安全策略、Guardrail、HITL、红队与持续保障；
- Observe → Act → Evolve、熔断和安全事件响应；
- Stateless 运行、外置状态、异步任务、重试、成本和扩缩容；
- MCP 与 A2A 的分层职责、Agent Card、分布式 Trace、Registry 引入条件。

映射到：`production-agentops.md`、`architecture-and-orchestration.md`。

## 技能的二次工程化

以下内容是基于白皮书原则并结合当前仓库规范形成的落地规则，不是白皮书原句：

- 生产就绪硬门槛；
- 以 `agent.toml`、版本化 Instructions、JSON Schema 和评测数据集为标准资产；
- 优先确定性代码处理校验、状态与不可逆动作；
- 从单 Agent 开始并要求子 Agent 可独立评测；
- 每个设计建议写出业务依据、代价和验证方式；
- 用设计交付模板和阶段退出证据组织评审。

## 时效性边界

白皮书写于/更新于 2026 年 5 月，涉及 Gemini Enterprise Agent Platform、ADK、MCP、A2A 以及协议支持率的描述具有时效性。技能保留稳定的架构原则，不把具体产品能力当作事实永久缓存。选型、协议字段或安全能力发生实装时，应查看当时的官方规范。
