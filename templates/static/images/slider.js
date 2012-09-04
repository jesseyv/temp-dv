$(function() {
	var o, b, j, e, c, t, html, int;
	o = $('ul#slider');
	b = o.find('li');
	j = b.size()-1;
	e = $('a.arr-left');
	c = $('a.arr-right');
	html = o.html();
	o.html(html+html+html);
	o.css('margin-left', -parseInt(o.width()/3));
	t = function(n) {
		if (o.is(':animated')) return false;
		if (parseInt(o.css('margin-left')) == 0 || parseInt(o.css('margin-left')) == parseInt(o.width()/3*2*(-1))) {
			o.css('margin-left', -parseInt(o.width()/3));	
		}
		o.animate({
			'marginLeft' : parseInt(o.css('margin-left')) - 172*n	
		}, 1000);
	}
	int = setInterval(function(){
		t(1);
	}, 5000)
	e.click(function() {
		clearInterval(int);
		t(1);
		int = setInterval(function(){
			t(1);
		}, 5000)
		return false;
	});
	c.click(function() {
		clearInterval(int);
		t(-1);
		int = setInterval(function(){
			t(1);
		}, 5000)
		return false;
	});
	
	
	$('a.buy').click(function(){
		$('div.bg').fadeIn(500);
		$('.window').fadeIn(500);
		return false;
	});
	$('a.close').click(function(){
		$('div.bg').fadeOut(500);
		$('.window').fadeOut(500);
		return false;
	});
	
});