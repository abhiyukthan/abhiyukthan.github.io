<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 0               */
/* CACHE FILE: Generated: Mon, 05 Jan 2015 14:06:56 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_teez_apps_0 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['importantLink'] = array('importantLinkgroups');


}

/* -- importantHeader --*/
function importantHeader($data, $pages) {
$IPBHTML = "";
$IPBHTML .= "" . ((count($data)) ? ("
<div id=\"category_motm\" class=\"category_block block_wrap\">
	<h3 class=\"maintitle\">
		{$this->lang->words['important_topics']}
	</h3>
	<div class=\"ipsBox table_wrap\">
	<div class=\"ipsBox_container\">
	<table class=\"ipsTable\">
		<tr>
												
												
			".$this->__f__dc00d897512fae2a0a3368d6aedc40a0($data,$pages)."					</div>
{$pages}
				</div>
			</td>
		</tr>
	</table>
	</div>

	</div></div>
<br>
") : ("")) . "";
return $IPBHTML;
}


function __f__dc00d897512fae2a0a3368d6aedc40a0($data, $pages)
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $data as $r )
	{
		
$aaa = IPSMember::load($r['starter_id'], 'members_display_name' );

		$__iteratorCount++;
		$_ips___x_retval .= "
							<td>
				<div style=\"position:relative;left:-8px;padding:3px 0px 5px 14px;\">
					<div style=\"border-bottom:1px solid lightgrey;padding-bottom:3px;\">
						<h4> <a style=\"font-size:11px\" href=\"index.php?/topic/{$r['tid']}-{$r['title_seo']}\"><span style=\"font-size:1.3em;\">{$r['title']}</span></a>
						<span style=\"float:right;color:grey;font-size:10px;position:relative;\">Started by " . IPSMember::makeProfileLink($aaa['members_display_name'], $r['starter_id'], $aaa['members_display_name'])  . " " . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($r['start_date'],"SHORT", 0)) . "</h4> 
						</div>
					<p class=\"desc __forum_desc ipsType_small\" style=\"padding-top:3px\">
					{$r['_post']}</strong>
					</p>
					<div style=\"padding:5px;float:right\">
						<span class=\"ipsBadge ipsBadge_green reset_cursor\">{$r['posts']} {$this->lang->words['replies']}</span> <span class=\"ipsBadge ipsBadge_green reset_cursor\">{$r['views']} {$this->lang->words['views']}</span> 
 
" . (($r['state'] == open) ? ("
<span class=\"ipsBadge ipsBadge_green reset_cursor\">{$this->lang->words['open']}</span>
") : ("
<span class=\"ipsBadge ipsBadge_red reset_cursor\">{$this->lang->words['lock']}</span>
")) . " 
" . (($r['pinned'] == 1) ? ("
<span class=\"ipsBadge ipsBadge_red reset_cursor\">{$this->lang->words['pinned']}</span>
") : ("")) . "
					
						
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- importantLink --*/
function importantLink($topic) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_teez_apps', $this->_funcHooks['importantLink'] ) )
{
$count_e18e969ec2044c49c7cc18a8bb0dd9ab = is_array($this->functionData['importantLink']) ? count($this->functionData['importantLink']) : 0;
$this->functionData['importantLink'][$count_e18e969ec2044c49c7cc18a8bb0dd9ab]['topic'] = $topic;
}
$IPBHTML .= "" . ((in_array( $this->memberData[ 'member_group_id' ], explode( ',', $this->settings[ 'important_groups' ] ) )) ? ("" . (($topic['important'] == 0) ? ("
<li><a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=forums&amp;module=important&amp;section=important&amp;t={$topic['tid']}&amp;f={$topic['forum_id']}&amp;auth_key={$this->member->form_hash}&amp;_fromTopic=1&amp;do=importantYes", "public",'' ), "", "" ) . "\">
{$this->lang->words['important']}</a></li>
") : ("
<li><a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=forums&amp;module=important&amp;section=important&amp;t={$topic['tid']}&amp;f={$topic['forum_id']}&amp;auth_key={$this->member->form_hash}&amp;do=importantNo", "public",'' ), "", "" ) . "\">{$this->lang->words['no_important']}</a></li>
")) . "") : ("")) . "";
return $IPBHTML;
}

/* -- importantSideblock --*/
function importantSideblock($data, $pages) {
$IPBHTML = "";
$IPBHTML .= "" . ((count($data)) ? ("
	  <div class='ipsSideBlock clearfix'>
	<h3>{$this->lang->words['important_topics']}</h3>
	<div class='_sbcollapsable'>
		<ul class='ipsList_withminiphoto'>".$this->__f__690c14afd2ac2fdd15b59bcbd72bc597($data,$pages)."		
		</ul>
		{$pages}
	</div>
</div>
") : ("")) . "";
return $IPBHTML;
}


function __f__690c14afd2ac2fdd15b59bcbd72bc597($data, $pages)
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $data as $r )
	{
		
$aaa = IPSMember::load($r['starter_id'], 'members_display_name' );

		$__iteratorCount++;
		$_ips___x_retval .= "
						<li class='clearfix'>
			
												<span class=\"left\" style=\"margin-right: 5px;\">" . IPSMember::buildProfilePhoto($r['starter_id'],$size=mini) . "</span>

			<div class='list_content'>
				<a href=\"index.php?/topic/{$r['tid']}-{$r['title_seo']}\"><span style=\"ipsType Small\">{$r['title']}</a>
				<p class='desc ipsType_smaller'>
					" . IPSMember::makeProfileLink($aaa['members_display_name'], $r['starter_id'], $aaa['members_display_name'])  . " -  " . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($r['start_date'],"SHORT", 0)) . "
				</p>
			</div>
		</li>

";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>