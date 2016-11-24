----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 01:10:02 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 93.136.78.188 - /index.php?app=core&module=search&section=search&do=search&fromsearch=1
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,t.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM posts p  LEFT JOIN topics t ON ( t.tid=p.topic_id ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE p.pid IN( 714781,714596,713319,329045,459046,489514,458013,651750,597988,578968,548998,541409,540652,525786,520785,510051,501105,498763,491983,490963,482790,482789,482788,482787,482786)
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