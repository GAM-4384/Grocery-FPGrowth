import os
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from config.config import DATA_CONFIG


class DataProcessor:
    def __init__(self, file_path=None):
        self.file_path = file_path or DATA_CONFIG['file_path']
        self.data = None
        self.encoded_data = None
        self.transactions = None

    def load_data(self):
        """加载数据文件"""
        try:
            # 检查文件是否存在
            if not os.path.exists(self.file_path):
                print(f"文件不存在: {self.file_path}")
                print(f"当前工作目录: {os.getcwd()}")
                print("请确保数据文件在正确的位置")
                return False

            # 直接读取文本文件，每行作为一个交易
            with open(self.file_path, 'r', encoding='utf-8') as file:
                # 读取所有行，去除空行，并将每行分割成商品列表
                self.transactions = [
                    [item.strip() for item in line.strip().split(',')]
                    for line in file.readlines()
                    if line.strip()
                ]

            print(f"成功加载数据，总交易数：{len(self.transactions)}")
            print("\n前5条交易记录示例：")
            for i, trans in enumerate(self.transactions[:5]):
                print(f"Transaction {i + 1}: {trans}")
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False

    def clean_data(self):
        """数据清洗"""
        if self.transactions is None:
            return False

        original_count = len(self.transactions)

        # 移除空的交易
        self.transactions = [trans for trans in self.transactions if trans]

        # 移除列表中的空字符串或只包含空格的字符串
        self.transactions = [
            [item for item in trans if item and not item.isspace()]
            for trans in self.transactions
        ]

        # 移除完全为空的交易
        self.transactions = [trans for trans in self.transactions if trans]

        print(f"\n清洗前交易数量：{original_count}")
        print(f"清洗后交易数量：{len(self.transactions)}")

        # 统计商品频率
        all_items = [item for trans in self.transactions for item in trans]
        item_freq = pd.Series(all_items).value_counts()

        print("\n前10个最常见的商品：")
        print(item_freq.head(10))

        return True

    def transform_data(self):
        """转换数据格式为FP-growth算法所需的形式"""
        if self.transactions is None:
            return False

        try:
            # 使用TransactionEncoder编码
            te = TransactionEncoder()
            te_ary = te.fit_transform(self.transactions)

            self.encoded_data = pd.DataFrame(
                te_ary,
                columns=te.columns_
            )

            print(f"\n编码后的数据形状：{self.encoded_data.shape}")
            print(f"特征（不同商品）数量：{len(te.columns_)}")

            return True
        except Exception as e:
            print(f"Error transforming data: {str(e)}")
            return False

    def get_processed_data(self):
        """获取处理后的数据"""
        return self.encoded_data

    def process_pipeline(self):
        """完整的数据处理流程"""
        print("\n=== 开始数据处理流程 ===")

        print("\n1. 加载数据...")
        if not self.load_data():
            print("数据加载失败")
            return None

        print("\n2. 清洗数据...")
        if not self.clean_data():
            print("数据清洗失败")
            return None

        print("\n3. 转换数据...")
        if not self.transform_data():
            print("数据转换失败")
            return None

        print("\n=== 数据处理完成 ===")
        return self.get_processed_data()