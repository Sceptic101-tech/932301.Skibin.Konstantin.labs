function createModal(header, text)
{
	let parent = document.getElementById('main');
	let child = document.createElement('div');
	child.className = 'modal';

	child.onclick = function() { removeModal('modal') };

	let modal = document.createElement('div');
	modal.className = 'modal_inner';

	child.appendChild(modal);
	modal.innerHTML =  (`<h2>${header}</h2> <p>${text}</p>`);

	parent.appendChild(child);
}

function removeModal(class_name)
{
	let modal = document.getElementsByClassName(class_name)[0];
	modal.remove();
}