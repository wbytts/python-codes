import requests # pip install requests
import json

wms_token = '82e79be93ff242daa964c39d960a5762'
wms_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'wms_token': wms_token,
    'ucClientApp': 'wms',
    'from': 'wms',
    'Host': '172.20.21.235:8443',
}

urls = {
    'save_menu': 'http://172.20.21.235:8443/uc-wms-pc/uc-manage-api/menu/save',
    'query_all_menus': 'http://172.20.21.235:8443/uc-wms-pc/uc-manage-api/menu/conditions'
}

menu_list = []

def menustree_to_list(menus):
    for menu in menus:
        if menu['hasChildren']:
            children = menu['children']
            menustree_to_list(children)

        del menu['menuUrl']
        del menu['menuIcon']
        del menu['children']
        del menu['hasChildren']
        menu_list.append(menu)


def get_menuid_by_code(menu):
    print(menu)
    res = list(filter(lambda m: m['menuCode'] == menu['pcode'], menu_list))
    return res[0]


def is_menu_exist(menu):
    res = list(filter(lambda m: m['menuCode'] == menu['code'], menu_list))
    return len(res) != 0

def query_menus():
    """
    查询所有菜单
    """
    data = {}
    res = requests.post(
        urls['query_all_menus'],
        data=json.dumps(data),
        headers=wms_headers,
    )
    menustree_to_list(res.json()['data'])


def save_menu(menuCode, menuName, menuSeq, menuType, parentId, status, TYPE):
    """
    添加菜单
    Args:
        menuCode (str): 菜单编码
        menuName (str): 菜单名称
        menuSeq (str): 菜单排序号
        menuType (str): 菜单类型
        parentId (str): 父菜单id
        status (str): 菜单状态
    """
    data = {
        'menuCode': menuCode,
        'menuName': menuName,
        'menuSeq': menuSeq,
        'menuType': menuType,
        'parentId': parentId,
        'status': status,
        'type': TYPE
    }
    if not TYPE: del data['type']
    res = requests.post(
            urls['save_menu'],
            data=json.dumps(data),  # JSON.stringify
            headers=wms_headers,
        )

    # 每次添加完菜单，更新总的菜单信息
    global menus
    menus = query_menus()

    return res.json()



need_add_menus = [
    # 最外层
    { 'code': 'JCSJ', 'name': '基础数据', 'pcode': None, 'type': 1, 'seq': 1 },
    { 'code': 'RKGL', 'name': '入库管理', 'pcode': None, 'type': 1, 'seq': 2 },
    { 'code': 'KNGL', 'name': '库内管理', 'pcode': None, 'type': 1, 'seq': 3 },
    { 'code': 'CKGL', 'name': '出库管理', 'pcode': None, 'type': 1, 'seq': 4 },
    { 'code': 'BBGL', 'name': '报表管理', 'pcode': None, 'type': 1, 'seq': 5 },
    # 基础数据 JCSJ
    { 'code': 'QXGL', 'name': '权限管理', 'pcode': 'JCSJ', 'type': 1, 'seq': 1 },
    { 'code': 'SPXX', 'name': '商品信息', 'pcode': 'JCSJ', 'type': 1, 'seq': 2 },
    { 'code': 'HZGL', 'name': '货主管理', 'pcode': 'JCSJ', 'type': 2, 'seq': 3 },
    { 'code': 'SJPZ', 'name': '数据配置', 'pcode': 'JCSJ', 'type': 1, 'seq': 4 },
    { 'code': 'CKXX', 'name': '仓库信息', 'pcode': 'JCSJ', 'type': 1, 'seq': 5 },
    { 'code': 'CLPZ', 'name': '策略配置', 'pcode': 'JCSJ', 'type': 1, 'seq': 6 },
    # 权限管理 QXGL
    { 'code': 'CDGL', 'name': '菜单管理', 'pcode': 'QXGL', 'type': 2, 'seq': 1 },
    { 'code': 'JSGL', 'name': '角色管理', 'pcode': 'QXGL', 'type': 2, 'seq': 2 },
    { 'code': 'YHGL', 'name': '用户管理', 'pcode': 'QXGL', 'type': 2, 'seq': 3 },
    # 商品信息 SPXX
    { 'code': 'DWGL', 'name': '单位管理', 'pcode': 'SPXX', 'type': 2, 'seq': 1 },
    { 'code': 'SPGL', 'name': '商品管理', 'pcode': 'SPXX', 'type': 2, 'seq': 2 },
    { 'code': 'DJBZGL', 'name': '多级包装管理', 'pcode': 'SPXX', 'type': 2, 'seq': 3 },
    # 数据配置 SJPZ
    { 'code': 'SXZD', 'name': '属性字典', 'pcode': 'SJPZ', 'type': 2, 'seq': 1 },
    { 'code': 'RQLXGL', 'name': '容器类型管理', 'pcode': 'SJPZ', 'type': 2, 'seq': 2 },
    { 'code': 'DYZX', 'name': '打印中心', 'pcode': 'SJPZ', 'type': 2, 'seq': 3 },
    { 'code': 'RQGL', 'name': '容器管理', 'pcode': 'SJPZ', 'type': 2, 'seq': 4 },
    # 仓库信息 CKXX
    { 'code': 'CKGL1', 'name': '仓库管理', 'pcode': 'CKXX', 'type': 2, 'seq': 1 },
    { 'code': 'KQGL', 'name': '库区管理', 'pcode': 'CKXX', 'type': 2, 'seq': 2 },
    { 'code': 'CWGL', 'name': '仓位管理', 'pcode': 'CKXX', 'type': 2, 'seq': 3 },
    { 'code': 'YTGL', 'name': '月台管理', 'pcode': 'CKXX', 'type': 2, 'seq': 4 },
    { 'code': 'GZTGL', 'name': '工作台管理', 'pcode': 'CKXX', 'type': 2, 'seq': 5 },
    # 策略配置 CLPZ
    { 'code': 'JXCL', 'name': '拣选策略', 'pcode': 'CLPZ', 'type': 2, 'seq': 1 },
    { 'code': 'FPCL', 'name': '分配策略', 'pcode': 'CLPZ', 'type': 2, 'seq': 2 },
    # 入库管理 RKGL
    { 'code': 'RKTZD', 'name': '入库通知单', 'pcode': 'RKGL', 'type': 2, 'seq': 1 },
    { 'code': 'SHRK', 'name': '收货入库', 'pcode': 'RKGL', 'type': 2, 'seq': 2 },
    # 库内管理 KNGL
    { 'code': 'WD', 'name': '物动', 'pcode': 'KNGL', 'type': 1, 'seq': 1 },
    { 'code': 'PD', 'name': '盘点', 'pcode': 'KNGL', 'type': 1, 'seq': 2 },
    # 物动 WD
    { 'code': 'SJDGL', 'name': '上架单管理', 'pcode': 'WD', 'type': 2, 'seq': 1 },
    { 'code': 'KCTZ', 'name': '库存调整', 'pcode': 'WD', 'type': 2, 'seq': 2 },
    { 'code': 'YWDGL', 'name': '移位单管理', 'pcode': 'WD', 'type': 2, 'seq': 3 },
    # 盘点 PD
    { 'code': 'PDDGL', 'name': '盘点单管理', 'pcode': 'PD', 'type': 2, 'seq': 1 },
    { 'code': 'PDJLCX', 'name': '盘点记录查询', 'pcode': 'PD', 'type': 2, 'seq': 2 },
    # 出库管理 CKGL
    { 'code': 'CKDGL', 'name': '出库单管理', 'pcode': 'CKGL', 'type': 2, 'seq': 1 },
    { 'code': 'BCHZ', 'name': '波次汇总', 'pcode': 'CKGL', 'type': 2, 'seq': 2 },
    { 'code': 'JXDCJYCCX', 'name': '拣选单创建异常查询', 'pcode': 'CKGL', 'type': 2, 'seq': 3 },
    { 'code': 'KCFPYCCX', 'name': '库存分配异常查询', 'pcode': 'CKGL', 'type': 2, 'seq': 4 },
    { 'code': 'JXDGL', 'name': '拣选单管理', 'pcode': 'CKGL', 'type': 2, 'seq': 5 },
    { 'code': 'FJ', 'name': '分拣', 'pcode': 'CKGL', 'type': 2, 'seq': 6 },
    { 'code': 'BZFHDL', 'name': '包装复核登录', 'pcode': 'CKGL', 'type': 2, 'seq': 7 },
    # 报表管理 BBGL
    { 'code': 'KCCX', 'name': '库存查询', 'pcode': 'BBGL', 'type': 1, 'seq': 1 },
    { 'code': 'RQSYJL', 'name': '容器使用记录', 'pcode': 'BBGL', 'type': 2, 'seq': 2 },
    # 库存查询 KCCX
    { 'code': 'SPCWKCMX', 'name': '商品仓位库存明细', 'pcode': 'KCCX', 'type': 2, 'seq': 1 },
    { 'code': 'KCCRLSMX', 'name': '库存出入流水明细', 'pcode': 'KCCX', 'type': 2, 'seq': 2 },
    # 菜单管理 CDGL
    { 'code': 'CDGL-CX', 'name': '查询', 'pcode': 'CDGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'CDGL-QK', 'name': '清空', 'pcode': 'CDGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'CDGL-XZ', 'name': '新增', 'pcode': 'CDGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 角色管理 JSGLm
    { 'code': 'JSGL-CX', 'name': '查询', 'pcode': 'JSGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'JSGL-QK', 'name': '清空', 'pcode': 'JSGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'JSGL-XZ', 'name': '新增', 'pcode': 'JSGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'JSGL-XZGYJS', 'name': '新增公用角色', 'pcode': 'JSGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    # 用户管理 YHGLm
    { 'code': 'YHGL-CX', 'name': '查询', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'YHGL-QK', 'name': '清空', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'YHGL-XZ', 'name': '新增', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'YHGL-QY', 'name': '启用', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'YHGL-JY', 'name': '禁用', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'YHGL-SC', 'name': '删除', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'YHGL-BDJSCK', 'name': '绑定角色仓库', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 7 },
    { 'code': 'YHGL-DR', 'name': '导入', 'pcode': 'YHGL', 'mtype': 3, 'type': 2, 'seq': 8 },
    # 单位管理 DWGL
    { 'code': 'DWGL-CX', 'name': '查询', 'pcode': 'DWGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'DWGL-QK', 'name': '清空', 'pcode': 'DWGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'DWGL-XZ', 'name': '新增', 'pcode': 'DWGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'DWGL-QY', 'name': '启用', 'pcode': 'DWGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'DWGL-JY', 'name': '禁用', 'pcode': 'DWGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'DWGL-SC', 'name': '删除', 'pcode': 'DWGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'DWGL-DR', 'name': '导入', 'pcode': 'DWGL', 'mtype': 3, 'type': 2, 'seq': 7 },
    # 商品管理 SPGL
    { 'code': 'SPGL-CX', 'name': '查询', 'pcode': 'SPGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'SPGL-QK', 'name': '清空', 'pcode': 'SPGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'SPGL-XZ', 'name': '新增', 'pcode': 'SPGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'SPGL-DR', 'name': '导入', 'pcode': 'SPGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'SPGL-SPLX', 'name': '商品类型', 'pcode': 'SPGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    # 多级包装管理 DJBZGL
    { 'code': 'DJBZGL-CX', 'name': '查询', 'pcode': 'DJBZGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'DJBZGL-QK', 'name': '清空', 'pcode': 'DJBZGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'DJBZGL-XZ', 'name': '新增', 'pcode': 'DJBZGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 货主管理 HZGL
    { 'code': 'HZGL-CX', 'name': '查询', 'pcode': 'HZGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'HZGL-QK', 'name': '清空', 'pcode': 'HZGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'HZGL-XZ', 'name': '新增', 'pcode': 'HZGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'HZGL-QY', 'name': '启用', 'pcode': 'HZGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'HZGL-JY', 'name': '禁用', 'pcode': 'HZGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    # 属性字典 SXZD
    { 'code': 'SXZD-CX', 'name': '查询', 'pcode': 'SXZD', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'SXZD-QK', 'name': '清空', 'pcode': 'SXZD', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'SXZD-XZSXZ', 'name': '新增属性组', 'pcode': 'SXZD', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 容器类型管理 RQLXGL
    { 'code': 'RQLXGL-CX', 'name': '查询', 'pcode': 'RQLXGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'RQLXGL-QK', 'name': '清空', 'pcode': 'RQLXGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'RQLXGL-XZ', 'name': '新增', 'pcode': 'RQLXGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'RQLXGL-QY', 'name': '启用', 'pcode': 'RQLXGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'RQLXGL-JY', 'name': '禁用', 'pcode': 'RQLXGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    # 打印中心 DYZX
    { 'code': 'DYZX-CX', 'name': '查询', 'pcode': 'DYZX', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'DYZX-QK', 'name': '清空', 'pcode': 'DYZX', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'DYZX-DY', 'name': '打印', 'pcode': 'DYZX', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 容器管理 RQGL
    { 'code': 'RQGL-CX', 'name': '查询', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'RQGL-QK', 'name': '清空', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'RQGL-XZ', 'name': '新增', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'RQGL-QY', 'name': '启用', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'RQGL-JY', 'name': '禁用', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'RQGL-SC', 'name': '删除', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'RQGL-SF', 'name': '释放', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 7 },
    { 'code': 'RQGL-DR', 'name': '导入', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 8 },
    { 'code': 'RQGL-DY', 'name': '打印', 'pcode': 'RQGL', 'mtype': 3, 'type': 2, 'seq': 9 },
    # 仓库管理 CKGL1
    { 'code': 'CKGL1-CX', 'name': '查询', 'pcode': 'CKGL1', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'CKGL1-QK', 'name': '清空', 'pcode': 'CKGL1', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'CKGL1-XZ', 'name': '新增', 'pcode': 'CKGL1', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 库区管理 KQGL
    { 'code': 'KQGL-CX', 'name': '查询', 'pcode': 'KQGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'KQGL-QK', 'name': '清空', 'pcode': 'KQGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'KQGL-XZ', 'name': '新增', 'pcode': 'KQGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'KQGL-QY', 'name': '启用', 'pcode': 'KQGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'KQGL-JY', 'name': '禁用', 'pcode': 'KQGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'KQGL-SC', 'name': '删除', 'pcode': 'KQGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'KQGL-DR', 'name': '导入', 'pcode': 'KQGL', 'mtype': 3, 'type': 2, 'seq': 7 },
    # 仓位管理 CWGL
    { 'code': 'CWGL-CX', 'name': '查询', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'CWGL-QK', 'name': '清空', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'CWGL-XZ', 'name': '新增', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'CWGL-QY', 'name': '启用', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'CWGL-JY', 'name': '禁用', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'CWGL-SC', 'name': '删除', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'CWGL-DR', 'name': '导入', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 7 },
    { 'code': 'CWGL-DY', 'name': '打印', 'pcode': 'CWGL', 'mtype': 3, 'type': 2, 'seq': 8 },
    #  月台管理 YTGL
    { 'code': 'YTGL-CX', 'name': '查询', 'pcode': 'YTGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'YTGL-QK', 'name': '清空', 'pcode': 'YTGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'YTGL-XZ', 'name': '新增', 'pcode': 'YTGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'YTGL-QY', 'name': '启用', 'pcode': 'YTGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'YTGL-JY', 'name': '禁用', 'pcode': 'YTGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'YTGL-SC', 'name': '删除', 'pcode': 'YTGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    # 工作台管理 GZTGL
    { 'code': 'GZTGL-CX', 'name': '查询', 'pcode': 'GZTGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'GZTGL-QK', 'name': '清空', 'pcode': 'GZTGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'GZTGL-XZ', 'name': '新增', 'pcode': 'GZTGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'GZTGL-QY', 'name': '启用', 'pcode': 'GZTGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'GZTGL-JY', 'name': '禁用', 'pcode': 'GZTGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'GZTGL-SC', 'name': '删除', 'pcode': 'GZTGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    # 拣选策略 JXCL
    { 'code': 'JXCL-CX', 'name': '查询', 'pcode': 'JXCL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'JXCL-QK', 'name': '清空', 'pcode': 'JXCL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'JXCL-XZ', 'name': '新增', 'pcode': 'JXCL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'JXCL-QY', 'name': '启用', 'pcode': 'JXCL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'JXCL-JY', 'name': '禁用', 'pcode': 'JXCL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'JXCL-SC', 'name': '删除', 'pcode': 'JXCL', 'mtype': 3, 'type': 2, 'seq': 6 },
    # 分配策略 FPCL
    { 'code': 'FPCL-CX', 'name': '查询', 'pcode': 'FPCL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'FPCL-QK', 'name': '清空', 'pcode': 'FPCL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'FPCL-XZ', 'name': '新增', 'pcode': 'FPCL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'FPCL-QY', 'name': '启用', 'pcode': 'FPCL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'FPCL-JY', 'name': '禁用', 'pcode': 'FPCL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'FPCL-SC', 'name': '删除', 'pcode': 'FPCL', 'mtype': 3, 'type': 2, 'seq': 6 },
    # 入库通知单 RKTZD
    { 'code': 'RKTZD-CX', 'name': '查询', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'RKTZD-QK', 'name': '清空', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'RKTZD-XZ', 'name': '新增', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'RKTZD-TJ', 'name': '提交', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'RKTZD-GB', 'name': '关闭', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'RKTZD-DHDJ', 'name': '到货登记', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'RKTZD-DYTZD', 'name': '打印通知单', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 7 },
    { 'code': 'RKTZD-DYSHD', 'name': '打印收货单', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 8 },
    { 'code': 'RKTZD-DR', 'name': '导入', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 9 },
    { 'code': 'RKTZD-SHWQC', 'name': '收货完成', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 10 },
    { 'code': 'RKTZD-DC', 'name': '导出', 'pcode': 'RKTZD', 'mtype': 3, 'type': 2, 'seq': 11 },
    # 收货入库 SHRK
    { 'code': 'SHRK-CX', 'name': '收货', 'pcode': 'SHRK', 'mtype': 3, 'type': 2, 'seq': 1 },
    # 上架单管理 SJDGL
    { 'code': 'SJDGL-CX', 'name': '查询', 'pcode': 'SJDGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'SJDGL-QK', 'name': '清空', 'pcode': 'SJDGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'SJDGL-FPDSJ', 'name': '分配单上架', 'pcode': 'SJDGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'SJDGL-DYSJD', 'name': '打印上架单', 'pcode': 'SJDGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    # 库存调整 KCTZ
    { 'code': 'KCTZ-CX', 'name': '查询', 'pcode': 'KCTZ', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'KCTZ-QK', 'name': '清空', 'pcode': 'KCTZ', 'mtype': 3, 'type': 2, 'seq': 2 },
    # 移位单管理 YWDGL
    { 'code': 'YWDGL-CX', 'name': '查询', 'pcode': 'YWDGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'YWDGL-QK', 'name': '清空', 'pcode': 'YWDGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'YWDGL-XZ', 'name': '新增', 'pcode': 'YWDGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'YWDGL-JH', 'name': '激活', 'pcode': 'YWDGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'YWDGL-ZP', 'name': '指派', 'pcode': 'YWDGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'YWDGL-DY', 'name': '打印', 'pcode': 'YWDGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'YWDGL-QZQX', 'name': '强制取消', 'pcode': 'YWDGL', 'mtype': 3, 'type': 2, 'seq': 7 },
    # 盘点单管理 PDDGL
    { 'code': 'PDDGL-CX', 'name': '查询', 'pcode': 'PDDGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'PDDGL-QK', 'name': '清空', 'pcode': 'PDDGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'PDDGL-XZ', 'name': '新增', 'pcode': 'PDDGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 盘点记录查询 PDJLCX
    { 'code': 'PDJLCX-CX', 'name': '查询', 'pcode': 'PDJLCX', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'PDJLCX-QK', 'name': '清空', 'pcode': 'PDJLCX', 'mtype': 3, 'type': 2, 'seq': 2 },
    # 出库单管理 CKDGL
    { 'code': 'CKDGL-CX', 'name': '查询', 'pcode': 'CKDGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'CKDGL-QK', 'name': '清空', 'pcode': 'CKDGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'CKDGL-XZ', 'name': '新增', 'pcode': 'CKDGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'CKDGL-TJ', 'name': '提交', 'pcode': 'CKDGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'CKDGL-QX', 'name': '取消', 'pcode': 'CKDGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    { 'code': 'CKDGL-DR', 'name': '导入', 'pcode': 'CKDGL', 'mtype': 3, 'type': 2, 'seq': 6 },
    { 'code': 'CKDGL-DC', 'name': '导出', 'pcode': 'CKDGL', 'mtype': 3, 'type': 2, 'seq': 7 },
    # 波次汇总 BCHZ
    { 'code': 'BCHZ-CX', 'name': '查询', 'pcode': 'BCHZ', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'BCHZ-QK', 'name': '清空', 'pcode': 'BCHZ', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'BCHZ-HZ', 'name': '汇总', 'pcode': 'BCHZ', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'BCHZ-QBHZ', 'name': '全部汇总', 'pcode': 'BCHZ', 'mtype': 3, 'type': 2, 'seq': 4 },
    # 拣选单创建异常查询 JXDCJYCCX
    { 'code': 'JXDCJYCCX-CX', 'name': '查询', 'pcode': 'JXDCJYCCX', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'JXDCJYCCX-QK', 'name': '清空', 'pcode': 'JXDCJYCCX', 'mtype': 3, 'type': 2, 'seq': 2 },
    # 库存分配异常查询 KCFPYCCX
    { 'code': 'KCFPYCCX-CX', 'name': '查询', 'pcode': 'KCFPYCCX', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'KCFPYCCX-QK', 'name': '清空', 'pcode': 'KCFPYCCX', 'mtype': 3, 'type': 2, 'seq': 2 },
    # 拣选单管理 JXDGL
    { 'code': 'JXDGL-CX', 'name': '查询', 'pcode': 'JXDGL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'JXDGL-QK', 'name': '清空', 'pcode': 'JXDGL', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'JXDGL-LQ', 'name': '领取', 'pcode': 'JXDGL', 'mtype': 3, 'type': 2, 'seq': 3 },
    { 'code': 'JXDGL-DY', 'name': '打印', 'pcode': 'JXDGL', 'mtype': 3, 'type': 2, 'seq': 4 },
    { 'code': 'JXDGL-JXZX', 'name': '拣选执行', 'pcode': 'JXDGL', 'mtype': 3, 'type': 2, 'seq': 5 },
    # 分拣 FJ
    # 商品仓位库存明细 SPCWKCMX
    { 'code': 'SPCWKCMX-CX', 'name': '查询', 'pcode': 'SPCWKCMX', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'SPCWKCMX-QK', 'name': '清空', 'pcode': 'SPCWKCMX', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'SPCWKCMX-DC', 'name': '导出', 'pcode': 'SPCWKCMX', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 库存出入流水明细 KCCRLSMX
    { 'code': 'KCCRLSMX-CX', 'name': '查询', 'pcode': 'KCCRLSMX', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'KCCRLSMX-QK', 'name': '清空', 'pcode': 'KCCRLSMX', 'mtype': 3, 'type': 2, 'seq': 2 },
    { 'code': 'KCCRLSMX-DC', 'name': '导出', 'pcode': 'KCCRLSMX', 'mtype': 3, 'type': 2, 'seq': 3 },
    # 容器使用记录 RQSYJL
    { 'code': 'RQSYJL-CX', 'name': '查询', 'pcode': 'RQSYJL', 'mtype': 3, 'type': 2, 'seq': 1 },
    { 'code': 'RQSYJL-QK', 'name': '清空', 'pcode': 'RQSYJL', 'mtype': 3, 'type': 2, 'seq': 2 },

]



query_menus()

# for menu in menu_list:
#     print(menu)


for menu in need_add_menus:
    if is_menu_exist(menu):
        print(f'菜单 {menu["name"]} --- {menu["code"]}  已存在')
    else:
        parent_id = None
        if menu['pcode']:
            parent_menu = get_menuid_by_code(menu)
            parent_id = parent_menu['menuId']

        save_res = save_menu(menu['code'], menu['name'], menu['seq'], menu['mtype'], parent_id, 0, menu['type'])
        print(f'菜单 {menu["name"]} --- {menu["code"]} 添加成功 ')
        print('保存结果', save_res)
        query_menus()




