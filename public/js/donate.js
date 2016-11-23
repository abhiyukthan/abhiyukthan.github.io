var _donate = window.IPBoard;

_donate.prototype.donate = {
	
	init: function()
	{
		Debug.write("Initializing donate.js");
		
		document.observe("dom:loaded", function(){
			ipb.donate.initEvents();			
		
		});
	},
	initEvents: function()
	{      
		if( $('show_filter') )
		{
			$('show_filter').observe('click', ipb.donate.toggleCatFilter );
			$('filter_form').hide();
		}	   
       
        $('donate_info').observe('click', ipb.donate.viewDonateInfo);  	
        
		ipb.donate.acURL = ipb.vars['base_url'] + 'app=core&module=ajax&section=findnames&do=get-member-names&secure_key=' + ipb.vars['secure_hash'] + '&name=';
		
		if( $('members_display_name') )
		{
			ipb.donate.autoComplete = new ipb.Autocomplete( $('members_display_name'), { multibox: false, url: ipb.donate.acURL, templates: { wrap: ipb.templates['autocomplete_wrap'], item: ipb.templates['autocomplete_item'] } } );
		}
    },    
        
	viewDonateInfo: function(e)
	{		
		Event.stop(e);
        
		var _url = ipb.vars['base_url'] + '&app=donate&module=ajax&section=display&do=donate_info&secure_key=' + ipb.vars['secure_hash'];	
		vehicle_share = new ipb.Popup( 'donate_info', {type: 'pane', modal: false, w: '600px', h: '400px', ajaxURL: _url, hideAtStart: false, close: '.cancel' } );
		
	},
	toggleCatFilter: function(e)
	{
		if( $('filter_form') )
		{
			Effect.toggle( $('filter_form'), 'blind', {duration: 0.2} );
			Effect.toggle( $('show_filter'), 'blind', {duration: 0.2} );
		}
	}	 
    			
}
ipb.donate.init();