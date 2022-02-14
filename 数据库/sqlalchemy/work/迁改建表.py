from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Numeric, String, DateTime, TIMESTAMP, NUMERIC

from datetime import datetime

# 操作Oracle的话需要安装 cx_Oracle
engine = create_engine("oracle://admduty:admduty@172.23.22.101:1521/orcl", encoding='utf-8', echo=True)
metadata = MetaData()
Base = declarative_base()


class MP_BZ_COLLECTION(Base):
    """收款报账表"""
    __tablename__ = 'MP_BZ_COLLECTION'
    id = Column(String(255), primary_key=True, comment="主键")
    # 报账信息
    bz_type = Column(String(255), primary_key=True, comment="报账单类型")
    # 迁改项目合同等信息
    modify_code = Column(String(255), comment="迁改编号")
    modify_name = Column(String(255), comment="迁改名称")
    project_code = Column(String(255), comment="项目编号")
    project_name = Column(String(255), comment="项目名称")
    contract_code = Column(String(255), comment="合同编号")
    contract_name = Column(String(255), comment="合同名称")
    contract_begin_time = Column(TIMESTAMP, comment="合同开始时间")
    contract_end_time = Column(TIMESTAMP, comment="合同结束时间")
    contract_account = Column(NUMERIC(38, 3), comment="合同总额")
    pay_type = Column(String(255), comment="迁改类型")
    # 大小类相关
    activity_code = Column(String(255), comment="活动编码")
    activity_name = Column(String(255), comment="活动名称")
    max_class_code = Column(String(255), comment="大类编号")
    max_class_name = Column(String(255), comment="大类名称")
    min_class_code = Column(String(255), comment="小类编号")
    min_class_name = Column(String(255), comment="小类名称")
    business_type_code = Column(String(255), comment="业务类型编号")
    business_type_name = Column(String(255), comment="业务类型名称")
    # 收款相关
    collection_info_id = Column(String(255), comment="收款信息表id")
    collection_plan_id = Column(String(255), comment="收款计划表id")
    collection_item_id = Column(String(255), comment="收款详情表id")
    collection_begin_time = Column(TIMESTAMP, comment="收款计划开始时间")
    collection_end_time = Column(TIMESTAMP, comment="收款计划结束时间")
    amount = Column(NUMERIC(38, 3), comment="本次应收")
    padin = Column(NUMERIC(38, 3), comment="本次实收")
    taxes = Column(NUMERIC(38, 3), comment="税金")
    # 发票相关
    is_invoice = Column(Integer, comment="是否开票")
    invoice_number = Column(String(255), comment="发票编号")
    # 其他
    remark = Column(String(255), comment="备注")
    create_date = Column(TIMESTAMP, default=datetime.now, comment="创建日期")
    update_date = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now, comment="更新日期")


class MP_BZ_EXPENDITURE(Base):
    """支出报账表"""
    __tablename__ = 'MP_BZ_EXPENDITURE'
    id = Column(String(255), primary_key=True, comment="主键")
    # 迁改项目合同等信息
    modify_code = Column(String(255), comment="迁改编号")
    modify_name = Column(String(255), comment="迁改名称")
    project_code = Column(String(255), comment="项目编号")
    project_name = Column(String(255), comment="项目名称")
    contract_code = Column(String(255), comment="合同编号")
    contract_name = Column(String(255), comment="合同名称")
    contract_begin_time = Column(TIMESTAMP, comment="合同开始时间")
    contract_end_time = Column(TIMESTAMP, comment="合同结束时间")
    contract_account = Column(NUMERIC(38, 3), comment="合同总额")
    epms_project_code = Column(String(255), comment="EPMS项目编号")
    # 支出信息
    reduced_rate = Column(NUMERIC(38, 3), comment="总冲减率")
    amount_paid = Column(NUMERIC(38, 3), comment="总支出金额")
    project_state = Column(Integer, comment="项目状态: 1. 已完成，2.未完成")
    subject = Column(String(255), comment="科目")
    suppliers = Column(String(255), comment="他方供应商")
    project_leader = Column(String(255), comment="项目负责人")
    construction_cost = Column(NUMERIC(38, 3), comment="施工费")
    design_cost = Column(NUMERIC(38, 3), comment="设计费")
    materials_cost = Column(NUMERIC(38, 3), comment="材料费")
    supervisor_cost = Column(NUMERIC(38, 3), comment="监理费")
    paid = Column(NUMERIC(38, 3), comment="本次支出金额")
    sum_paid = Column(NUMERIC(38, 3), comment="累计支出金额")
    impact_rate =  Column(NUMERIC(38, 3), comment="本次冲减率")
    file_ids = Column(String(255), comment="附件表id")
    # 其他
    create_date = Column(TIMESTAMP, default=datetime.now, comment="创建日期")
    update_date = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now, comment="更新日期")


class MP_BZ_ALL(Base):
    """总报账表"""
    __tablename__ = 'MP_BZ_ALL'
    id = Column(String(255), primary_key=True, comment="主键")
    # 迁改项目合同等信息
    modify_code = Column(String(255), comment="迁改编号")
    modify_name = Column(String(255), comment="迁改名称")
    project_code = Column(String(255), comment="项目编号")
    project_name = Column(String(255), comment="项目名称")
    contract_code = Column(String(255), comment="合同编号")
    contract_name = Column(String(255), comment="合同名称")
    contract_begin_time = Column(TIMESTAMP, comment="合同开始时间")
    contract_end_time = Column(TIMESTAMP, comment="合同结束时间")
    contract_account = Column(NUMERIC(38, 3), comment="合同总额")
    # 其他
    create_date = Column(TIMESTAMP, default=datetime.now, comment="创建日期")
    update_date = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now, comment="更新日期")


# 更新表结构
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# 生成java实体类

# 生成通用基础Mapper配置文件



