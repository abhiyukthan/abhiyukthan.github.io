----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Fri, 25 Nov 2016 06:38:34 +0000
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