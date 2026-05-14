import time
import pandas as pd
from config.config import PERFORMANCE_CONFIG


class PerformanceAnalyzer:
    def __init__(self):
        self.support_ranges = PERFORMANCE_CONFIG['support_ranges']
        self.repeat_times = PERFORMANCE_CONFIG['repeat_times']

    def measure_execution_time(self, func, *args, **kwargs):
        """测量函数执行时间"""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        return {
            'execution_time': end_time - start_time,
            'result': result
        }

    def analyze_performance(self, fp_analyzer, data):
        """分析不同支持度下的性能"""
        results = []

        for support in self.support_ranges:
            times = []
            itemsets_count = []

            # 重复测试多次取平均值
            for _ in range(self.repeat_times):
                fp_analyzer.min_support = support
                measurement = self.measure_execution_time(
                    fp_analyzer.analyze,
                    data
                )

                times.append(measurement['execution_time'])
                if measurement['result']:
                    itemsets_count.append(
                        len(fp_analyzer.get_results())
                    )

            # 计算平均值
            avg_time = sum(times) / len(times)
            avg_count = sum(itemsets_count) / len(itemsets_count) if itemsets_count else 0

            results.append({
                'support': support,
                'execution_time': avg_time,
                'itemsets_count': avg_count
            })

        return pd.DataFrame(results)

    def generate_report(self, performance_results):
        """生成性能报告"""
        report = "Performance Analysis Report\n"
        report += "=" * 30 + "\n\n"

        for _, row in performance_results.iterrows():
            report += f"Support: {row['support']}\n"
            report += f"Execution Time: {row['execution_time']:.4f} seconds\n"
            report += f"Itemsets Found: {int(row['itemsets_count'])}\n"
            report += "-" * 30 + "\n"

        return report