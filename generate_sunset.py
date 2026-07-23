import csv
import os

# 1. 配置你的 CSV 文件名
csv_file = r'D:/OneDrive/桌面/20260721.csv'
html_file = 'index.html'

# 2. 读取 CSV 数据
data_rows = []
try:
    with open(csv_file, 'r', encoding='utf-8-sig') as f:  # utf-8-sig 兼容 Excel 导出的 CSV
        reader = csv.DictReader(f)
        for row in reader:
            data_rows.append(row)
except Exception as e:
    print(f"读取 CSV 失败: {e}")
    exit()

# 3. 生成 HTML 表格行
table_body = ""
for row in data_rows:
    table_body += f"""
        <tr>
            <td>{row.get('观赏点', '')}</td>
            <td><span class="badge">{row.get('晚霞等级', '')}</span></td>
            <td>{row.get('出现概率', '')}</td>
            <td>{row.get('预计开始时间', '')} - {row.get('预计结束时间', '')}</td>
        </tr>
    """

# 4. 完整的 HTML 模板（包含现代 CSS 样式）
html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>晚霞观赏预报</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(to bottom, #ff9a9e, #fad0c4); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 900px; margin: 0 auto; background: rgba(255,255,255,0.9); border-radius: 12px; padding: 30px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); }}
        h1 {{ text-align: center; color: #d35400; margin-bottom: 30px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ padding: 15px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background-color: #f8f9fa; color: #555; font-weight: 600; }}
        tr:hover {{ background-color: #fff5f5; }}
        .badge {{ background: #ff7675; color: white; padding: 4px 10px; border-radius: 12px; font-size: 0.9em; }}
        .footer {{ text-align: center; margin-top: 30px; color: #888; font-size: 0.8em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌅 晚霞观赏预报</h1>
        <table>
            <thead>
                <tr>
                    <th>观赏点</th>
                    <th>晚霞等级</th>
                    <th>出现概率</th>
                    <th>预计时间</th>
                </tr>
            </thead>
            <tbody>
                {table_body}
            </tbody>
        </table>
        <div class="footer">数据来源: 20260721.csv | 自动生成网页</div>
    </div>
</body>
</html>
"""

# 5. 写入 HTML 文件
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ 网页生成成功！")
print(f"📂 文件位置: {os.path.abspath(html_file)}")
print("💡 提示: 直接将这个 HTML 文件发给朋友，他们用浏览器打开即可查看！")
