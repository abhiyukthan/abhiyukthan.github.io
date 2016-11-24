----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 23:25:45 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.249.88.29 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 SUB SELECT query joins are not allowed.
Add \ipsRegistry::DB()->allow_sub_select=1; before any query construct to allow them
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.