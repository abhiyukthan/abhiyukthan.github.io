
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:17:20 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:17:20 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:17:20 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.242.228.140 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(10,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:17:25 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:17:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:18:01 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 178.42.130.61 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:18:29 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.228.97 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:18:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:18:36 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.228.97 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:18:49 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.254.125.169 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:19:05 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.228.97 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:19:07 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.228.97 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:19:08 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.228.97 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:19:08 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.228.97 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:19:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:20:11 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 113.172.5.180 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:20:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:20:59 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 76.72.172.208 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:21:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:22:01 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 113.172.5.180 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:22:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:22:42 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.242.228.140 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(10,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:22:46 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 45.33.138.40 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(13,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:22:48 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 45.33.138.40 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(13,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:23:07 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.242.228.140 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(10,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:23:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:24:09 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 82.19.114.81 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:24:17 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.65.16.139 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:24:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:24:49 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.65.16.139 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:25:17 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 62.114.239.158 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:25:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:26:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 67.228.213.178 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:26:10 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.65.16.139 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:26:17 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.65.16.139 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:26:19 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.65.16.139 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:26:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:26:55 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.28.194.134 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:05 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.28.194.134 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:08 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.28.194.134 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:41 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:45 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:50 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:52 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:27:54 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:28:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:28:03 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:28:06 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:28:09 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:28:11 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.147.201.148 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:28:30 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.65.16.139 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:28:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:29:08 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 88.27.106.140 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:29:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:29:36 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 50.3.230.177 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:29:37 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 62.23.200.228 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:29:48 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.249.65.56 - /index.php?s=google=211d8d9bc4e47dd469a2a399b6c0ea90_session&
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:30:03 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 78.15.91.64 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:30:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:30:59 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 85.93.93.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:31:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:32:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:33:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:33:42 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 81.226.237.13 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:33:46 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 81.226.237.13 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:33:51 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 81.226.237.13 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:26 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 54.244.54.128 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:29 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:31 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:33 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:34 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:39 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:53 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:34:56 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:35:20 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:35:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:35:59 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 204.152.200.42 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:36:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:37:17 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 54.242.164.91 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:37:17 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 54.242.164.91 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:37:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:38:08 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 197.186.84.63 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:38:16 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 23.108.12.17 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:38:30 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 250.212.109.20 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:38:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:38:36 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 250.212.109.20 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:38:55 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 244.120.138.159 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:04 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 244.120.138.159 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:06 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 244.120.138.159 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:08 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 244.120.138.159 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:14 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 245.136.104.122 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:17 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 245.136.104.122 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:41 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.242.228.140 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(10,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:39:50 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 185.137.17.83 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:40:05 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:40:22 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:40:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:40:45 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 141.8.143.227 - /index.php?s=google=8afc23519589af328dfeb214e0dea170_session&
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:40:48 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 141.8.143.227 - /index.php?s=google=8afc23519589af328dfeb214e0dea170_session&
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:40:51 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 141.8.143.227 - /index.php?s=google=8afc23519589af328dfeb214e0dea170_session&
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:40:53 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 141.8.143.227 - /index.php?s=google=8afc23519589af328dfeb214e0dea170_session&
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:41:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 178.255.155.2 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:41:28 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 185.137.17.83 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:41:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:41:54 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 54.244.54.128 - /index.php
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:42:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:11 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:14 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:15 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:17 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:18 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:19 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:20 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:23 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:28 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:37 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 86.85.158.179 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:38 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:39 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 251.244.96.37 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:42 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:42 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 251.244.96.37 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:56 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 23.92.65.77 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:43:59 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 23.92.65.77 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:10 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:26 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:29 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:30 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:31 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:31 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:44:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:45:26 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 94.209.240.255 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:45:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:45:43 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 197.186.84.63 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:45:59 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 184.75.210.226 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:46:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:47:16 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 179.210.29.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:47:22 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 179.210.29.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:47:31 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 179.210.29.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:47:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:47:41 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 179.210.29.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:47:45 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 179.210.29.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:47:52 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 245.136.104.122 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:48:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 186.3.246.241 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:48:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:49:06 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 186.3.246.241 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:49:10 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 186.3.246.241 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:49:12 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 186.3.246.241 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:49:13 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 186.3.246.241 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:49:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:50:30 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 71.60.104.175 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:50:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:50:37 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 71.60.104.175 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:50:41 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 71.60.104.175 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:50:59 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 64.237.55.3 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:51:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:52:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:04 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.85.139.243 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:09 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.85.139.243 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:13 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 246.12.170.133 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:18 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.85.139.243 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:22 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.85.139.243 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:37 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 113.22.110.160 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:43 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 113.22.110.160 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:53:57 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 107.178.37.94 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(13,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:54:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:55:07 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 176.122.122.202 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:55:18 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 73.133.110.108 - /index.php?
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:55:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:55:34 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 201.69.252.55 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:56:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 85.17.156.11 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:56:01 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 90.85.16.237 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:56:12 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:56:19 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 201.69.252.55 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:56:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:56:46 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:05 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:11 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:11 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:14 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:16 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:19 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:25 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:29 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:35 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:36 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:38 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 121.7.214.164 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:57:44 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.228.44.170 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:58:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:59:30 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 37.59.11.51 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:59:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 69.162.124.230 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:59:37 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 98.247.137.193 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:59:41 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 98.247.137.193 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 00:59:45 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 98.247.137.193 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(3,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 01:00:04 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.249.65.57 - /index.php?s=google=59b9417fa11273eca7c050dfd3cb6210_session&
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(2,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
 ORDER BY times DESC
LIMIT 0, 50
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/sources/classes/hooks/gateway.php              | [classes_tags_cloud].getCloudData                                             | 78                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | hooks/boardIndexTags_252b2b9f7399381a7a1e2c3d373787b8.php                  | [forums_hookGateway].tags                                                     | 17                |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [boardIndexTags].getOutput                                                    | 3785              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php(3849) : eval()'d code      | [output].templateHooks                                                        | 6                 |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/formats/html/htmlOutput.php                 | [shoutboxGlobalJs].globalTemplate                                             | 320               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/classes/output/publicOutput.php                            | [htmlOutput].fetchOutput                                                      | 2970              |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/forums/modules_public/forums/boards.php               | [output].sendOutput                                                           | 124               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_boards].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'