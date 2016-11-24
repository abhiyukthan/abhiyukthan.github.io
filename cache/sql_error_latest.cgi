----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 15:25:01 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.156 - /index.php?app=core&module=search&do=search&andor_type=&search_app_filters[forums][sortKey]=date&search_tags=exploits&search_app_filters[forums][sortKey]=date&search_term=&search_app=forums&st=25
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 96741,67960,79871,133199,100214,100204,145927,145926,144358,148092,145943,145568,146242,145952,70156,141185,100205,133198,145571,143641,146971,145970,99793,145931,107144)
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