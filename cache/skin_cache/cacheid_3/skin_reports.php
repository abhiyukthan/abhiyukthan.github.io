<?php
/*--------------------------------------------------*/
/* FILE GENERATED BY INVISION POWER BOARD 3         */
/* CACHE FILE: Skin set id: 3               */
/* CACHE FILE: Generated: Tue, 05 Jan 2016 20:03:59 GMT */
/* DO NOT EDIT DIRECTLY - THE CHANGES WILL NOT BE   */
/* WRITTEN TO THE DATABASE AUTOMATICALLY            */
/*--------------------------------------------------*/

class skin_reports_3 extends skinMaster{

/**
* Construct
*/
function __construct( ipsRegistry $registry )
{
	parent::__construct( $registry );
	

$this->_funcHooks = array();


}

/* -- basicReportForm --*/
function basicReportForm($name="", $url="", $extra_data="") {
$IPBHTML = "";
$IPBHTML .= "<postingForm>
	<action><![CDATA[{$this->settings['base_url']}app=core&amp;module=reports&amp;rcom={$this->request['rcom']}&amp;send=1]]></action>
	<formHash><![CDATA[{$this->member->form_hash}]]></formHash>
	<topicID>{$this->request['tid']}</topicID>
	<postID>{$this->request['pid']}</postID>
	<forumID>{$this->request['fid']}</forumID>
	</postingForm>";
return $IPBHTML;
}

/* -- reportsIndex --*/
function reportsIndex($reports=array(), $acts="", $pages="", $statuses=array()) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- statusIcon --*/
function statusIcon($img, $width, $height) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}

/* -- viewReport --*/
function viewReport($options=array(), $reports=array(), $comments=array()) {
$IPBHTML = "";
$IPBHTML .= "<!--no data in this master skin-->";
return $IPBHTML;
}


}


/*--------------------------------------------------*/
/* END OF FILE                                      */
/*--------------------------------------------------*/

?>