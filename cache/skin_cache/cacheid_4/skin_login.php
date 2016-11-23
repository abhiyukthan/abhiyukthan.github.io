<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 4               */
/* CACHE FILE: Generated: Tue, 05 Jan 2016 20:04:02 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_login_4 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['ajax__inlineLogInForm'] = array('registerUsingFb','twitterBox','haswindowslive','registerServices','anonymous','hasRedirect');
$this->_funcHooks['showLogInForm'] = array('extrafields','referer','facebook','twitterBox','haswindowslive','extraform','liveform','anonymous','privvy','toggleLive');


}

/* -- ajax__inlineLogInForm --*/
function ajax__inlineLogInForm() {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_login', $this->_funcHooks['ajax__inlineLogInForm'] ) )
{
$count_de71c923f5f50d278e31eb815a6ac8e4 = is_array($this->functionData['ajax__inlineLogInForm']) ? count($this->functionData['ajax__inlineLogInForm']) : 0;
}

$uses_name		= false;
	$uses_email		= false;
	$_redirect		= '';
	
	foreach( $this->cache->getCache('login_methods') as $method )
	{
		if( $method['login_user_id'] == 'username' or $method['login_user_id'] == 'either' )
		{
			$uses_name	= true;
		}
		
		if( $method['login_user_id'] == 'email' or $method['login_user_id'] == 'either' )
		{
			$uses_email	= true;
		}
		
		if( $method['login_login_url'] )
		{
			$_redirect	= $method['login_login_url'];
		}
	}
	if( $uses_name AND $uses_email )
	{
		$this->lang->words['enter_name']	= $this->lang->words['enter_name_and_email'];
	}
	else if( $uses_email )
	{
		$this->lang->words['enter_name']	= $this->lang->words['enter_useremail'];
	}
	else
	{
		$this->lang->words['enter_name']	= $this->lang->words['enter_username'];
	}
$IPBHTML .= "" . (($_redirect) ? ("
<script type='text/javascript'>
window.location = '{$_redirect}';
</script>
") : ("<div id='inline_login_form'>
	<form action=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process", "public",'' ), "", "" ) . "\" method=\"post\" id='login'>
		<input type='hidden' name='auth_key' value='{$this->member->form_hash}' />
		<input type=\"hidden\" name=\"referer\" value=\"" . str_replace( array( '<', '>', '(', ')' ), '-', my_getenv('HTTP_REFERER') ) . "\" />
		<h3>{$this->lang->words['log_in']}</h3>
		" . ((IPSLib::loginMethod_enabled('facebook') || IPSLib::loginMethod_enabled('twitter') || IPSLib::loginMethod_enabled('live')) ? ("<div class='ipsBox_notice'>
				<ul class='ipsList_inline'>
					" . ((IPSLib::loginMethod_enabled('facebook')) ? ("
						<li><a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;serviceClick=facebook", "public",'' ), "", "" ) . "\"><img src=\"{$this->settings['img_url']}/facebook_login.png\" alt=\"\" /></a></li>
					") : ("")) . "
					" . ((IPSLib::loginMethod_enabled('twitter')) ? ("
						<li><a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;serviceClick=twitter", "public",'' ), "", "" ) . "\"><img src=\"{$this->settings['img_url']}/twitter_login.png\" alt=\"\" /></a></li>
					") : ("")) . "
					" . ((IPSLib::loginMethod_enabled('live')) ? ("
						<li><a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process&amp;use_live=1&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' title='{$this->lang->words['use_live']}'>" . $this->registry->getClass('output')->getReplacement("live_small") . " {$this->lang->words['sign_in_winlive']}</a></li>
					") : ("")) . "
				</ul>
			</div>") : ("")) . "
		<br />
		<div class='ipsForm ipsForm_horizontal'>
			<fieldset>
				<ul>
					<li class='ipsField'>
						<div class='ipsField_content'>
							{$this->lang->words['register_prompt_1']} <a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=register", "public",'' ), "", "" ) . "\" title='{$this->lang->words['register_prompt_2']}'>{$this->lang->words['register_prompt_2']}</a>
						</div>
					</li>
					<li class='ipsField ipsField_primary'>
						<label for='ips_username' class='ipsField_title'>{$this->lang->words['enter_name']}</label>
						<div class='ipsField_content'>
							<input id='ips_username' type='text' class='input_text' name='ips_username' size='30' />
						</div>
					</li>
					<li class='ipsField ipsField_primary'>
						<label for='ips_password' class='ipsField_title'>{$this->lang->words['enter_pass']}</label>
						<div class='ipsField_content'>
							<input id='ips_password' type='password' class='input_text' name='ips_password' size='30' /><br />
							<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=lostpass", "public",'' ), "", "" ) . "' title='{$this->lang->words['retrieve_pw']}'>{$this->lang->words['login_forgotten_pass']}</a>
						</div>
					</li>
					<li class='ipsField ipsField_checkbox'>
						<input type='checkbox' id='inline_remember' checked='checked' name='rememberMe' value='1' class='input_check' />
						<div class='ipsField_content'>
							<label for='inline_remember'>
								<strong>{$this->lang->words['rememberme']}</strong><br />
								<span class='desc lighter'>{$this->lang->words['notrecommended']}</span>
							</label>
						</div>
					</li>
					" . ((!$this->settings['disable_anonymous']) ? ("
						<li class='ipsField ipsField_checkbox'>
							<input type='checkbox' id='inline_invisible' name='anonymous' value='1' class='input_check' />
							<div class='ipsField_content'>
								<label for='inline_invisible'>
									<strong>{$this->lang->words['form_invisible']}</strong><br />
									<span class='desc lighter'>{$this->lang->words['anon_name']}</span>
								</label>
							</div>
						</li>
					") : ("")) . "<!--hook.if.skin_login.ajax__inlineLogInForm.anonymous.post.endif-->
				</ul>
			</fieldset>
			<div class='ipsForm_submit ipsForm_center'>
				<input type='submit' class='ipsButton' value='{$this->lang->words['log_in']}' />
			</div>
		</div>
	</form>
</div>")) . "";
return $IPBHTML;
}

/* -- errors --*/
function errors($data="") {
$IPBHTML = "";
$IPBHTML .= "<p class='message error'>
	{$data}
</p>
<br /><br />";
return $IPBHTML;
}

/* -- loginCaptcha --*/
function loginCaptcha($html="") {
$IPBHTML = "";
$IPBHTML .= "<hr />
<div>
	<h3 class='bar'>{$this->lang->words['reg_step4_spam']}</h3>
	<div class=\"extra\" style=\"float:left;\">
		{$html}
	</div>
</div>";
return $IPBHTML;
}

/* -- loginCaptchaInline --*/
function loginCaptchaInline($html="") {
$IPBHTML = "";
$IPBHTML .= "</ul>
</fieldset>
{$html}
<fieldset><ul>

" . (($this->settings['bot_antispam_type'] == 'recaptcha') ? ("
	<script type=\"text/javascript\">
		$( 'captcha' ).down( '.ipsField_content' ).identify();
		Debug.write( $( 'captcha' ).down( '.ipsField_content' ).identify() );
		var RecaptchaOptions = { 
								lang : '{$this->settings['recaptcha_language']}',
								theme : '{$this->settings['recaptcha_theme']}'
								};
		Recaptcha.create( \"{$this->registry->class_captcha->public_key}\", $( 'captcha' ).down( '.ipsField_content' ).identify(), RecaptchaOptions );
	</script>
") : ("")) . "";
return $IPBHTML;
}

/* -- showLogInForm --*/
function showLogInForm($message="",$referer="",$extra_form="", $login_methods=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_login', $this->_funcHooks['showLogInForm'] ) )
{
$count_838cc34e614dd8d0383b72df17e02e06 = is_array($this->functionData['showLogInForm']) ? count($this->functionData['showLogInForm']) : 0;
$this->functionData['showLogInForm'][$count_838cc34e614dd8d0383b72df17e02e06]['message'] = $message;
$this->functionData['showLogInForm'][$count_838cc34e614dd8d0383b72df17e02e06]['referer'] = $referer;
$this->functionData['showLogInForm'][$count_838cc34e614dd8d0383b72df17e02e06]['extra_form'] = $extra_form;
$this->functionData['showLogInForm'][$count_838cc34e614dd8d0383b72df17e02e06]['login_methods'] = $login_methods;
}
$IPBHTML .= "" . $this->registry->getClass('output')->addJSModule("signin", "0" ) . "
<div id='login_form' class='clearfix'>
	<div id='member_login'>
		<h2 class='maintitle'>{$this->lang->words['log_in']}</h2>
		<form action=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process", "public",'' ), "", "" ) . "\" method=\"post\" id='login'>
			<input type='hidden' name='auth_key' value='{$this->member->form_hash}' />
			" . (($referer) ? ("<input type=\"hidden\" name=\"referer\" value=\"{$referer}\" />") : ("")) . "
			<div id='regular_signin'>
				<a id='_regularsignin'></a>
				<h3 class='bar'>{$this->lang->words['enter_name_and_pass']}</h3>
				<ul class='ipsForm ipsForm_vertical ipsPad_double left'>
					<li class='ipsField'>
						<label for='ips_username' class='ipsField_title'>{$this->lang->words['enter_name']}</label>
						<p class='ipsField_content'>
							<input id='ips_username' type='text' class='input_text' name='ips_username' size='50' tabindex='1' /><br />
							<span class='desc ipsType_smaller'>{$this->lang->words['register_prompt_1']} <a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=register", "public",'' ), "", "" ) . "' title='{$this->lang->words['register_prompt_2']}'>{$this->lang->words['register_prompt_2']}</a></span>
						</p>
					</li>
					<li class='ipsField'>
						<label for='ips_password' class='ipsField_title'>{$this->lang->words['enter_pass']}</label>
						<p class='ipsField_content'>
							<input id='ips_password' type='password' class='input_text' name='ips_password' size='50' tabindex='2' /><br />
							<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=lostpass", "public",'' ), "", "" ) . "' class='ipsType_smaller' title='{$this->lang->words['retrieve_pw']}'>{$this->lang->words['login_forgotten_pass']}</a>
						</p>
					</li>
				</ul>
				<div class='right ipsPad_double' id='other_signin'>
					<ul class='ipsList_data clear ipsType_small'>
						" . ((IPSLib::loginMethod_enabled('facebook')) ? ("
							<li><a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;serviceClick=facebook", "public",'' ), "", "" ) . "\" class='ipsButton_secondary fixed_width'><img src=\"{$this->settings['img_url']}/loginmethods/facebook.png\" alt=\"Facebook\" /> &nbsp; {$this->lang->words['have_facebook']}</a></li>
						") : ("")) . "
						" . ((IPSLib::loginMethod_enabled('twitter')) ? ("
							<li><a href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;serviceClick=twitter", "public",'' ), "", "" ) . "\" class='ipsButton_secondary fixed_width'><img src=\"{$this->settings['img_url']}/loginmethods/twitter.png\" alt=\"Twitter\" /> &nbsp; {$this->lang->words['have_twitter']}</a></li>
						") : ("")) . "
						" . ((IPSLib::loginMethod_enabled('live')) ? ("
							<li><a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process&amp;use_live=1&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' title='{$this->lang->words['use_live']}' class='ipsButton_secondary fixed_width'><img src=\"{$this->settings['img_url']}/loginmethods/windows.png\" alt=\"Windows Live\" /> &nbsp; {$this->lang->words['sign_in_winlive']}</a></li>
						") : ("")) . "
						" . ((is_array($extra_form) AND count($extra_form)) ? ("
							".$this->__f__5c542432b0444706bf88364daa17e3b8($message,$referer,$extra_form,$login_methods)."						") : ("")) . "
					</ul>
				</div>
			</div>
			" . ((IPSLib::loginMethod_enabled('live')) ? ("
				<div id='live_signin'>
					<a id='_live'></a>
					<h3 class='bar'>{$this->lang->words['sign_in_winlive']}</h3>
					<div class='ipsPad_double'>
						<br />
						<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process&amp;use_live=1&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "' class='ipsButton'>" . $this->registry->getClass('output')->getReplacement("live_large") . " &nbsp;&nbsp;{$this->lang->words['signin_with_live']}</a>
					</div>
					<p class='extra'><a href='#_regularsignin' title='{$this->lang->words['regular_signin']}' id='live_close'>{$this->lang->words['use_regular']}</a></p>
				</div>
			") : ("")) . "<!--hook.if.skin_login.showLogInForm.liveform.post.endif-->
			<hr />
			<fieldset id='signin_options'>
				<legend>{$this->lang->words['sign_in_options']}</legend>
				<ul class='ipsForm ipsForm_vertical ipsPad_double'>
					<li class='ipsField ipsField_checkbox clearfix'>
						<input type='checkbox' id='remember' checked='checked' name='rememberMe' value='1' class='input_check' tabindex='3' />
						<p class='ipsField_content'>
							<label for='remember'>{$this->lang->words['rememberme']}</label><br />
							<span class='desc lighter'>{$this->lang->words['notrecommended']}</span>
						</p>
					</li>
					" . ((!$this->settings['disable_anonymous']) ? ("
						<li class='ipsField ipsField_checkbox clearfix'>
							<input type='checkbox' id='invisible' name='anonymous' value='1' class='input_check' tabindex='4' />
							<p class='ipsField_content'>
								<label for='invisible'>{$this->lang->words['form_invisible']}</label><br />
								<span class='desc lighter'>{$this->lang->words['anon_name']}</span>
							</p>
						</li>
					") : ("")) . "
					" . (($this->settings['priv_title']) ? ("
					<li class='ipsPad_top ipsForm_center desc ipsType_smaller'>
						<a rel=\"nofollow\" href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=privacy", "public",'' ), "false", "privacy" ) . "'>{$this->settings['priv_title']}</a>
					</li>
					") : ("")) . "
				</ul>
			</fieldset>
			<fieldset class='submit'>
				<input type='submit' class='input_submit' value='{$this->lang->words['sign_in_button']}' tabindex='5' /> {$this->lang->words['or']} <a href='{$this->settings['board_url']}' title='{$this->lang->words['cancel']}' class='cancel'>{$this->lang->words['cancel']}</a>
			</fieldset>
		</form>
	</div>
</div>
" . (($this->request['serviceClick'] == 'live') ? ("
<script type='text/javascript'>
document.observe(\"dom:loaded\", function(e){ ipb.signin.toggleLive(e); });
</script>
") : ("")) . "";
return $IPBHTML;
}


function __f__5c542432b0444706bf88364daa17e3b8($message="",$referer="",$extra_form="", $login_methods=array())
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $extra_form as $form_fields )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
								{$form_fields}
							
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