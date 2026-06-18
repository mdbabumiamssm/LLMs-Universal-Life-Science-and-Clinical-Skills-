<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

---
name: bio-cjk-viz
description: "CJK (\u4E2D\u65E5\u97E9) \u5B57\u4F53\u68C0\u6D4B\u4E0E matplotlib \u914D\
  \u7F6E\u3002\u4EFB\u4F55\u6D89\u53CA\u4E2D\u6587\u6807\u7B7E\u3001\u6807\u9898\u3001\
  \u56FE\u4F8B\u7684 \u53EF\u89C6\u5316\u4EFB\u52A1\u542F\u52A8\u524D\u5FC5\u987B\u5148\
  \u6267\u884C\u672C skill \u7684\u5B57\u4F53\u68C0\u6D4B\u6D41\u7A0B\uFF0C\u786E\u4FDD\
  \u4E0D\u4F1A\u51FA\u73B0\u65B9\u5757\u4E71\u7801\u3002 \u9002\u7528\u4E8E matplotlib\
  \ / seaborn / plotly \u9759\u6001\u5BFC\u51FA\u7B49\u573A\u666F\u3002\n"
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

> **Repository note:** Stored at `repo/Skills/Data_Visualization/data-visualization/cjk-viz`.
> Update import paths accordingly when referencing `setup_cjk_font.py` from other skills.

# CJK 可视化字体配置

## 何时使用

任何绘图代码中包含中文文本（标题、轴标签、图例、注释）时，**必须在绘图前**
执行字体检测。不要假设某个字体一定存在。

## 快速使用

### 方式一：导入 helper（推荐）

将 `scripts/setup_cjk_font.py` 复制到工作目录，或直接引用：

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'skills/cjk-viz/scripts'))
from setup_cjk_font import setup_cjk_font

font_name = setup_cjk_font()  # 自动检测、配置、返回字体名
# 如果返回 None，说明系统无可用 CJK 字体，会打印警告
```

调用后 `plt.rcParams` 已经配置好，直接绘图即可。

### 方式二：内联代码片段

如果不想引入外部文件，在脚本开头加入：

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def _setup_cjk():
    candidates = [
        'Noto Sans CJK SC', 'Noto Sans SC', 'Source Han Sans SC',
        'WenQuanYi Micro Hei', 'WenQuanYi Zen Hei',
        'Droid Sans Fallback', 'AR PL UMing CN',
        'SimHei', 'Microsoft YaHei', 'PingFang SC',
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            plt.rcParams['font.sans-serif'] = [name, 'DejaVu Sans']
            plt.rcParams['axes.unicode_minus'] = False
            return name
    # 尝试从常见路径加载 .ttf
    search_paths = [
        '/usr/share/fonts', '/usr/local/share/fonts',
        os.path.expanduser('~/.local/share/fonts'),
        os.path.join(os.path.dirname(__file__), 'fonts'),
    ]
    for base in search_paths:
        for root, _, files in os.walk(base):
            for f in files:
                if f.lower().endswith('.ttf') and any(
                    k in f.lower() for k in ['noto', 'cjk', 'hei', 'han', 'wenquan', 'droid']
                ):
                    path = os.path.join(root, f)
                    fm.fontManager.addfont(path)
                    prop = fm.FontProperties(fname=path)
                    name = prop.get_name()
                    plt.rcParams['font.sans-serif'] = [name, 'DejaVu Sans']
                    plt.rcParams['axes.unicode_minus'] = False
                    return name
    print("⚠️  未找到 CJK 字体，中文可能显示为方块。")
    print("   安装建议: apt install fonts-noto-cjk 或 pip install matplotlib-cjk-fonts")
    return None

_cjk_font = _setup_cjk()
```

### 方式三：安装字体后再绘图

如果检测失败，在 Docker 容器内安装：

```bash
apt-get update && apt-get install -y fonts-noto-cjk
# 或者用 pip 安装打包好的字体
pip install matplotlib-cjk-fonts
```

安装后需要清除 matplotlib 字体缓存：

```python
import matplotlib
import shutil, os
cache_dir = matplotlib.get_cachedir()
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)
    print(f"已清除缓存: {cache_dir}")
```

## 关键陷阱：`.ttc` 文件与 matplotlib

**这是最常见的坑。** 很多 Linux/Docker 环境安装的 CJK 字体是 `.ttc`（TrueType Collection）
格式（如 `NotoSansCJK-Regular.ttc`），matplotlib 能检测到但 `rcParams` 设置后不生效。

### 症状
- `setup_cjk_font()` 报告成功，但图片中文仍显示为方块 □□□
- `findfont()` 能找到字体文件，但渲染时不使用

### 解决方案：FontProperties 模式

对 `.ttc` 文件，必须用 `FontProperties(fname=path)` 显式传给每个文本元素：

```python
from matplotlib.font_manager import FontProperties

# 全局 FontProperties 对象
CJK_FP = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')

# 用法: 每个含中文的文本元素都要传 fontproperties=CJK_FP
ax.set_xlabel('中文标签', fontproperties=CJK_FP)
ax.set_ylabel('中文标签', fontproperties=CJK_FP)
ax.set_title('中文标题', fontproperties=CJK_FP)
ax.set_yticklabels(chinese_labels, fontproperties=CJK_FP)

# legend 需要特殊处理: prop= 设置条目字体, title 需要单独设置
ax.legend(title='中文图例标题', prop=CJK_FP)
ax.get_legend().get_title().set_fontproperties(CJK_FP)

# suptitle 同理
plt.suptitle('中文总标题', fontproperties=CJK_FP)
```

### 优先级策略

1. **优先找 `.ttf` 文件** → 可以用 `rcParams` 全局设置，最省事
2. **只有 `.ttc` 文件** → 必须用 `FontProperties(fname=)` 逐个传参
3. **都没有** → 安装字体或用内嵌 `.ttf`

### helper 脚本已内置此逻辑

`scripts/setup_cjk_font.py` 的 `setup_cjk_font()` 会优先找 `.ttf`，
找不到时返回 `.ttc` 路径。调用 `get_cjk_fp()` 获取 `FontProperties` 对象。

## 字体优先级

按以下顺序尝试（覆盖大多数 Linux / Docker / macOS 环境）：

| 优先级 | 字体名 | 常见来源 |
|--------|--------|----------|
| 1 | Noto Sans CJK SC | `fonts-noto-cjk` (Debian/Ubuntu) |
| 2 | Noto Sans SC | Google Fonts |
| 3 | Source Han Sans SC | Adobe 思源黑体 |
| 4 | WenQuanYi Micro Hei | `fonts-wqy-microhei` |
| 5 | WenQuanYi Zen Hei | `fonts-wqy-zenhei` |
| 6 | Droid Sans Fallback | Android / 旧版 Docker 镜像 |
| 7 | AR PL UMing CN | `fonts-arphic-uming` |
| 8 | SimHei | Windows |
| 9 | Microsoft YaHei | Windows |
| 10 | PingFang SC | macOS |

## 与其他 skill 配合

- 使用 `scientific-visualization` 或 `matplotlib` skill 时，先执行本 skill 的字体配置
- 使用 `plotly` 生成静态图片（`write_image`）时同样需要配置字体
- 在 `biomed-dispatch` 的 prompt 中可以加入："绘图前先运行 cjk-viz 字体检测"

## 验证

绘图后可以用以下代码快速验证中文是否正常渲染：

```python
fig, ax = plt.subplots(figsize=(4, 2))
ax.text(0.5, 0.5, '中文测试 Chinese Test 123',
        ha='center', va='center', fontsize=16, transform=ax.transAxes)
ax.set_title('字体验证')
fig.savefig('/workspace/outputs/cjk_font_test.png', dpi=100, bbox_inches='tight')
print("✅ 验证图已保存，请检查中文是否正常显示")
```

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->