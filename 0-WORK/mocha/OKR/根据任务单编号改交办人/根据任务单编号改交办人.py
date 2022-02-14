info = {
    'JS004-0000000473': ('jiangtx', '姜田先'),
    'JS004-0000000471': ('jiangtx', '姜田先'),
    'JS004-0000000470': ('jiangtx', '姜田先'),
    'JS004-0000000469': ('jiangtx', '姜田先'),
    'JS004-0000000468': ('baojb', '包建斌'),
    'JS004-0000000466': ('jiangtx', '姜田先'),
    'JS004-0000000465': ('jiangtx', '姜田先'),
    'JS004-0000000402': ('zhoulq', '周立芹'),
    'JS004-0000000401': ('jiangtx', '姜田先'),
    'JS004-0000000400': ('duchh', '杜长浩'),
    'JS004-0000000396': ('jiangtx', '姜田先'),
    'JS004-0000000395': ('duchh', '杜长浩'),
    'JS004-0000000393': ('jiangtx', '姜田先'),
}

f = open('OKR根据任务单编号修改交办人.sql', 'w', encoding='utf8')

for task_num in info.keys():
    initiator = info[task_num][0]
    initiatorname = info[task_num][1]
    modify_corework_sql = f"update  t_corework set c_initiator='{initiator}' where c_task_num='{task_num}';\n"
    modify_task_sql = f"update t_task set c_initiator='{initiator}', c_initiatorname='{initiatorname}' c_workid=(select c_id from t_corework where c_task_num='{task_num}') and c_parent_id='-1';\n"
    modify_task_relations_sql = f"update t_task_relations set c_userid='{initiator}',c_username='{initiatorname}' where c_taskid=(select c_id from t_task where c_workid=(select c_id from t_corework where c_task_num='{task_num}') and c_parent_id='-1') and c_type=1;\n"
    f.write(modify_corework_sql)
    f.write(modify_task_sql)
    f.write(modify_task_relations_sql)


f.close()
