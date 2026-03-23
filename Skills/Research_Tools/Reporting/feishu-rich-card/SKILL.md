---
name: feishu-rich-card
description: >
  Send rich interactive cards with embedded images in Feishu group chats.
  Use when reporting progress, sharing analysis results, or presenting any content
  that benefits from mixed text+image layout in Feishu.
  Combines SVG UI templates (or matplotlib/PIL charts) with Feishu Card Kit API.
---

> **Repository note:** Stored at `repo/Skills/Research_Tools/Reporting/feishu-rich-card`
> with helper scripts in `references/`. Works best with the neighboring
> `svg-ui-templates` skill for high-fidelity graphics.

# Feishu Rich Card — 飞书图文混排卡片

在飞书群聊中发送**图文并茂**的交互式卡片，用于汇报进展、展示分析结果、项目状态等。

## When to Use

- 汇报任务进展、项目状态
- 展示数据分析结果（图表 + 解读）
- 发送研究简报、阶段性成果
- 任何需要图文混排的飞书消息

## Architecture

```
生成图片(SVG→PNG / matplotlib / PIL)
        ↓
上传图片到飞书 → 获取 image_key
        ↓
构造 Card JSON (schema 2.0) → 嵌入 img 元素 + markdown 元素
        ↓
调用飞书 API 发送 interactive 消息
```

## Workflow

### Step 1: Prepare Images

图片来源可以是：
- **SVG UI 模板** → 用 `svg-ui-templates` skill 生成 SVG → cairosvg 转 PNG
- **matplotlib/seaborn** → 直接 savefig 为 PNG
- **PIL/Pillow** → 程序化生成图片
- **已有文件** → 直接使用本地 PNG/JPG

### Step 2: Upload & Send

使用 `references/send_card.py` 中的辅助函数：

```python
# 完整用法参见 references/send_card.py
from send_card import FeishuCardSender

sender = FeishuCardSender()  # 自动读取 openclaw.json 凭证

# 发送图文卡片
sender.send_rich_card(
    chat_id="oc_xxx",
    title="📊 分析报告",
    elements=[
        {"type": "markdown", "content": "## 结果摘要\n\n发现 **3 个**显著差异基因"},
        {"type": "image", "path": "/tmp/volcano_plot.png", "alt": "火山图"},
        {"type": "markdown", "content": "> Gene X: FC=2.5, p<0.001"},
        {"type": "hr"},
        {"type": "image", "path": "/tmp/heatmap.png", "alt": "热图"},
        {"type": "markdown", "content": "**结论：** 样本间差异显著，建议进一步验证。"},
    ],
    header_template="blue"  # blue/indigo/green/red/purple/violet/wathet/turquoise/yellow/grey
)
```

### Step 3: Quick One-liner (for simple cases)

```python
sender.send_image_report(
    chat_id="oc_xxx",
    title="🧬 单细胞分析完成",
    intro="UMAP 降维完成，共识别 12 个细胞群：",
    image_path="/tmp/umap.png",
    conclusion="Cluster 5 为目标细胞群，marker: CD8A, GZMB, PRF1",
    header_template="indigo"
)
```

## Card Elements Reference

| Element | Tag | 说明 |
|---------|-----|------|
| **Markdown** | `markdown` | 支持加粗、斜体、链接、列表、引用块、代码块 |
| **Image** | `img` | 需要 `image_key`（上传后获取） |
| **Divider** | `hr` | 水平分割线 |
| **Column Set** | `column_set` | 多列并排布局 |
| **Note** | `note` | 底部灰色备注 |

## Header Templates (颜色)

`blue` `wathet` `turquoise` `green` `yellow` `orange` `red` `carmine` `violet` `purple` `indigo` `grey`

## Key Rules

1. **图片必须先上传**到飞书获取 `image_key`，不能用 URL
2. **Card schema 必须是 `"2.0"`**
3. **每张卡片最多 50 个元素**
4. 图片建议宽度 600-1200px，飞书会自动缩放
5. markdown 中**不能嵌入图片**，图片必须是独立的 `img` 元素
6. 发送后 OpenClaw 的正常回复会重复，用 `NO_REPLY` 避免

## Integration with SVG UI Templates

当需要专业级可视化时，结合 `svg-ui-templates` skill：

```bash
# 1. 生成 SVG（用模板或自定义）
# 2. 转 PNG
python3 -c "import cairosvg; cairosvg.svg2png(url='report.svg', write_to='report.png', output_width=2400)"
# 3. 用本 skill 上传并发送卡片
```

## Default Chat ID

通过环境变量配置：`FEISHU_DEFAULT_CHAT_ID`（在 `.env` 中设置）
