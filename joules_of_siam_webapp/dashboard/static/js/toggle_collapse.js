let changeIcon = function(icon) {
    var collapse_content = document.getElementById('collapseContent');

    if (icon.classList.contains('fa-chevron-down')){
        icon.classList.replace('fa-chevron-down', 'fa-chevron-right')
        collapse_content.style.display = "none";
    }

    else if (icon.classList.contains('fa-chevron-right')){
        icon.classList.replace('fa-chevron-right', 'fa-chevron-down')
        collapse_content.style.display = "block";
    }

}
// changeIcon = (icon) => icon.classList.toggle('fa-chevron-down');