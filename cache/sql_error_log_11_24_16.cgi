
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:01:09 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.56 - /index.php/topic/121573-bytewhale-premium-account/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=121573 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:01:19 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.102.6.82 - /
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
 Date: Thu, 24 Nov 2016 00:01:23 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/147425-brazzerscom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=147425 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:01:23 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/132711-uploadednet-1-weeks-5-days-and-13-hours-premium-left/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=132711 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:01:24 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.78.73 - /
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
 Date: Thu, 24 Nov 2016 00:01:26 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.73.208.154 - /index.php/topic/116029-lynda/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=116029 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:01:27 +0000
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
 Date: Thu, 24 Nov 2016 00:01:28 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.55 - /index.php/topic/150793-littlemuttcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150793 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:01:32 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.249.93.71 - /
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
 Date: Thu, 24 Nov 2016 00:01:35 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.78.73 - /
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
 Date: Thu, 24 Nov 2016 00:01:37 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 180.76.15.157 - /index.php/topic/112989-videobox-active-subscription-by-codecrypt-premium-membership-account-status-subscribed-mar-23/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=112989 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:01:41 +0000
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
 Date: Thu, 24 Nov 2016 00:02:03 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.168.34.109 - /
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
 Date: Thu, 24 Nov 2016 00:02:10 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.168.34.109 - /
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
 Date: Thu, 24 Nov 2016 00:02:14 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/138539-netflix-account-no-dvd-13/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=138539 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:15 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 241.68.62.112 - /index.php/topic/138708-mycherrycrushcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=138708 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:16 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.56 - /index.php/topic/78625-myxxxpasscom-1/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=78625 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:17 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 87.156.81.111 - /index.php/topic/60649-chaturbatecom-full-capture-tokensstatusmembership/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=60649 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:18 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/120080-favorite-porn-star/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=120080 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:19 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/138855-kickassteenscom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=138855 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:20 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 87.156.81.111 - /index.php/topic/60649-chaturbatecom-full-capture-tokensstatusmembership/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=60649 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:25 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 241.68.62.112 - /index.php/topic/138708-mycherrycrushcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=138708 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:29 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/tags/forums/Virtual%2BReality/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 109608)
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:02:32 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.73.208.154 - /index.php/topic/381-how-to-use-account-hitman/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=381 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:34 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/120072-hulucom-next-bill-date-2016-06-02/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=120072 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:36 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 79.221.125.158 - /index.php/topic/141777-1x-yourfreeporntv-premium-account/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=141777 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:37 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/103555-gain-instagram-likes-fast-cheap-famousgram-coins/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=103555 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:40 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.142.78.73 - /
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
 Date: Thu, 24 Nov 2016 00:02:40 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/82004-200-filehost-dorks/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=82004 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:41 +0000
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
 Date: Thu, 24 Nov 2016 00:02:41 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/123478-hardpornoflixcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123478 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:44 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /tags/forums/pro/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 9526,140249,73932,5149,5152,7684,7686,7683,7690,5168,5151,5150,5153,5147,3658,1956)
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:02:45 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/123851-game-of-thrones-se6-link-please/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123851 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:46 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 79.221.125.158 - /index.php/topic/132578-yourfreeporntv-x4-premium-member/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=132578 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:49 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/4044-depositfilescom-1x-premium-account-valid-till-03102014/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=4044 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:51 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/77667-dezeercom-premium-1x/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=77667 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:53 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/139311-gifgaff-config-api/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=139311 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:53 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/35649-rapidgator-premium-1x-for-active-member-new-new-new/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=35649 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:54 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/tags/forums/directtv/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 138604,138603,137353)
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:02:55 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 178.213.6.180 - /index.php/topic/5765-051014proxy/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=5765 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:02:56 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 108.61.68.151 - /index.php/topic/120564-blackedcom-100-hd-bacdoors/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=120564 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=55929 ) 
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
 Date: Thu, 24 Nov 2016 00:02:59 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/4238-fileflashcom-1x-premium-account-valid-till-2014-09-29/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=4238 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:03:06 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/145824-1x-rapidgatornet-bandwith-available101621-gb-of-1-tb/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=145824 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:03:09 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /topic/79871-15-private-high-quality-dorks-for-combolists/page-4
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=79871 AND  queued=0  ORDER BY pid asc LIMIT 60,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:03:13 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.249.65.56 - /index.php?s=google=3eab522a229a25b4e1322b9af6edcdd6_session&
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
 Date: Thu, 24 Nov 2016 00:03:17 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 108.61.68.151 - /index.php/topic/150908-bangbroscom-subscription-bangbros-full-access/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150908 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=55929 ) 
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
 Date: Thu, 24 Nov 2016 00:03:29 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.102.61.206 - /
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
 Date: Thu, 24 Nov 2016 00:03:41 +0000
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
 Date: Thu, 24 Nov 2016 00:03:43 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 41.102.61.206 - /
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
 Date: Thu, 24 Nov 2016 00:03:54 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 156.220.191.89 - /index.php/topic/100672-origincom-250x-110116
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=100672 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:03:54 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/129847-zenmatecom-premium-expires-on-december-26-2016/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=129847 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:03:55 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.115.96.190 - /
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
 Date: Thu, 24 Nov 2016 00:03:58 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 93.115.96.190 - /
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
 Date: Thu, 24 Nov 2016 00:04:06 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 137.74.113.197 - /index.php/topic/137257-vr-porn/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=137257 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:10 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/122709-bangbroscom-with-dancing-bear%E2%94%82culioneros%E2%94%82haze-her%E2%94%82college-rules%E2%94%82mygf%E2%94%82cfnm-show%E2%94%82brandi-belle%E2%94%82public-invasion%E2%94%82busty-adventures/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=122709 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:21 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.73.208.154 - /index.php/tags/forums/skins/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 85622,111807)
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:04:22 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/132452-hello-ev/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=132452 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:23 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/65269-walmartcom-1x-premium-account-orders-12/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=65269 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:27 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.168.34.109 - /
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
 Date: Thu, 24 Nov 2016 00:04:28 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/12350-21sexturycom-credit-388/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=12350 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:30 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.168.34.109 - /
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
 Date: Thu, 24 Nov 2016 00:04:33 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /topic/90057-user-warned-smidser/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=90057 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:41 +0000
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
 Date: Thu, 24 Nov 2016 00:04:41 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/129141-atomix-virtualdj-pro-infinity-v8232911172/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=129141 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:41 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.73.208.154 - /index.php/topic/110793-request-for-two-essays-from-studymode/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=110793 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:43 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.58 - /index.php/topic/80398-jamesdeencom-premium-account-x1/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=80398 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:43 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/93271-restaurantcom-2x-premium-account-giftcard-value-25-giftcard-balance-25/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=93271 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:48 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php?app=core&module=search&do=user_activity&mid=52732
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 121678,147145,147141,141676,140866,142694,142664,142772,142695,141881,142460,142464,142475)
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/sources/classes/search/controller.php                              | [search_format_forums].processResults                                         | 653               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/core/modules_public/search/search.php                 | [IPSSearch].viewUserContent                                                   | 925               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/core/modules_public/search/search.php                 | [public_core_search_search].viewUserContent                                   | 162               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_core_search_search].doExecute                                         | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:04:49 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/131534-mofoscom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=131534 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:50 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/137352-chronos-daylife-103-macosx/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=137352 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:51 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php?app=core&module=search&do=user_activity&mid=52732
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 121678,147145,147141,141676,140866,142694,142664,142772,142695,141881,142460,142464,142475)
 .--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.
 | File                                                                       | Function                                                                      | Line No.          |
 |----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------|
 | tslogin/sources/classes/search/controller.php                              | [search_format_forums].processResults                                         | 653               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/core/modules_public/search/search.php                 | [IPSSearch].viewUserContent                                                   | 925               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/applications/core/modules_public/search/search.php                 | [public_core_search_search].viewUserContent                                   | 162               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 | tslogin/sources/base/ipsController.php                                     | [public_core_search_search].doExecute                                         | 306               |
 '----------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------'
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:04:51 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/132889-sentry-mba-success-keywords/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=132889 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:51 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 95.174.237.35 - /index.php/topic/148954-1x-depositfiles-gold-account/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=148954 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:51 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/102169-hello-guys/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=102169 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:04:55 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 77.168.34.109 - /
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
 Date: Thu, 24 Nov 2016 00:04:59 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/tags/forums/Latest%2BCFOSSPEED%2B10.10/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 84338)
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:04:59 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/125340-stiffiacom-x10/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=125340 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:05:01 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 180.76.15.146 - /index.php/topic/140331-15-a-day-simple-proof/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=140331 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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