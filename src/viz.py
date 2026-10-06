from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager


def setup_style():
    """配置 matplotlib 中文字体和统一风格。"""
    # 自动找可用的中文字体
    candidates = [
        "C:/Windows/Fonts/msyh.ttc",                          # Windows 微软雅黑
        "C:/Windows/Fonts/simhei.ttf",                        # Windows 黑体
        "/System/Library/Fonts/PingFang.ttc",                 # macOS
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",       # Linux
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    ]
    for path in candidates:
        if Path(path).exists():
            prop = font_manager.FontProperties(fname=path)
            plt.rcParams["font.family"] = prop.get_name()
            print(f"使用中文字体: {prop.get_name()}")
            break
    else:
        print("未找到中文字体，中文可能显示为方块")

    plt.rcParams["axes.unicode_minus"] = False

    # 统一风格
    sns.set_theme(style="whitegrid", palette="Set2")
    plt.rcParams["figure.figsize"] = (10, 5)
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["savefig.dpi"] = 150
    plt.rcParams["savefig.bbox"] = "tight"

    # 常用色板
    return {
        "blue": "#4C72B0",
        "green": "#55A868",
        "orange": "#DD8452",
        "red": "#C44E52",
        "purple": "#8172B2",
        "colors": ["#4C72B0", "#55A868", "#DD8452", "#C44E52"],
    }


def get_font_prop():
    """返回一个中文字体 FontProperties，跨平台自动找。"""
    candidates = [
        "C:/Windows/Fonts/msyh.ttc",       # Windows 微软雅黑
        "C:/Windows/Fonts/simhei.ttf",     # Windows 黑体
        "C:/Windows/Fonts/simsun.ttc",     # Windows 宋体
        "/System/Library/Fonts/PingFang.ttc",  # macOS
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",  # Linux
    ]
    for path in candidates:
        if Path(path).exists():
            font_manager.fontManager.addfont(path)
            print(f"使用字体: {path}")
            return font_manager.FontProperties(fname=path)
    raise FileNotFoundError("未找到中文字体")


def apply_chinese(ax, font_prop):
    """给一个 Axes 的所有文本设置中文字体。"""
    ax.set_title(ax.get_title(), fontproperties=font_prop)
    ax.set_xlabel(ax.get_xlabel(), fontproperties=font_prop)
    ax.set_ylabel(ax.get_ylabel(), fontproperties=font_prop)
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_prop)
    for label in ax.get_yticklabels():
        label.set_fontproperties(font_prop)
    # 图例
    legend = ax.get_legend()
    if legend:
        for text in legend.get_texts():
            text.set_fontproperties(font_prop)

def save_fig(fig, name, figures_dir):
    """保存图片到 figures_dir。"""
    path = Path(figures_dir) / name
    fig.savefig(path, bbox_inches="tight")
    print(f"已保存: {path}")