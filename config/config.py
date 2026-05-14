import os

# 获取当前文件所在目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据处理配置
DATA_CONFIG = {
    'file_path': os.path.join(BASE_DIR, 'groceries.csv'),
    'encoding': 'utf-8'
}

# FP-growth算法配置
FP_CONFIG = {
    'min_support': 0.01,  # 设置为1%的支持度
    'use_colnames': True
}

# 可视化配置
VIZ_CONFIG = {
    'figure_size': (12, 8),
    'dpi': 100,
    'output_path': os.path.join(BASE_DIR, 'output', 'figures')
}

# 性能测试配置
PERFORMANCE_CONFIG = {
    'support_ranges': [0.005, 0.01, 0.02, 0.03, 0.05],
    'repeat_times': 3
}