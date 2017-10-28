'use strict';
var $gd_header = $("#header"),
    $gd_menu = $("#menu-mobile"),
    $gd_cover = $("#cover"),
    $gd_search_btn = $("#search-btn"),
    $gd_search_input = ($("#header-search"), $(".search-field")),
    $gd_scroll_top = $(".scroll_top"),
    $document = $(document),
    $window = $(window),
    overlay = {
        opacity: 1,
        visibility: "visible"
    };
function menuClose(e) {
    e.preventDefault(), $("html").removeAttr("mapache-state"), $(".overlay").removeAttr("style"), $gd_menu.removeClass("open")
}

function mouseUp(e) {
    $gd_menu.hasClass("open") && 0 === $gd_menu.has(e.target).length && menuClose(e)
}

$document.on("mouseup", mouseUp), $("#menu-open").on("click", function (e) {
    e.preventDefault(), $("html").attr("mapache-state", "no-scroll"), $(".overlay").css(overlay), $gd_menu.addClass("open")
}), "undefined" != typeof title_home && $("#title-home").html(title_home), $gd_search_btn.on("click", function (e) {
    e.preventDefault(), $(this).toggleClass("i-search"), $gd_header.toggleClass("responsive-search-open"), $gd_search_input.focus()
}), $("p.excerpt").length > 0 && $("p.excerpt").insertAfter($("h1.title")), $document.on("ready", function () {

});
$document.on("ready", function () {
    $("a.navigation-link").on("click", function (e) {
        window.open($(this).attr("href"),"_self");
        menuClose(e);
        return false;
    });
    $gd_search_input.focus(function () {
        $gd_header.addClass("search-active");
        $(".search-popout").removeClass("closed")
    });
    $gd_search_input.blur(function () {
        setTimeout(function () {
            $gd_header.removeClass("search-active");
            $(".search-popout").addClass("closed")
        }, 200)
    });
    $gd_search_input.keyup(function () {
        $(".search-suggest-results").css("display", "block")
    })
}), $window.on("scroll", function () {
    $(this).scrollTop() > 100 ? $gd_scroll_top.addClass("visible") : $gd_scroll_top.removeClass("visible")
}), $gd_scroll_top.on("click", function (e) {
    e.preventDefault(), $("html, body").animate({
        scrollTop: 0
    }, 500)
});

/* ==============================================
 7. WOW plugin triggers animate.css on scroll
 =============================================== */

