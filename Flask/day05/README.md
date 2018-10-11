## 二 批量数据的产生
```
# 1 创建模型类
# 商品模型类
class Goods(db.Model):
    # 商品id，主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 商品名称
    name = db.Column(db.String(20))
    # 商品图片
    icon = db.Column(db.String(255))
    # 商品价格
    price = db.Column(db.Integer)
    # 商品描述
    detail = db.Column(db.String(255))


# 2 执行迁移生成对应表单


# 3 查看表单结构是否一致
# 表单结构goods
mysql> desc goods;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int(11)      | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)  | NO   |     | NULL    |                |
| icon   | varchar(255) | NO   |     | NULL    |                |
| price  | int(11)      | NO   |     | NULL    |                |
| detail | varchar(255) | NO   |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)



# 4 定义存储过程
# 存储过程: 创建商品数据
# insert into goods(name,icon,price,detail) value(name,icon,price,detail)
delimiter //
create procedure add_goods(num int(4))
begin
    # 定义变量
    declare _i,_price,_temp int(4) default 0;
    declare _name,_icon,_detail varchar(255) default '';
    declare BASE_PATH varchar(255) default '/static/img/';

    # 循环
    while _i<num do
        # 设置变量
        set _temp = round(rand()*10000+1000);
        set _name = concat(_temp,'-商品名称');
        set _temp = round(rand()*5+1);
        case _temp
        when 1 then
            set _icon = concat(BASE_PATH,'cymbal.png');
        when 2 then
            set _icon = concat(BASE_PATH,'drink.png');
        when 3 then
            set _icon = concat(BASE_PATH,'eat.png');
        when 4 then
            set _icon = concat(BASE_PATH,'fart.png');
        when 5 then
            set _icon = concat(BASE_PATH,'pie.png');
        when 6 then
            set _icon = concat(BASE_PATH,'scratch.png');
        else
            set _icon = concat(BASE_PATH,'cymbal.png');
        end case;
        set _temp = round(rand()*10000+1000);
        set _price = _temp;
        set _temp = round(rand()*10000+1000);
        set _detail = concat(_temp,'-Apple/苹果 iPhone 7 Plus苹果7代7pluss国行美版三网5.5寸7p手机');

        # 插入数据
        insert into goods(name,icon,price,detail) value(_name,_icon,_price,_detail);

        # 修改次数
        set _i = _i + 1;
    end while;

    # 显示数据
    select * from goods;
end
//
delimiter ;


# 5 调用存储过程
call add_goods(30);

# 6 备注
# 使用图片,即图片要拷贝到项目中,对应的目录结构是/static/img/xxx.png
```