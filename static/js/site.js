// Menu behavior, the theme toggle, and the email buttons.
// The site reads fine without this file.
(function () {
  var nav = document.getElementById("nav");
  var menuButton = document.querySelector(".menu-button");

  menuButton.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    menuButton.setAttribute("aria-expanded", open);
  });

  document.querySelector(".theme-button").addEventListener("click", function () {
    var root = document.documentElement;
    var dark = root.dataset.theme
      ? root.dataset.theme === "dark"
      : window.matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try {
      localStorage.setItem("theme", root.dataset.theme);
    } catch (e) {}
  });

  // Each address stays encoded until a visitor asks for it, so a program
  // that reads the page, or runs its scripts on load, finds no address.
  // A button names its address with data-to.
  var NAMES = {
    mindview: [116, 112, 117, 107, 125, 112, 108, 126, 112, 117, 106],
    bruce: [73, 121, 124, 106, 108, 91, 76, 106, 114, 108, 115]
  };
  var HOST = [110, 116, 104, 112, 115, 53, 106, 118, 116];

  function decode(codes) {
    return codes
      .map(function (code) {
        return String.fromCharCode(code - 7);
      })
      .join("");
  }

  Array.prototype.forEach.call(
    document.querySelectorAll(".email-button"),
    function (button) {
      button.addEventListener("click", function () {
        var name = NAMES[button.dataset.to] || NAMES.mindview;
        var address = decode(name) + String.fromCharCode(64) + decode(HOST);
        var subject = button.dataset.subject;
        var link = document.createElement("a");
        link.href =
          "mai" + "lto:" + address +
          (subject ? "?subject=" + encodeURIComponent(subject) : "");
        link.textContent = address;
        button.replaceWith(link);
      });
    }
  );
})();
