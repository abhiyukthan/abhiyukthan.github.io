----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 13:46:53 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.58 - /index.php?app=core&module=search&do=search&andor_type=&sid=ed288aacb570ecc5bccfaef5ca81df2a&search_app_filters%5Bforums%5D%5BsortKey%5D=date&search_tags=WWE&search_app_filters%5Bforums%5D%5BsortKey%5D=date&search_term=&search_app=forums&st=100
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 146704,111314,142179,144929,146581,146579,142986,130589,146357,146438,146436,146435,146431,146430,146429,114025,146363,146362,146361,146360,146358,146355,146354,146353,146351)
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/sources/classes/search/controller.php                              | [search_format_forums].processResults                                         | 553               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/core/modules_public/search/search.php                 | [IPSSearch].search                                                            | 671               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/core/modules_public/search/search.php                 | [public_core_search_search].searchResults                                     | 173               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_core_search_search].doExecute                                         | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'