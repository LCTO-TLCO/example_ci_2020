window.onload = function () {
    document.getElementById("second").style.display = "none";
    document.getElementById("third").style.display = "none";


};

function first_clicked() {
    document.getElementById("second").style.display = "block";
    document.getElementById("first").style.display = "none";

}

function second_clicked() {
    document.getElementById("second").style.display = "none";
    document.getElementById("third").style.display = "block";
}
