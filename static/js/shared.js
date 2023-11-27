function resize(e) {
    const size = `${e.x}px`;
    sidebar.style.flexBasis = size;
}


let lastElement;

function showAndHideOthers(classToShow) {
    const elementToShow = document.querySelector(classToShow);
    const sidebar = document.getElementById('sidebar');

    if (sidebar.style.flexBasis < '234px' || sidebar.style.flexBasis < '99px') {
        sidebar.style.flexBasis = '234px';
    }


    if (lastElement === elementToShow) {
        elementToShow.classList.remove('selected');
        sidebar.style.flexBasis = '0px';
    } else {
        elementToShow.classList.add('selected');
        sidebar.style.flexBasis = '234px';
    }

    if (lastElement != null) {
        lastElement.classList.remove('selected');
    }

    lastElement = elementToShow;

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
            "https://storage.iran.liara.space/public-static-rezashakeri/static/images/icons/findAndShowNextMatches.svg"
        );
        element.className += " open";
        sidebarItems.removeAttribute("style");
    } else {
        element.setAttribute("src", "https://storage.iran.liara.space/public-static-rezashakeri/static/images/icons/play_forward.svg");
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
