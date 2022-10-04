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
// let post = document.querySelector('#test').nextElementSibling;
//     let postText = post.innerText;
//     console.log(postText)

// Edit Post
let editing = false
const editPost = (el, event) => {
    event.stopPropagation()
    if (editing) {
        let dropdown = el.closest('.dropdown').children[0];
        dropdown = bootstrap.Dropdown.getInstance(dropdown);
        dropdown.hide();
        return;
    }
    
    editing = true;
    let dropdown = el.closest('.dropdown').children[0];
    dropdown = bootstrap.Dropdown.getInstance(dropdown);
    dropdown.hide();
    let post = el.closest('#post').nextElementSibling.nextElementSibling;
    let postText = post.innerText;
    
    const textarea = document.createElement('textarea');
    textarea.classList.add('form-control', 'my-2');
    textarea.value = postText;
    post.replaceWith(textarea);

    const save = document.createElement('button');
    save.classList.add('btn', 'btn-primary', 'mb-2');
    save.innerText = 'Edit';
    textarea.insertAdjacentElement('afterend', save);

    save.onclick = (event) => {
        event.stopPropagation();
        postText = textarea.value;

        let postId = el.closest('div[data-id]').dataset.id;

        fetch(`/edit_post/${postId}`, {
            method: 'PUT',
            body: JSON.stringify({
                new_post: postText,
            }),
        }).then((res) => {
            if (res.status === 204) {
                post.innerText = postText;
                textarea.replaceWith(post);
                save.remove();
                editing = false;
            }
        });
    };
};


// Delete Post
document.querySelectorAll('#down').forEach(el => {
    el.addEventListener('click', () => {
        let postId = el.closest('div[data-id]').dataset.id;
        fetch(`/delete/${postId}`).then((response) => {
            if (response.status === 200) {
                let post = el.closest('div[data-id]');
                post.remove();
            }
        })
    })
})

// Like on posts
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

// Profile Single page
const editContainer = document.querySelector('#edit-profile')
const postContainer = document.querySelector('#my-post');
const aboutContainer = document.querySelector('#about');
const postBtn = document.querySelector('#my-post-btn');
const aboutBtn = document.querySelector('#about-btn');
const editBtn = document.querySelector('#edit-btn');
postBtn.addEventListener('click', (e) => {
    postBtn.classList.add('active');
    aboutBtn.classList.remove('active');
    if (editBtn) editBtn.classList.remove('active');
    postContainer.hidden = false;
    aboutContainer.hidden = true;
    if (editContainer) editContainer.hidden = true;
});
aboutBtn.addEventListener('click', () => {
    aboutBtn.classList.add('active');
    postBtn.classList.remove('active');
    if (editBtn) editBtn.classList.remove('active');
    aboutContainer.hidden = false;
    postContainer.hidden = true;
    if (editContainer) editContainer.hidden = true;
});
editBtn.addEventListener('click', () => {
    editBtn.classList.add('active');
    postBtn.classList.remove('active');
    aboutBtn.classList.remove('active');
    editContainer.hidden = false;
    postContainer.hidden = true;
    aboutContainer.hidden = true;
})


// Profile change cover color
const cover = document.querySelector('#cover');
const color = document.querySelector('input[type="color"]');
color.addEventListener('input', (event) => {
    cover.style.backgroundColor = event.srcElement.value;
});