# Local Research Dashboard Skill

## 概述
每次科研任务开始时，生成一个临时的本地 dashboard，动态展示任务关键信息和产物预览。

## 组件
- `state.json`：数据协议，openclaw 负责写入和更新
- `dashboard.html`：本地单文件页面，轮询 state.json 并渲染
- `dashboard_serve.py`：静态文件服务器，serve 任务根目录

所有文件放在**任务独立目录**中（如 `data/<task_name>/dashboard/`）。

> **Repository note:** 模板位于 `repo/Skills/Research_Tools/Reporting/dashboard/`。
> 启动任务时从该路径复制 `dashboard.html` 与 `dashboard_serve.py`。

---

## state.json Schema

```json
{
  "title": "任务标题",
  "updated_at": "2024-01-01 12:00:00",
  "panels": [
    {
      "type": "progress|text|list|code|table|image|files|step",
      "label": "面板标题（可折叠的标识）",
      "content": "内容（格式取决于 type）"
    }
  ]
}
```

### Panel 类型说明

| type | content 格式 | 用途 | 渲染 |
|------|------------|------|------|
| `progress` | number (0-100) | 整体进度 | **置顶在 header**，不出现在面板区 |
| `text` | string | 状态描述、摘要、发现 | 预格式化文本，自动换行 |
| `list` | string[] | 步骤列表、待办、已完成项 | 带左边框的条目列表 |
| `code` | string | 代码片段、命令输出 | 等宽字体，可滚动，带复制按钮 |
| `table` | `{src: "path"}` 或 `{headers: [...], rows: [...]}` | CSV/统计结果 | 从文件实时加载或内嵌数据 |
| `image` | string 或 string[] | 图片产物预览 | 内联图片，点击放大，带下载按钮 |
| `files` | `string[] 或 {name, size}[]` | 输出目录文件列表 | 可点击预览/下载的文件列表 |
| `step` | `{desc, code?, outputs?}` | **步骤卡片**：展示一个分析步骤的代码和产物 | 代码 + 产物预览 + 描述 |

### step 类型（核心面板）

**目标：** 每个分析步骤 = 做了什么 + 跑了什么代码 + 产出了什么

```json
{
  "type": "step",
  "label": "① 数据加载与清洗",
  "content": {
    "desc": "加载 CHARLS .dta 数据，编码 8 项 ACE 指标...",
    "code": "import pandas as pd\ndf = pd.read_stata('charls.dta')\n...",
    "outputs": [
      {"kind": "text", "value": "原始 96,628 行 → 筛选后 46,628 行（12,877 人）"},
      {"kind": "image", "src": "/output/fig1_ace_distribution.png", "caption": "ACE 评分分布"},
      {"kind": "table", "src": "/output/table1_baseline.csv", "caption": "基线特征"},
      {"kind": "file", "src": "/output/table1_baseline.csv"}
    ]
  }
}
```

#### step.content 字段

| 字段 | 必填 | 说明 |
|------|------|------|
| `desc` | ✅ | 这步做了什么、发现了什么（完整句子） |
| `code` | 可选 | 核心代码片段（默认折叠，展示关键逻辑） |
| `code_file` | 可选 | 完整脚本文件路径（如 `/analysis.py`），前端按需加载 |
| `outputs` | 可选 | 产物列表 |

> **约定：** `code` 放精华片段帮助快速理解逻辑；`code_file` 指向完整可运行的脚本。两者可同时存在。

#### outputs[].kind

| kind | 说明 |
|------|------|
| `text` | 文字结果（`value` 字段） |
| `image` | 图片（`src` 路径，可选 `caption`） |
| `table` | 表格（`src` 指向 CSV 文件路径，前端实时加载解析） |
| `file` | 文件下载链接（`src` 路径） |

### table 类型的两种模式

**模式1：文件引用（推荐）** — 前端实时 fetch CSV 文件：
```json
{"type": "table", "label": "表1: 基线", "content": {"src": "/output/table1.csv"}}
```

**模式2：内嵌数据（向后兼容）** — 数据直接写在 state.json：
```json
{"type": "table", "label": "表1", "content": {"headers": [...], "rows": [...]}}
```

---

## 交互功能

### 复制与下载
所有可预览内容都有操作按钮：
- **代码块** → 「📋 复制」按钮
- **表格** → 「📋 复制 TSV」「⬇ 下载 CSV」按钮
- **图片** → 「⬇ 下载」按钮
- **文本预览** → 「📋 复制」按钮
- **文件列表** → 每项可点击预览或下载

### 面板可折叠
- 点击面板标题栏可折叠/展开
- 折叠状态在同一次页面会话中记忆
- 动画有阻尼感（cubic-bezier ease）

---

## 配色

使用 **IBM 色盲友好色板**：
- Blue: #648FFF
- Purple: #785EF0
- Magenta: #DC267F
- Orange: #FE6100
- Yellow: #FFB000

暗色背景使用 GitHub Dark 色系。

---

## openclaw 的职责

### 1. 任务开始时
在任务目录下创建 `dashboard/` 子目录，复制模板文件，生成初始 `state.json`。

### 2. 每个关键步骤完成后
更新 state.json，**使用 `step` 面板**：
- 更新 progress panel 的值
- 为当前步骤创建 `step` panel，包含：
  - `desc`：详细描述做了什么、发现了什么
  - `code`：关键代码片段（不需要完整脚本，抓核心逻辑）
  - `outputs`：这步产出的所有东西（图片、表格、文字结果、文件）

### 3. 文字描述原则
- 不要只写"完成了"，要写**做了什么、发现了什么**
- 统计结果要写具体数值（OR、CI、p值）
- 数据筛选要写筛选前后的样本量变化
- 异常/警告要明确说明原因和影响

**✅ 好的 step 描述：**
```json
{
  "type": "step",
  "label": "① 数据加载与清洗",
  "content": {
    "desc": "加载 CHARLS .dta 数据（5 波次），编码 8 项 ACE 指标（身体虐待、情感忽视等），构建 3 个 CVD 结局变量。按年龄≥60、ACE 非缺失≥5 项、≥2 波次筛选，保留 12,877 人（46,628 人次观测），流失 50.2% 主要因年龄限制。",
    "code": "df = pd.read_stata('charls.dta')\nace_cols = ['abuse_physical', 'abuse_emotional', ...]\ndf['ace_score'] = df[ace_cols].sum(axis=1)\ndf = df[df.age >= 60]\ndf = df.groupby('id').filter(lambda x: len(x) >= 2)",
    "outputs": [
      {"kind": "text", "value": "原始: 96,628 行 (25,873 人) → 筛选后: 46,628 行 (12,877 人)"},
      {"kind": "text", "value": "ACE Cronbach's α = 0.477"}
    ]
  }
}
```

**❌ 差的描述：**
> desc: "数据加载完成"

### 4. 任务结束时
- 进度设为 100
- 添加 files panel 列出所有产物
- 写最终总结 step

---

## 使用方式

**Step 1** — 复制模板到任务目录：
```bash
TASK_DIR=/path/to/task
mkdir -p "$TASK_DIR/dashboard"
cp skills/dashboard/dashboard.html "$TASK_DIR/dashboard/"
cp skills/dashboard/dashboard_serve.py "$TASK_DIR/dashboard/"
```

**Step 2** — 生成初始 state.json

**Step 3** — 启动服务器（serve 任务根目录）：
```bash
python "$TASK_DIR/dashboard/dashboard_serve.py" --port 7788
# 或显式指定根目录：
python "$TASK_DIR/dashboard/dashboard_serve.py" --root "$TASK_DIR" --port 7788
```
Dashboard URL: `http://localhost:7788/dashboard/dashboard.html`

**Step 4** — 告诉用户打开链接，然后执行任务并持续更新 state.json

### 路径约定

**重要：** `dashboard_serve.py` 默认 serve **任务根目录**（dashboard/ 的父目录）。

所有资源路径使用**绝对路径**（相对于 serve 根 = 任务根目录），以 `/` 开头：
```json
{"src": "/output/fig1.png"}
{"content": "/output/fig1.png"}
```

Dashboard URL: `http://localhost:PORT/dashboard/dashboard.html`
