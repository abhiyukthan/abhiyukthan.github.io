----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 09:49:01 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.241.229.212 - /index.php?app=core&module=search&do=search&andor_type=&sid=3f136c374934e276a9fc2f1c0eafd81f&search_app_filters[forums][sortKey]=date&search_tags=free+member+service&search_app_filters[forums][sortKey]=date&search_term=&search_app=forums&st=25
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 150247,144412,149151,82821,144108,102272,142683,150774,121849,146659,148793,110304,150716,150715,150714,150713,150712,150711,150710,137646,129495,94971,106711,147004,144461)
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