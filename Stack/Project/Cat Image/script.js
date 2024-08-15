var pics = [
    "Images/img1.jpg",
    "Images/img2.jpg",
    "Images/img3.jpg",
    "Images/img4.jpg"
];

// var btn = document.querySelector("button")
var currentImage = Number();

function changeImage() {
    currentImage = (currentImage + 1) % pics.length;
    document.querySelector("img").src = pics[currentImage];
}

// btn.addEventListener("click", function() {
    
// });