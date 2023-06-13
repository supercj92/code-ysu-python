import matplotlib.pyplot as plt
import mplcursors
import numpy as np

# 生成数据
labels = ['A', 'B', 'C', 'D']
data = np.array([
    [20, 30, 40, 10],
    [10, 25, 35, 20],
    [15, 20, 25, 30]
])

# 绘制堆叠柱状图
fig, ax = plt.subplots()
ax.bar(labels, data[0], label='Group 1')
for i in range(1, len(data)):
    ax.bar(labels, data[i], bottom=np.sum(data[:i], axis=0), label=f'Group {i+1}')

# 添加标签
ax.set_xlabel("Group")
ax.set_ylabel("Value")
ax.set_title("Stacked Bar Chart")
ax.legend()

# 显示数值
cursor = mplcursors.cursor(ax)
@cursor.connect("add")
def on_add(sel):
    index = sel.target.index
    label = sel.artist.get_label()
    value = data[int(label[-1])-1][index]
    sel.annotation.set_text(f"{label}: {value}")

# 显示图形
plt.show()
