
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
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Date: Thu, 24 Nov 2016 00:05:12 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/138148-pornativecom-1x-premium-account/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=138148 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:05:12 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/27957-auntjudyscom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=27957 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:05:12 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/144276-x1-seniorcuntcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=144276 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:05:13 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150744-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150744 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:05:23 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 105.103.216.15 - /
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
 Date: Thu, 24 Nov 2016 00:05:33 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/78187-firehawk-paid-addons-games/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=78187 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:05:38 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 176.42.29.70 - /
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
 Date: Thu, 24 Nov 2016 00:05:41 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 176.42.29.70 - /
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
 Date: Thu, 24 Nov 2016 00:05:41 +0000
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
 Date: Thu, 24 Nov 2016 00:05:42 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 176.42.29.70 - /
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
 Date: Thu, 24 Nov 2016 00:05:43 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/149077-193063-mailpass-combolist-11-11-2016-123mb-by-0verride/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=149077 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:05:43 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 176.42.29.70 - /
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
 Date: Thu, 24 Nov 2016 00:05:48 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 80.3.93.250 - /
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
 Date: Thu, 24 Nov 2016 00:05:54 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/143569-filejokernet-traffic-available-38803-mb-premium-account-expires-1-november-2016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=143569 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:05:58 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 5.255.75.239 - /
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
 Date: Thu, 24 Nov 2016 00:06:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 109.123.101.103 - /
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
 Date: Thu, 24 Nov 2016 00:06:05 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 80.3.93.250 - /
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
 Date: Thu, 24 Nov 2016 00:06:06 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150744-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150744 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:06:11 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 80.3.93.250 - /
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
 Date: Thu, 24 Nov 2016 00:06:13 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 80.3.93.250 - /
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
 Date: Thu, 24 Nov 2016 00:06:16 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/116129-zeveracom-premium-cookie-2016-until-4232016-by-lamso/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=116129 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:17 +0000
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
 Date: Thu, 24 Nov 2016 00:06:19 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150744-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150744 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:06:21 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/5212-backdoor-josiejuniorcom-images-videos/?view=getnextunread
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=5212 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:24 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/123599-spotifycompremiumsubscription-will-autorenew-on-150616country-us/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123599 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:30 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/123133-goddessfootdominationcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123133 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:30 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150742-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150742 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:06:34 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150742-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150742 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:06:37 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/123934-x1-hbonowcom-expiration-date-2016-06-24/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123934 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:37 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 244.184.230.91 - /index.php/topic/107946-psn-api-config-by-me-no-capture-by-me-need-proxy/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=107946 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:40 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150773-spotify-premium-by-dark0de/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150773 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:06:41 +0000
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
 Date: Thu, 24 Nov 2016 00:06:42 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/4456-35free-premium-link-generators-rapidgator-uploaded-bitshare-and-others-30-filehosts/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=4456 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:49 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 188.187.5.54 - /index.php/topic/116662-vip-socks-5/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=116662 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:52 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/37776-quick-torrentcom-x1-traffic-left-617-gb/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=37776 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:06:55 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/116053-netflix-your-membership-is-paid-through-itunes/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=116053 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:00 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/57597-the-witcher-3-wild-hunt-gog/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=57597 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:01 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/125356-tidalcom-premium-active-subscription/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=125356 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:09 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150744-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150744 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:07:10 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.58 - /index.php/topic/148652-naughtyamericacom/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=148652 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:15 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/111116-need-help-please/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=111116 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:15 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/2368-18xgirls-hd-videos-watch-and-download/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=2368 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:15 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/143045-hello-everyone/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=143045 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:15 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/138980-tencom-premium-account-x1/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=138980 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:17 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 109.228.46.130 - /index.php/topic/147291-30-10-16-free-proxy-server-list/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=147291 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:17 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 77.168.34.109 - /index.php/topic/150744-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150744 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=52732 ) 
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
 Date: Thu, 24 Nov 2016 00:07:18 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/42382-rapigator-expire-23032015-tib-100/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=42382 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:07:41 +0000
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
 Date: Thu, 24 Nov 2016 00:07:55 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 80.3.93.250 - /
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
 Date: Thu, 24 Nov 2016 00:07:59 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/67674-novamovcom-premium-till-25-dec-2015/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=67674 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:01 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 177.223.89.176 - /index.php/topic/146069-proxy-list-2500-proxies-10222016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=146069 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:08 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/133955-brazzerscom/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=133955 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:17 +0000
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
 Date: Thu, 24 Nov 2016 00:08:22 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/141057-j-cee-presentation/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=141057 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:25 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 180.76.15.18 - /index.php/topic/105346-music-download-sites/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=105346 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:27 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/113211-windows-10-or-8/page-10
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=113211 AND  queued=0  ORDER BY pid asc LIMIT 180,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:29 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/14014-combo-leecher-v114-by-roy-dj/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=14014 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:38 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 190.117.114.254 - /index.php/topic/101964-campoo/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=101964 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:40 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 41.101.103.190 - /index.php/topic/101964-campoo/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=101964 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:41 +0000
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
 Date: Thu, 24 Nov 2016 00:08:42 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/65338-origin/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=65338 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:43 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/60768-%E2%98%85-%E2%98%86-%E2%98%85-priv8-dorks-sql-injection-daily-fresh-%E2%98%85-%E2%98%86-%E2%98%85/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=60768 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:48 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/116381-pointscom%E2%94%82aadvantage-56384-miles/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=116381 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:48 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/147187-erstiescom-premium-account-x3/?view=getnextunread
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=147187 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:53 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/109618-avistazto-1x-premium-account-uploaded-100-kb-downloaded-137-gb-ratio-000/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=109618 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:08:58 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.249.65.57 - /index.php?s=google=9170931c225ab19a66d37ab4e4dd072a_session&
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
 Date: Thu, 24 Nov 2016 00:09:03 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/131776-netflixcom-4-screens-ultra-hd-next-billing-date-030816/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=131776 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:07 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 247.123.205.205 - /index.php/tags/forums/STREAMING/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 150744,150904,150897,150896,150894,150893,150834,150728,150742,150865,150832,150852,150851,150850,150849,150848,150387,150341,150388,150839,150838,150730,150739,150837,150836)
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
 Date: Thu, 24 Nov 2016 00:09:07 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/123644-netflix-next-billing-date-june-22-2016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123644 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:08 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/120524-favorite-tv-series/page-4
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=120524 AND  queued=0  ORDER BY pid asc LIMIT 60,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:08 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/124928-ubercom-account-crackingportal-with-active-cards-15-us/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=124928 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:09 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.73.208.154 - /index.php/topic/8774-membersbffscom06112014fullhd/page-2
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=8774 AND  queued=0  ORDER BY pid asc LIMIT 20,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:10 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 247.123.205.205 - /index.php/tags/forums/STREAMING/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 150744,150904,150897,150896,150894,150893,150834,150728,150742,150865,150832,150852,150851,150850,150849,150848,150387,150341,150388,150839,150838,150730,150739,150837,150836)
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
 Date: Thu, 24 Nov 2016 00:09:11 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 247.123.205.205 - /index.php/tags/forums/STREAMING/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 150744,150904,150897,150896,150894,150893,150834,150728,150742,150865,150832,150852,150851,150850,150849,150848,150387,150341,150388,150839,150838,150730,150739,150837,150836)
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
 Date: Thu, 24 Nov 2016 00:09:12 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 247.123.205.205 - /index.php/tags/forums/STREAMING/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 150744,150904,150897,150896,150894,150893,150834,150728,150742,150865,150832,150852,150851,150850,150849,150848,150387,150341,150388,150839,150838,150730,150739,150837,150836)
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
 Date: Thu, 24 Nov 2016 00:09:13 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 247.123.205.205 - /index.php/tags/forums/STREAMING/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 150744,150904,150897,150896,150894,150893,150834,150728,150742,150865,150832,150852,150851,150850,150849,150848,150387,150341,150388,150839,150838,150730,150739,150837,150836)
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
 Date: Thu, 24 Nov 2016 00:09:14 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 247.123.205.205 - /index.php/tags/forums/STREAMING/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 150744,150904,150897,150896,150894,150893,150834,150728,150742,150865,150832,150852,150851,150850,150849,150848,150387,150341,150388,150839,150838,150730,150739,150837,150836)
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
 Date: Thu, 24 Nov 2016 00:09:15 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/100805-slingbox-directory-1-talk2dugs-slingbox-2-slingbox-pro-3-usa-1x-newnewnew/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=100805 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:18 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 247.123.205.205 - /index.php/topic/150733-netflixcom-premium-usa-screens-hultra-hd-has-dvd-true/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150733 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:37 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 66.249.65.57 - /index.php?s=google=19e20a2cb64131cbf2a86b8c383d8024_session&
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
 Date: Thu, 24 Nov 2016 00:09:39 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 241.224.235.112 - /index.php/topic/141847-samair-proxy-leecher-by-ry-dj/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=141847 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:09:41 +0000
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
 Date: Thu, 24 Nov 2016 00:09:56 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/145426-realitykings/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=145426 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:01 +0000
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
 Date: Thu, 24 Nov 2016 00:10:09 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/137038-samsclubcom-credit-reward-40/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=137038 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:10 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 173.192.21.89 - /index.php/topic/146069-proxy-list-2500-proxies-10222016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=146069 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:10 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/123650-netflix-next-billing-date-june-7-2016/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123650 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:17 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/117615-slingbox-directory-1-my-slingbox-2-slingbox-500-3-usa/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=117615 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:22 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 188.115.140.45 - /index.php/topic/57487-plusultimate-guitarcom-need-pro-account/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=57487 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:23 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/3932-mix-combos-1200-by-junaid/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=3932 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:27 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/143561-eternaldesirecom-premium-acc-gold-18-10102016-new-new-new/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=143561 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:28 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/62699-1fichiercom-premim-exp-09082015/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=62699 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:29 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/137413-hotbodycom-premium-account-x1/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=137413 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:29 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/102022-brazzers-premium-account-x1/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=102022 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:32 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 161.202.226.194 - /index.php/topic/146069-proxy-list-2500-proxies-10222016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=146069 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:36 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/131587-hello/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=131587 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:36 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 163.172.66.31 - /index.php/topic/119579-javhderitoalljapnese-hd-japnese-backdoors/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=119579 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:36 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/123667-pornportalcom-4-sites-access-brazzers-gf-revengel-black-gfs-daredorm-by-codecrypt-june-05/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123667 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:40 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
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
 Date: Thu, 24 Nov 2016 00:10:41 +0000
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
 Date: Thu, 24 Nov 2016 00:10:43 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
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
 Date: Thu, 24 Nov 2016 00:10:46 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
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
 Date: Thu, 24 Nov 2016 00:10:46 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/94925-rockfileeu-expire-211215/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=94925 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:48 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
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
 Date: Thu, 24 Nov 2016 00:10:51 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
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
 Date: Thu, 24 Nov 2016 00:10:54 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.246.239.190 - /
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
 Date: Thu, 24 Nov 2016 00:10:55 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/114564-alljapanesepasscom-premium-account-auto-renewal/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=114564 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:10:58 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/122845-howdy/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=122845 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:11:00 +0000
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
 Date: Thu, 24 Nov 2016 00:11:03 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/141500-seemygfcom-premium-account/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=141500 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:11:08 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/134353-zenmatecom-your-zenmate-premium-will-expire-on-august-27-2016/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=134353 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:11:08 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/31868-21sexturycom-credit-8555/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=31868 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:11:14 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 62.57.196.68 - /index.php/topic/150465-metartnetworkcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150465 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=13238 ) 
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
 Date: Thu, 24 Nov 2016 00:11:16 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/150115-nubilefilmscom-23-days/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150115 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:11:16 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.58 - /index.php/topic/880-uploadablech/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=880 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:11:24 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 62.57.196.68 - /index.php/topic/150464-metartnetworkcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150464 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=13238 ) 
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
 Date: Thu, 24 Nov 2016 00:11:32 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 62.57.196.68 - /index.php/topic/150465-metartnetworkcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150465 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=13238 ) 
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
 Date: Thu, 24 Nov 2016 00:11:35 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 62.57.196.68 - /index.php/topic/150465-metartnetworkcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150465 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN profile_portal pp ON ( m.member_id=pp.pp_member_id ) 
 LEFT JOIN members_warn_logs w ON ( w.wl_content_app='forums' and w.wl_content_id1=p.pid ) 
 LEFT JOIN pfields_content pc ON ( pc.member_id=p.author_id ) 
 LEFT JOIN reputation_index rep_index ON ( rep_index.app='forums' AND 
						             rep_index.type='pid' AND 
						             rep_index.type_id=p.pid AND 
						             rep_index.member_id=13238 ) 
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
 Date: Thu, 24 Nov 2016 00:11:41 +0000
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
 Date: Thu, 24 Nov 2016 00:11:48 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/150723-23k-emailpass-combo-list-private/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=150723 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:11:49 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 180.76.15.14 - /index.php/topic/126558-someone-good-in-assemblerpython-shell-50%E2%82%AC-if-you-help-me-ger/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=126558 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:08 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 5.254.65.123 - /
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
 Date: Thu, 24 Nov 2016 00:12:13 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/136652-hello-all-crackingportal-users/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=136652 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:13 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/98288-console-vs-pc/page-3
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=98288 AND  queued=0  ORDER BY pid asc LIMIT 40,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:17 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.19 - /index.php/topic/53965-sentry-mba-vs-vertex-poll-open/page-7
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=53965 AND  queued=0  ORDER BY pid asc LIMIT 120,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:22 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.69.133.231 - /index.php/topic/120360-project-cars-game-of-the-year-edition-multi2-xxriddickxx/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=120360 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:24 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/123509-bangbroscom/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123509 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:24 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.57 - /index.php/topic/123507-bangbroscom/?view=getnewpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=123507 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:28 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.69.133.69 - /index.php/topic/143217-hello-all/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=143217 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:31 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 37.147.223.2 - /index.php/topic/314-06-08-14-free-ssl-proxies-2810/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=314 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:32 +0000
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
 Date: Thu, 24 Nov 2016 00:12:35 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.69.133.69 - /index.php/topic/143214-x-artcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=143214 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:40 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.69.133.232 - /index.php/tags/forums/lj.com/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT t.*,p.*,m.member_id, m.members_display_name, m.members_seo_name,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig,xxx.* FROM topics t  LEFT JOIN posts p ON ( p.pid=t.topic_firstpost ) 
 LEFT JOIN members m ON ( m.member_id=p.author_id ) 
 LEFT JOIN content_cache_posts cca ON ( cca.cache_content_id=p.pid ) 
 LEFT JOIN content_cache_sigs ccb ON ( ccb.cache_content_id=p.author_id ) 
 LEFT JOIN core_tags_cache xxx ON ( xxx.tag_cache_key=MD5(CONCAT('forums',';','topics',';',t.tid)) )   WHERE t.tid IN( 4207)
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
 Date: Thu, 24 Nov 2016 00:12:41 +0000
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
 Date: Thu, 24 Nov 2016 00:12:45 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 157.55.39.11 - /index.php/topic/115095-netflixcom-4-screens-ultrahd-next-billing-date-may-5-2016/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=115095 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:46 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.69.133.69 - /topic/35539-private-dorks-for-sql-injection-to-get-fresh-cc/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=35539 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:52 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 207.46.13.112 - /index.php/topic/114058-westcoastgangbangscom-x1/?view=getlastpost
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=114058 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:54 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.69.133.233 - /index.php/topic/110429-apply-for-moderator-%C6%88%CF%83%CE%B7%D1%95%D1%82%CE%B1%CE%B7%D1%82%CE%B9%CE%B7%D1%94/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=110429 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:12:54 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.102.86.44 - /
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
 Date: Thu, 24 Nov 2016 00:12:54 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 66.249.65.57 - /index.php/topic/145743-digitalplaygroundcom/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=145743 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:13:00 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.102.86.44 - /
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
 Date: Thu, 24 Nov 2016 00:13:00 +0000
 Error: 144 - Table './crackingportal/content_cache_posts' is marked as crashed and last (automatic?) repair failed
 IP Address: 217.69.133.69 - /index.php/topic/139314-hello-everyone/
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mySQL query error: SELECT p.*,m.member_id as mid,m.name,m.member_group_id,m.email,m.joined,m.posts, m.last_visit, m.last_activity,m.login_anonymous,m.title as member_title, m.warn_level, m.warn_lastwarn, m.members_display_name, m.members_seo_name, m.member_banned, m.has_gallery, m.has_blog, m.members_bitoptions,m.mgroup_others,m.feedb_percent,m.feedb_pos,m.feedb_neu,m.feedb_neg,m.donate_donations,m.donate_amount,pp.*,w.wl_id,pc.*,rep_index.rep_rating as has_given_rep,rep_cache.rep_points, rep_cache.rep_like_cache,cca.*,ccb.cache_content as cache_content_sig, ccb.cache_updated as cache_updated_sig FROM ( SELECT pid, post_date FROM posts WHERE topic_id=139314 AND  queued=0  ORDER BY pid asc LIMIT 0,20 ) z  LEFT JOIN posts p ON ( p.pid=z.pid ) 
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
 Date: Thu, 24 Nov 2016 00:13:03 +0000
 Error: 1055 - Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'crackingportal.t.tag_meta_app' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
 IP Address: 177.102.86.44 - /
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