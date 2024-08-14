var pics = [
    "Images/cat_1.jpg",
    "Images/cat_2.jpg",
    "Images/cat_3.jpg",
    "Images/cat_4.jpg"
];

// var btn = document.querySelector("button")
var currentImage = Number();

function changeImage() {
    currentImage = (currentImage + 1) % pics.length;
    document.querySelector("img").src = pics[currentImage];
}

// btn.addEventListener("click", function() {
    
// });