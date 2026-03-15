var foldBtns = document.getElementsByClassName("fold-button");


for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        var button = event.target;
        var post = button.parentElement.parentElement; 

        if (post.classList.contains("folded")) {

            post.classList.remove("folded");
            button.innerHTML = "Свернуть";
        } else {

            post.classList.add("folded");
            button.innerHTML = "Развернуть";
        }
    });
}