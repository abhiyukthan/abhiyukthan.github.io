<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 4               */
/* CACHE FILE: Generated: Tue, 05 Jan 2016 20:04:02 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_shoutbox_4 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['archive'] = array('ampmForStart','ampmForEnd');
$this->_funcHooks['popupWrapper'] = array('istm','istl','jsBugPatch');
$this->_funcHooks['shout_row'] = array('showAtTag','showColon');
$this->_funcHooks['shout_row_sidebar'] = array('showAtTag');
$this->_funcHooks['shoutbox'] = array('showPopupLink','myShoutCount','hideGuestCount');


}

/* -- ajax_jscmd --*/
function ajax_jscmd($data='') {
$IPBHTML = "";
$IPBHTML .= "Event.observe(window, 'load', function() {
" . (($data['type'] == 'mod-shout' && $data['id'] > 0) ? ("ipb.shoutbox.modOptsLoadShout({$data['id']});") : ("")) . "
" . (($data['type'] == 'mod-member' && $data['mid'] > 0) ? ("ipb.shoutbox.modOptsLoadMember({$data['mid']});") : ("")) . "
" . (($data['type'] == 'archive') ? ("ipb.shoutbox.displayArchive();") : ("")) . "
" . (($data['type'] == 'myprefs') ? ("ipb.shoutbox.myPrefsLoad();") : ("")) . "
" . (($data['type'] == 'edit-shout' && $data['id']) ? ("ipb.shoutbox.editShout({$data['id']});") : ("")) . "
});";
return $IPBHTML;
}

/* -- announcement --*/
function announcement($global=true, $hide=true) {
$IPBHTML = "";
$IPBHTML .= "<tr id='shoutbox-announcement-row' class='row2'" . (($hide) ? (" style='display:none;'") : ("")) . ">
	<td class='altrow' valign='middle'" . (($global) ? (" colspan='2'") : ("")) . ">
		<div id='shoutbox-announcement-text' class='message'>
			{$this->settings['shoutbox_announcement']}
		</div>
	</td>
</tr>";
return $IPBHTML;
}

/* -- archive --*/
function archive($d='') {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox', $this->_funcHooks['archive'] ) )
{
$count_7bf4d9764c0e1f4fa1e5ecdd3effe825 = is_array($this->functionData['archive']) ? count($this->functionData['archive']) : 0;
$this->functionData['archive'][$count_7bf4d9764c0e1f4fa1e5ecdd3effe825]['d'] = $d;
}
$IPBHTML .= "<h3>{$this->lang->words['sb_archive']}</h3>
" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(archive) : '' ) . "
<div id='beforeButtonClick' class='ipsBox_container'>
	<table class='ipb_table'>
		<tr>
			<td valign='top' colspan='2'>
			  {$this->lang->words['sb_archive_welcome']}
			</td>
			<td style=\"vertical-align: top;\">
				<input type='button' id='shoutbox_archive_filters' value='{$this->lang->words['quick_filters']}' class='input_submit ipbmenu right' style='width:140px'/>
				<ul class='ipbmenu_content' id='shoutbox_archive_filters_menucontent' style='width:138px'>
					<li id='filter_mine' class='clickable'><a href=\"#\">{$this->lang->words['my_shouts']}</a></li>
					<li id='filter_today' class='clickable'><a href=\"#\">{$this->lang->words['today_shouts']}</a></li>
					<li id='filter_yesterday' class='clickable'><a href=\"#\">{$this->lang->words['yesterday_shouts']}</a></li>
					<li id='filter_month' class='clickable'><a href=\"#\">{$this->lang->words['month_shouts']}</a></li>
					<li id='filter_all' class='clickable'><a href=\"#\">{$this->lang->words['all_shouts']}</a></li>
				</ul>
			</td>
		</tr>
		<tr class='row2'>
			<td class='altrow' valign='top' colspan='3'>
				<strong><span id='shoutbox-popup-status'></span></strong>
			</td>
		</tr>
		<tr>
			<td valign='middle' width='5%'>
				<strong>{$this->lang->words['start']}:</strong>
			</td>
			<td valign='top' width='70%'>
				<select class='input_text' id='filter_start_month'>{$d['s_months']}</select>
				<select class='input_text' id='filter_start_day'>{$d['s_days']}</select>
				<select class='input_text' id='filter_start_year'>{$d['s_years']}</select>
				<select class='input_text' id='filter_start_hour'>{$d['s_hours']}</select>
				<select class='input_text' id='filter_start_minute'>{$d['s_minutes']}</select>
				" . (($this->settings['shoutbox_archive_clock'] == 'ampm') ? ("
					<select class='input_text' id='filter_start_meridiem'>{$d['s_meridiems']}</select>
				") : ("")) . "
			</td>
			<td valign='bottom' width='25%'>
			  <strong>{$this->lang->words['filter_by_names']}:</strong>
			</td>
		</tr>
		<tr>
			<td valign='middle'>
				<strong>{$this->lang->words['end']}:</strong>
			</td>
			<td valign='top'>
				<select class='input_text' id='filter_end_month'>{$d['e_months']}</select>
				<select class='input_text' id='filter_end_day'>{$d['e_days']}</select>
				<select class='input_text' id='filter_end_year'>{$d['e_years']}</select>
				<select class='input_text' id='filter_end_hour'>{$d['e_hours']}</select>
				<select class='input_text' id='filter_end_minute'>{$d['e_minutes']}</select>
				" . (($this->settings['shoutbox_archive_clock'] == 'ampm') ? ("
					<select class='input_text' id='filter_end_meridiem'>{$d['e_meridiems']}</select>
				") : ("")) . "
			</td>
			<td valign='top'>
			  <input class='input_text' type='text' id='filter_member_name' value='' />
			</td>
		</tr>
		<tr>
			<td colspan='3' style='padding:0;margin:0;'>
				<p class='submit' width='100%'>
					<input type='button' id='shoutbox-archive-filter-button' value='{$this->lang->words['filter']}' class='input_submit' />
				</p>
			</td>
		</tr>
	</table>
</div>
<div id='afterButtonClick' class='ipsBox_container' style='display:none;'>
	<table class='ipb_table'>
		<tr>
			<td align='left'>
				<div id='shoutbox-archive-pages-floater' class='right'>
					<div id='shoutbox-archive-pages-data'>abc</div>
				</div>
				<a href='javascript:void(0);' id='backToFilters'>{$this->lang->words['back_to_filters']}</a><br />
				<div id='shoutbox-popup-content' style='position:relative'>
					<div id='shoutbox-archive-shouts-div' style='width:100%;height:{$d['height']}px;overflow:auto'>
						<table id='shoutbox-archive-shouts'>
							<tbody>
							</tbody>
						</table>
					</div>
				</div>
			</td>
	  </tr>
	</table>
</div>
<script type='text/javascript'>
ipb.shoutbox.my_dname     = \"" . str_replace( '"', '"', $this->memberData['members_display_name'] ) . "\";
ipb.shoutbox.oldest_shout = \"{$d['oldestShout']}\";
//$('shoutbox-archive-shouts-div').observe('scroll', ipb.shoutbox.archive_update_floaters );
$('filter_member_name').observe('click', function() {
	if( $('filter_member_name').value == \"" . str_replace( '"', '"', $this->lang->words['member_name'] ) . "\" )
	{
		$('filter_member_name').value='';
	}
} );
$('filter_member_name').observe('focus', function() {
	ipb.shoutbox.popupUpdateStatus('filter_member_name_status');
} );
$('filter_member_name').observe('blur', function() {
	ipb.shoutbox.popupUpdateStatus('sb_archive_loaded');
} );
</script>";
return $IPBHTML;
}

/* -- archive_ajax --*/
function archive_ajax($d='') {
$IPBHTML = "";
$IPBHTML .= "<script type='text/javascript'>
ipb.shoutbox.shout_pages = {$d['pages']};
ipb.shoutbox.archive_update_pager({$d['curpage']});
</script>";
return $IPBHTML;
}

/* -- archive_message --*/
function archive_message($m='') {
$IPBHTML = "";
$IPBHTML .= "<div class='desc'>{$m}</div>";
return $IPBHTML;
}

/* -- inactivePrompt --*/
function inactivePrompt($d='') {
$IPBHTML = "";
$IPBHTML .= "<table id='shoutbox-inactive-prompt' style='display:none;'>
	<tr class='row1'>
		<td class='altrow short' valign='middle'>
			" . str_replace( "<#MINUTES#>", $this->registry->getClass('shoutboxLibrary')->inactivity_cutoff, $this->lang->words['inactive_text'] ) . "
			<br /><br />
			<input type='button' value=\"{$this->lang->words['im_back']}\" class='input_submit' onclick='ipb.shoutbox.processInactivePrompt();' />
		</td>
	</tr>
</table>";
return $IPBHTML;
}

/* -- javascript --*/
function javascript($d='') {
$IPBHTML = "";
$IPBHTML .= "ipb.shoutbox.myMemberID       = parseInt({$this->memberData['member_id']});
ipb.shoutbox.can_use          = parseInt({$this->memberData['g_shoutbox_use']});
ipb.shoutbox.can_edit         = parseInt({$this->memberData['g_shoutbox_edit']});
ipb.shoutbox.flood_limit      = parseInt({$this->settings['shoutbox_flood_limit']});
ipb.shoutbox.bypass_flood     = parseInt({$this->memberData['g_shoutbox_bypass_flood']});
ipb.shoutbox.can_access_acp   = parseInt({$this->memberData['g_access_cp']});
ipb.shoutbox.view_archive     = " . (($this->memberData['g_shoutbox_view_archive']) ? ("true") : ("false")) . ";
ipb.shoutbox.enable_fade      = parseInt({$this->settings['shoutbox_shout_fade']});
ipb.shoutbox.inactive_timeout = parseInt({$this->registry->getClass('shoutboxLibrary')->inactivity_cutoff});
ipb.shoutbox.hide_refresh     = parseInt({$this->settings['shoutbox_autohide_refresh']});
ipb.shoutbox.members_refresh  = $this->settings['shoutbox_members_viewing_refresh'] < 30 ? 30000 : parseInt({$this->settings['shoutbox_members_viewing_refresh']})*1000;
ipb.shoutbox.shouts_refresh   = $this->settings['shoutbox_shouts_refresh'] < 30 ? 30000 : parseInt({$this->settings['shoutbox_shouts_refresh']})*1000;
ipb.shoutbox.total_shouts     = parseInt({$this->registry->getClass('shoutboxLibrary')->shout_total});
ipb.shoutbox.shout_order      = '{$this->registry->getClass('shoutboxLibrary')->shouts_order}';
ipb.shoutbox.moderator        = {$this->registry->getClass('shoutboxLibrary')->moderator};
" . (($this->registry->getClass('shoutboxLibrary')->moderator) ? ("
ipb.shoutbox.mod_perms        = { {$this->registry->getClass('shoutboxLibrary')->mod_perms_js} };
") : ("")) . "
ipb.shoutbox.my_prefs         = { {$this->registry->getClass('shoutboxLibrary')->prefs_js} };
ipb.shoutbox.img_disable      = parseInt({$this->settings['shoutbox_disable_refresh_image']});
ipb.shoutbox.member_name      = '{$this->memberData['members_display_name']}';
ipb.shoutbox.can_me_tag       = parseInt({$this->settings['shoutbox_me_tag']});";
return $IPBHTML;
}

/* -- memberViewingName --*/
function memberViewingName($id, $link) {
$IPBHTML = "";
$IPBHTML .= "<span class='name'>{$link}" . (($this->registry->getClass('shoutboxLibrary')->moderator) ? ("&nbsp;<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "#member{$id}' onclick='return ipb.shoutbox.modOptsLoadMember({$id})' title='{$this->lang->words['mmenu_load_mod_opts']}'><img src=\"{$this->settings['img_url']}/user_edit.png\" alt=\"{$this->lang->words['macro__useredit']}\" /></a>") : ("")) . "</span>";
return $IPBHTML;
}

/* -- mod_opts_content --*/
function mod_opts_content($action='',$data=array()) {
$IPBHTML = "";

$pluginEditorHook = IPSLib::loadLibrary( IPS_ROOT_PATH . 'sources/classes/editor/composite.php', 'classes_editor_composite' );
	$editor = new $pluginEditorHook();
$IPBHTML .= "" . ((substr( $action, 0, 4 ) != 'edit') ? ("" . (($action == 'delete') ? ("
		{$this->lang->words['mod_opt_confirm_delete']}
	") : ("")) . "" . (($action == 'delete-all') ? ("
		{$this->lang->words['mod_opt_confirm_delete_all']}<br /><br />
		<em>{$this->lang->words['mod_shouts_to_delete']}:&nbsp;&nbsp;&nbsp;{$data['total']}</em>
	") : ("")) . "" . (($action == 'ban') ? ("
		{$this->lang->words['mod_opt_confirm_ban']}
	") : ("")) . "" . (($action == 'ban24') ? ("
		{$this->lang->words['mod_opt_confirm_ban']}
	") : ("")) . "" . (($action == 'ban48') ? ("
		{$this->lang->words['mod_opt_confirm_ban']}
	") : ("")) . "" . (($action == 'unban') ? ("
		{$this->lang->words['mod_opt_confirm_unban']}
	") : ("")) . "" . (($action == 'delmod') ? ("
		{$this->lang->words['mod_opt_confirm_delmod']}
	") : ("")) . "
	<br /><br />
	<div class=\"short\">
		<input type=\"button\" id=\"confirm_option_yes\" value=\"{$this->lang->words['yes']}\" class=\"input_submit\" />&nbsp;&nbsp;&nbsp;
		<input type=\"button\" id=\"confirm_option_no\" value=\"{$this->lang->words['no']}\" class=\"ipsButton_secondary\" />
	</div>") : ("" . (($action == 'editHistory') ? ("
		{$this->lang->words['mod_edit_history_text']}
		<br /><br />
		<table class=\"ipb_table\">
			<tr class=\"header\">
				<th style=\"width: 75%;\">{$this->lang->words['member_name']}</th>
				<th class=\"short\" style=\"width: 25%;\">{$this->lang->words['date']}</th>
			</tr>
			".$this->__f__8519c9ae51b555b6419ffd07b442c749($action,$data)."		</table>
		<br />
	") : ("" . (($this->registry->getClass('shoutboxLibrary')->global_on) ? ("
			<h3>{$this->lang->words['mod_opt_edit']}</h3>
			" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(editShout) : '' ) . "") : ("")) . "
		<div class=\"ipsPad\">
			" . $editor->show('shout_msg', array( 'height' => 100 ), "$data[text]")  . "
			<div class=\"short ipsPad\">
				<input type=\"button\" id=\"mod_edit_shout_confirm\" value=\"{$this->lang->words['mod_edit_shout']}\" class=\"input_submit\" />
				<input type=\"button\" id=\"mod_edit_shout_clear\" value=\"{$this->lang->words['clear']}\" class=\"ipsButton_secondary\" />
				<input type=\"button\" id=\"mod_edit_shout_cancel\" value=\"{$this->lang->words['cancel']}\" class=\"ipsButton_secondary\" />
			</div>
		</div>")) . "")) . "";
return $IPBHTML;
}


function __f__8519c9ae51b555b6419ffd07b442c749($action='',$data=array())
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $data as $edit )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
				<tr class=\"{$edit['class']}\">
					<td valign=\"top\">
						<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$edit['member_id']}", "public",'' ), "", "" ) . "\">{$edit['_name']}</a><br />
						<span class=\"desc\">{$this->lang->words['ip']}: <em>{$edit['ip']}</em></span>
					</td>
					<td class=\"short\" valign=\"middle\">{$edit['_date']}</td>
				</tr>
			
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- no_mods --*/
function no_mods() {
$IPBHTML = "";
$IPBHTML .= "<div id='shoutbox-no-mods-message' class='message error short block_wrap'>{$this->lang->words['error_no_mods']}</div>";
return $IPBHTML;
}

/* -- no_shouts --*/
function no_shouts() {
$IPBHTML = "";
$IPBHTML .= "<div id='shoutbox-no-shouts-message' class='message error short block_wrap'>{$this->lang->words['error_no_shouts']}</div>";
return $IPBHTML;
}

/* -- popupInlineError --*/
function popupInlineError($area='app') {
$IPBHTML = "";
$IPBHTML .= "<div id='shoutbox-inline-error-{$area}' class='message error block_wrap' style='display:none;'></div>";
return $IPBHTML;
}

/* -- popupModerator --*/
function popupModerator($d='',$m='',$t='', $own=0) {
$IPBHTML = "";
$IPBHTML .= "<h3>{$this->lang->words['mod_panel_title']}</h3>
<div class=\"ipsBox table_wrap\">
	<div class=\"ipsBox_container\">
		" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(moderator) : '' ) . "
		<table class=\"ipb_table\">
			<tr>
				<td valign='top' width='25%'>
					" . (($t == 'shout') ? ("
						<strong>{$this->lang->words['shout_number']} #{$d['s_id']}</strong><br />
						<strong>{$this->lang->words['by']}</strong>: {$d['shouted_by']}
					") : ("
						<strong>{$this->lang->words['member']}</strong>:
						<br />
						<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$d['member_id']}", "public",'' ), "{$d['members_seo_name']}", "showuser" ) . "' title='{$d['members_display_name']}'>{$d['_members_display_name']}</a>
					")) . "
				</td>
				<td valign='top' width='75%'>
					{$this->lang->words['mod_opts_welcome']}
				</td>
			</tr>
			<tr>
				<td colspan='2'>
					<span class='shoutbox_text'>{$d['s_message']}</span>
				</td>
			</tr>
			<tr  class='row2'>
				<td class='altrow' colspan='2'>
					<strong id='shoutbox-popup-status'>{$this->lang->words['mod_opts_start_status']}</strong>
				</td>
			</tr>
			<tr class='row2'>
				<td id='shoutbox-popup-content' colspan='2'>
					{$this->lang->words['mod_opts_start_content']}
				</td>
			</tr>
			<tr>
				<td colspan='2'>
					<ul class=\"topic_buttons\">
						" . (($m['m_edit_shouts'] && $t == 'shout') ? ("<li id='edit_shout' class='clickable'><img src=\"{$this->settings['img_url']}/comment_edit.png\" alt=\"{$this->lang->words['macro__edit']}\" /> {$this->lang->words['mod_opt_edit']}</li>
							<li id='editHistory_shout' class='clickable'" . ((!is_array($d['s_edit_history']) || !count($d['s_edit_history'])) ? (" style='display:none;'") : ("")) . ">" . $this->registry->getClass('output')->getReplacement("display_name") . " {$this->lang->words['mod_opt_edit_history']}</li>") : ("")) . "" . ((( ($m['m_delete_shouts'] && $own) || $m['m_delete_shouts_user'] ) && $t == 'shout') ? ("
							<li id='delete_shout' class='clickable'><img src=\"{$this->settings['img_url']}/comment_delete.png\" alt=\"{$this->lang->words['macro__delete']}\" /> {$this->lang->words['mod_opt_delete']}</li>
						") : ("")) . "" . ((($m['m_delete_shouts'] && $own) || $m['m_delete_shouts_user']) ? ("
							<li id='deleteAll_shout' class='clickable'><img src=\"{$this->settings['img_url']}/comment_delete.png\" alt=\"{$this->lang->words['macro__delete']}\" /> {$this->lang->words['mod_opt_delete_all']}</li>
						") : ("")) . "" . (($d['member_id'] > 0 && $this->memberData['member_id'] != $d['member_id']) ? ("" . (($m['m_ban_members']) ? ("<li id='ban_shout' class='clickable'" . (($d['_cache']['shoutbox_banned']) ? (" style='display:none;'") : ("")) . ">" . $this->registry->getClass('output')->getReplacement("spammer_on") . " {$this->lang->words['mod_opt_ban']}</li>") : ("")) . "" . (($m['m_ban_members']) ? ("<li id='ban24_shout' class='clickable'" . (($d['_cache']['shoutbox_banned']) ? (" style='display:none;'") : ("")) . ">" . $this->registry->getClass('output')->getReplacement("spammer_on") . " {$this->lang->words['mod_opt_ban_24']}</li>") : ("")) . "" . (($m['m_ban_members']) ? ("<li id='ban48_shout' class='clickable'" . (($d['_cache']['shoutbox_banned']) ? (" style='display:none;'") : ("")) . ">" . $this->registry->getClass('output')->getReplacement("spammer_on") . " {$this->lang->words['mod_opt_ban_48']}</li>") : ("")) . "" . (($m['m_unban_members']) ? ("<li id='unban_shout' class='clickable'" . ((!$d['_cache']['shoutbox_banned']) ? (" style='display:none;'") : ("")) . ">" . $this->registry->getClass('output')->getReplacement("spammer_off") . " {$this->lang->words['mod_opt_unban']}</li>") : ("")) . "" . (($m['m_remove_mods'] && $d['_is_a_mod'] && $d['member_id'] > 0) ? ("
							<li id='removeMod_shout' class='clickable'><img src=\"{$this->settings['img_url']}/cross.png\" title=\"{$this->lang->words['macro__deletedmsg']}\" alt=\"*\" /> {$this->lang->words['mod_opt_delmod']}</li>
						") : ("")) . "") : ("")) . "
					</ul>
				</td>
			</tr>
		</table>
	</div>
</div>
<script type='text/javascript'>
" . (($t == 'shout') ? ("
	ipb.shoutbox.mod_shout_id = parseInt({$d['s_id']});
") : ("
	ipb.shoutbox.mod_member_id = parseInt({$d['member_id']});
")) . "
</script>";
return $IPBHTML;
}

/* -- popupMyPrefs --*/
function popupMyPrefs($d='') {
$IPBHTML = "";
$IPBHTML .= "<h3>{$this->lang->words['my_prefs_panel']}</h3>
<div class=\"ipsBox table_wrap\">
	<div class=\"ipsBox_container\">
		" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(myprefs) : '' ) . "
		<table class=\"ipb_table\">
			<tr>
				<td colspan=\"2\">
					{$this->lang->words['my_prefs_welcome']}
				</td>
			</tr>
			<tr class=\"row2\">
				<td class=\"altrow\" colspan=\"2\">
					<strong id=\"shoutbox-popup-status\">{$this->lang->words['my_prefs_loaded']}</strong>
				</td>
			</tr>
			<tr>
				<td style=\"width: 50%;\" class=\"short\">
					<strong>{$this->lang->words['my_prefs_gsb']}</strong>
					<br />
					" . (($d['global_shoutbox']) ? ("
						<label for=\"my_prefs_gsb_y\">{$this->lang->words['yes']}</label> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_gsb\" value=\"1\" id=\"my_prefs_gsb_y\" {$d['gsb_y']}/> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_gsb\" value=\"0\" id=\"my_prefs_gsb_n\" {$d['gsb_n']}/> <label for=\"my_prefs_gsb_n\">{$this->lang->words['no']}</label>
					") : ("<span class=\"shoutbox_disabled\">{$this->lang->words['global_shoutbox_off']}</span>
						<input type=\"hidden\" name=\"my_prefs_gsb\" value=\"" . (($d['gsb_y'] == 'checked') ? ("1") : ("0")) . "\" id=\"my_prefs_gsb_y\" />")) . "
				</td>
				<td style=\"width: 50%;\" class=\"short\">
					<strong>{$this->lang->words['my_prefs_ets']}</strong>
					<br />
					<label for=\"my_prefs_ets_y\">{$this->lang->words['yes']}</label> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_ets\" value=\"1\" id=\"my_prefs_ets_y\" {$d['ets_y']}/> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_ets\" value=\"0\" id=\"my_prefs_ets_n\" {$d['ets_n']}/> <label for=\"my_prefs_ets_n\">{$this->lang->words['no']}</label>
				</td>
			</tr>
			<tr>
				<td class=\"short\">
					<strong>{$this->lang->words['my_prefs_drb']}</strong>
					<br />
					<label for=\"my_prefs_drb_y\">{$this->lang->words['yes']}</label> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_drb\" value=\"1\" id=\"my_prefs_drb_y\" {$d['drb_y']}/> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_drb\" value=\"0\" id=\"my_prefs_drb_n\" {$d['drb_n']}/> <label for=\"my_prefs_drb_n\">{$this->lang->words['no']}</label>
				</td>
				<td class=\"short\">
					<strong>{$this->lang->words['my_prefs_eqc']}</strong>
					<br />
					<label for=\"my_prefs_eqc_y\">{$this->lang->words['yes']}</label> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_eqc\" value=\"1\" id=\"my_prefs_eqc_y\" {$d['eqc_y']}/> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_eqc\" value=\"0\" id=\"my_prefs_eqc_n\" {$d['eqc_n']}/> <label for=\"my_prefs_eqc_n\">{$this->lang->words['no']}</label>
				</td>
			</tr>
			<tr>
				<td class=\"short\">
					<strong>{$this->lang->words['my_prefs_sdo']}</strong>
					<br />
					<select name=\"my_prefs_sdo\" id=\"my_prefs_sdo\">
						<option value=''" . (($d['sdo'] == '') ? (" selected") : ("")) . ">{$this->lang->words['default']}</option>
						<option value='1'" . (($d['sdo'] == '1') ? (" selected") : ("")) . ">{$this->lang->words['olderNewer']}</option>
						<option value='2'" . (($d['sdo'] == '2') ? (" selected") : ("")) . ">{$this->lang->words['newerOlder']}</option>
					</select>
					<br />
					<span class='error'>{$this->lang->words['refreshMe']}</span>
				</td>
				<td class=\"short\">
					<strong>{$this->lang->words['my_prefs_snd']}</strong>
					<br />
					<label for=\"my_prefs_snd_y\">{$this->lang->words['yes']}</label> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_snd\" value=\"1\" id=\"my_prefs_snd_y\" {$d['snd_y']}/> <input type=\"radio\" class=\"input_radio\" name=\"my_prefs_snd\" value=\"0\" id=\"my_prefs_snd_n\" {$d['snd_n']}/> <label for=\"my_prefs_snd_n\">{$this->lang->words['no']}</label>
				</td>
			</tr>

			<tr>
				<td class=\"short\" colspan=\"2\">
					<input type=\"button\" id=\"myprefs_save\" value=\"{$this->lang->words['save_prefs']}\" class=\"input_submit\" />
					<input type=\"button\" id=\"myprefs_restore\" value=\"{$this->lang->words['restore_default']}\" class=\"ipsButton_secondary\" />
				</td>
			</tr>
		</table>
	</div>
</div>";
return $IPBHTML;
}

/* -- popupMyPrefsUpdate --*/
function popupMyPrefsUpdate($d='') {
$IPBHTML = "";
$IPBHTML .= "<script type='text/javascript'>
ipb.shoutbox.my_prefs = { {$d['prefs']} };
ipb.shoutbox.popupUpdateStatus(\"{$d['msg']}\", true);
ipb.shoutbox.updateJSPreferences();
</script>";
return $IPBHTML;
}

/* -- popupWrapper --*/
function popupWrapper($output) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox', $this->_funcHooks['popupWrapper'] ) )
{
$count_dd98360471a9bed90d9a1ee8214966fe = is_array($this->functionData['popupWrapper']) ? count($this->functionData['popupWrapper']) : 0;
$this->functionData['popupWrapper'][$count_dd98360471a9bed90d9a1ee8214966fe]['output'] = $output;
}
$IPBHTML .= "" . (($this->caches['app_cache']['core']['app_long_version'] < 32007) ? ("<script type=\"text/javascript\">
	//<![CDATA[
		inACP				= false;
		ipb.vars['is_touch']		= " . (($this->registry->output->isLargeTouchDevice()) ? ("'large';") : ("" . (($this->registry->output->isSmallTouchDevice()) ? ("'small';") : ("false;")) . "")) . "
		ipb.vars['member_group']	= " . json_encode( array( 'g_mem_info' => $this->memberData['g_mem_info'] ) ) . "
	//]]>
	</script>") : ("")) . "
<div id=\"content\">
	{$output}
</div>";
return $IPBHTML;
}

/* -- shout_row --*/
function shout_row($d='',$can_edit=false,$ajax=false) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox', $this->_funcHooks['shout_row'] ) )
{
$count_1c75cbf8a8960a74d68f0794282bf040 = is_array($this->functionData['shout_row']) ? count($this->functionData['shout_row']) : 0;
$this->functionData['shout_row'][$count_1c75cbf8a8960a74d68f0794282bf040]['d'] = $d;
$this->functionData['shout_row'][$count_1c75cbf8a8960a74d68f0794282bf040]['can_edit'] = $can_edit;
$this->functionData['shout_row'][$count_1c75cbf8a8960a74d68f0794282bf040]['ajax'] = $ajax;
}
$IPBHTML .= "" . (($ajax==false) ? ("<tr class='row2' id='shout-{$d['_archive']}row-{$d['s_id']}'>") : ("")) . "" . (($this->settings['shoutbox_show_photos']) ? ("<td style='width: 1%; white-space: nowrap;'>{$d['photo']}</td>") : ("")) . "
	<td style='width: 1%; white-space: nowrap;'>
		" . (($this->settings['shoutbox_at_tag']) ? ("
			<a href=\"#\" class=\"at_member\" data-store=\"{$d['members_display_name']}\" title=\"{$this->lang->words['insert_name']}\">@</a>&nbsp;
		") : ("")) . "
		" . (($d['member_id']) ? ("" . IPSMember::makeProfileLink($d['_members_display_name'], $d['member_id'], $d['members_seo_name']) . "") : ("
			<abbr title=\"{$d['members_display_name']}\">{$d['_members_display_name']}</abbr>
		")) . "
	</td>
	" . (($this->settings['shoutbox_format_colon']) ? ("<td style='width: 1%; white-space: nowrap;'>:</td>") : ("")) . "
	<td style='width: 98%;'>
		<span class='right desc' title='{$d['_date']}'>({$d['s_date']})" . (($can_edit || ($this->registry->getClass('shoutboxLibrary')->moderator && $this->registry->getClass('shoutboxLibrary')->checkModeratorPerm('edit_shouts', true))) ? ("&nbsp;<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "#edit{$d['s_id']}' onclick='return ipb.shoutbox.editShout({$d['s_id']})' title='{$this->lang->words['mod_opt_edit']}'><img src=\"{$this->settings['img_url']}/comment_edit.png\" alt=\"{$this->lang->words['macro__edit']}\" /></a>") : ("")) . "" . (($this->registry->getClass('shoutboxLibrary')->moderator) ? ("&nbsp;<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "#shout{$d['s_id']}' onclick='return ipb.shoutbox.modOptsLoadShout({$d['s_id']})' title='{$this->lang->words['mmenu_load_mod_opts']}'>" . $this->registry->getClass('output')->getReplacement("edit_folder") . "</a>") : ("")) . "" . ((!$this->registry->shoutboxLibrary->checkModeratorPerm('delete_shouts', true) && $this->memberData['g_shoutbox_delete_own'] && $d['member_id'] == $this->memberData['member_id']) ? ("&nbsp;<a class=\"deleteMyShout\" id=\"delete_{$d['s_id']}\" href=\"#\" title=\"{$this->lang->words['mod_opt_delete']}\"><img src=\"{$this->settings['img_url']}/delete.png\" alt=\"\" /></a>") : ("")) . "</span>
		" . (($d['_ignored'] == 1) ? ("
			<span id='unhide_shout_{$d['s_id']}' class='desc'>{$this->lang->words['ignored_shouter']} <a href='#shout{$d['s_id']}' onclick='return ipb.shoutbox.showHiddenShout({$d['s_id']})' title='{$this->lang->words['ignored_shouter_view']}'>{$this->lang->words['ignored_shouter_view']}</a></span>
			<span id='hidden_shout_{$d['s_id']}' class='shoutbox_text' style='display:none'>{$d['s_message']}</span>
		") : ("
			<span class='shoutbox_text'>{$d['s_message']}</span>
		")) . "
	</td>
" . (($ajax==false) ? ("</tr>") : ("")) . "";
return $IPBHTML;
}

/* -- shout_row_sidebar --*/
function shout_row_sidebar($d='',$can_edit=false,$ajax=false) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox', $this->_funcHooks['shout_row_sidebar'] ) )
{
$count_796c0d96d313115b8e2415c16a646588 = is_array($this->functionData['shout_row_sidebar']) ? count($this->functionData['shout_row_sidebar']) : 0;
$this->functionData['shout_row_sidebar'][$count_796c0d96d313115b8e2415c16a646588]['d'] = $d;
$this->functionData['shout_row_sidebar'][$count_796c0d96d313115b8e2415c16a646588]['can_edit'] = $can_edit;
$this->functionData['shout_row_sidebar'][$count_796c0d96d313115b8e2415c16a646588]['ajax'] = $ajax;
}
$IPBHTML .= "" . (($ajax==false) ? ("<tr class='row1' id='shout-{$d['_archive']}row-{$d['s_id']}'>") : ("")) . "
	<td align='top' class='sidebar_shout'>
		<div class='sidebar_shout_div'>
			" . (($this->settings['shoutbox_show_photos']) ? ("{$d['photo']}&nbsp;") : ("")) . "
			" . (($this->settings['shoutbox_at_tag']) ? ("
				&nbsp;<a href=\"#\" class=\"at_member\" data-store=\"{$d['members_display_name']}\" title=\"{$this->lang->words['insert_name']}\">@</a>&nbsp;
			") : ("")) . "
			" . (($d['member_id']) ? ("" . IPSMember::makeProfileLink($d['_members_display_name'], $d['member_id'], $d['members_seo_name']) . "") : ("
				<abbr title=\"{$d['members_display_name']}\">{$d['_members_display_name']}</abbr>
			")) . "&nbsp;-&nbsp;<span class='desc' title='{$d['_date']}'>({$d['s_date']})" . (($can_edit || ($this->registry->getClass('shoutboxLibrary')->moderator && $this->registry->getClass('shoutboxLibrary')->checkModeratorPerm('edit_shouts',true))) ? ("&nbsp;<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "#edit{$d['s_id']}' onclick='return ipb.shoutbox.editShout({$d['s_id']})' title='{$this->lang->words['mod_opt_edit']}'><img src=\"{$this->settings['img_url']}/comment_edit.png\" alt=\"{$this->lang->words['macro__edit']}\" /></a>") : ("")) . "" . (($this->registry->getClass('shoutboxLibrary')->moderator) ? ("&nbsp;<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=shoutbox", "public",'' ), "false", "" ) . "#shout{$d['s_id']}' onclick='return ipb.shoutbox.modOptsLoadShout({$d['s_id']})' title='{$this->lang->words['mmenu_load_mod_opts']}'>" . $this->registry->getClass('output')->getReplacement("edit_folder") . "</a>") : ("")) . "" . ((!$this->registry->shoutboxLibrary->checkModeratorPerm('delete_shouts', true) && $this->memberData['g_shoutbox_delete_own'] && $d['member_id'] == $this->memberData['member_id']) ? ("&nbsp;<a class=\"deleteMyShout\" id=\"delete_{$d['s_id']}\" href=\"#\" title=\"{$this->lang->words['mod_opt_delete']}\"><img src=\"{$this->settings['img_url']}/delete.png\" alt=\"\" /></a>") : ("")) . "</span>
		</div>
		<div style='padding: 5px;'>
			" . (($d['_ignored'] == 1) ? ("
				<span id='unhide_shout_{$d['s_id']}' class='desc'>{$this->lang->words['ignored_shouter']} <a href='#shout{$d['s_id']}' onclick='return ipb.shoutbox.showHiddenShout({$d['s_id']})' title='{$this->lang->words['ignored_shouter_view']}'>{$this->lang->words['ignored_shouter_view']}</a></span>
				<span id='hidden_shout_{$d['s_id']}' class='shoutbox_text' style='display:none'>{$d['s_message']}</span>
			") : ("
				<span class='shoutbox_text'>{$d['s_message']}</span>
			")) . "
		</div>
	</td>
" . (($ajax==false) ? ("</tr>") : ("")) . "";
return $IPBHTML;
}

/* -- shoutbox --*/
function shoutbox($data='', $stats) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_shoutbox', $this->_funcHooks['shoutbox'] ) )
{
$count_d4019661bc528aec76f0b2ff89bb32b7 = is_array($this->functionData['shoutbox']) ? count($this->functionData['shoutbox']) : 0;
$this->functionData['shoutbox'][$count_d4019661bc528aec76f0b2ff89bb32b7]['data'] = $data;
$this->functionData['shoutbox'][$count_d4019661bc528aec76f0b2ff89bb32b7]['stats'] = $stats;
}

$pluginEditorHook = IPSLib::loadLibrary( IPS_ROOT_PATH . 'sources/classes/editor/composite.php', 'classes_editor_composite' );
	$editor = new $pluginEditorHook();
$IPBHTML .= "<!--- ShoutBoxJsLoader --->
" . ( method_exists( $this->registry->getClass('output')->getTemplate('editors'), 'editorLoadJs' ) ? $this->registry->getClass('output')->getTemplate('editors')->editorLoadJs($data) : '' ) . "
<h3 id='category_shoutbox' class='maintitle'>
	{$this->settings['shoutbox_title']}
	" . (($this->settings['shoutbox_popup'] && $this->request['do'] != 'popup') ? ("
		<a href=\"#\" id=\"shoutbox-popup-button\" title=\"{$this->lang->words['open_popup']}\">
			<img src=\"{$this->settings['img_url']}/shoutbox/popup.png\" alt=\"{$this->lang->words['open_popup']}\" />
		</a>
	") : ("")) . "
</h3>
<div id='shoutbox-wrapper' class='ipsBox table_wrap'><div class='ipsBox_container'>
	<table class='ipb_table shoutbox_table'>
		<tr class='header'>
			<th scope='col'>
				" . (($this->memberData['g_shoutbox_use'] && $this->memberData['g_shoutbox_view_archive']) ? ("
					<div id='shoutbox-archive-link' class='right'>[ <a href='#' id='load-shoutbox-archive'>{$this->lang->words['archive']}</a> ]</div>
				") : ("")) . "
				{$this->lang->words['latest_shouts']}
			</th>
		</tr>
		{$data['announcement']}
		<tr class='row1'>
			<td id='shoutbox-shouts-td' valign='top' class='altrow'>
				{$data['nomods']}
				{$data['noshouts']}
				<div id='shoutbox-shouts' style='height:{$data['shout_height']}px;overflow:auto;'>
					<table id='shoutbox-shouts-table'>
						<tbody>
							{$data['shouts']}
						</tbody>
					</table>
				</div>
				<div id=\"shouts-resizer\"></div>
				" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'popupInlineError' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->popupInlineError(app) : '' ) . "
			</td>
		</tr>
		" . (($this->memberData['g_shoutbox_use']) ? ("
			<tr class='row1'>
				<td class='short' class='altrow'>
					" . $editor->show('shout_msg', array( 'height' => 100 ), "")  . "
				</td>
			</tr>
			<tr class='row2'>
			  	<td class='altrow short'>
					<input type='button' id='shoutbox-submit-button' value='{$this->lang->words['shout']}' class='input_submit'/>
					<input type='button' id='shoutbox-clear-button' value='{$this->lang->words['clear']}' class='input_submit alt'/>
					<input type='button' id='shoutbox-refresh-button' value='{$this->lang->words['refresh']}' class='input_submit alt'/>
					<input type='button' id='shoutbox-myprefs-button' value='{$this->lang->words['my_prefs']}' class='input_submit alt'/>
				</td>
			</tr>
		") : ("")) . "
	</table>
</div></div>
" . ( method_exists( $this->registry->getClass('output')->getTemplate('shoutbox'), 'inactivePrompt' ) ? $this->registry->getClass('output')->getTemplate('shoutbox')->inactivePrompt() : '' ) . "
<br />
<div id='board_stats'>
	<ul class='ipsType_small ipsList_inline'>
		<li class='clear'>
			<span id=\"shoutbox-total-shouts\" class='value'>{$this->registry->getClass('shoutboxLibrary')->shout_total}</span>
			{$this->lang->words['total_shouts']}
		</li>
		" . (($this->memberData['member_id']) ? ("
			<li class='clear'>
				<span class='value'>{$stats['my_shouts_num']}</span>
				{$this->lang->words['my_shouts']}
			</li>
		") : ("")) . "
		<li class='clear'>
			<span class='value'>" . (($stats['top_shouter_id']) ? ("{$stats['top_shouter_name']}" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'user_popup' ) ? $this->registry->getClass('output')->getTemplate('global')->user_popup($stats['top_shouter_id'], $stats['top_shouter_seo']) : '' ) . " ({$stats['top_shouts_num']})") : ("--")) . "</span>
			{$this->lang->words['top_shouter']}
		</li>
		<li class='clear'>
			<span class='value'>" . count($this->caches['shoutbox_mods']['groups']) . "</span>
			{$this->lang->words['total_mods_groups']}
		</li>
		<li class='clear'>
			<span class='value'>" . count($this->caches['shoutbox_mods']['members']) . "</span>
			{$this->lang->words['total_mods_members']}
		</li>
	</ul>
</div>
<div id='board_statistics' class='statistics clearfix'>
	<h4 class='statistics_head'>
		<div id='shoutbox-active-total' class='left'>{$stats['TOTAL']}</div>&nbsp;{$this->lang->words['active_users_text']} <span>{$this->lang->words['active_users']}</span><br />
		<span class='desc'><span id='shoutbox-active-member'>{$stats['MEMBERS']}</span> {$this->lang->words['members']}, " . (($this->caches['group_cache'][ $this->settings['guest_group'] ]['g_shoutbox_view']) ? ("<span id='shoutbox-active-guests'>{$stats['GUESTS']}</span> {$this->lang->words['guests']}, ") : ("")) . "<span id='shoutbox-active-anon'>{$stats['ANON']}</span> {$this->lang->words['anon_users']}</span>
	</h4>
	<p id='shoutbox-active-names'>
		" . ((count($stats['NAMES'])) ? ("" . implode( ", ", $stats['NAMES'] ) . "") : ("")) . "
	</p>
</div>
<script type='text/javascript'>
/* Setup global value */
ipb.shoutbox.shoutboxGLOBAL = false;
{$data['js']}
{$data['langs']}
if (ipb.textEditor.getEditor().CKEditor) { ipb.textEditor.getEditor().CKEditor.on('key', ipb.shoutbox.keypress_handler ); }
</script>";
return $IPBHTML;
}

/* -- shouts_ajax --*/
function shouts_ajax($d='') {
$IPBHTML = "";
$IPBHTML .= "{$d['shouts']}
<script type='text/javascript'>
{$d['sound']}
ipb.shoutbox.shouts_fade([{$d['ids']}]);
</script>";
return $IPBHTML;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>