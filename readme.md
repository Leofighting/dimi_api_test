## DIM 项目接口自动化脚本

### 目录结构

- `api`：系统各功能接口
- `base_api`：基础接口类
- `data`：各接口的基础数据
- `test_case`：测试用例
- `utils`：工具函数封装
- `settings.py`：基本配置数据
- `requirements.txt`：项目依赖文件

### 项目环境
- python >= 3.0

项目依赖安装：
```python
pip install -r requirements.txt
```

### 用例执行
在 `testcase` 目录下：

命令终端输入：`pytest`