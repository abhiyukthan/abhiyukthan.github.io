<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 2               */
/* CACHE FILE: Generated: Tue, 05 Jan 2016 20:03:57 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_login_2 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['showLogInForm'] = array('referer','haswindowslive','hasFacebook','hasTwitter','showAlternate','anonymous');


}

/* -- ajax__inlineLogInForm --*/
function ajax__inlineLogInForm() {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- errors --*/
function errors($data="") {
$IPBHTML = "";
$IPBHTML .= "<div class='row message error'>
	{$data}
</div>";
return $IPBHTML;
}

/* -- loginCaptcha --*/
function loginCaptcha($html="") {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- loginCaptchaInline --*/
function loginCaptchaInline($html="") {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- showLogInForm --*/
function showLogInForm($message="",$referer="",$extra_form="", $login_methods=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_login', $this->_funcHooks['showLogInForm'] ) )
{
$count_a78ee4769943eb74dab85e9dd8893a58 = is_array($this->functionData['showLogInForm']) ? count($this->functionData['showLogInForm']) : 0;
$this->functionData['showLogInForm'][$count_a78ee4769943eb74dab85e9dd8893a58]['message'] = $message;
$this->functionData['showLogInForm'][$count_a78ee4769943eb74dab85e9dd8893a58]['referer'] = $referer;
$this->functionData['showLogInForm'][$count_a78ee4769943eb74dab85e9dd8893a58]['extra_form'] = $extra_form;
$this->functionData['showLogInForm'][$count_a78ee4769943eb74dab85e9dd8893a58]['login_methods'] = $login_methods;
}
$IPBHTML .= "<form action=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process", "public",'' ), "", "" ) . "\" method=\"post\" id='login'>
<input type='hidden' name='auth_key' value='{$this->member->form_hash}' />
	" . (($referer) ? ("
		<input type=\"hidden\" name=\"referer\" value=\"{$referer}\" />
	") : ("")) . "
	<h2>{$this->lang->words['log_in']}</h2>
		<div class='ipsForm_vertical'>
		
		
		" . ((( $this->request['show'] == 'live' && in_array( 'live', $login_methods ) )) ? ("
			<div class='ipsField'>
				<label class='ipsField_title'>" . $this->registry->getClass('output')->getReplacement("live_small") . " {$this->lang->words['sign_in_winlive']}</label>
				<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process&amp;use_live=1&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "'>" . $this->registry->getClass('output')->getReplacement("live_large") . "</a> <a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;do=process&amp;use_live=1&amp;auth_key={$this->member->form_hash}", "public",'' ), "", "" ) . "'>{$this->lang->words['signin_with_live']}</a>
			</div>
		") : ("<div class='ipsField'>
				<label for='ips_username' class='ipsField_title'>{$this->lang->words['enter_name']}</label>
				<input id='username' type='text' class='input_text' name='ips_username' size='30' />
			</div>
			<div class='ipsField'>
				<label for='ips_password' class='ipsField_title'>{$this->lang->words['enter_pass']}</label>
				<input id='password' type='password' class='input_text' name='ips_password' size='30' />
			</div>
			
			<div class='ipsField'>
				" . ((IPSLib::loginMethod_enabled('live')) ? ("
					<p>" . $this->registry->getClass('output')->getReplacement("live_small") . " {$this->lang->words['have_msnlive']} <a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=core&amp;module=global&amp;section=login&amp;show=live", "public",'' ), "", "" ) . "'>{$this->lang->words['sign_in_here']}</a></p><br />
				") : ("")) . "
				" . ((IPSLib::loginMethod_enabled('facebook')) ? ("
					<p><a href=\"{$this->settings['_original_base_url']}/interface/facebook/index.php?_reg=1&amp;mobile=true\"><img src=\"{$this->settings['img_url']}/facebook_login.png\" alt=\"\" /></a></p><br />
				") : ("")) . "
				" . ((IPSLib::loginMethod_enabled('twitter')) ? ("
					<p><a href=\"{$this->settings['_original_base_url']}/interface/twitter/index.php?_reg=1&amp;mobile=true\"><img src=\"{$this->settings['img_url']}/twitter_login.png\" alt=\"\" /></a></p>
				") : ("")) . "
			</div>")) . "
		
		<h3>{$this->lang->words['sign_in_options']}</h3>
		<div class='ipsField ipsField_checkbox'>
			<input type='checkbox' id='remember' checked='checked' name='rememberMe' value='1' class='input_check' />
			<p class='ipsField_content'>
				<label for='remember'>{$this->lang->words['rememberme']}</label><br />
				<span class='desc'>{$this->lang->words['notrecommended']}</span>
			</p>
		</div>	
			" . ((!$this->settings['disable_anonymous']) ? ("
				<div class='ipsField ipsField_checkbox'>
					<input type='checkbox' id='invisible' name='anonymous' value='1' class='input_check' />
					<p class='ipsField_content'>
						<label for='invisible'>{$this->lang->words['form_invisible']}</label><br />
						<span class='desc'>{$this->lang->words['anon_name']}</span>
					</p>
				</div>
			") : ("")) . "
		</div>
		
		<div class='submit'>
			<input type='submit' class='button' value='{$this->lang->words['sign_in_button']}' />
		</div>
	</div>
</form>";
return $IPBHTML;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>