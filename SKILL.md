---
name: huang-zheng-company-thinking
description: "Use this skill when analyzing a company, product strategy, founder, CEO decision, or latest business move through Huang Zheng/Huang Zheng-style company-building logic, especially for 黄峥, 黄铮, 拼多多, Pinduoduo, PDD, Temu, 新电商, 社交电商, C2M, 农产品上行, Costco+Disney, 本分, 普惠, 人为先, 错位竞争, 需求侧变革, or prompts like 如果黄峥是 CEO 会怎么想."
---

# Huang Zheng Company Thinking

Use this skill to judge whether a company is moving in a Huang Zheng-style direction: creating consumer value through new demand aggregation, supply-chain efficiency, social/interactive experience, long-term institution building, and `本分`.

The source corpus came from `/Users/michaelrochon/Desktop/黄铮`, including Huang Zheng public-account essays, shareholder letters, interview transcripts/media, and third-party commentary. Treat the distilled graph as the default memory, then load source details only when needed.

## Start Here

Before giving a substantive answer, search the skill references for relevant nodes:

```bash
python3 /Users/michaelrochon/.codex/skills/huang-zheng-company-thinking/scripts/search_references.py "本分" "需求侧" "Costco"
```

Load references selectively:

- `references/knowledge_graph.md`: core nodes, edges, timeline, source-backed claims.
- `references/operating_model.md`: how to analyze a company or latest move, including the "if Huang Zheng were CEO" counterfactual.
- `references/knowledge_graph.json`: machine-readable nodes, edges, and alignment heuristics.
- `references/source_inventory.md`: original file map, media durations, coverage, and limitations.

If the user asks about current strategy, filings, prices, management, news, regulations, or "latest" business moves, browse current primary sources first. The Huang Zheng corpus is stable historical context; current facts are not.

## Workflow

1. **Pin the current facts.** Identify the company, business line, geography, time period, and the concrete move being judged. For current events, verify with official filings, earnings calls, investor relations, company announcements, or reputable reporting.

2. **Retrieve the matching graph nodes.** Search by product words and strategic concepts, not only company names. Useful keywords include `本分`, `普惠`, `人为先`, `流量`, `错位`, `供给侧`, `需求侧`, `农产品`, `C2M`, `Costco`, `Disney`, `开放`, `公众机构`, `内生价值`, `良币`.

3. **Judge fit against Huang Zheng's operating logic.** Ask whether the move:
   - serves the broad ordinary user rather than treating people as traffic;
   - aggregates latent or scattered demand into useful certainty for supply;
   - lowers structural cost or improves quality, not just subsidizing price;
   - creates joy, social interaction, or a new shopping/use scenario;
   - improves platform trust so good actors win over bad actors;
   - increases long-term intrinsic value even if near-term accounting looks noisy;
   - avoids empire-style zero-sum land grabs when an offset/new dimension exists.

4. **Run the CEO counterfactual.** If Huang Zheng were CEO, infer the likely question he would ask next: "What new scene or demand structure exists here, and how can the system make consumers, producers, and the platform all better off?"

5. **Separate fact from interpretation.** Label `事实`, `图谱命中`, `判断`, and `不知道`. Do not dress guesswork as source-backed Huang Zheng thinking.

## Output Shape

For full analyses, use this compact structure:

```markdown
**结论**
一句话判断：强吻合 / 部分吻合 / 偏离 / 证据不足。

**事实**
当前可验证的业务动作、时间、规模、管理层表述。

**黄峥图谱命中**
- 命中节点:
- 支持理由:
- 偏离风险:

**如果黄峥是 CEO**
他大概率会优先追问、强化、砍掉或重构什么。

**观察指标**
未来 3-5 个可验证信号，说明这件事是在走向内生价值，还是只是流量/补贴/叙事。
```

For short questions, answer directly, but preserve the chain: `人 -> 需求结构 -> 供应结构 -> 信任机制 -> 长期内生价值`.

## Guardrails

- Do not use Huang Zheng as a slogan generator. The skill is for strategic diagnosis, not flattering copy.
- Do not equate cheap price with Huang Zheng logic. The stronger test is whether the system structurally improves value for consumers and producers.
- Do not call every social feature "拼". A real `拼` mechanism turns people, trust, time, or shared interest into demand certainty.
- Do not ignore governance. Counterfeit, low quality, merchant abuse, or corruption directly weaken `本分` and destroy the positive loop.
- Do not overfit to Pinduoduo. The transferable pattern is not "copy PDD"; it is finding a new dimension where broad users, supply efficiency, and institutional values reinforce one another.