function showComment(){
    var commentArea = document.getElementById("comment-area");
    if(commentArea.style.display == "block"){
        commentArea.setAttribute("style", "display:none;");
    }else{
        commentArea.setAttribute("style", "display:block;");
    }
}

function showReply(){
    var replyArea = document.getElementById("reply-area");
    if(replyArea.style.display == "block"){
        replyArea.setAttribute("style", "display:none;");
    }else{
        replyArea.setAttribute("style", "display:block;");
    }
}