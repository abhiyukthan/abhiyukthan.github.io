<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 3               */
/* CACHE FILE: Generated: Tue, 05 Jan 2016 20:03:59 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_boards_3 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['boardIndexTemplate'] = array('subforums','hasUnread','forums','cat_has_forums','categories','cats_forums');


}

/* -- boardIndexTemplate --*/
function boardIndexTemplate($lastvisit="", $stats=array(), $cat_data=array(), $show_side_blocks=true, $side_blocks=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_boards', $this->_funcHooks['boardIndexTemplate'] ) )
{
$count_44842320a8c4efd6dec1d9b85d60cf88 = is_array($this->functionData['boardIndexTemplate']) ? count($this->functionData['boardIndexTemplate']) : 0;
$this->functionData['boardIndexTemplate'][$count_44842320a8c4efd6dec1d9b85d60cf88]['lastvisit'] = $lastvisit;
$this->functionData['boardIndexTemplate'][$count_44842320a8c4efd6dec1d9b85d60cf88]['stats'] = $stats;
$this->functionData['boardIndexTemplate'][$count_44842320a8c4efd6dec1d9b85d60cf88]['cat_data'] = $cat_data;
$this->functionData['boardIndexTemplate'][$count_44842320a8c4efd6dec1d9b85d60cf88]['show_side_blocks'] = $show_side_blocks;
$this->functionData['boardIndexTemplate'][$count_44842320a8c4efd6dec1d9b85d60cf88]['side_blocks'] = $side_blocks;
}
$IPBHTML .= "<template>boardIndex</template>
<subtext>authorName|date</subtext><!--authorName|date|postTitle-->
" . ((is_array( $cat_data ) AND count( $cat_data )) ? ("
		<categories>
		".$this->__f__acda0420bc4574b7cb8dafc7488be6ce($lastvisit,$stats,$cat_data,$show_side_blocks,$side_blocks)."		</categories>
	") : ("")) . "
		<statistics>
			<posts>{$stats['info']['total_posts']}</posts>
			<members>{$stats['info']['mem_count']}</members>
			<user>
				<id>{$stats['info']['last_mem_id']}</id>
				<name><![CDATA[{$stats['info']['last_mem_name']}]]></name>
				<url><![CDATA[{$stats['info']['last_mem_link']}]]></url>
			</user>
			<onlinerecord>{$stats['info']['most_online']}</onlinerecord>
		</statistics>";
return $IPBHTML;
}


function __f__556f539172061398b485f47469d84de9($lastvisit="", $stats=array(), $cat_data=array(), $show_side_blocks=true, $side_blocks=array(),$_data='',$forum_id='',$forum_data='')
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $forum_data['subforums'] as $__id => $__data )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
							<subforum>
								<id>{$__data[0]}</id>
								<name><![CDATA[{$__data[1]}]]></name>
								<url><![CDATA[" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showforum={$__data[0]}", "public",'' ), "{$__data[2]}", "showforum" ) . "]]></url>
							</subforum>
							
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

function __f__585649f75136795907ee7f8db4d48fad($lastvisit="", $stats=array(), $cat_data=array(), $show_side_blocks=true, $side_blocks=array(),$_data='')
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $_data['forum_data'] as $forum_id => $forum_data )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
					<forum>
						<id>{$forum_data['id']}</id>
						<name><![CDATA[{$forum_data['name']}]]></name>
						
						<url><![CDATA[" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showforum={$forum_data['id']}", "public",'' ), "{$forum_data['name_seo']}", "showforum" ) . "]]></url>
						<description><![CDATA[{$forum_data['description']}]]></description>
							" . (($forum_data['redirect_on']) ? ("							
						<redirect>1</redirect>
						<redirectHits>{$forum_data['redirect_hits']}</redirectHits>
						<redirect_url><![CDATA[{$forum_data['redirect_url']}]]></redirect_url>
							") : ("" . (($forum_data['_has_unread']) ? ("
							<isRead>0</isRead>
						") : ("
							<isRead>1</isRead>
						")) . "
						<redirect>0</redirect>
						<type>{$forum_data['status']}</type>
						<topics>{$forum_data['topics']}</topics>
						<replies>{$forum_data['posts']}</replies>
						<lastpost>
								" . (($forum_data['hide_last_info']) ? ("
							<name>{$this->lang->words['f_protected']}</name>
								") : ("<date>" . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($forum_data['last_post'],"DATE", 0)) . "</date>
							<name><![CDATA[{$forum_data['last_title']}]]></name>
							<id>{$forum_data['last_id']}</id>
							<url><![CDATA[" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showtopic={$forum_data['last_id']}&amp;view=getnewpost", "public",'' ), "{$forum_data['seo_last_title']}", "showtopic" ) . "]]></url>
							<user>
								" . (($forum_data['last_poster_id']) ? ("						
								<id>{$forum_data['last_poster_id']}</id>
								<name><![CDATA[{$forum_data['last_poster_name']}]]></name>
								<url><![CDATA[" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$forum_data['last_poster_id']}", "public",'' ), "{$forum_data['seo_last_name']}", "showuser" ) . "]]></url>
									") : ("
								<id>0</id>
								<name><![CDATA[{$this->settings['guest_name_pre']}{$forum_data['last_poster_name']}{$this->settings['guest_name_suf']}]]></name>
								<url></url>
								")) . "
							</user>")) . "
						</lastpost>")) . "					
										" . (($forum_data['show_subforums'] AND count( $forum_data['subforums'] ) AND $forum_data['show_subforums']) ? ("
						<subforums>
											".$this->__f__556f539172061398b485f47469d84de9($lastvisit,$stats,$cat_data,$show_side_blocks,$side_blocks,$_data,$forum_id,$forum_data)."						</subforums>
						") : ("")) . "
					</forum>
						
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

function __f__acda0420bc4574b7cb8dafc7488be6ce($lastvisit="", $stats=array(), $cat_data=array(), $show_side_blocks=true, $side_blocks=array())
{
	$_ips___x_retval = '<!--hook.foreach.skin_boards.boardIndexTemplate.categories.outer.pre-->';
	$__iteratorCount = 0;
	foreach( $cat_data as $_data )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
			" . ((is_array( $_data['forum_data'] ) AND count( $_data['forum_data'] )) ? ("
			<category>
				<id>{$_data['cat_data']['id']}</id>
				<name><![CDATA[{$_data['cat_data']['name']}]]></name>
				<url><![CDATA[" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showforum={$_data['cat_data']['id']}", "public",'' ), "{$_data['cat_data']['name_seo']}", "showforum" ) . "]]></url>
				<forums>
						".$this->__f__585649f75136795907ee7f8db4d48fad($lastvisit,$stats,$cat_data,$show_side_blocks,$side_blocks,$_data)."				</forums>
			</category>
			") : ("")) . "
		
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- guestMessageSidebar --*/
function guestMessageSidebar() {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- hookBoardIndexStatusUpdates --*/
function hookBoardIndexStatusUpdates($updates=array()) {
$IPBHTML = "";
$IPBHTML .= "<!-- NoData -->";
return $IPBHTML;
}

/* -- hookFacebookActivity --*/
function hookFacebookActivity() {
$IPBHTML = "";
$IPBHTML .= "<!-- NoData -->";
return $IPBHTML;
}

/* -- hookFacebookLikeBox --*/
function hookFacebookLikeBox($extra='') {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- hookGroupNameIndicator --*/
function hookGroupNameIndicator($groups=array()) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- hookMembersOnlineToday --*/
function hookMembersOnlineToday($mems=array(), $count=0, $state='expanded') {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- hookRecentTopics --*/
function hookRecentTopics($topics) {
$IPBHTML = "";
$IPBHTML .= "<!-- NoData -->";
return $IPBHTML;
}

/* -- hooksos_topicosrecentes_parseTopic --*/
function hooksos_topicosrecentes_parseTopic($r=array()) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- hooksos_topicosrecentes_tema1 --*/
function hooksos_topicosrecentes_tema1($topics=array()) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- hooksos_topicosrecentesAjax_tema1 --*/
function hooksos_topicosrecentesAjax_tema1($topics=array()) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- hookTagCloud --*/
function hookTagCloud($tags) {
$IPBHTML = "";
$IPBHTML .= "<!-- NoData -->";
return $IPBHTML;
}

/* -- membersSidebarStats_block --*/
function membersSidebarStats_block($title, $users, $type, $text, $column, $default, $defaultName) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- membersSidebarStats_insert --*/
function membersSidebarStats_insert($title, $users, $type, $text, $column, $default, $defaultName) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- mmstaffOnlineSidebarBlock --*/
function mmstaffOnlineSidebarBlock($staff) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- recentPosts --*/
function recentPosts($recentPosts) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- statusReplies --*/
function statusReplies($replies=array()) {
$IPBHTML = "";
$IPBHTML .= "<!-- NoData -->";
return $IPBHTML;
}

/* -- statusUpdates --*/
function statusUpdates($updates=array(), $smallSpace=0, $latestOnly=0) {
$IPBHTML = "";
$IPBHTML .= "<!-- NoData -->";
return $IPBHTML;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>