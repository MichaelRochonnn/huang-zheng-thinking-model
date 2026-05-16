# Huang Zheng Thinking Model

> A Codex Skill and knowledge graph for reasoning about companies through Huang Zheng's company-building logic: people-first demand aggregation, supply-chain reform, benfen, long-term intrinsic value, and the `Costco + Disney` retail vision.

## About

`huang-zheng-thinking-model` turns a local corpus of Huang Zheng materials into a reusable Codex Skill. Use it when analyzing Pinduoduo, Temu, PDD Holdings, or any company where you want to ask: "If Huang Zheng were CEO, how would he judge this business direction?"

## What This Skill Does

This Skill helps Codex:

- map company moves to Huang Zheng's core operating logic;
- judge whether a strategy is genuinely people-first or only traffic/subsidy-driven;
- evaluate whether a product creates demand certainty that can reshape supply;
- distinguish structural value-for-money from cheapness;
- test whether platform rules protect `本分`, trust, and good actors;
- run the counterfactual: "If Huang Zheng were CEO, what would he strengthen, question, or cut?"

The central chain is:

```text
ordinary people -> latent/scattered demand -> coordination and trust -> demand certainty -> supply reform -> lower structural cost and better quality -> joy/social experience -> long-term public institution
```

## Install

Clone the repository into your Codex skills directory:

```bash
cd ~/.codex/skills
git clone https://github.com/MichaelRochonnn/huang-zheng-thinking-model.git huang-zheng-company-thinking
```

Or, if you already cloned it elsewhere, symlink it:

```bash
ln -s /path/to/huang-zheng-thinking-model ~/.codex/skills/huang-zheng-company-thinking
```

## Usage

Invoke it explicitly:

```text
Use $huang-zheng-company-thinking to analyze whether Pinduoduo's new initiative fits Huang Zheng's company-building logic.
```

Useful prompts:

```text
用 $huang-zheng-company-thinking 判断 Temu 接下来的供应链策略是否符合黄峥思路。
```

```text
如果黄峥仍然是 CEO，他会如何思考这家公司现在的业务方向？
```

```text
用黄峥的“人为先、需求侧变革、本分、Costco+Disney”框架分析这个新产品。
```

## Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── knowledge_graph.md
│   ├── knowledge_graph.json
│   ├── operating_model.md
│   └── source_inventory.md
└── scripts/
    └── search_references.py
```

## Reference Files

- `SKILL.md`: compact entrypoint and invocation workflow.
- `references/knowledge_graph.md`: human-readable knowledge graph with nodes, edges, timeline, and source-backed claims.
- `references/knowledge_graph.json`: machine-readable graph and alignment heuristics.
- `references/operating_model.md`: practical analysis template for company strategy and CEO counterfactuals.
- `references/source_inventory.md`: source corpus map and extraction limitations.
- `scripts/search_references.py`: quick local search across Skill references.

Example search:

```bash
python3 scripts/search_references.py 本分 需求侧 Costco
```

## Source Corpus

The model was distilled from a local folder named `黄铮`, containing:

- Huang Zheng public-account essays;
- shareholder letters and company letters;
- media interviews and reports;
- related audio/video files indexed by title and duration.

Primary-weight material is Huang Zheng's own writing, shareholder letters, company letters, and direct interviews. Third-party commentary is treated as background only.

## Analysis Guardrails

- Do not reduce Huang Zheng's logic to "low price".
- Do not call every social-commerce tactic `拼`; a real `拼` mechanism creates demand certainty or trust.
- Do not ignore governance: counterfeit goods, weak quality, fake orders, merchant abuse, or internal corruption directly weaken `本分`.
- For current company moves, verify fresh facts from current sources first, then apply this historical framework.

## Suggested GitHub About Text

```text
Codex Skill + knowledge graph for analyzing companies through Huang Zheng's people-first, demand-side, benfen, and Costco+Disney operating logic.
```