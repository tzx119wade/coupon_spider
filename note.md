# 加载思路
1.首先要给图片添加滚动事件
2.监听滚动事件
3.在符合加载条件的情况下读取参数


# vue里面本身带有两个回调函数：
1. 一个是`Vue.nextTick(callback)`，当数据发生变化，更新后执行回调。
2. 另一个是`Vue.$nextTick(callback)`，当dom发生变化，更新后执行的回调。

# vue on:click($event)
on:click指令里可以传递一个$event参数，这个参数就是原生的dom事件，通过访问event.target属性可以得到绑定这个事件的元素本身

# 领券说明的页面
# 首页领券领券成功的业务
# 搜券功能

# 搜券
1. 获取查询关键字
2. 查询name属性中包含关键字的所有结果
3. 操作分页

# 尝试封装惠喵的搜券接口
http://m.huim.com/ajax/searchquan?key=%E9%81%AE%E9%98%B3%E5%B8%BD&p=0&s=1

http://uland.taobao.com/coupon/edetail?e=QRaQTOOaiSLsbecaumMgZDNa%2BSwpRvrPjNhWWA8N5PNfe2hXhxrnQXC0YbkduL4v5mWo2EubojuXag2X7%2Fez7HgQnp%2FkR2Eu9h0V5GdJyUiyFfeb5yGeZGqqL5IL2kNQ%2BJF%2FYSdAETu2%2FwVislvJlBjbpO%2BcmZVNhZrIc7jaIgutYW0YMGFDnw%3D%3D&traceId=0bba613815020909610774136e&dx=1

# 首先实现分页接口请求和图片懒加载

# 热门关键词实现思路
1. 写个定时任务，在当前的23:59分的时候将当前这个时间之前的商品名写入到一个对应时间为文件名的txt文件中。
2. 将文件中的所有商品名进行分词处理，然后根据分词的结果统计出排名前10的热门关键词,将结果存储在数据库中:
item = {
	date:'date',
	value:[value],
}
3. 接口在请求的时候调用的就是这个缓存中数据,缓存中的数据每天会更新一次（与定时任务同步)。