import unittest
import sys
import os
from unittestreport import TestRunner

if __name__ == "__main__":
    # run_tests.py 所在目录（user_center_project_phase1）
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 项目根目录（PythonProject2）
    project_root = os.path.dirname(base_dir)

    # 将项目根目录加入模块搜索路径
    sys.path.insert(0, project_root)

    # 测试用例目录（绝对路径）
    testcases_dir = os.path.join(base_dir, "testcases")
    # 报告保存目录（绝对路径）
    report_dir = os.path.join(base_dir, "reports")

    # 发现测试用例
    suite = unittest.defaultTestLoader.discover(start_dir=testcases_dir, pattern="test_*.py")

    # 生成 HTML 报告
    runner = TestRunner(
        suite=suite,
        filename="report.html",
        report_dir=report_dir,
        title="用户中心接口测试报告",
        tester="接口测试员",
        desc="接口测试覆盖注册、登录、查询用户等核心功能"
    )

    runner.run()
