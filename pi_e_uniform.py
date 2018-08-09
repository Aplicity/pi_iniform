# 以下是为了验证 圆周率pi中出现的数字服从均匀分布
import matplotlib.pyplot as plt
from mpmath import mp

mp.dps=100000  # 确定数值的精度，可以理解保留多少为有效数字
A=list(str(mp.pi))  # 把有效数字为100000的pi中各个数字放到A中
del A[1]    # 删掉pi中的小数点
x=range(10)
n=[]
for i in range(10):
    n.append(A.count(str(i)))   # 统计pi中每个数值出现的频数
plt.bar(x,n)    # 画出条形图
plt.title('圆周率pi中各个数字频数')
plt.show()

##### 除了圆周率pi之外，另外一个 特殊数值e=2.7...也有同样的均匀性
## 同样把上面的代码中 的pi换成 e即可得到
E=list(str(mp.e))
del E[1]

n=[]
for i in range(10):
    n.append(E.count(str(i)))
x=range(10)
plt.bar(x,n)
plt.title('e中各个数字频数')
plt.show()


