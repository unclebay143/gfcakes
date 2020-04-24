function navfold() {
    var x = document.getElementById("nav-right-id");
    if (x.className === "nav-right") {
        x.className += " responsive";
    } else {
        x.className = "nav-right";
    }
}