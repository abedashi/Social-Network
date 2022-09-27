// const navAbout = document.querySelector('#about-btn');
// const navPosts = document.querySelector('#my-post');
// const containerPosts = document.querySelector('#my-post');
// const containerAbout = document.querySelector('#about');
// document.querySelector('#profile-tabs').addEventListener('click', (event) => {
//     event.preventDefault();
//     target = event.target;
//     if (target.tagName != 'A') {
//         return;
//     } else {
//         if (target === navPosts) {
//             if (navPosts.classList.contains('active')) return;
//             navPosts.classList.add('active');
//             navAbout.classList.remove('active');
//             if (navEdit) navEdit.classList.remove('active');
//             containerPosts.hidden = false;
//             containerAbout.hidden = true;
//             if (containerEdit) containerEdit.hidden = true;
//         } else if (target === navAbout) {
//             if (navAbout.classList.contains('active')) return;
//             navAbout.classList.add('active');
//             navPosts.classList.remove('active');
//             if (navEdit) navEdit.classList.remove('active');
//             containerPosts.hidden = true;
//             containerAbout.hidden = false;
//             if (containerEdit) containerEdit.hidden = true;
//   } else if (target === navEdit) {
//     navAbout.classList.remove('active');
//     navPosts.classList.remove('active');
//     navEdit.classList.add('active');
//     containerPosts.hidden = true;
//     containerAbout.hidden = true;
//     containerEdit.hidden = false;
// }
// }
// });
// document.querySelector('#my-post').style.display = 'block';
// document.querySelector('#about').style.display = 'none';

// document.querySelector('#about-btn').style.backgroundColor = 'white';
// document.querySelector('#my-post-btn').style.backgroundColor = 'rgb(239, 239, 239)';

// document.querySelector('#my-post-btn').addEventListener('click', () => {
//     document.querySelector('#my-post-btn').style.backgroundColor = 'rgb(239, 239, 239)';
//     document.querySelector('#about-btn').style.backgroundColor = 'white';
//     document.querySelector('#my-post').style.display = 'block';
//     document.querySelector('#about').style.display = 'none';
// });
// document.querySelector('#about-btn').addEventListener('click', () => {
//     document.querySelector('#my-post-btn').style.backgroundColor = 'white';
//     document.querySelector('#about-btn').style.backgroundColor = 'rgb(239, 239, 239)';
//     document.querySelector('#my-post').style.display = 'none';
//     document.querySelector('#about').style.display = 'block';
// });

// document.querySelector('#edit').addEventListener('submit', (e) => {
//     const email = document.querySelector('#email');
//     const emailFeedback = document.querySelector('#email-feedback');
//     document.querySelector('#close').addEventListener('click', () => {
//         email.classList.remove("is-invalid", "is-valid");
//         email.value = "";
//         emailFeedback.classList.remove("invalid-feedback", "valid-feedback");
//         bio.classList.remove("is-invalid", "is-valid");
//         bio.value = "";
//         bioFeedback.classList.remove("invalid-feedback", "valid-feedback");
//     })

//     document.querySelector('#reset').addEventListener('click', () => {
//         email.classList.remove("is-invalid", "is-valid");
//         email.value = "";
//         emailFeedback.classList.remove("invalid-feedback", "valid-feedback");
//         bio.classList.remove("is-invalid", "is-valid");
//         bio.value = "";
//         bioFeedback.classList.remove("invalid-feedback", "valid-feedback");
//     })

//     const bio = document.querySelector('#floatingTextarea');
//     const bioFeedback = document.querySelector('#textarea-feedback');
//     if (email.value.length <= 0 && bio.value.length <= 0) {
//         e.preventDefault();
//         email.classList.add("is-invalid");
//         emailFeedback.classList.add("invalid-feedback");

//         bio.classList.add("is-invalid");
//         bioFeedback.classList.add("invalid-feedback");
//     } else if (email.value.length <= 0 || bio.value.length <= 0) {
//         if (email.value.length <= 0) {
//             e.preventDefault();
//             email.classList.add("is-invalid");
//             emailFeedback.classList.add("invalid-feedback");
//         } else {
//             email.classList.add("is-valid");
//             emailFeedback.classList.add("valid-feedback");
//         }

//         if (bio.value.length <= 0) {
//             e.preventDefault();
//             bio.classList.add("is-invalid");
//             bioFeedback.classList.add("invalid-feedback");
//         } else {
//             bio.classList.add("is-valid");
//             bioFeedback.classList.add("valid-feedback");
//         }

//     } else if (email.value.length > 0 && bio.value.length > 0) {
//         email.classList.add("is-valid");
//         emailFeedback.classList.add("valid-feedback");

//         bio.classList.add("is-valid");
//         bioFeedback.classList.add("valid-feedback");
//     }
// })
// })

// function profile() {
// e.stopPropagation();
// console.log('shi')
// document.querySelector('#my-post').style.display = 'block';
// document.querySelector('#about').style.display = 'none';

// document.querySelector('#about-btn').style.backgroundColor = 'white';
// document.querySelector('#my-post-btn').style.backgroundColor = 'rgb(239, 239, 239)';

// document.querySelector('#my-post-btn').addEventListener('click', () => {
//     document.querySelector('#my-post-btn').style.backgroundColor = 'rgb(239, 239, 239)';
//     document.querySelector('#about-btn').style.backgroundColor = 'white';
//     document.querySelector('#my-post').style.display = 'block';
//     document.querySelector('#about').style.display = 'none';
// });
// document.querySelector('#about-btn').addEventListener('click', () => {
//     document.querySelector('#my-post-btn').style.backgroundColor = 'white';
//     document.querySelector('#about-btn').style.backgroundColor = 'rgb(239, 239, 239)';
//     document.querySelector('#my-post').style.display = 'none';
//     document.querySelector('#about').style.display = 'block';
// });

// document.querySelector('#edit').addEventListener('submit', (e) => {
//     const email = document.querySelector('#email');
//     const emailFeedback = document.querySelector('#email-feedback');
//     document.querySelector('#close').addEventListener('click', () => {
//         email.classList.remove("is-invalid", "is-valid");
//         email.value = "";
//         emailFeedback.classList.remove("invalid-feedback", "valid-feedback");
//         bio.classList.remove("is-invalid", "is-valid");
//         bio.value = "";
//         bioFeedback.classList.remove("invalid-feedback", "valid-feedback");
//     })

//     document.querySelector('#reset').addEventListener('click', () => {
//         email.classList.remove("is-invalid", "is-valid");
//         email.value = "";
//         emailFeedback.classList.remove("invalid-feedback", "valid-feedback");
//         bio.classList.remove("is-invalid", "is-valid");
//         bio.value = "";
//         bioFeedback.classList.remove("invalid-feedback", "valid-feedback");
//     })

//     const bio = document.querySelector('#floatingTextarea');
//     const bioFeedback = document.querySelector('#textarea-feedback');
//     if (email.value.length <= 0 && bio.value.length <= 0) {
//         e.preventDefault();
//         email.classList.add("is-invalid");
//         emailFeedback.classList.add("invalid-feedback");

//         bio.classList.add("is-invalid");
//         bioFeedback.classList.add("invalid-feedback");
//     } else if (email.value.length <= 0 || bio.value.length <= 0) {
//         if (email.value.length <= 0) {
//             e.preventDefault();
//             email.classList.add("is-invalid");
//             emailFeedback.classList.add("invalid-feedback");
//         } else {
//             email.classList.add("is-valid");
//             emailFeedback.classList.add("valid-feedback");
//         }

//         if (bio.value.length <= 0) {
//             e.preventDefault();
//             bio.classList.add("is-invalid");
//             bioFeedback.classList.add("invalid-feedback");
//         } else {
//             bio.classList.add("is-valid");
//             bioFeedback.classList.add("valid-feedback");
//         }

//     } else if (email.value.length > 0 && bio.value.length > 0) {
//         email.classList.add("is-valid");
//         emailFeedback.classList.add("valid-feedback");

//         bio.classList.add("is-valid");
//         bioFeedback.classList.add("valid-feedback");
//     }
// })
// }

// console.log("hii")
document.querySelectorAll('#heart-icon').forEach(i => {
    i.addEventListener('click', () => {
        const postID = i.closest('div[data-id]').dataset.id;
        const action = i.dataset.action;
        const count = i.parentElement.nextElementSibling;
        console.log(postID);
        console.log(action);
        console.log(count)
        fetch(`/post/${action}/${postID}`).then((res) => {
            if (res.status == 401) {
                window.location.replace('/login');
            } else if (res.status == 204) {
                if (i.dataset.action === 'like') {
                    i.dataset.action = 'unlike';
                    i.classList.replace('bi-heart', 'bi-heart-fill');
                    i.classList.add('text-danger');
                    count.innerText = parseInt(count.innerText) + 1;
                } else {
                    i.dataset.action = 'like';
                    i.classList.replace('bi-heart-fill', 'bi-heart');
                    i.classList.remove('text-danger');
                    count.innerText = parseInt(count.innerText) - 1;
                }
            }
        })
    })
});

// const likePost = (i) => {
//     const postID = i.closest('div[data-id]').dataset.id;
//     const action = i.dataset.action;
//     const icon = i.children[0];
//     const count = i.children[1];
//     console.log(postID);
//     console.log(action)
//     console.log(icon);
//     console.log(count);
//     // const count = i.children[1];
//     fetch(`/post/${action}/${postID}`).then((res) => {
//         if (res.status == 401) {
//             window.location.replace('/login');
//         } else if (res.status == 204) {
//             if (i.dataset.action === 'like') {
//                 i.dataset.action = 'unlike';
//                 icon.classList.replace('bi-heart', 'bi-heart-fill');
//                 icon.classList.add('text-danger');
//                 count.innerText = parseInt(count.innerText) + 1;
//             } else {
//                 i.dataset.action = 'like';
//                 icon.classList.replace('bi-heart-fill', 'bi-heart');
//                 icon.classList.remove('text-danger');
//                 count.innerText = parseInt(count.innerText) - 1;
//             }
//         }
//     })
// };

// document.querySelectorAll('#heart-icon').forEach(i => {
//     i.addEventListener('click', likePost)
// })

const postContainer = document.querySelector('#my-post');
const aboutContainer = document.querySelector('#about');
const postBtn = document.querySelector('#my-post-btn');
const aboutBtn = document.querySelector('#about-btn');
postBtn.addEventListener('click', () => {
    postBtn.classList.add('active');
    aboutBtn.classList.remove('active');
    aboutContainer.hidden = true;
    postContainer.hidden = false;
});
aboutBtn.addEventListener('click', () => {
    postBtn.classList.remove('active');
    aboutBtn.classList.add('active');
    postContainer.hidden = true;
    aboutContainer.hidden = false;
})