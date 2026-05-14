import matplotlib.pyplot as plt
import seaborn as sns
from config.config import VIZ_CONFIG
import os


class Visualizer:
    def __init__(self):
        self.output_path = VIZ_CONFIG['output_path']
        self._setup_output_dir()

    def _setup_output_dir(self):
        """创建输出目录"""
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def plot_support_distribution(self, frequent_itemsets, save=True):
        """绘制支持度分布图"""
        plt.figure(figsize=VIZ_CONFIG['figure_size'], dpi=VIZ_CONFIG['dpi'])

        sns.histplot(data=frequent_itemsets, x='support', bins=30)
        plt.title('Distribution of Support Values')
        plt.xlabel('Support')
        plt.ylabel('Count')

        if save:
            plt.savefig(os.path.join(self.output_path, 'support_dist.png'))
        plt.close()

    def plot_itemset_sizes(self, frequent_itemsets, save=True):
        """绘制频繁项集大小分布图"""
        plt.figure(figsize=VIZ_CONFIG['figure_size'], dpi=VIZ_CONFIG['dpi'])

        sizes = frequent_itemsets['itemsets'].apply(len)
        sns.countplot(x=sizes)
        plt.title('Distribution of Itemset Sizes')
        plt.xlabel('Itemset Size')
        plt.ylabel('Count')

        if save:
            plt.savefig(os.path.join(self.output_path, 'itemset_sizes.png'))
        plt.close()

    def plot_performance_comparison(self, performance_results, save=True):
        """绘制性能比较图"""
        plt.figure(figsize=VIZ_CONFIG['figure_size'], dpi=VIZ_CONFIG['dpi'])

        plt.plot(
            performance_results['support'],
            performance_results['execution_time'],
            marker='o'
        )
        plt.title('Performance Analysis')
        plt.xlabel('Minimum Support')
        plt.ylabel('Execution Time (s)')

        if save:
            plt.savefig(os.path.join(self.output_path, 'performance.png'))
        plt.close()