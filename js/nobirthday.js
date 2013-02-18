// File: nobirthday.js

var g_count = 100;

var g_parent_el_id = "ntf";
var g_element_id = "ntf-bd";

function nobirthday()
{
	var bd = document.getElementById(g_element_id);
	var el = document.getElementById(g_parent_el_id);

	if ( bd != null && el != null )
	{
		el.hidden = true;

		console.log("[Birthday86er] Removed birthday notification");
		chrome.extension.sendMessage({m:'enable_page_action'}, function(r){});

		return;
	}

	if ( g_count <= 0 )
	{
		console.log("[Birthday86er] Nothing found after a period of time, exiting");

		return;
	}

	g_count--;
	window.setTimeout(nobirthday, 50);
}

console.log("[Birthday86er] Birthday 86er for Google+ loading...");

nobirthday()

// vim: ts=4:sw=4:
