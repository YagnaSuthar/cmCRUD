const navslide = () => {
    const burger = document.querySelector(".box");  // Get the burger icon
    const nav = document.querySelector(".nav");  // Get the navigation menu

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');  // Toggle the visibility of the navigation

        // Optional: Toggle the class on the burger icon for animation
        burger.classList.toggle('toggle');  // This will allow you to animate the burger icon
    });
}

navslide();
