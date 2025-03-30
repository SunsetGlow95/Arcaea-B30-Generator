# Arcaea-B30-Generator

本地使用 Python 生成可视化 Arcaea B30，指导 Arcaea 推分。

## 环境要求

- 下载 Python3，并装有 `pygal` 库。

## 使用说明

- 建立一个文件夹。下放 `render.py` 和一个文件名为 `data.txt` 的文件，格式如示例一样，曲名部分不可以加空格。
- 终端运行 `python -m render.py`。
- 在该文件夹下会生成 `table.svg` 和 `table.txt` 为生成结果。
