<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 0               */
/* CACHE FILE: Generated: Tue, 19 Jan 2016 05:37:47 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_shoutbox_hooks_0 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['hookActiveUsers'] = array('hideGuestCount');
$this->_funcHooks['hookActiveUsersSidebar'] = array('hideGuestCount');
$this->_funcHooks['hookGlobalShoutbox'] = array('showPopupLink');
$this->_funcHooks['hookGlobalShoutboxEmoticons'] = array('startRow','endRow','showPrevious','showNext','showPagination','cellCleanup');
$this->_funcHooks['hookGlobalShoutboxSidebar'] = array('showPopupLink');
$this->_funcHooks['hookOnlineTab'] = array('hasSomeToShow');
$this->_funcHooks['hookVCard'] = array('hasSomeToShow');
$this->_funcHooks['shoutboxJavascript'] = array('soundsOn');


}

/* -- hookActiveUsers --*/
function hookActiveUsers($stats) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['hookActiveUsers'] ) )
{
$count_691a5e7afb714b2395d16cf8dbffb76f = is_array($this->functionData['hookActiveUsers']) ? count($this->functionData['hookActiveUsers']) : 0;
$this->functionData['hookActiveUsers'][$count_691a5e7afb714b2395d16cf8dbffb76f]['stats'] = $stats;
}
$IPBHTML .= "<!--- ShoutBoxJsLoader ---><br />
<h4 class='statistics_head'>
	<div id='shoutbox-active-total' class='left" . (($this->settings['shoutbox_active_ajax']) ? (" ajax_update") : ("")) . "'>{$stats['TOTAL']}</div>&nbsp;{$this->lang->words['active_users_text']}&nbsp;{$this->lang->words['on']}&nbsp;<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "\" title='{$this->lang->words['view_main_shoutbox']}'>{$this->settings['shoutbox_title']}</a> <span>{$this->lang->words['active_users']}</span><br />
	<span class='desc'><span id='shoutbox-active-member'>{$stats['MEMBERS']}</span> {$this->lang->words['members']}, " . (($this->caches['group_cache'][ $this->settings['guest_group'] ]['g_shoutbox_view']) ? ("<span id='shoutbox-active-guests'>{$stats['GUESTS']}</span> {$this->lang->words['guests']}, ") : ("")) . "<span id='shoutbox-active-anon'>{$stats['ANON']}</span> {$this->lang->words['anon_users']}</span>
</h2>
<p id='shoutbox-active-names'>
	" . ((count($stats['NAMES'])) ? ("" . implode( ", ", $stats['NAMES'] ) . "") : ("")) . "
</p>";
return $IPBHTML;
}

/* -- hookActiveUsersSidebar --*/
function hookActiveUsersSidebar($stats) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['hookActiveUsersSidebar'] ) )
{
$count_3d4103cee0df1f7df9c684510ebf2129 = is_array($this->functionData['hookActiveUsersSidebar']) ? count($this->functionData['hookActiveUsersSidebar']) : 0;
$this->functionData['hookActiveUsersSidebar'][$count_3d4103cee0df1f7df9c684510ebf2129]['stats'] = $stats;
}
$IPBHTML .= "<!--- ShoutBoxJsLoader ---><div id='active_users' class='ipsSideBlock clearfix'>
	<h3><a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "\" title='{$this->lang->words['view_main_shoutbox']}'>{$this->lang->words['sb_hook_active_users']} (<span id='shoutbox-active-total'" . (($this->settings['shoutbox_active_ajax']) ? (" class='ajax_update''") : ("")) . ">{$stats['TOTAL']}</span>)</a></h3>
	<div>
		<span class='desc'><span id='shoutbox-active-member'>{$stats['MEMBERS']}</span> {$this->lang->words['members']}, " . (($this->caches['group_cache'][ $this->settings['guest_group'] ]['g_shoutbox_view']) ? ("<span id='shoutbox-active-guests'>{$stats['GUESTS']}</span> {$this->lang->words['guests']}, ") : ("")) . "<span id='shoutbox-active-anon'>{$stats['ANON']}</span> {$this->lang->words['anon_users']}</span>
		<br /><br />
		<p id='shoutbox-active-names'>
			" . ((count($stats['NAMES'])) ? ("" . implode( ", ", $stats['NAMES'] ) . "") : ("")) . "
		</p>
	</div>
</div>";
return $IPBHTML;
}

/* -- hookGlobalShoutbox --*/
function hookGlobalShoutbox($d='') {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['hookGlobalShoutbox'] ) )
{
$count_7530f8220822d788ec628a2e4317789a = is_array($this->functionData['hookGlobalShoutbox']) ? count($this->functionData['hookGlobalShoutbox']) : 0;
$this->functionData['hookGlobalShoutbox'][$count_7530f8220822d788ec628a2e4317789a]['d'] = $d;
}
$IPBHTML .= "<!--- ShoutBoxJsLoader --->
<script type='text/javascript'>
/* Setup some value */
ipb.shoutbox.shoutboxGLOBAL = true;
</script>
" . ((in_array( $this->settings['shoutbox_global_hook'], array( 'b' ) )) ? ("<br class=\"clear\"/>") : ("")) . "
<div class='category_block block_wrap' id='category_shoutbox'>
	<h3 class='maintitle'>
		<a class='toggle right' href='#' title='{$this->lang->words['toggle_shoutbox']}'>{$this->lang->words['toggle_shoutbox']}</a>
		<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "\" title='{$this->lang->words['view_main_shoutbox']}'>{$this->settings['shoutbox_title']}</a>
		" . (($this->settings['shoutbox_popup']) ? ("<a href=\"#\" id=\"shoutbox-popup-button\" title=\"{$this->lang->words['open_popup']}\"><img src=\"{$this->settings['img_url']}/shoutbox/popup.png\" alt=\"{$this->lang->words['open_popup']}\" /></a>") : ("")) . "
	</h3>
	<div class='ipsBox table_wrap'><div class='ipsBox_container'>
		<table class='ipb_table shoutbox_table'>
			{$d['announcement']}
			" . (($this->settings['shoutbox_global_theme'] == 2) ? ("<tr class='row1'>
					<td valign='top' class='altrow' colspan='2'>
						<div id='shoutbox-shouts' style='height:{$d['shout_height']}px;overflow:auto'>
							{$d['noshouts']}
							" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'inactivePrompt' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->inactivePrompt() : '' ) . "
							<table id='shoutbox-shouts-table'>
								<tbody>
									{$d['shouts']}
								</tbody>
							</table>
						</div>
						<div id='shouts-global-resizer'></div>
						" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(glb) : '' ) . "
					</td>
				</tr>
				" . (($this->memberData['g_shoutbox_use']) ? ("<tr class='row1'>
						<td class='altrow' valign='top' colspan='2'>
							<input type='text' id='shoutbox-global-shout' size='70' class='input_text' />
							<input type='button' id='shoutbox-submit-button' value='{$this->lang->words['shout']}' class='input_submit' />
							<input type='button' id='shoutbox-clear-button' value='{$this->lang->words['clear']}' class='input_submit alt' />
							<input type='button' id='shoutbox-refresh-button' value='{$this->lang->words['refresh']}' class='input_submit alt' />
							" . (($this->settings['shoutbox_allow_smilies']) ? (" <input type='button' id='shoutbox-smilies-button' value='{$this->lang->words['smilies']}' class='input_submit alt' data-clicklaunch=\"populateSmilies\" data-scope=\"shoutbox\" />") : ("")) . "" . (($this->settings['shoutbox_allow_bbcode']) ? (" <input type='button' id='shoutbox-bbcode-button' value='{$this->lang->words['bbcode']}' class='input_submit alt' />") : ("")) . "
							<input type='button' id='shoutbox-myprefs-button' value='{$this->lang->words['my_prefs']}' class='input_submit alt' />
						</td>
					</tr>") : ("")) . "") : ("<tr class='row1'>
					<td class='altrow' valign='top'" . (($this->memberData['g_shoutbox_use']) ? (" style='width:75%'") : (" colspan='2'")) . ">
						<div id='shoutbox-shouts' style='height:{$d['shout_height']}px;overflow:auto'>
							{$d['noshouts']}
							" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'inactivePrompt' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->inactivePrompt() : '' ) . "
							<table id='shoutbox-shouts-table'>
								<tbody>
									{$d['shouts']}
								</tbody>
							</table>
						</div>
						<div id='shouts-global-resizer'></div>
						" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(glb) : '' ) . "
					</td>
					" . (($this->memberData['g_shoutbox_use']) ? ("<td class='short row2 altrow' style='width:25%;min-width:250px;' valign='top'>
							<textarea id='shoutbox-global-shout' style='width:92%;overflow:auto;' rows='3' cols='50' class='input_text'></textarea>
							<br /><br />
							<input type='button' id='shoutbox-submit-button' value='{$this->lang->words['shout']}' class='input_submit' />
							<input type='button' id='shoutbox-clear-button' value='{$this->lang->words['clear']}' class='input_submit alt' />
							<input type='button' id='shoutbox-refresh-button' value='{$this->lang->words['refresh']}' class='input_submit alt' />
							<br /><br />
							" . (($this->settings['shoutbox_allow_smilies']) ? (" <input type='button' id='shoutbox-smilies-button' value='{$this->lang->words['smilies']}' class='input_submit alt' data-clicklaunch=\"populateSmilies\" data-scope=\"shoutbox\" />") : ("")) . "" . (($this->settings['shoutbox_allow_bbcode']) ? (" <input type='button' id='shoutbox-bbcode-button' value='{$this->lang->words['bbcode']}' class='input_submit alt' />") : ("")) . "
							<input type='button' id='shoutbox-myprefs-button' value='{$this->lang->words['my_prefs']}' class='input_submit alt' />
						</td>") : ("")) . "
				</tr>")) . "
		</table>
	</div></div>
</div>
" . ((in_array( $this->settings['shoutbox_global_hook'], array( 't', 'ct' ) )) ? ("<br class=\"clear\"/>") : ("")) . "
<script type='text/javascript'>
//<![CDATA[
{$d['js']}
//]]>
</script>";
return $IPBHTML;
}

/* -- hookGlobalShoutboxEmoticons --*/
function hookGlobalShoutboxEmoticons($emoticons=array(), $total=0, $prev=0, $next=0) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['hookGlobalShoutboxEmoticons'] ) )
{
$count_d6be2d1f5750716bfa3e920c2eed5b84 = is_array($this->functionData['hookGlobalShoutboxEmoticons']) ? count($this->functionData['hookGlobalShoutboxEmoticons']) : 0;
$this->functionData['hookGlobalShoutboxEmoticons'][$count_d6be2d1f5750716bfa3e920c2eed5b84]['emoticons'] = $emoticons;
$this->functionData['hookGlobalShoutboxEmoticons'][$count_d6be2d1f5750716bfa3e920c2eed5b84]['total'] = $total;
$this->functionData['hookGlobalShoutboxEmoticons'][$count_d6be2d1f5750716bfa3e920c2eed5b84]['prev'] = $prev;
$this->functionData['hookGlobalShoutboxEmoticons'][$count_d6be2d1f5750716bfa3e920c2eed5b84]['next'] = $next;
}

if ( ! isset( $this->registry->templateStriping['shoutboxEmo'] ) ) {
$this->registry->templateStriping['shoutboxEmo'] = array( FALSE, "row1","row2");
}

$count=0;

$extra = ""; for ( $i=count($emoticons)%$this->settings['shoutbox_emos_perrow']; $i<$this->settings['shoutbox_emos_perrow']; $i++ ) { $extra .= "<td>&nbsp;</td>"; }
$IPBHTML .= "" . (($total>count($emoticons)) ? ("<h3 class=\"maintitle short\">
		<span class=\"pager\">" . (($prev!=-1) ? ("<a href=\"#\" class=\"emoticonPager\" id=\"page_{$prev}\">&#0171;</a>") : ("")) . "&nbsp;</span>
		{$this->lang->words['more']}
		<span class=\"pager\">&nbsp;" . (((count($emoticons)+(($next-1)*$this->settings['shoutbox_emos_perpage']))<$total) ? ("<a href=\"#\" class=\"emoticonPager\" id=\"page_{$next}\">&#0187;</a>") : ("")) . "</span>
	</h3>") : ("")) . "
<table class=\"ipb_table\">
			".$this->__f__390eda26c898c26a4251182a226eb4ec($emoticons,$total,$prev,$next)."	" . ((count($emoticons)%$this->settings['shoutbox_emos_perrow']>0) ? ("
				{$extra}
		</tr>
	") : ("")) . "
</table>";
return $IPBHTML;
}


function __f__390eda26c898c26a4251182a226eb4ec($emoticons=array(), $total=0, $prev=0, $next=0)
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $emoticons as $emo )
	{
		
$count++;

		$__iteratorCount++;
		$_ips___x_retval .= "
				" . (($count%$this->settings['shoutbox_emos_perrow']==1) ? ("
			<tr class=\"" .  IPSLib::next( $this->registry->templateStriping["shoutboxEmo"] ) . "\">
		") : ("")) . "
		<td class=\"short\">
			<a title=\"{$emo['image']}\" onclick='ipb.shoutbox.emoticonOnclick(\"{$emo['text']}\"); return false;' href=\"#\">
				<img alt=\"{$emo['image']}\" src=\"{$this->settings['emoticons_url']}/{$emo['image']}\" />
			</a>
		</td>
		" . (($count%$this->settings['shoutbox_emos_perrow']==0) ? ("
			</tr>
		") : ("")) . "
	
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- hookGlobalShoutboxSidebar --*/
function hookGlobalShoutboxSidebar($d='') {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['hookGlobalShoutboxSidebar'] ) )
{
$count_3e0c5d7ef64e2d6d48de9534c92fa381 = is_array($this->functionData['hookGlobalShoutboxSidebar']) ? count($this->functionData['hookGlobalShoutboxSidebar']) : 0;
$this->functionData['hookGlobalShoutboxSidebar'][$count_3e0c5d7ef64e2d6d48de9534c92fa381]['d'] = $d;
}
$IPBHTML .= "<!--- ShoutBoxJsLoader --->
<script type='text/javascript'>
/* Setup some value */
ipb.shoutbox.shoutboxGLOBAL = true;
</script>
{$d['emoticons']}
<div id='shoutbox_sidebar' class='ipsSideBlock clearfix'>
	<h3>
		{$this->settings['shoutbox_title']}
		" . (($this->settings['shoutbox_popup']) ? ("<a href=\"#\" id=\"shoutbox-popup-button\" title=\"{$this->lang->words['open_popup']}\"><img src=\"{$this->settings['img_url']}/shoutbox/popup.png\" alt=\"{$this->lang->words['open_popup']}\" /></a>") : ("")) . "
</h3>
	<ul class='hfeed block_list'>
		<table class='ipb_table shoutbox_table'>
			{$d['announcement']}
			<tr class='row1'>
				<td valign='top' class='altrow'>
					<div id='shoutbox-shouts' style='height: {$d['shout_height']}px; overflow-x: hidden;'>
						{$d['noshouts']}
						" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'inactivePrompt' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->inactivePrompt() : '' ) . "
						<table id='shoutbox-shouts-table'>
							<tbody>
								{$d['shouts']}
							</tbody>
						</table>
					</div>
					<img src='{$this->settings['img_url']}/spacer.gif' id='shouts-global-resizer' border='0' height='4px' alt='{$this->lang->words['resize_shouts_area']}' style='cursor:n-resize;width:100%;' />
					" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(glb) : '' ) . "" . (($this->memberData['g_shoutbox_use']) ? ("<br />
						<input type='text' id='shoutbox-global-shout' style='width:95%;' class='input_text' /><br /><br />
						<div class='short'>
							<input type='button' id='shoutbox-submit-button' value='{$this->lang->words['shout']}' class='input_submit' />
							<input type='button' id='shoutbox-clear-button' value='{$this->lang->words['clear']}' class='input_submit alt' />
							<input type='button' id='shoutbox-refresh-button' value='{$this->lang->words['refresh']}' class='input_submit alt' />
						</div><br />
						<div class='short'>
							" . (($this->settings['shoutbox_allow_smilies']) ? (" <input type='button' id='shoutbox-smilies-button' value='{$this->lang->words['smilies']}' class='input_submit alt' data-clicklaunch=\"populateSmilies\" data-scope=\"shoutbox\" />") : ("")) . "" . (($this->settings['shoutbox_allow_bbcode']) ? (" <input type='button' id='shoutbox-bbcode-button' value='{$this->lang->words['bbcode']}' class='input_submit alt' />") : ("")) . "
							<input type='button' id='shoutbox-myprefs-button' value='{$this->lang->words['my_prefs']}' class='input_submit alt' />
						</div>") : ("")) . "
				</td>
			</tr>
		</table>
	</ul>
</div>
<script type='text/javascript'>
{$d['js']}
</script>";
return $IPBHTML;
}

/* -- hookOnlineTab --*/
function hookOnlineTab($count=0) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['hookOnlineTab'] ) )
{
$count_0f6c31d4bdb3b747c048a202db4af523 = is_array($this->functionData['hookOnlineTab']) ? count($this->functionData['hookOnlineTab']) : 0;
$this->functionData['hookOnlineTab'][$count_0f6c31d4bdb3b747c048a202db4af523]['count'] = $count;
}
$IPBHTML .= "" . (($count > 0) ? ("
	<div id=\"shoutbox-tab-count-wrap\"><span id=\"shoutbox-tab-count\" class=\"ipsHasNotifications\" style=\"display: none;\">{$count}</span></div>
	<script type=\"text/javascript\">
		document.observe(\"dom:loaded\", function(){
			var _thisHtml	= $('nav_app_shoutbox').innerHTML;
			_thisHtml = _thisHtml.replace( /\\<\\/a\\>/ig, '' ) + $('shoutbox-tab-count-wrap').innerHTML + \"</a>\";
			$('nav_app_shoutbox').update( _thisHtml );
			$('shoutbox-tab-count-wrap').remove();
			$('shoutbox-tab-count').show();
		});
	</script>
") : ("")) . "";
return $IPBHTML;
}

/* -- hookVCard --*/
function hookVCard($member) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['hookVCard'] ) )
{
$count_4932548a97f83244695cc54b24d2b37c = is_array($this->functionData['hookVCard']) ? count($this->functionData['hookVCard']) : 0;
$this->functionData['hookVCard'][$count_4932548a97f83244695cc54b24d2b37c]['member'] = $member;
}
$IPBHTML .= "" . (($member['shoutbox_shouts'] > 0) ? ("
	<li>
		<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$member['member_id']}&amp;tab=shoutbox", "public",'' ), "{$member['members_seo_name']}", "showuser" ) . "'>
			<img src=\"{$this->settings['img_url']}/shoutbox/shout.png\" title=\"{$member['shoutbox_shouts']} {$this->lang->words['shouts']}\" alt=\"{$member['shoutbox_shouts']} {$this->lang->words['shouts']}\" /></a>
		</a>
	</li>
") : ("")) . "";
return $IPBHTML;
}

/* -- shoutboxJavascript --*/
function shoutboxJavascript() {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox_hooks', $this->_funcHooks['shoutboxJavascript'] ) )
{
$count_d51da87b180add10c9e8cf1a95eba19c = is_array($this->functionData['shoutboxJavascript']) ? count($this->functionData['shoutboxJavascript']) : 0;
}
$IPBHTML .= "<script type='text/javascript' src='{$this->settings['js_base_url']}js/shoutbox.js'></script>
" . (($this->settings['shoutbox_enable_sound']) ? ("
<script type='text/javascript' src='{$this->settings['public_dir']}sounds/soundmanager2-nodebug-jsmin.js'></script>
<script type='text/javascript'>document.observe('dom:loaded', function() { soundManager.url = '{$this->settings['public_dir']}sounds/';soundManager.debugMode=false; });</script>
") : ("")) . "";
return $IPBHTML;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>