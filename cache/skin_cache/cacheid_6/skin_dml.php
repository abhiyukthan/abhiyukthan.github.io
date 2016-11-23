<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 6               */
/* CACHE FILE: Generated: Tue, 17 May 2016 20:43:23 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_dml_6 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();


}

/* -- duplicatesFraudAccessAlert --*/
function duplicatesFraudAccessAlert($link, $counter) {
$IPBHTML = "";
$IPBHTML .= "<li class=\"active\">
	" . (($link) ? ("
	<a>{$counter} {$this->lang->words['fraud_access_alert']}</a>
	") : ("
	<a href=\"{$this->settings['_admin_link']}?app=duplicates&amp;module=manage&amp;section=duplicates&amp;do=listDuplicates\" title=\"{$this->lang->words['fraud_access_alert']}\" target=\"_blank\">{$counter} {$this->lang->words['fraud_access_alert']}</a>
	")) . "
</li>";
return $IPBHTML;
}

/* -- duplicatesFraudRegistrationAlert --*/
function duplicatesFraudRegistrationAlert($tab, $counter) {
$IPBHTML = "";
$IPBHTML .= "<li class=\"active\">
	<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=modcp&amp;fromapp=duplicates&amp;tab=registrations{$tab}", "public",'' ), "", "" ) . "\" title=\"{$this->lang->words['fraud_registrations_alert']}\">{$counter} {$this->lang->words['fraud_registrations_alert']}</a>
</li>";
return $IPBHTML;
}

/* -- duplicatesLoadMovie --*/
function duplicatesLoadMovie($host, $path, $id, $md5) {
$IPBHTML = "";
$IPBHTML .= "<div style=\"position: absolute; top: 0px; left: -5000px;\"><object type=\"application/x-shockwave-flash\" data=\"{$this->settings['board_url']}/public/dml.swf\" width=\"1\" height=\"1\"><param name=\"movie\" value=\"{$this->settings['board_url']}/public/dml.swf\" /><param name=\"FlashVars\" value=\"{$host}&amp;{$path}&amp;{$id}&amp;{$md5}\" /></object></div>";
return $IPBHTML;
}

/* -- duplicatesRegistrationsBanned --*/
function duplicatesRegistrationsBanned($list) {
$IPBHTML = "";
$IPBHTML .= "" . ( method_exists( $this->registry->getClass('output')->getTemplate('modcp'), 'subTabLoop' ) ? $this->registry->getClass('output')->getTemplate('modcp')->subTabLoop() : '' ) . "
<div class=\"clearfix\">
	" . ((is_array( $list ) and count( $list )) ? ("
	<div>
		".$this->__f__94799ec82ae9072b89608343de8c549b($list)."		<div class=\"moderation_bar rounded\" style=\"text-align: center;\">
			<ul class=\"ipsList_inline modcp_post_controls\">
				<li>
					<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=duplicates&amp;module=moderate&amp;section=moderate&amp;do=delete_all&amp;return=modcp:banned", "public",'' ), "", "" ) . "\" class=\"ipsButton_secondary important\" style=\"opacity: 1;\" title=\"{$this->lang->words['perm_delete_all']}\">{$this->lang->words['perm_delete_all']}</a>
				</li>
			</ul>
		</div>
	</div>
	") : ("
	<div class=\"no_messages\">
		{$this->lang->words['no_banned_registrations']}
	</div>
	")) . "
</div>";
return $IPBHTML;
}


function __f__ec5cc79ed32e6302d34f47d5f0539d5c($list,$member='')
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $member['attempts'] as $attempt )
	{
		
$new_member = array_merge( IPSMember::load( $attempt['new_member_id'] ), IPSMember::buildProfilePhoto( $attempt['new_member_id'] ) );

		$__iteratorCount++;
		$_ips___x_retval .= "
										<ul class=\"ipsList_inline modcp_post_controls\">
						<li class=\"desc\">
							<strong>{$this->lang->words['attempted']}</strong>
							<span class=\"desc lighter\">" . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($attempt['time'],"long", 0)) . "</span>
						</li>
						<li class=\"desc\">
							<strong>{$this->lang->words['created_member']}</strong>
							<span class=\"author vcard\">" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'userHoverCard' ) ? $this->registry->getClass('output')->getTemplate('global')->userHoverCard($new_member) : '' ) . "</span>
						</li>
						<li class=\"desc\">
							<strong>{$this->lang->words['ip']}</strong>
							<span class=\"desc lighter\">
								" . (($member['g_access_cp']) ? ("
								<em>{$this->lang->words['ip_private']}</em>
								") : ("
								<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=modcp&amp;tab=iplookup&amp;fromapp=members&amp;_do=submit&amp;ip={$attempt['ip_address']}", "public",'' ), "", "" ) . "\" title=\"{$this->lang->words['info_about_this_ip']}\">{$attempt['ip_address']}</a>
								")) . "
							</span>
						</li>
					</ul>
					
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

function __f__94799ec82ae9072b89608343de8c549b($list)
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $list as $member )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
		<div class=\"post_block hentry no_sidebar\">
			<div class=\"post_wrap\">
				<h3 class=\"row2\">
					<img src=\"{$member['pp_small_photo']}\" class=\"ipsUserPhoto ipsUserPhoto_tiny\" />
					<span class=\"author vcard\">" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'userHoverCard' ) ? $this->registry->getClass('output')->getTemplate('global')->userHoverCard($member) : '' ) . "</span>
					<span class=\"ip right ipsType_small\">({$this->lang->words['ip']}:
						" . (($member['g_access_cp']) ? ("
						<em>{$this->lang->words['ip_private']}</em>
						") : ("
						<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=modcp&amp;tab=iplookup&amp;fromapp=members&amp;_do=submit&amp;ip={$member['ip_address']}", "public",'' ), "", "" ) . "\" title=\"{$this->lang->words['info_about_this_ip']}\">{$member['ip_address']}</a>
						")) . ")
					</span>
				</h3>
				<div class=\"post_body\">
					<ul class=\"ipsList_inline modcp_post_controls right\">
						<li>
							<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=duplicates&amp;module=moderate&amp;section=moderate&amp;do=delete&amp;mid={$member['member_id']}&amp;return=modcp:banned", "public",'' ), "", "" ) . "\" class=\"ipsButton_secondary ipsType_smaller important\" title=\"{$this->lang->words['perm_delete_post']}\">{$this->lang->words['perm_delete_post']}</a>
						</li>
					</ul>
					".$this->__f__ec5cc79ed32e6302d34f47d5f0539d5c($list,$member)."				</div>
			</div>
		</div>
		
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- duplicatesRegistrationsProhibited --*/
function duplicatesRegistrationsProhibited($list) {
$IPBHTML = "";
$IPBHTML .= "" . ( method_exists( $this->registry->getClass('output')->getTemplate('modcp'), 'subTabLoop' ) ? $this->registry->getClass('output')->getTemplate('modcp')->subTabLoop() : '' ) . "
<div class=\"clearfix\">
	" . ((is_array( $list ) and count( $list )) ? ("
	<div>
		".$this->__f__33b6cfb7072b3ef5fca612296985c4fe($list)."		<div class=\"moderation_bar rounded\" style=\"text-align: center;\">
			<ul class=\"ipsList_inline modcp_post_controls\">
				<li>
					<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=duplicates&amp;module=moderate&amp;section=moderate&amp;do=delete_all&amp;return=modcp:prohibited", "public",'' ), "", "" ) . "\" class=\"ipsButton_secondary important\" style=\"opacity: 1;\" title=\"{$this->lang->words['perm_delete_all']}\">{$this->lang->words['perm_delete_all']}</a>
				</li>
			</ul>
		</div>
	</div>
	") : ("
	<div class=\"no_messages\">
		{$this->lang->words['no_prohibited_registrations']}
	</div>
	")) . "
</div>";
return $IPBHTML;
}


function __f__f232a5c396a6e2cf7486cc5cadf0a8bc($list,$member='')
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $member['attempts'] as $attempt )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
					<ul class=\"ipsList_inline modcp_post_controls\">
						<li class=\"desc\">
							<strong>{$this->lang->words['attempted']}</strong>
							<span class=\"desc lighter\">" . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($attempt['time'],"long", 0)) . "</span>
						</li>
						<li class=\"desc\">
							<strong>{$this->lang->words['ip']}</strong>
							<span class=\"desc lighter\">
								" . (($member['g_access_cp']) ? ("
								<em>{$this->lang->words['ip_private']}</em>
								") : ("
								<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=modcp&amp;tab=iplookup&amp;fromapp=members&amp;_do=submit&amp;ip={$attempt['ip_address']}", "public",'' ), "", "" ) . "\" title=\"{$this->lang->words['info_about_this_ip']}\">{$attempt['ip_address']}</a>
								")) . "
							</span>
						</li>
					</ul>
					
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

function __f__33b6cfb7072b3ef5fca612296985c4fe($list)
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $list as $member )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
		<div class=\"post_block hentry no_sidebar\">
			<div class=\"post_wrap\">
				<h3 class=\"row2\">
					<img src=\"{$member['pp_small_photo']}\" class=\"ipsUserPhoto ipsUserPhoto_tiny\" />
					<span class=\"author vcard\">" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'userHoverCard' ) ? $this->registry->getClass('output')->getTemplate('global')->userHoverCard($member) : '' ) . "</span>
					<span class=\"ip right ipsType_small\">({$this->lang->words['ip']}:
						" . (($member['g_access_cp']) ? ("
						<em>{$this->lang->words['ip_private']}</em>
						") : ("
						<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=modcp&amp;tab=iplookup&amp;fromapp=members&amp;_do=submit&amp;ip={$member['ip_address']}", "public",'' ), "", "" ) . "\" title=\"{$this->lang->words['info_about_this_ip']}\">{$member['ip_address']}</a>
						")) . ")
					</span>
				</h3>
				<div class=\"post_body\">
					<ul class=\"ipsList_inline modcp_post_controls right\">
						<li>
							<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=duplicates&amp;module=moderate&amp;section=moderate&amp;do=delete&amp;mid={$member['member_id']}&amp;return=modcp:prohibited", "public",'' ), "", "" ) . "\" class=\"ipsButton_secondary ipsType_smaller important\" title=\"{$this->lang->words['perm_delete_post']}\">{$this->lang->words['perm_delete_post']}</a>
						</li>
					</ul>
					".$this->__f__f232a5c396a6e2cf7486cc5cadf0a8bc($list,$member)."				</div>
			</div>
		</div>
		
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