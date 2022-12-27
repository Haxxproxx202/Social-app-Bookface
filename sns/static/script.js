let settingsmenu = document.querySelector(".settings-menu");
let darkBtn = document.getElementById("dark-btn");
const conversationField = document.querySelector('.conversation-window');
const hideChatButton = document.querySelector('.sidebar-title2 p')

const advertisementField = document.querySelector('.sidebar-aaddss')
const hideAdButton = document.querySelector('.sidebar-title p')

function settingsMenuToggle(){
    settingsmenu.classList.toggle("settings-menu-height");
}

darkBtn.onclick = function(){
    darkBtn.classList.toggle("dark-btn-on");
    document.body.classList.toggle("dark-theme");

    if(localStorage.getItem("theme") == "light"){
        localStorage.setItem("theme", "dark");
    }
    else{
        localStorage.setItem("theme", "light");
    }
}


if(localStorage.getItem("theme") == "light"){
    darkBtn.classList.remove("dark-btn-on");
    document.body.classList.remove("dark-theme");
}
else if(localStorage.getItem("theme") == "dark"){
    darkBtn.classList.add("dark-btn-on");
    document.body.classList.add("dark-theme");
}
else{
    localStorage.setItem("theme", "light")
}

function hideOrShowConversationField(event){
    if(this.textContent === "Hide Chat") {
        this.textContent = "Show Chat";
        conversationField.style.display = "none";
    } else {
        conversationField.style.display = "block";
        this.textContent = "Hide Chat";
    }
}
function hideOrShowAdField(event){
    if(this.textContent === "Close"){
        this.textContent = "Show";
        advertisementField.style.display = "none";
    } else {
        this.textContent = "Close";
        advertisementField.style.display = "block";
    }
}


hideChatButton.addEventListener('click', hideOrShowConversationField);
hideAdButton.addEventListener('click', hideOrShowAdField);

