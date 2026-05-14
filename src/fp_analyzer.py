from mlxtend.frequent_patterns import fpgrowth
from config.config import FP_CONFIG


class FPAnalyzer:
    def __init__(self, min_support=None):
        self.min_support = min_support or FP_CONFIG['min_support']
        self.frequent_itemsets = None

    def analyze(self, data):
        """执行FP-growth分析"""
        try:
            self.frequent_itemsets = fpgrowth(
                data,
                min_support=self.min_support,
                use_colnames=FP_CONFIG['use_colnames']
            )
            return True
        except Exception as e:
            print(f"Error in FP-growth analysis: {str(e)}")
            return False

    def get_results(self):
        """获取分析结果"""
        return self.frequent_itemsets

    def get_stats(self):
        """获取分析统计信息"""
        if self.frequent_itemsets is None:
            return None

        stats = {
            'total_itemsets': len(self.frequent_itemsets),
            'avg_support': self.frequent_itemsets['support'].mean(),
            'max_support': self.frequent_itemsets['support'].max(),
            'min_support': self.frequent_itemsets['support'].min()
        }

        return stats

    def filter_results(self, min_length=2, max_length=None):
        """筛选特定长度的频繁项集"""
        if self.frequent_itemsets is None:
            return None

        filtered = self.frequent_itemsets[
            self.frequent_itemsets['itemsets'].apply(len) >= min_length
            ]

        if max_length:
            filtered = filtered[
                filtered['itemsets'].apply(len) <= max_length
                ]

        return filtered