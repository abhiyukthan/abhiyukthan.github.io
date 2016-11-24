
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:33 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/138170-milfmaniaxxxcom-1x-premium-account/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=138170 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:33 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/124803-metartvipcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=124803 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:34 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/118064-iomoiocom-premium-acc-2216-new/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=118064 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:35 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 88.16.50.118 - /index.php/topic/146155-katfilecom-premium-expire-on-12-dec-2016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=146155 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:36 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/141568-dagfscom-premium-account-with-all-sites-access-x1/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=141568 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:36 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/121927-internet-speed/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=121927 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:37 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/122988-brazzerscom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=122988 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:37 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/4936-mp3mixxcom-balance-8600-total-downloads-2857/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=4936 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:38 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.56 - /index.php/topic/144499-1x-torrentleech-ratio-0812-ul-11-tb-dl-135-tb-dl-slots-4/?view=getnextunread
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=144499 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:38 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 103.230.106.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(4,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
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
 Date: Thu, 24 Nov 2016 00:00:41 +0000
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
 Date: Thu, 24 Nov 2016 00:00:41 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/143951-uptoboxcom-premium/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=143951 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:42 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 103.230.106.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(4,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
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
 Date: Thu, 24 Nov 2016 00:00:45 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 103.230.106.1 - /
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.tag_text, COUNT(t.tag_text) as times, t.tag_meta_app, t.tag_meta_area
					FROM core_tags t WHERE  tag_meta_app IN ('core','forums','members','donate','subscriptions','tb_pcr','contactus','trackmembers','duplicates','shoutbox','topictemplate','feedback')
					AND t.tag_aai_lookup IN( SELECT p.tag_perm_aai_lookup FROM core_tags_perms p WHERE
				 ( ( FIND_IN_SET(4,p.tag_perm_text) ) OR ( p.tag_perm_text='*' ) ) AND p.tag_perm_visible=1 ) GROUP BY t.tag_text
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
 Date: Thu, 24 Nov 2016 00:00:46 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/123318-netflix-or-hulu/page-4
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123318 AND  queued=0  ORDER BY pid asc LIMIT 60,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:46 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/147973-lyndacom-you-pay-2499-today-and-your-subscription-will-auto-renew-on-december-03-2016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=147973 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:46 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 88.16.50.118 - /index.php/topic/146155-katfilecom-premium-expire-on-12-dec-2016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=146155 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:51 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/131705-who-will-become-president/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=131705 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:00:52 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 163.172.65.124 - /index.php/topic/126171-directvcom-premier-315-digital-channels/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=126171 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:01:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 50.23.94.74 - /
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