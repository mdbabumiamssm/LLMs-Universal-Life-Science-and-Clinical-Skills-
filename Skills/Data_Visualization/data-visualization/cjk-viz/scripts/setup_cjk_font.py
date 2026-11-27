#!/usr/bin/env python3
"""
CJK 字体自动检测与 matplotlib 配置

用法:
    from setup_cjk_font import setup_cjk_font, get_cjk_fp
    font_name = setup_cjk_font()  # 返回字体名或 None
    CJK_FP = get_cjk_fp()         # 返回 FontProperties 对象 (用于 .ttc 回退)

    # 绑定到 matplotlib 文本元素:
    ax.set_xlabel('中文', fontproperties=CJK_FP)
    ax.legend(title='图例', prop=CJK_FP)
    ax.get_legend().get_title().set_fontproperties(CJK_FP)

也可以直接运行来诊断当前环境:
    python3 setup_cjk_font.py
"""

import os

# 确保非交互环境下不报错
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties


# 按优先级排列的 CJK 字体候选列表
CJK_FONT_CANDIDATES = [
    'Noto Sans CJK SC',
    'Noto Sans SC',
    'Source Han Sans SC',
    'WenQuanYi Micro Hei',
    'WenQuanYi Zen Hei',
    'Droid Sans Fallback',
    'AR PL UMing CN',
    'SimHei',
    'Microsoft YaHei',
    'PingFang SC',
    'STHeiti',
    'Hiragino Sans GB',
]

# 用于在文件系统中搜索字体文件的关键词
CJK_FILE_KEYWORDS = [
    'noto', 'cjk', 'hei', 'han', 'wenquan', 'droid',
    'source', 'fang', 'song', 'ming', 'yahei',
]

# 常见字体搜索路径
FONT_SEARCH_PATHS = [
    '/usr/share/fonts',
    '/usr/local/share/fonts',
    os.path.expanduser('~/.local/share/fonts'),
    os.path.expanduser('~/.fonts'),
    # 项目内嵌字体目录
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fonts'),
]

# 全局状态
_CJK_FONT_PATH = None   # 字体文件路径
_CJK_FONT_NAME = None   # 字体名称
_CJK_IS_TTC = False      # 是否为 .ttc 格式 (需要 FontProperties 模式)


def _find_in_registered(candidates: list[str]) -> str | None:
    """从 matplotlib 已注册字体中查找候选 CJK 字体 (仅 .ttf/.otf 有效)"""
    available = {}
    for f in fm.fontManager.ttflist:
        if f.fname.lower().endswith(('.ttf', '.otf')):
            available[f.name] = f.fname
    for name in candidates:
        if name in available:
            return name
    return None


def _find_in_filesystem(keywords: list[str], search_paths: list[str]) -> tuple[str | None, str | None, bool]:
    """
    扫描文件系统查找 CJK 字体文件并注册到 matplotlib。
    优先返回 .ttf/.otf，其次 .ttc。
    Returns: (font_name, font_path, is_ttc)
    """
    ttf_hits = []
    ttc_hits = []

    for base in search_paths:
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for f in files:
                fl = f.lower()
                if not any(k in fl for k in keywords):
                    continue
                path = os.path.join(root, f)
                if fl.endswith(('.ttf', '.otf')):
                    ttf_hits.append(path)
                elif fl.endswith('.ttc'):
                    ttc_hits.append(path)

    # 优先 .ttf (rcParams 兼容性最好)
    for path in ttf_hits:
        try:
            fm.fontManager.addfont(path)
            prop = FontProperties(fname=path)
            name = prop.get_name()
            if name:
                return name, path, False
        except Exception:
            continue

    # 其次 .ttc (需要 FontProperties 模式)
    for path in ttc_hits:
        try:
            prop = FontProperties(fname=path)
            name = prop.get_name()
            fm.fontManager.addfont(path)
            if name:
                return name, path, True
        except Exception:
            continue

    return None, None, False


def _try_install_hint() -> str:
    """返回安装建议"""
    hints = []
    # 检测包管理器
    if os.path.exists('/usr/bin/apt-get') or os.path.exists('/usr/bin/apt'):
        hints.append("apt-get install -y fonts-noto-cjk")
    elif os.path.exists('/usr/bin/yum'):
        hints.append("yum install -y google-noto-sans-cjk-sc-fonts")
    elif os.path.exists('/usr/bin/dnf'):
        hints.append("dnf install -y google-noto-sans-cjk-sc-fonts")
    elif os.path.exists('/opt/homebrew') or os.path.exists('/usr/local/Homebrew'):
        hints.append("brew install font-noto-sans-cjk-sc")
    # pip 方案始终可用
    hints.append("pip install matplotlib-cjk-fonts")
    return " 或 ".join(hints)


def setup_cjk_font(
    candidates: list[str] | None = None,
    extra_paths: list[str] | None = None,
    verbose: bool = False,
) -> str | None:
    """
    检测并配置 CJK 字体用于 matplotlib。

    策略:
      1. 从已注册字体中查找 (仅 .ttf/.otf)
      2. 扫描文件系统, 优先 .ttf, 其次 .ttc
      3. .ttf → rcParams 全局设置 (最省事)
      4. .ttc → rcParams + FontProperties 模式 (需要逐个传参)

    Args:
        candidates: 自定义字体候选列表（默认使用内置列表）
        extra_paths: 额外的字体搜索路径
        verbose: 是否打印检测过程

    Returns:
        成功配置的字体名，或 None（未找到可用字体）
    """
    global _CJK_FONT_PATH, _CJK_FONT_NAME, _CJK_IS_TTC

    candidates = candidates or CJK_FONT_CANDIDATES
    search_paths = FONT_SEARCH_PATHS + (extra_paths or [])

    # 第一步：从已注册字体中查找 (仅 .ttf/.otf, 这些 rcParams 能正常工作)
    if verbose:
        print("🔍 检查 matplotlib 已注册字体 (.ttf/.otf)...")
    font_name = _find_in_registered(candidates)

    if font_name:
        # 找到 .ttf/.otf 注册字体, rcParams 方式
        plt.rcParams['font.sans-serif'] = [font_name, 'DejaVu Sans', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False
        # 找到对应文件路径
        for f in fm.fontManager.ttflist:
            if f.name == font_name and f.fname.lower().endswith(('.ttf', '.otf')):
                _CJK_FONT_PATH = f.fname
                break
        _CJK_FONT_NAME = font_name
        _CJK_IS_TTC = False
        if verbose:
            print(f"✅ CJK 字体已配置 (ttf, rcParams): {font_name}")
        return font_name

    # 第二步：扫描文件系统
    if verbose:
        print("🔍 扫描文件系统查找 CJK 字体 (优先 .ttf, 其次 .ttc)...")
    font_name, font_path, is_ttc = _find_in_filesystem(CJK_FILE_KEYWORDS, search_paths)

    if font_name:
        _CJK_FONT_PATH = font_path
        _CJK_FONT_NAME = font_name
        _CJK_IS_TTC = is_ttc
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = [font_name, 'DejaVu Sans', 'sans-serif']

        mode = "ttc, FontProperties 模式" if is_ttc else "ttf, rcParams"
        if verbose or is_ttc:
            print(f"✅ CJK 字体已配置 ({mode}): {font_name} -> {font_path}")
        if is_ttc:
            print("   ⚠️  .ttc 格式: rcParams 可能不生效, 请对每个文本元素传 fontproperties=get_cjk_fp()")
        return font_name

    # 未找到
    print(f"⚠️  未找到可用的 CJK 字体，中文可能显示为方块。")
    print(f"   安装建议: {_try_install_hint()}")
    return None


def get_cjk_fp() -> FontProperties:
    """
    获取 CJK FontProperties 对象。

    用于 matplotlib 文本元素的 fontproperties= 参数。
    对 .ttc 文件这是唯一可靠的渲染方式；对 .ttf 也兼容。

    用法:
        CJK_FP = get_cjk_fp()
        ax.set_xlabel('中文', fontproperties=CJK_FP)
        ax.set_title('标题', fontproperties=CJK_FP)
        ax.legend(title='图例', prop=CJK_FP)
        ax.get_legend().get_title().set_fontproperties(CJK_FP)
    """
    if _CJK_FONT_PATH:
        return FontProperties(fname=_CJK_FONT_PATH)
    return FontProperties()


def is_ttc_mode() -> bool:
    """是否处于 .ttc FontProperties 模式 (需要逐个传参)"""
    return _CJK_IS_TTC


def diagnose():
    """诊断当前环境的 CJK 字体情况"""
    print("=" * 60)
    print("CJK 字体诊断")
    print("=" * 60)

    # 列出所有已注册的 CJK 相关字体
    all_fonts = sorted(set(f.name for f in fm.fontManager.ttflist))
    cjk_fonts = [
        name for name in all_fonts
        if any(k in name.lower() for k in CJK_FILE_KEYWORDS + ['cjk', 'chinese', 'sc', 'tc', 'jp', 'kr'])
    ]

    print(f"\n📋 matplotlib 已注册的 CJK 相关字体 ({len(cjk_fonts)}):")
    for name in cjk_fonts:
        paths = [f.fname for f in fm.fontManager.ttflist if f.name == name]
        ext = os.path.splitext(paths[0])[1] if paths else '?'
        marker = "  ✅" if name in CJK_FONT_CANDIDATES else "  •"
        ttc_warn = " ⚠️ .ttc需FontProperties" if ext == '.ttc' else ""
        print(f"{marker} {name} ({ext}){ttc_warn}")

    if not cjk_fonts:
        print("  (无)")

    # 扫描文件系统
    print(f"\n🔍 文件系统字体文件:")
    for base in FONT_SEARCH_PATHS:
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for f in files:
                fl = f.lower()
                if any(k in fl for k in CJK_FILE_KEYWORDS) and fl.endswith(('.ttf', '.otf', '.ttc')):
                    ext = os.path.splitext(f)[1]
                    tag = "⚠️ .ttc" if ext == '.ttc' else "✅ .ttf"
                    print(f"  {tag}  {os.path.join(root, f)}")

    # 尝试配置
    print(f"\n🔧 自动配置结果:")
    result = setup_cjk_font(verbose=True)

    if result:
        fp = get_cjk_fp()
        print(f"\n📌 模式: {'FontProperties (.ttc)' if is_ttc_mode() else 'rcParams (.ttf)'}")
        print(f"   字体路径: {_CJK_FONT_PATH}")

        # 生成测试图
        print(f"\n🖼️  生成测试图...")
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.text(0.5, 0.6, '中文字体测试 Chinese Font Test',
                ha='center', va='center', fontsize=18, transform=ax.transAxes,
                fontproperties=fp)
        ax.text(0.5, 0.3, f'字体: {result} ({"ttc→FontProperties" if is_ttc_mode() else "ttf→rcParams"})',
                ha='center', va='center', fontsize=12, color='gray',
                transform=ax.transAxes, fontproperties=fp)
        ax.set_title('CJK 字体验证', fontproperties=fp)
        ax.axis('off')

        out_path = '/tmp/cjk_font_test.png'
        fig.savefig(out_path, dpi=100, bbox_inches='tight')
        plt.close(fig)
        print(f"✅ 测试图已保存: {out_path}")
    else:
        print(f"\n💡 安装建议: {_try_install_hint()}")

    print("=" * 60)


if __name__ == '__main__':
    diagnose()
