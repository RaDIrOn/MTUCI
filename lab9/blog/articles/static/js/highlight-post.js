$(document).ready(function() {
    $('.one-post').hover(
        function() {
            console.log("Навели на пост");
            $(this).find('.one-post-shadow').animate({
                opacity: 0.2
            }, 200);
        },
        function() {
            console.log("Убрали курсор с поста");
            $(this).find('.one-post-shadow').animate({
                opacity: 0
            }, 200);
        }
    );
    
    $('.header img').hover(
        function() {
            $(this).animate({
                width: '338px',
                opacity: 0.8
            }, 300);
        },
        function() {
            $(this).animate({
                width: '318px',
                opacity: 1.0
            }, 300);
        }
    );
});