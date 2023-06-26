function resize(e) {
    const size = `${e.x}px`;
    sidebar.style.flexBasis = size;
}

function showContent() {
    let element = document.querySelector(".sidebar-content");
    let sideBar = document.querySelector("#sidebar")
    if (element.style.display === "none") {
        element.setAttribute(
            "style",
            "display: flex; flex-direction: column; width: 210px;"
        );
    } else {
        element.setAttribute("style", "display: none;");
        sideBar.removeAttribute("style");

    }
}

const resizer = document.querySelector("#resizer");
const sidebar = document.querySelector("#sidebar");

resizer.addEventListener("mousedown", (event) => {
    document.addEventListener("mousemove", resize, false);
    document.addEventListener(
        "mouseup",
        () => {
            document.removeEventListener("mousemove", resize, false);
        },
        false
    );
});

setInterval(() => $("#dateTime").text(new Date().toLocaleString()), 1000);

function OpenClose(elementClass, SidebarItemsClass) {
    let element = document.querySelector(`.${elementClass}`);
    let sidebarItems = document.querySelector(`.${SidebarItemsClass}`);
    if (element.className === elementClass) {
        element.setAttribute(
            "src",
            "/static/images/icons/findAndShowNextMatches.svg"
        );
        element.className += " open";
        sidebarItems.removeAttribute("style");
    } else {
        element.setAttribute("src", "/static/images/icons/play_forward.svg");
        element.className = elementClass;
        sidebarItems.setAttribute("style", "display: none;");
    }
}

let docTitle = document.title;
window.addEventListener("blur", () => {
    document.title = "Come Back :(";
});

window.addEventListener("focus", () => {
    document.title = docTitle;
});
