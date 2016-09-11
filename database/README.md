# 3个常用数据库对比——选择合适数据库  
> 更新于2016-09-10 10:09 持续更新中  作者:[baobaopangzi88](https://github.com/baobaopangzi88 "github")  
  
| 名字      | 特性             | 描述                           |  
|-----------|------------------|--------------------------------|  
| MongoDB   | 文档型数据库     | 简单来说就是加强版的mysql      |  
| Redis     | 键值型内存数据库 | 通常用法是记录一整块数据       |      |  
| Mysql     | 关系型数据库     |                                |  
  
  
## MongoDB 特性  
- 可以任意增加字段、属性。适合需求不固定的项目。  
    用法: `db.student.update({"name":"yaoge"},{$set:{"age":13}})`  
  
    - Redis用法  
        `hset student:yaoge age 13`  
        缺点:查询的时候需要自己创建索引  
        简单实现索引的两种方法  
        1. 根据首字母创建索引  
        `zadd student:nameindex 0 yaoge 0 aaa 0 bbb`  
        `zrangebyindex student:nameindex [y (z`  
        2. 根据年龄创建索引  
        `zadd student:ageindex 13 yaoge 14 aaa 15 bbb`  
        `zrangebyscore student:ageindex 13 14`  
  
    - MySQL用法  
        只能通过给所有行都增加这个字段来实现,最关键的是如果是线上的数据库，锁表的时间是不可接受的  
  
- 易于扩展,自动分片  
    通常要提升服务器的性能需要考虑横向扩展和纵向扩展。纵向扩展也就是提升单机的性能，开销是很大的,同时一定会有一个限制。另一种是横向扩展，也就是说能在只增加机器的情况下就能线性的提升性能。  
    - Redis用法  
        相同  
    - MySQL用法  
        通常的做法是人为分库、分表,然后增加一层路由查找需要的数据库。  
  
  
## Redis 特性  
- 基于内存的数据库  
    速度快，适用于需要高频写入的应用  
    - MongoDB用法  
        支持，需要设置,性能还是会有差异  
    - MySQL-Memcached  
        不能持久化，没有数据类型  
  
- 丰富的数据类型  
    字典、集合、有序集合、字符串、链表  
    - MongoDB用法  
        可以用索引实现排序,集合不支持  
    - MySQL用法  
        可以用索引实现排序  
  
## MySQL 特性  
- 支持事务(Innodb)  
    - MongoDB用法  
        支持单文档级别的ACID  
    - Redis用法  
        支持  
  
- 支持回滚  
    - MongoDB用法  
        不支持  
    - Redis用法  
        不支持  
  
## 三、简单总结  
1. MongoDB适合网站类的应用,经常修改表结构，能够横向扩展。  
2. Redis适合缓存类的应用,特别是高速写入有要求，能够横向扩展。  
3. MySQL支持事务和回滚,适合高价值的数据  
  
  
优秀的文章:  
[redis 用法实例](https://www.google.com "哈哈，自己google啊")  
[MongoDB 用法实例](https://www.google.com "哈哈，自己google啊")  
[Mysql 用法实例](https://www.google.com "哈哈，自己google啊")  
