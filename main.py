from src.data_processor import DataProcessor
from src.fp_analyzer import FPAnalyzer
from src.visualizer import Visualizer
from utils.performance import PerformanceAnalyzer
import logging
import sys
import os

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def setup_logging(log_file='fp_analysis.log'):
    """设置日志配置"""
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )
    logger.addHandler(file_handler)


def main():
    try:
        setup_logging()
        logger.info("Starting FP-growth analysis...")

        # 初始化各个模块
        data_processor = DataProcessor()
        fp_analyzer = FPAnalyzer()
        visualizer = Visualizer()
        perf_analyzer = PerformanceAnalyzer()

        # 数据处理
        logger.info("Processing data...")
        processed_data = data_processor.process_pipeline()
        if processed_data is None:
            logger.error("Error in data processing")
            return

        # FP-growth分析
        logger.info("Performing FP-growth analysis...")
        if not fp_analyzer.analyze(processed_data):
            logger.error("Error in FP-growth analysis")
            return

        # 获取结果
        results = fp_analyzer.get_results()
        stats = fp_analyzer.get_stats()

        # 打印统计信息
        logger.info("\nAnalysis Statistics:")
        for key, value in stats.items():
            logger.info(f"{key}: {value}")

        # 可视化
        logger.info("Generating visualizations...")
        visualizer.plot_support_distribution(results)
        visualizer.plot_itemset_sizes(results)

        # 性能分析
        logger.info("Analyzing performance...")
        perf_results = perf_analyzer.analyze_performance(
            fp_analyzer,
            processed_data
        )

        # 绘制性能比较图
        visualizer.plot_performance_comparison(perf_results)

        # 生成性能报告
        report = perf_analyzer.generate_report(perf_results)

        # 将报告写入文件
        with open('performance_report.txt', 'w') as f:
            f.write(report)

        # 过滤结果示例：获取长度为2的频繁项集
        filtered_results = fp_analyzer.filter_results(
            min_length=2,
            max_length=2
        )

        if filtered_results is not None:
            logger.info(f"\nFound {len(filtered_results)} frequent itemsets of length 2")

        logger.info("Analysis completed successfully!")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Program terminated with error: {str(e)}")
        sys.exit(1)