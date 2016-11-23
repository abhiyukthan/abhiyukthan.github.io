// Created by ipbforumskins.com

jQuery.noConflict();

jQuery(document).ready(function($){

	$('a[href=#top]').click(function(){
		$('html, body').animate({scrollTop:0}, 400);
        return false;
	});
	
	$(".forum_name").hover(function() {
		$(this).next(".forum_desc_pos").children(".forum_desc_con").stop()
		.animate({left: "0", opacity:1}, "fast")
		.css("display","block")
	}, function() {
		$(this).next(".forum_desc_pos").children(".forum_desc_con").stop()
		.animate({left: "10", opacity: 0}, "fast", function(){
			$(this).hide();
		})
	});
	
	$("#nav_search").click(function(){
		$("#toggle_background").slideUp();
		$("#toggle_search").slideToggle();
		$("#main_search").focus();
	});
	
	$("#nav_background").click(function(){
		$("#toggle_search").slideUp();
		$("#toggle_background").slideToggle();
	});

	$("#custom_background span").click(function(){
		$.cookie('custom_url',null,{ expires: -5, path: '/'});
		var bgid = $(this).attr("id");
		$.cookie('custombg',bgid,{ expires: 365, path: '/'});
		$("body").removeClass().addClass(bgid);
	});
	
	$("#custom_submit").click(function(){
		$.cookie('custombg',"bg_custom",{ expires: 365, path: '/'});
		var customurl = $("#custom_input").val();
		$.cookie('custom_url',customurl,{ expires: 365, path: '/'});
		$("<style type='text/css'>body.bg_custom, .bg_custom .forum_icon, .bg_custom .maintitle, .bg_custom #branding, .bg_custom #user_navigation ul#user_link_menucontent{ background-image: url(" + customurl + ")}</style>").appendTo("head");
		$("body").removeClass().addClass("bg_custom");
	});
		
	if ( ($.cookie('custombg') != null))	{
		$("body").addClass($.cookie('custombg'));
	}
	else{
		$("body").addClass("bg1");
	}
	
	if ( ($.cookie('custom_url') != null))	{
		$("<style type='text/css'>body.bg_custom, .bg_custom .forum_icon, .bg_custom .maintitle, .bg_custom #branding, .bg_custom #user_navigation ul#user_link_menucontent{ background-image: url(" + $.cookie('custom_url') + ")}</style>").appendTo("head");
		$("body").addClass("bg_custom");
	}
	
	$("#custom_input[placeholder]").focus(function() {
	  var input = $(this);
	  if (input.val() == input.attr("placeholder")) {
		input.val("");
		input.removeClass("placeholder");
	  }
	}).blur(function() {
	  var input = $(this);
	  if (input.val() == "" || input.val() == input.attr("placeholder")) {
		input.addClass("placeholder");
		input.val(input.attr("placeholder"));
	  }
	}).blur();

});