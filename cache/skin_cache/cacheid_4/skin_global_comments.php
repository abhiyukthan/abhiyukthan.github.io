<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 4               */
/* CACHE FILE: Generated: Tue, 05 Jan 2016 20:04:02 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_global_comments_4 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['comment'] = array('canEditNoPost','commentQueued','authorwarn','userIgnoredLang','hasauthormemid','hasauthormidclose','commentignored','moderateCheckbox','enableRep','hasQ','canReply','canEdit','canHide','canApprove','canDelete','hasReport','commentinitignored');
$this->_funcHooks['commentHidden'] = array('canEditNoPost','moderateCheckbox','canUnhide','canDelete');
$this->_funcHooks['commentsList'] = array('comments','comments_top','comments_bottom','hasCaptcha','guestName','allow_comments');
$this->_funcHooks['form'] = array('comment_errors','isEditing','guest_captcha');


}

/* -- comment --*/
function comment($r, $parent, $settings) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_global_comments', $this->_funcHooks['comment'] ) )
{
$count_6c5b352f398c17d9a69f31701004d233 = is_array($this->functionData['comment']) ? count($this->functionData['comment']) : 0;
$this->functionData['comment'][$count_6c5b352f398c17d9a69f31701004d233]['r'] = $r;
$this->functionData['comment'][$count_6c5b352f398c17d9a69f31701004d233]['parent'] = $parent;
$this->functionData['comment'][$count_6c5b352f398c17d9a69f31701004d233]['settings'] = $settings;
}

// Adjust author name as needed
if( empty($r['author']['member_id']) && !empty($r['author']['comment_author_name']) )
{
	$r['author']['members_display_name'] = $r['author']['comment_author_name'];
}
$IPBHTML .= "" . ((!$this->hasEditJs AND !$parent['_canComment'] AND $r['comment']['_canEdit']) ? ("
	" . ( method_exists( $this->registry->getClass('output')->getTemplate('global_comments'), 'getEditJs' ) ? $this->registry->getClass('output')->getTemplate('global_comments')->getEditJs() : '' ) . "
") : ("")) . "
<a id='comment_{$r['comment']['comment_id']}'></a>
<div data-commentid='{$r['comment']['comment_id']}' class='ipsComment clearfix " . ((!$r['comment']['comment_approved']) ? ("moderated") : ("")) . "' id='comment_id_{$r['comment']['comment_id']}'>
	<div class='ipsComment_author'>
		<div class='right'>
			" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'userSmallPhoto' ) ? $this->registry->getClass('output')->getTemplate('global')->userSmallPhoto(array_merge( $r['author'], array( '_customClass' => 'ipsUserPhoto_mini' ) )) : '' ) . "
		</div>
		<div class='clear'>
			" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'userHoverCard' ) ? $this->registry->getClass('output')->getTemplate('global')->userHoverCard($r['author']) : '' ) . "<br />
		</div>
		<span class='post_id'>
			<a rel='bookmark' class='desc lighter ipsType_smaller' href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=findComment&amp;comment_id={$r['comment']['comment_id']}", "public",'' ), "", "" ) . "' title='{$this->lang->words['comment_permalink']}'>" . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($r['comment']['comment_date'],"short", 0)) . "</a>
		</span>
		" . (($r['author']['show_warn']) ? ("<br />
			" . (($options['wl_id']) ? ("
				<img src='{$this->settings['img_url']}/warn.png' class='clickable' onclick='warningPopup( this, {$options['wl_id']} )' title='{$this->lang->words['warnings_issued']}' />
			") : ("")) . "
			<a class='desc lighter ipsType_smaller blend_links' href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=members&amp;module=profile&amp;section=warnings&amp;member={$r['author']['member_id']}&amp;from_app={$settings['thisApp']}&amp;from_id1={$settings['fromApp']}&amp;from_id2={$parent['parent_id']}-{$r['comment']['comment_id']}", "public",'' ), "", "" ) . "' id='warn_link_{$r['comment']['comment_id']}_{$r['author']['member_id']}' title='{$this->lang->words['warn_view_history']}'>" . sprintf( $this->lang->words['warn_status'], $r['author']['warn_level'] ) . "</a>") : ("")) . "
	</div>
	<div id='comment_{$r['comment']['comment_id']}' class='ipsComment_comment'>
		" . (($r['comment']['_ignored'] || $r['comment']['_repignored']) ? ("<div class='post_ignore'>
				" . (($r['comment']['_repignored'] == 1) ? ("{$this->lang->words['comment_ignored_rep']}") : ("{$this->lang->words['ignored_comments_not']}")) . " " . (($r['author']['member_id']) ? ("<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$r['author']['member_id']}", "public",'' ), "", "" ) . "'>") : ("")) . "{$r['author']['members_display_name']}" . (($r['author']['member_id']) ? ("</a>") : ("")) . ". <a href='#entry{$r['comment']['comment_id']}' title=\"{$this->lang->words['ignored_comments_not']} {$r['author']['members_display_name']}\" style='display: none' id='unhide_post_{$r['comment']['comment_id']}'>{$this->lang->words['rep_view_anyway']}</a>
			</div>") : ("")) . "
		<div class='comment_content'>{$r['comment']['comment_text']}</div>
		
		<ul class='ipsComment_controls ipsList_inline ipsType_smaller'>
			" . (($parent['_canModerate']) ? ("
				<li class='right'>&nbsp;&nbsp;<input class=\"ipsComment_mod\" type='checkbox' name='' id='mod_comment_id_{$r['comment']['comment_id']}' data-status='{$r['comment']['comment_approved']}' /></li>
			") : ("")) . "
			" . (($settings['enableRep']) ? ("
				<li class='right'>
					" . ( method_exists( $this->registry->getClass('output')->getTemplate('global_other'), 'repButtons' ) ? $this->registry->getClass('output')->getTemplate('global_other')->repButtons($r['author'], array_merge( array( 'primaryId' => $r['comment']['comment_id'], 'domLikeStripId' => 'like_post_' . $r['comment']['comment_id'], 'domCountId' => 'rep_comment_' . $r['comment']['comment_id'], 'app' => $settings['repApp'] ? $settings['repApp'] : $settings['thisApp'], 'type' => $settings['repType'], 'likeFormatted' => $r['comment']['like']['formatted'] ), $r['comment'] )) : '' ) . "
				</li>
			") : ("")) . "
			" . (($r['comment']['_canReply']) ? ("<li><a href='{$this->settings['this_url']}" . ((strstr($this->settings['this_url'], '?')) ? ("&amp;") : ("?")) . "_rcid[]={$r['comment']['comment_id']}#fastreply' title=\"{$this->lang->words['reply_to_comment']}\" id='reply_comment_{$r['comment']['comment_id']}' class='ipsButton_secondary reply_comment'>{$this->lang->words['comment_reply']}</a></li>") : ("")) . "
			" . (($r['comment']['_canEdit']) ? ("
				<li>
					<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=showEdit&amp;comment_id={$r['comment']['comment_id']}", "public",'' ), "", "" ) . "\" id='edit_comment_{$r['comment']['comment_id']}' class='edit_comment'>{$this->lang->words['edit_link']}</a>
				</li>
			") : ("")) . "
			" . (($r['comment']['comment_approved'] == 1 and $r['comment']['_canHide']) ? ("
				<li><a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=hide&amp;comment_id={$r['comment']['comment_id']}&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' title='{$this->lang->words['hide_link']}' id='hide_comment_{$r['comment']['comment_id']}' class='hide_comment'>{$this->lang->words['hide_link']}</a></li>
			") : ("")) . "
			" . (($r['comment']['comment_approved'] == 0 and $r['comment']['_canApprove']) ? ("
				<li><a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=approve&amp;comment_id={$r['comment']['comment_id']}&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' title='{$this->lang->words['approve_link']}'>{$this->lang->words['approve_link']}</a></li>
			") : ("")) . "
			" . (($r['comment']['_canDelete']) ? ("
				<li>
					<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=delete&amp;comment_id={$r['comment']['comment_id']}&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' id='delete_comment_{$r['comment']['comment_id']}' class='delete_comment'  title='{$this->lang->words['delete_comment']}' data-confirmaction=\"true\">{$this->lang->words['delete_link']}</a>
				</li>
			") : ("")) . "
			" . (($r['comment']['urls-report']) ? ("
				<li>
					<a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$r['comment']['urls-report']}&amp;st={$this->request['st']}", "public",'' ), "", "" ) . "\">{$this->lang->words['report_link']}</a>
				</li>
			") : ("")) . "
		</ul>
		
	</div>
</div>
" . (($r['comment']['_ignored'] || $r['comment']['_repignored']) ? ("
	<script type='text/javascript'>
		ipb.comments.setCommentHidden( {$r['comment']['comment_id']} );
	</script>
") : ("")) . "";
return $IPBHTML;
}

/* -- commentHidden --*/
function commentHidden($r, $parent, $settings) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_global_comments', $this->_funcHooks['commentHidden'] ) )
{
$count_d93e8e9c2e6672755d380aa306c8160e = is_array($this->functionData['commentHidden']) ? count($this->functionData['commentHidden']) : 0;
$this->functionData['commentHidden'][$count_d93e8e9c2e6672755d380aa306c8160e]['r'] = $r;
$this->functionData['commentHidden'][$count_d93e8e9c2e6672755d380aa306c8160e]['parent'] = $parent;
$this->functionData['commentHidden'][$count_d93e8e9c2e6672755d380aa306c8160e]['settings'] = $settings;
}

// Adjust author name as needed
if( empty($r['author']['member_id']) && !empty($r['author']['comment_author_name']) )
{
	$r['author']['members_display_name'] = $r['author']['comment_author_name'];
}
$IPBHTML .= "" . ((!$this->hasEditJs AND !$parent['_canComment'] AND $r['comment']['_canEdit']) ? ("
	" . ( method_exists( $this->registry->getClass('output')->getTemplate('global_comments'), 'getEditJs' ) ? $this->registry->getClass('output')->getTemplate('global_comments')->getEditJs() : '' ) . "
") : ("")) . "
<a id='comment_{$r['comment']['comment_id']}'></a>
<div data-commentid='{$r['comment']['comment_id']}' class='ipsComment clearfix moderated' id='comment_id_{$r['comment']['comment_id']}'>
	<div class='ipsComment_author'>
		" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'userHoverCard' ) ? $this->registry->getClass('output')->getTemplate('global')->userHoverCard($r['author']) : '' ) . "<br />
	</div>
	<div id='comment_{$r['comment']['comment_id']}' class='ipsComment_comment'>
		<div class='comment_content' id='hidden_text_{$r['comment']['comment_id']}'>
			{$this->lang->words['post_deleted_by']} <a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$r['sD']['sdl_obj_member_id']}", "public",'' ), "{$r['sD']['member']['members_seo_name']}", "showuser" ) . "'>{$r['sD']['member']['members_display_name']}</a> {$this->lang->words['on']} " . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($r['sD']['sdl_obj_date'],"long", 0)) . ".
			<p class='desc'>" . (($r['sD']['sdl_obj_reason']) ? ("{$r['sD']['sdl_obj_reason']}") : ("{$this->lang->words['no_reason_given']}")) . "</p>
		</div>
		<div class='comment_content' id='comment_content_{$r['comment']['comment_id']}' style='display:none'>
			{$r['comment']['comment_text']}
		</div>
		<ul class='ipsComment_controls ipsList_inline ipsType_smaller'>
			" . (($parent['_canModerate']) ? ("
				<li class='right'>&nbsp;&nbsp;<input class=\"ipsComment_mod\" type='checkbox' name='' id='mod_comment_id_{$r['comment']['comment_id']}' data-status='{$r['comment']['comment_approved']}' /></li>
			") : ("")) . "
			<li>
				<span class='clickable' onclick=\"$('hidden_text_{$r['comment']['comment_id']}').toggle();$('comment_content_{$r['comment']['comment_id']}').toggle();\">{$this->lang->words['comment_hidden_content']}</span>
			</li>
			" . (($r['comment']['_canUnhide']) ? ("
				<li><a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=unhide&amp;comment_id={$r['comment']['comment_id']}&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' title='{$this->lang->words['unhide_link']}'>{$this->lang->words['unhide_link']}</a></li>
			") : ("")) . "
			" . (($r['comment']['_canDelete']) ? ("
				<li>
					<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=delete&amp;comment_id={$r['comment']['comment_id']}&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' id='delete_comment_{$r['comment']['comment_id']}' class='delete_comment' title='{$this->lang->words['delete_comment']}' data-confirmaction=\"true\">{$this->lang->words['delete_link']}</a>
				</li>
			") : ("")) . "
		</ul>
	</div>
</div>";
return $IPBHTML;
}

/* -- commentsList --*/
function commentsList($comments, $settings, $pages, $parent, $preReply='') {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_global_comments', $this->_funcHooks['commentsList'] ) )
{
$count_8aa0e6a7aa40d578df87d05bb89cdf20 = is_array($this->functionData['commentsList']) ? count($this->functionData['commentsList']) : 0;
$this->functionData['commentsList'][$count_8aa0e6a7aa40d578df87d05bb89cdf20]['comments'] = $comments;
$this->functionData['commentsList'][$count_8aa0e6a7aa40d578df87d05bb89cdf20]['settings'] = $settings;
$this->functionData['commentsList'][$count_8aa0e6a7aa40d578df87d05bb89cdf20]['pages'] = $pages;
$this->functionData['commentsList'][$count_8aa0e6a7aa40d578df87d05bb89cdf20]['parent'] = $parent;
$this->functionData['commentsList'][$count_8aa0e6a7aa40d578df87d05bb89cdf20]['preReply'] = $preReply;
}

$pluginEditorHook = IPSLib::loadLibrary( IPS_ROOT_PATH . 'sources/classes/editor/composite.php', 'classes_editor_composite' );
	$editor = new $pluginEditorHook();
$IPBHTML .= "<script type='text/javascript'>
	ipb.templates['comment_moderation'] = new Template(\"<div id='comment_moderate_box' class='ipsFloatingAction' style='display: none'><span class='desc'>{$this->lang->words['comment_action_count']} </span><select name='modOptions' class='input_select' id='commentModAction'><option value='approve'>{$this->lang->words['approve_x_comments']}</option><option value='hide'>{$this->lang->words['hide_x_comments']}</option><option value='unhide'>{$this->lang->words['unhide_x_comments']}</option><option value='delete'>{$this->lang->words['delete_x_comments']}</option></select>&nbsp;&nbsp;<input type='button' class='input_submit' id='submitModAction' value='{$this->lang->words['comments_act_go']}' /></div>\");
	
	ipb.templates['comment_delete'] = new Template(\"<h3>{$this->lang->words['comm_confirm_delete']}</h3><div class='ipsPad ipsForm_center desc'>{$this->lang->words['comm_confirm_delete_desc']}<br /><br /><input type='button' class='input_submit' id='delPush' onclick='ipb.comments.deleteIt(event)' value='{$this->lang->words['del_comm_now']}' />\");
	
	ipb.templates['comment_hide'] = new Template(\"<form action='#{url}' method='post'><h3>{$this->lang->words['comm_confirm_hide']}</h3><div class='ipsPad ipsForm_center desc'>{$this->lang->words['comm_confirm_hide_desc']}<br /><br /><input type='text' name='reason' id='hidePop_reason' value='' class='input_text' style='width: 60%' /> <input type='submit' class='input_submit' value='{$this->lang->words['comm_confirm_hide']}' /></form>\");
</script>
" . $this->registry->getClass('output')->addJSModule("comments", "0" ) . "
<a id='commentsStart'></a>
" . (($pages) ? ("
	<div class='topic_controls'>
		{$pages}
	</div>
") : ("")) . "
<div class='ipsComment_wrap' id='comment_wrap'>
	".$this->__f__f5df12b17944f6b6f83c3099cc79a9f3($comments,$settings,$pages,$parent,$preReply)."</div>
" . (($pages) ? ("
	<div class='topic_controls'>
		{$pages}
	</div>
") : ("")) . "
" . (($parent['_canComment']) ? ("<br />
	<a id=\"fastreply\"></a>
	<div id='fast_reply' class='ipsComment_reply row2 ipsPad'>
		<form action=\"{$settings['formUrl']}\" method=\"post\">
			<input type=\"hidden\" name=\"auth_key\" value=\"{$this->member->form_hash}\" />
			<input type=\"hidden\" name=\"fromApp\" value=\"{$settings['fromApp']}\" />
			<input type=\"hidden\" name=\"app\" value=\"{$settings['formApp']}\" />
			<input type=\"hidden\" name=\"module\" value=\"{$settings['formModule']}\" />
			<input type=\"hidden\" name=\"section\" value=\"{$settings['formSection']}\" />
			<input type=\"hidden\" name=\"do\" value=\"add\" />
			<input type=\"hidden\" name=\"parentId\" value=\"{$parent['parent_id']}\" />
			<input type=\"hidden\" name=\"fast_reply_used\" value=\"1\" />
			<div class='ipsComment_reply_user_photo'>
				" . ( method_exists( $this->registry->getClass('output')->getTemplate('global'), 'userSmallPhoto' ) ? $this->registry->getClass('output')->getTemplate('global')->userSmallPhoto(array_merge( $this->memberData, array( '_customClass' => 'ipsUserPhoto_medium' ) )) : '' ) . "
			</div>
			<div id='commentReply' class='ipsComment_comment'>
				" . ((!$this->memberData['member_id']) ? ("<div id='commentName'>
						<label for='comment_name'>{$this->lang->words['yourname_captcha']}</label> <input type='text' id='comment_name' name='comment_name' class='input_text' />
						{$this->lang->words['or']} <a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login", "public",'' ), "", "" ) . "' title='{$this->lang->words['sign_in']}'>{$this->lang->words['sign_in']}</a>
					</div>
					" . (($settings['captcha']) ? ("
						<div id='commentCaptcha' style='display:none;'>
							{$settings['captcha']}
						</div>
					") : ("")) . "") : ("")) . "
				" . $editor->show('Post', array( 'type' => 'mini', 'minimize' => 1, 'autoSaveKey' => $settings['autoSaveKey'], 'warnInfo' => 'fastReply', 'editorName' => 'commentFastReply' ), "$preReply")  . "
				<br />
				" . ((!$this->memberData['unacknowledged_warnings'] and !$this->memberData['restrict_post']) ? ("
					<div id='commentButtons'>
						<input type='submit' name=\"submit\" class='input_submit' id='commentPost' value='{$this->lang->words['comment_button_post']}' tabindex='50' accesskey='s' />
					</div>
				") : ("")) . "
			</div>
		</form>
	</div>") : ("")) . "
<script type='text/javascript'>
	ipb.global.post_width			= 500;
	document.observe(\"dom:loaded\", function(){
		ipb.comments.parentId = " . intval( $parent['parent_id'] ) . ";
		ipb.comments.setData( " . json_encode( $settings ) . " );
	});
</script>";
return $IPBHTML;
}


function __f__f5df12b17944f6b6f83c3099cc79a9f3($comments, $settings, $pages, $parent, $preReply='')
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $comments as $id => $r )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
		" . (($r['comment']['_canView']) ? ("" . (($r['comment']['comment_approved'] == -1) ? ("
				" . ( method_exists( $this->registry->getClass('output')->getTemplate('global_comments'), 'commentHidden' ) ? $this->registry->getClass('output')->getTemplate('global_comments')->commentHidden($r, $parent, $settings) : '' ) . "
			") : ("
				" . ( method_exists( $this->registry->getClass('output')->getTemplate('global_comments'), 'comment' ) ? $this->registry->getClass('output')->getTemplate('global_comments')->comment($r, $parent, $settings) : '' ) . "
			")) . "") : ("")) . "
	
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- form --*/
function form($comment, $parent, $editor="", $settings, $errors="", $do='saveEdit') {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_global_comments', $this->_funcHooks['form'] ) )
{
$count_423019bab1d83a9ab4ec6a5ff454523e = is_array($this->functionData['form']) ? count($this->functionData['form']) : 0;
$this->functionData['form'][$count_423019bab1d83a9ab4ec6a5ff454523e]['comment'] = $comment;
$this->functionData['form'][$count_423019bab1d83a9ab4ec6a5ff454523e]['parent'] = $parent;
$this->functionData['form'][$count_423019bab1d83a9ab4ec6a5ff454523e]['editor'] = $editor;
$this->functionData['form'][$count_423019bab1d83a9ab4ec6a5ff454523e]['settings'] = $settings;
$this->functionData['form'][$count_423019bab1d83a9ab4ec6a5ff454523e]['errors'] = $errors;
$this->functionData['form'][$count_423019bab1d83a9ab4ec6a5ff454523e]['do'] = $do;
}
$IPBHTML .= "" . (($errors) ? ("
	<p class='message error'>{$errors}</p>
") : ("")) . "
<div class='post_form'>
	<form method=\"post\" action=\"{$settings['formAction']}\" name=\"REPLIER\">
		<input type=\"hidden\" name=\"auth_key\" value=\"{$this->member->form_hash}\" />
		<input type=\"hidden\" name=\"fromApp\" value=\"{$settings['fromApp']}\" />
		<input type=\"hidden\" name=\"app\" value=\"{$settings['formApp']}\" />
		<input type=\"hidden\" name=\"module\" value=\"{$settings['formModule']}\" />
		<input type=\"hidden\" name=\"section\" value=\"{$settings['formSection']}\" />
		<input type=\"hidden\" name=\"do\" value=\"saveEdit\" />
		<input type=\"hidden\" name=\"parentId\" value=\"{$parent['parent_id']}\" />
		<input type=\"hidden\" name=\"comment_id\" value=\"{$comment['comment']['comment_id']}\" />
		<input type=\"hidden\" name=\"auth_key\" value=\"{$this->member->form_hash}\" />
		<input type=\"hidden\" name=\"modcp\" value=\"{$this->request['modcp']}\" />
		
		<h3 class='maintitle'>
		" . (($do == 'saveEdit') ? ("
			{$this->lang->words['edit_comment']} {$parent['parent_title']}
		") : ("")) . "
		</h3>
		<div class='generic_bar'></div>
		
		" . ((!$this->memberData['member_id'] AND $this->settings['guest_captcha'] AND $this->settings['bot_antispam_type'] != 'none') ? ("
			<fieldset>
				<ul>
					<li class='field'>
						<label for=''>{$this->lang->words['guest_captcha']}</label>
					</li>
				</ul>
			</fieldset>
		") : ("")) . "
		
		<fieldset>
			{$editor}
		</fieldset>
		<fieldset class='submit'>
			<input type=\"submit\" name=\"submit\" value=\"{$this->lang->words['comment_save']}\" tabindex=\"0\" class=\"input_submit\" accesskey=\"s\" /> {$this->lang->words['or']} <a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "{$settings['baseUrl']}&amp;do=findComment&amp;comment_id={$comment['comment']['comment_id']}", "public",'' ), "", "" ) . "' class='cancel' title='{$this->lang->words['cancel']}'>{$this->lang->words['cancel']}</a>
		</fieldset>
	</form>
</div>";
return $IPBHTML;
}

/* -- getEditJs --*/
function getEditJs() {
$IPBHTML = "";

$pluginEditorHook = IPSLib::loadLibrary( IPS_ROOT_PATH . 'sources/classes/editor/composite.php', 'classes_editor_composite' );
$editor = new $pluginEditorHook();
$smilies	= $editor->fetchEmoticons( 20 );
$bypass		= $editor->getRteEnabled() ? 0 : 1;
$this->hasEditJs = true;
$IPBHTML .= "" . ( method_exists( $this->registry->getClass('output')->getTemplate('editors'), 'editorLoadJs' ) ? $this->registry->getClass('output')->getTemplate('editors')->editorLoadJs(array( 'bypassCKEditor' => $bypass, 'smilies' => $smilies )) : '' ) . "";
return $IPBHTML;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>