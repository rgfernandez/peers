// Function by Jukka Lähetkangas, used with permission

if (!($.browser.msie && $.browser.version < 7)){
	$(window).resize(fix);
	$(document).ready(fix);
}

function fix() {
	if ($(window).width() < ($('.multi').attr("media")).match("(.*:)[^0-9a-z]*([0-9]*)px")[2]) {
  		$('.multi').attr('disabled', 'true');
	} else {
		$('.multi').attr('disabled', '');
	}
}