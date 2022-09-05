document.querySelector('#my-post').style.display = 'none';
document.querySelector('#about').style.display = 'block';

document.querySelector('#my-post-btn').style.backgroundColor = 'white';
document.querySelector('#about-btn').style.backgroundColor = 'rgb(239, 239, 239)';

document.querySelector('#my-post-btn').addEventListener('click', () => {
    document.querySelector('#my-post-btn').style.backgroundColor = 'rgb(239, 239, 239)';
    document.querySelector('#about-btn').style.backgroundColor = 'white';
    document.querySelector('#my-post').style.display = 'block';
    document.querySelector('#about').style.display = 'none';
});
document.querySelector('#about-btn').addEventListener('click', () => {
    document.querySelector('#my-post-btn').style.backgroundColor = 'white';
    document.querySelector('#about-btn').style.backgroundColor = 'rgb(239, 239, 239)';
    document.querySelector('#my-post').style.display = 'none';
    document.querySelector('#about').style.display = 'block';
});