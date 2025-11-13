const background = document.querySelector('.background');

background.addEventListener('click', () => {
   background.classList.add('remove');
});

const lamp = document.querySelector('.lamp_image');
const light = document.querySelector('.light');
const figures = document.querySelector('.in_light_figures_container');

lamp.addEventListener('mousedown', () => {
   lamp.classList.add('mousedown');
});

lamp.addEventListener('mouseup', () => {
   lamp.classList.remove('mousedown');
});

lamp.addEventListener('click', () => {
   light.classList.toggle('on');
   figures.classList.toggle('display');
});

const rabbit = document.querySelector('.rabbit_container');
const bird = document.querySelector('.bird_container');

rabbit.addEventListener('click', () => {
   rabbit.classList.add('hide');
   bird.classList.remove('hide');
});

bird.addEventListener('click', () => {
   bird.classList.add('hide');
   rabbit.classList.remove('hide');
});
