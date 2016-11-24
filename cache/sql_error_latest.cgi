----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 18:37:57 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php?app=core&module=search&do=search&andor_type=&sid=1e87f1ce0f5aa2d1b0ebb1f3d6e02ee8&search_app_filters%5Bforums%5D%5BsortKey%5D=date&search_tags=uptobox.com&search_app_filters%5Bforums%5D%5BsortKey%5D=date&search_app_filters%5Bforums%5D%5BsearchInKey%5D=&search_term=&search_app=forums&st=50
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 61715,61729,61728,61725,61724,61722,61721,61719,61718,61716,61713,61710,12995,12999,12998,12994,12992,12991,12990,12989,12988,11114,8656,8654,8657)
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