const leftLayoutBtn = document.querySelector('.navigation_button_left');
const bothLayoutBtn = document.querySelector('.navigation_button_middle');
const rightLayoutBtn = document.querySelector('.navigation_button_right');

const leftColumn = document.querySelector('.left_image_container');
const rightColumn = document.querySelector('.right_image_container');

leftLayoutBtn.addEventListener('click', () => {
    createAsymmetricColumns(leftColumn, rightColumn);
});

rightLayoutBtn.addEventListener('click', () => {
    createAsymmetricColumns(rightColumn, leftColumn);
});

bothLayoutBtn.addEventListener('click', () => {
    rightColumn.style.flexBasis = '50%';
    rightColumn.querySelector('img').style.width = '100%';
    rightColumn.querySelector('img').style.display = 'block';
    leftColumn.style.flexBasis = '50%';
    leftColumn.querySelector('img').style.display = 'block';
    leftColumn.querySelector('img').style.width = '100%';
});

const createAsymmetricColumns = (wideColumnEl, narrowColumnEl) => {
    wideColumnEl.style.flexBasis = '95%';
    wideColumnEl.querySelector('img').style.width = '75%';
    wideColumnEl.querySelector('img').style.display = 'block';
    narrowColumnEl.style.flexBasis = '5%';
    narrowColumnEl.querySelector('img').style.display = 'none';
};

bothLayoutBtn.click();