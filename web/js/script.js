var currentTheme
isCreditsWindowOpen = false

eel.getThemes()(function(themes){
    console.log("Themes: " + themes)
    var i
    for (i = 0; i < themes.length; i++) {
        var button = document.createElement("BUTTON")
        button.className = "themeButton"
        button.innerText = themes[i]
        button.setAttribute("onClick", "setPreview(" + '"' + themes[i] + '"' + ")" )
        document.getElementById("themes").appendChild(button)
    }
})

function setPreview(themeName) {
    var preview = document.getElementById("themePreviewImage")
    eel.getPreviewImg(themeName)(function (image){
        console.log(image)
        console.log("Preview changed")
        preview.src = image
        document.getElementById("clickAThemeAlert").style.display = "none"
        preview.style.visibility = "visible"
        document.getElementById("hoverToExpandText").style.visibility = "visible"
        document.getElementById("setThemeButton").style.display = "block"
    })
    currentTheme = themeName
    document.getElementById("setThemeButton").addEventListener("click", setTheme)
}

function setTheme(){
    console.log("Setting theme: " + currentTheme)
    eel.setTheme(currentTheme)
}

function toggleCredits() {
    if (isCreditsWindowOpen == false) {
        document.getElementById("credits").style.visibility = "visible"
        isCreditsWindowOpen = true
    } else {
        document.getElementById("credits").style.visibility = "hidden"
        isCreditsWindowOpen = false
    }  
}

VanillaTilt.init(document.querySelector("#themePreviewImage"), {
    max: 1,
    speed: 200
});
VanillaTilt.init(document.querySelector("#credits"), {
    max: 3,
    speed: 200
});
VanillaTilt.init(document.querySelector("#setThemeButton"), {
    max: 10,
    speed: 100
});