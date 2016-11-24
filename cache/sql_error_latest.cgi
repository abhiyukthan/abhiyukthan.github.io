----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 02:18:58 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/124287-naughtyamericacom-x4/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=124287 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=0 ) 
 LEFT JOIN reputation_cache rep_cache ON ( rep_cache.app='forums' AND rep_cache.type='pid' AND rep_cache.type_id=p.pid ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=m.member_id )   ORDER BY z.pid asc
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/applications/forums/modules_public/forums/topics.php               | [public_forums_forums_topics]._getPosts                                       | 208               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_forums_forums_topics].doExecute                                       | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'