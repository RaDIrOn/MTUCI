$(document).ready(function() {
    var scrolled = 0;
    var $parallaxElements = $('.icons-for-parallax img');
    
    $(window).scroll(function() {
        scrolled = $(window).scrollTop();
        
        for (var i = 0; i < $parallaxElements.length; i++) {
            var yPosition = scrolled * (0.15 * (i + 1));
            
            $parallaxElements.eq(i).css({
                top: yPosition
            });
        }
    });
    
    var $logo = $('.header .logo');
    if ($logo.length) {
        $(window).scroll(function() {
            var logoSpeed = 0.08;
            var logoY = $(window).scrollTop() * logoSpeed;
            $logo.css({
                top: logoY
            });
        });
    }
});