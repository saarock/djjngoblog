// alert('Done')
const  openNav = document.querySelector('.open-nav');
const   mobileNav = document.querySelector('.mobile-nav');
openNav.addEventListener('click', () => {
    mobileNav.classList.toggle('extra-mobile-nav');
})

const navs = document.getElementsByClassName('navs')[0];
        function bodyScroll() {
            // alert('Yes')
            console.log(window.scrollY)
            if(window.scrollY>40) {
                navs.classList.add('new-bac-navs');
            } else {
                navs.classList.remove('new-bac-navs');

            }
        }



const saved = document.querySelector('.message-contact');
if(saved) {
    setInterval(() => {
        saved.style.display = 'none';
    }, 1000);
}
// alert('Done')

