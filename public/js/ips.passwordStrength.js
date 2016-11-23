/**
 * 
 */


var _pwdStrength = window.IPBoard;

_pwdStrength.prototype.pwdStrength = 
{
	oneLcScore: 			( ipb.vars['pwm_oneLcScore'] 			|| 1 ),
	oneUcScore: 			( ipb.vars['pwm_oneUcScore'] 			|| 5 ),
	oneNumScore: 			( ipb.vars['pwm_oneNumScore'] 			|| 5 ),
	threeNumScore: 			( ipb.vars['pwm_threeNumScore'] 		|| 5 ),
	oneScScore: 			( ipb.vars['pwm_oneScScore'] 			|| 5 ),
	twoScScore: 			( ipb.vars['pwm_twoScScore'] 			|| 5 ),
	mixedLettersScore: 		( ipb.vars['pwm_mixedLettersScore'] 	|| 5 ),
	mixedNumbersScore: 		( ipb.vars['pwm_mixedNumbersScore'] 	|| 5 ),
	bigComboScore: 			( ipb.vars['pwm_bigComboScore'] 		|| 5 ),
	onlyNumOrLetterScore: 	( ipb.vars['pwm_onlyNumOrLetterScore'] 	|| 10 ),
	maxScore: 0,
	popup: [],
	
	init: function()
	{
		document.observe( 'dom:loaded', ipb.pwdStrength.initEvents );
	},
	
	initEvents: function()
	{	
		$( 'password_1' ).observe( 'keyup', ipb.pwdStrength.checkPasswordStrength );
		
		$( 'openPwdStrengthPopup' ).observe( 'click', ipb.pwdStrength.openPopup );
		
		// Calculate max score
		ipb.pwdStrength.maxScore 	= ipb.pwdStrength.oneLcScore + ipb.pwdStrength.oneUcScore + ipb.pwdStrength.oneNumScore + ipb.pwdStrength.threeNumScore + ipb.pwdStrength.oneScScore
									+ ipb.pwdStrength.twoScScore + ipb.pwdStrength.mixedLettersScore + ipb.pwdStrength.mixedNumbersScore + ipb.pwdStrength.bigComboScore;
		
		ipb.pwdStrength.maxScore	+= 14; // Threshold for password length (You need 7 chars to fulfill all "goals")

	},
	
	openPopup: function(e)
	{
		Event.stop(e);
		
		popup = new ipb.Popup( 'passwordStrengthPopup', { type: 'pane', stem: false, modal: true, w: '700px', initial: $( 'passwordStrengthPopup' ).innerHTML, hideAtStart: false } );
	},
	
	checkPasswordStrength: function(e)
	{
		Event.stop(e);
		
		if ( $F( 'password_1' ).length > 2 )
		{
			$( 'pwdStrengthWrapper' ).show();
		}
		
		strength = ipb.pwdStrength.passwordStrength();
		Debug.write( strength );
		
		width = ( 309 / ipb.pwdStrength.maxScore ) * strength;
		width = ( width > 309 ) ? 309 : width;
		
		new Effect.Morph( 'psStrength', { style: 'width:' + width + 'px', duration: '0.6' } ); 
		
		if ( password.length < 3 )
		{
			$( 'psInfo' ).update( ipb.lang['pwm_tooShortPwd'], document.getElementById("psInfo").className = "reg_msg reg_error" );
		}
		else if ( width > 300 )
		{
			$( 'psInfo' ).update( ipb.lang['pwm_strongPwd'], document.getElementById("psInfo").className = "reg_msg reg_accept" );
		}
		else if ( width > 150 )
		{
			$( 'psInfo' ).update( ipb.lang['pwm_goodPwd'], document.getElementById("psInfo").className = "reg_msg reg_accept" );
		}
		else
		{
			$( 'psInfo' ).update( ipb.lang['pwm_badPwd'], document.getElementById("psInfo").className = "reg_msg reg_error" )
		}
	},
	
	passwordStrength: function()
	{
		score 		= 0;			
		password 	= $F( 'password_1' );
		email 		= $F( 'email_1' );
		username 	= ( $('login_name' ) ? $F( 'login_name' ) : '' );
		displayname = ( $( 'display_name' ) ? $F( 'display_name' ) : '' );


		score = password.length * 2;
		
		// Letters
		if (password.match(/[a-z]/)) // [verified] at least one lower case letter
		{
			Debug.write( "Point for one LC" );
			score += ( score + ipb.pwdStrength.oneLcScore );
		} 
		
		if (password.match(/[A-Z]/)) // [verified] at least one upper case letter
		{
			Debug.write( "Point for one UC" );
			score += ipb.pwdStrength.oneUcScore;
		} 
		
		// Numbers
		if (password.match(/\d+/)) // [verified] at least one number
		{
			Debug.write( "Point for one num" );
			score += ipb.pwdStrength.oneNumScore;
		} 
		
		if (password.match(/(\d.*\d.*\d)/)) // [verified] at least three numbers
		{
			Debug.write( "Point for three num" );
			score += ipb.pwdStrength.threeNumScore;
		} 
		
		// Special charatcters
		if (password.match(/[!,@#$%^&*?_~]/)) // [verified] at least one special character
		{
			Debug.write( "Point for one SC" );
			score += ipb.pwdStrength.oneScScore;
		} 
		
		if (password.match(/([!,@#$%^&*?_~].*[!,@#$%^&*?_~])/)) // [verified] at least two special characters
		{
			Debug.write( "Point for two SC" );
			score += ipb.pwdStrength.twoScScore;
		} 
		
		// Combos
		if (password.match(/[a-z]/) && password.match(/[A-Z]/)) // [verified] both upper and lower case
		{
			Debug.write( "Point for mixed LC and UC" );
			score += ipb.pwdStrength.mixedLettersScore;
		} 
		
		if (password.match(/\d/) && password.match(/\D/)) // [verified] both letters and numbers
		{
			Debug.write( "Point for mixed letters and num" );
			score += ipb.pwdStrength.mixedNumbersScore;
		} 
		
		// [Verified] Upper Letters, Lower Letters, numbers and special characters
		if (password.match(/[a-z]/) && password.match(/[A-Z]/) && password.match(/\d/) && password.match(/[!,@#$%^&*?_~]/))
		{
			Debug.write( "Point for big combo" );
			score += ipb.pwdStrength.bigComboScore;
		}
		
		//password is just a nubers or chars
	    if ( password.match(/^\w+$/) || password.match(/^\d+$/) ) 
	    {
	    	score -= ipb.pwdStrength.onlyNumOrLetterScore; 
	    }

		// Password the same as username, display name or email
		if ( password != '' && ( password.toLowerCase() == username.toLowerCase() || password.toLowerCase() == displayname.toLowerCase() || password.toLowerCase() == displayname.toLowerCase() || password.toLowerCase() == email.toLowerCase() ) ) 
		{
			// Resetting score
			score = 1;
		}
		
		return score;
	}
}
ipb.pwdStrength.init();