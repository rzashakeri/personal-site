
$(".main-menu-head-title").codex({
    effect: "charbychar",
    reveal: 200, // the number of miliseconds
});

new TypeIt(".main-menu-head-description", {
    speed: 10,
    waitUntilVisible: true,
}).go();

function ReadMoreAboutText() {
    let aboutTextReadMore = document.getElementById("about-text-read-more");
    let moreText = document.getElementById("about-text-more");

    if (aboutTextReadMore.style.display === "none") {
        aboutTextReadMore.style.display = "inline";
        aboutTextReadMore.innerHTML = "Read more";
        moreText.style.display = "none";
    } else {
        aboutTextReadMore.style.display = "none";
        aboutTextReadMore.innerHTML = "Read less";
        moreText.style.display = "inline";
    }
}
