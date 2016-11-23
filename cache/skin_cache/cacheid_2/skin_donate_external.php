<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 2               */
/* CACHE FILE: Generated: Tue, 05 Jan 2016 20:03:57 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_donate_external_2 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();
$this->_funcHooks['donateGraph'] = array('fixedGraphColor');
$this->_funcHooks['donationAmount'] = array('showFee','calculateFee','anonymous_amount');
$this->_funcHooks['donorName'] = array('donorName','donor','anonymous');
$this->_funcHooks['featuredGoalsSidebar'] = array('hasDescription','privateGoal','amount_dropdown','showDonateBox','makeDonationPerms','goal_row','hasgoals');
$this->_funcHooks['latestDonationsPortal'] = array('donation_row','hasdonations');
$this->_funcHooks['latestDonationsSidebar'] = array('donation_row','hasdonations');
$this->_funcHooks['profileList'] = array('has_note');
$this->_funcHooks['topDonorsSidebar'] = array('donation_row','hasdonations');
$this->_funcHooks['topicLink'] = array('showDonorLink');
$this->_funcHooks['totalStats'] = array('calculateFee','showTotalFees','donationsFull','showGoalStats','amount_dropdown','showDonateBox','makeDonationPerms');


}

/* -- donateGraph --*/
function donateGraph($percent='', $g_id, $width='90%', $height='12px') {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['donateGraph'] ) )
{
$count_4bdb2b3c60192c140f4f136bc0915e9e = is_array($this->functionData['donateGraph']) ? count($this->functionData['donateGraph']) : 0;
$this->functionData['donateGraph'][$count_4bdb2b3c60192c140f4f136bc0915e9e]['percent'] = $percent;
$this->functionData['donateGraph'][$count_4bdb2b3c60192c140f4f136bc0915e9e]['g_id'] = $g_id;
$this->functionData['donateGraph'][$count_4bdb2b3c60192c140f4f136bc0915e9e]['width'] = $width;
$this->functionData['donateGraph'][$count_4bdb2b3c60192c140f4f136bc0915e9e]['height'] = $height;
}

if( $percent >= 0 AND $percent <= 24.99 )
{
    $statusImg = "status1.png";
}
else if( $percent >= 25 AND $percent <= 49.99 )
{
    $statusImg = "status2.png";
}
else if( $percent >= 50 AND $percent <= 74.99 )
{
    $statusImg = "status3.png";
}
else if( $percent >= 75 )
{
    $statusImg = "status4.png";
}
$IPBHTML .= "<style type='text/css'>
#progress-container_{$g_id} {
  border: 1px solid #ccc; 
  width: {$width}; 
  height: {$height};
  margin: 0; 
  padding: 1px;
  background: white;

}
#progress-container_{$g_id} > div {
" . (($this->settings['dt_bar_bg']) ? ("
     background-color: {$this->settings['dt_bar_bg']};
") : ("
     background-color: #5C87C7;
     background-image: url({$this->settings['img_url']}/{$statusImg});
     background-repeat: no-repeat;
")) . "
     height: 100%;
}
</style>

<div id='progress-container_{$g_id}' title='{$percent}% {$this->lang->words['of_goal_reached']}'><div style='width: {$percent}%'></div></div>";
return $IPBHTML;
}

/* -- donationAmount --*/
function donationAmount($donation) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['donationAmount'] ) )
{
$count_3724d63518de5e03778954c1b10c2379 = is_array($this->functionData['donationAmount']) ? count($this->functionData['donationAmount']) : 0;
$this->functionData['donationAmount'][$count_3724d63518de5e03778954c1b10c2379]['donation'] = $donation;
}
$IPBHTML .= "" . ((!$donation['anon_amount'] && !$donation['g_private']) ? ("<span " . (($this->settings['dt_include_fees']) ? ("data-tooltip=\"{$donation['c_symbol']} " . $this->registry->getClass('class_localization')->formatNumber( $donation['fees'], 2 ) . " {$this->lang->words['fee']}\"") : ("")) . ">{$donation['c_symbol']} " . (($this->settings['dt_include_fees']) ? ("" . $this->registry->getClass('class_localization')->formatNumber( $donation['amount']-$donation['fees'], 2 ) . "") : ("" . $this->registry->getClass('class_localization')->formatNumber( $donation['amount'], 2 ) . "")) . "</span>") : ("--")) . "";
return $IPBHTML;
}

/* -- donorName --*/
function donorName($r=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['donorName'] ) )
{
$count_020286d2892d9a8656d146e0f2cad67e = is_array($this->functionData['donorName']) ? count($this->functionData['donorName']) : 0;
$this->functionData['donorName'][$count_020286d2892d9a8656d146e0f2cad67e]['r'] = $r;
}
$IPBHTML .= "" . ((!$r['anon']) ? ("" . (($r['member_id'] AND $r['member_name']) ? ("
<a hovercard-ref=\"member\" hovercard-id=\"{$r['member_id']}\" class=\"_hovertrigger url fn\" href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$r['member_id']}", "public",'' ), "{$r['member_seo_name']}", "showuser" ) . "' title='{$this->lang->words['view_profile']}'>{$r['member_name']}</a>
") : ("" . (($r['member_name']) ? ("
{$r['member_name']}
") : ("
<i>{$this->lang->words['offline_donation']}</i>
")) . "")) . "") : ("

<i>{$this->lang->words['anonymous']}</i>

")) . "";
return $IPBHTML;
}

/* -- featuredGoalsSidebar --*/
function featuredGoalsSidebar($goals=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['featuredGoalsSidebar'] ) )
{
$count_b7b4ceb27a93ebc678b8095a1f894c5d = is_array($this->functionData['featuredGoalsSidebar']) ? count($this->functionData['featuredGoalsSidebar']) : 0;
$this->functionData['featuredGoalsSidebar'][$count_b7b4ceb27a93ebc678b8095a1f894c5d]['goals'] = $goals;
}
$IPBHTML .= "<div class='ipsSideBlock'>
	<h3>{$this->lang->words['featured_donation_goals']}</h3>
        <div class='_sbcollapsable'>
	<ul class='ipsList_inline'>
		" . ((is_array( $goals ) && count( $goals )) ? ("
			".$this->__f__a287d55ce234912bb3dd5c8b2ef957f6($goals)."		") : ("")) . "
	</ul>
        </div>
</div>";
return $IPBHTML;
}


function __f__3b2c602eb568de960918ea2b7bb569a1($goals=array(),$r='')
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( explode(",", $this->settings['dt_amounts'] ) as $value )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
    <option value=\"{$value}\">{$value}</option>
    
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

function __f__a287d55ce234912bb3dd5c8b2ef957f6($goals=array())
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $goals as $r )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
				<li class='clearfix'>
<div class='list_content ipsPad_half'>
<h2><a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=donate&amp;module=display&amp;section=donations&amp;do=view_goal&amp;id={$r['g_id']}", "public",'' ), "{$r['seo_name']}", "view_goal" ) . "'>{$r['g_name']}</a></h2>
" . (($r['g_desc']) ? ("<p>{$r['g_desc']}</p>") : ("")) . "

" . ((!$r['g_private']) ? ("<br />" . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donateGraph' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donateGraph($r['status'], $r['g_id']) : '' ) . "
<span class='ipsType_smaller desc lighter'>{$r['status']}% {$this->lang->words['complete']} - {$r['c_symbol']}{$r['g_received']} {$this->lang->words['of_this']} {$r['c_symbol']}{$r['g_amount']} {$this->lang->words['goal_reached']}</span><br />") : ("")) . "

" . (($this->memberData['g_dt_donate']) ? ("" . (($this->settings['dt_disable_completed'] && ( $this->caches['donate_cache']['total_donations'] + $this->caches['donate_cache']['total_fees'] ) >= $this->caches['donate_cache']['total_goals']) ? (" 
     &nbsp;
") : ("<br /><form action='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=donate&amp;module=display&amp;section=display&amp;do=donate&amp;goal={$r['g_id']}", "public",'' ), "", "" ) . "' method=\"post\">
 
    " . (($this->settings['dt_amounts']) ? ("
    <select name='amount'>
    ".$this->__f__3b2c602eb568de960918ea2b7bb569a1($goals,$r)."    </select>
    ") : ("
    <input type='text' id='enter_amount2' name='amount' class='input_text' size='4' />
    <script type='text/javascript'>
    $('enter_amount2').defaultize( \"5.00\" );
    </script>
    ")) . "
    
    <input type='submit' class='input_submit' value='{$this->lang->words['donate']}' />
    </form>")) . "") : ("")) . "
</div>
				</li>
			
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- latestDonationsPortal --*/
function latestDonationsPortal($donations=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['latestDonationsPortal'] ) )
{
$count_06c1c6f3566e5b40b9358f1cc876d67e = is_array($this->functionData['latestDonationsPortal']) ? count($this->functionData['latestDonationsPortal']) : 0;
$this->functionData['latestDonationsPortal'][$count_06c1c6f3566e5b40b9358f1cc876d67e]['donations'] = $donations;
}
$IPBHTML .= "<div class='ipsSideBlock'>
	<h3>{$this->lang->words['latest_donations']}</h3>
        <div class='_sbcollapsable'>
	<ul class='ipsList'>
		" . ((is_array( $donations ) && count( $donations )) ? ("
			".$this->__f__37c6634ec31d0253fd35c67c4295ceb6($donations)."		") : ("")) . "
	</ul>
        </div>
</div>";
return $IPBHTML;
}


function __f__37c6634ec31d0253fd35c67c4295ceb6($donations=array())
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $donations as $r )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
				<li class='clearfix'>
<div class='list_content ipsPad_half'>
" . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donorName' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donorName($r) : '' ) . " ( " . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donationAmount' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donationAmount($r) : '' ) . " )<br />

<span class='date'>" . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($r['date'],"long", 0)) . "</span>
</div>
				</li>
			
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- latestDonationsSidebar --*/
function latestDonationsSidebar($donations=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['latestDonationsSidebar'] ) )
{
$count_a56cdba33ffcd0f66c66df6226df9a6b = is_array($this->functionData['latestDonationsSidebar']) ? count($this->functionData['latestDonationsSidebar']) : 0;
$this->functionData['latestDonationsSidebar'][$count_a56cdba33ffcd0f66c66df6226df9a6b]['donations'] = $donations;
}
$IPBHTML .= "<div class='ipsSideBlock'>
	<h3>{$this->lang->words['latest_donations']}</h3>
        <div class='_sbcollapsable'>
	<ul class='ipsList_withminiphoto'>
		" . ((is_array( $donations ) && count( $donations )) ? ("
			".$this->__f__8c53f6ed417527d672be3ecc8d19db7d($donations)."		") : ("")) . "
	</ul>
        </div>
</div>";
return $IPBHTML;
}


function __f__8c53f6ed417527d672be3ecc8d19db7d($donations=array())
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $donations as $r )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
				<li class='clearfix'>

<a href='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "showuser={$r['member_id']}", "public",'' ), "{$r['members_seo_name']}", "showuser" ) . "' title='{$this->lang->words['view_profile']}' class='ipsUserPhotoLink left'><img src='{$r['pp_mini_photo']}' alt=\"{$r['members_display_name']}{$this->lang->words['users_photo']}\" class='ipsUserPhoto ipsUserPhoto_mini' /></a>

<div class='list_content'>
" . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donorName' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donorName($r) : '' ) . " ( " . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donationAmount' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donationAmount($r) : '' ) . " )<br />

<p class=\"desc ipsType_smaller\">" . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($r['date'],"long", 0)) . "</p>
</div>
				</li>
			
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- profileList --*/
function profileList($data=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['profileList'] ) )
{
$count_f9238fd5331efa5fc421d22cfa94f5d0 = is_array($this->functionData['profileList']) ? count($this->functionData['profileList']) : 0;
$this->functionData['profileList'][$count_f9238fd5331efa5fc421d22cfa94f5d0]['data'] = $data;
}

if ( ! isset( $this->registry->templateStriping['cat_row'] ) ) {
$this->registry->templateStriping['cat_row'] = array( FALSE, "row1","row2 altrow");
}
$IPBHTML .= "<h3 class='maintitle'>{$this->lang->words['member_donations']}</h3>
<div class='ipsBox'>
<div class='ipsBox_container'>

<table class=\"ipb_table\">
<tr class='header hide'>
<th scope='col'>{$this->lang->words['donor_name']}</th>
<th scope='col'>{$this->lang->words['donation_note']}</th>
<th scope='col' class='short'>{$this->lang->words['donation_date']}</th>
<th scope='col' class='short'>{$this->lang->words['amount']}</th>
</tr>".$this->__f__5fa5482ce589de5063f45ddeb11d67f0($data)."</table>

</div>
</div>";
return $IPBHTML;
}


function __f__5fa5482ce589de5063f45ddeb11d67f0($data=array())
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $data as $a => $r )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "

<tr class='" .  IPSLib::next( $this->registry->templateStriping["cat_row"] ) . "'>
	<td class='altrow'>" . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donorName' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donorName($r) : '' ) . "</td>
<td class='altrow'>" . (($r['note']) ? ("{$r['note']}") : ("<i>{$this->lang->words['no_note']}</i>")) . "</td>
<td class='short'>" . IPSText::htmlspecialchars($this->registry->getClass('class_localization')->getDate($r['date'],"long", 0)) . "</td>
<td class='altrow short'><strong>" . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donationAmount' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donationAmount($r) : '' ) . "</strong></td>	
</tr>

";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- topDonorsSidebar --*/
function topDonorsSidebar($topDonors=array()) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['topDonorsSidebar'] ) )
{
$count_f522023a47dc9387f9434274c3430f82 = is_array($this->functionData['topDonorsSidebar']) ? count($this->functionData['topDonorsSidebar']) : 0;
$this->functionData['topDonorsSidebar'][$count_f522023a47dc9387f9434274c3430f82]['topDonors'] = $topDonors;
}
$IPBHTML .= "<div class='ipsSideBlock'>
	<h3>{$this->lang->words['top_donors']}</h3>
        <div class='_sbcollapsable'>
	<ul class='ipsList_inline'>
		" . ((is_array( $topDonors ) && count( $topDonors )) ? ("
			".$this->__f__131869c311bc120d1aa332570ca93024($topDonors)."		") : ("")) . "
	</ul>
        </div>
</div>";
return $IPBHTML;
}


function __f__131869c311bc120d1aa332570ca93024($topDonors=array())
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( $topDonors as $r )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
				<li>{$r['suffix']}  " . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donorName' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donorName($r) : '' ) . "</li>
			
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- topicLink --*/
function topicLink($author) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['topicLink'] ) )
{
$count_d2199916398050fbb5059bc2814921b5 = is_array($this->functionData['topicLink']) ? count($this->functionData['topicLink']) : 0;
$this->functionData['topicLink'][$count_d2199916398050fbb5059bc2814921b5]['author'] = $author;
}
$IPBHTML .= "" . (($author['donate_donations'] > 0) ? ("<br />
<a class='ipsBadge ipsBadge_green'href=\"" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=donate&amp;module=display&amp;section=donations&amp;do=view_donations&amp;member_id={$author['member_id']}", "public",'' ), "view_donations", "view_donations" ) . "\" title='" . $this->registry->getClass('class_localization')->formatNumber( $author['donate_donations'] ) . " {$this->lang->words['member_donations']}'>{$this->lang->words['donator']}</a><br /><br />
") : ("")) . "";
return $IPBHTML;
}

/* -- totalStats --*/
function totalStats($stats) {
$IPBHTML = "";
if( IPSLib::locationHasHooks( 'skin_donate_external', $this->_funcHooks['totalStats'] ) )
{
$count_da89bdcfc91d87a71b322d512ce537ec = is_array($this->functionData['totalStats']) ? count($this->functionData['totalStats']) : 0;
$this->functionData['totalStats'][$count_da89bdcfc91d87a71b322d512ce537ec]['stats'] = $stats;
}
$IPBHTML .= "<div class='ipsSideBlock'>
	<h3>{$this->lang->words['donation_statistics']}</h3>
        <div class='_sbcollapsable'>
{$this->lang->words['total_donation_amount']} - <strong>{$stats['currency_symbol']}" . (($this->settings['dt_include_fees']) ? ("" . $this->registry->getClass('class_localization')->formatNumber( $stats['total_donations']-$stats['total_fees'], 2 ) . "") : ("" . $this->registry->getClass('class_localization')->formatNumber( $stats['total_donations'], 2 ) . "")) . "</strong><br />
" . (($this->settings['dt_include_fees']) ? ("
{$this->lang->words['total_fees']} - <strong>{$stats['currency_symbol']}" . $this->registry->getClass('class_localization')->formatNumber( $stats['total_fees'], 2 ) . "</strong><br />
") : ("")) . "
" . (($stats['total_goals']) ? ("{$this->lang->words['total_goal_amount']} - <strong>{$stats['currency_symbol']}" . $this->registry->getClass('class_localization')->formatNumber( $stats['total_goals'], 2 ) . "</strong><br /><br />
{$this->lang->words['still_needed']} - <strong>" . (($stats['still_needed'] < 0) ? ("--") : ("{$stats['currency_symbol']}" . $this->registry->getClass('class_localization')->formatNumber( $stats['still_needed'], 2 ) . "")) . "</strong><br /><br />
 " . ( method_exists( $this->registry->getClass('output')->getTemplate('donate_external'), 'donateGraph' ) ? $this->registry->getClass('output')->getTemplate('donate_external')->donateGraph($stats['status'], $goal['g_id'], '95%', '50px') : '' ) . "") : ("")) . "

" . (($this->memberData['g_dt_donate']) ? ("<br /><form action='" . $this->registry->getClass('output')->formatUrl( $this->registry->getClass('output')->buildUrl( "app=donate&amp;module=display&amp;section=display&amp;do=donate", "public",'' ), "", "" ) . "' method=\"post\">

" . (($this->settings['dt_disable_completed'] && ( $this->caches['donate_cache']['total_donations'] + $this->caches['donate_cache']['total_fees'] ) >= $this->caches['donate_cache']['total_goals']) ? (" 
     <strong>{$this->lang->words['goal_total_met']}</strong>
") : ("" . (($this->settings['dt_amounts']) ? ("
    <select name='amount'>
    ".$this->__f__2caaf7cabb9c24578d8b843575ce29d0($stats)."    </select>
    ") : ("
    <input type='text' id='enter_amount' name='amount' class='input_text' size='4' />
    <script type='text/javascript'>
    $('enter_amount').defaultize( \"5.00\" );
    </script>
    ")) . "
    
    <input type='submit' class='input_submit' value='{$this->lang->words['donate']}' />")) . "

</form>") : ("")) . "
        </div>
</div>";
return $IPBHTML;
}


function __f__2caaf7cabb9c24578d8b843575ce29d0($stats)
{
	$_ips___x_retval = '';
	$__iteratorCount = 0;
	foreach( explode(",", $this->settings['dt_amounts'] ) as $value )
	{
		
		$__iteratorCount++;
		$_ips___x_retval .= "
    <option value=\"{$value}\">{$value}</option>
    
";
	}
	$_ips___x_retval .= '';
	unset( $__iteratorCount );
	return $_ips___x_retval;
}

/* -- viewDonateInfo --*/
function viewDonateInfo() {
$IPBHTML = "";
$IPBHTML .= "" . (($this->request['module']=='ajax') ? ("
    <h3>{$this->lang->words['donation_information']}</h3>
") : ("
    <h3 class='maintitle'>{$this->lang->words['donation_information']}</h3>
")) . "
<div class='ipsBox table_wrap'>
<div class='ipsBox_container ipsPad_half'>
     {$this->lang->words['dt_donation_details']}
</div>
</div>";
return $IPBHTML;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>