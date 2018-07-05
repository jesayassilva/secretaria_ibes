function validaBusca(){
	if(document.querySelector('#q').value == ''){
	   document.querySelector('#q').style.border = '2px solid red';
		return false;
	}
}

document.querySelector('#form-busca').onsubmit = function validaBusca(){
	if(document.querySelector('#q').value == ''){
	   document.querySelector('#q').style.border = '2px solid red';
		return false;
	}	
};

var banners = ["img/techcenter.jpg", "img/tecenter.jpg"];
var bannerAtual = 0;
function trocaBanner(){
	bannerAtual = (bannerAtual + 1) % 2;
	document.querySelector('.destaque img').src = banners[bannerAtual];
}
var timer = setInterval(trocaBanner, 4000);

var controle = document.querySelector('.pause');
controle.onclick = function(){
	if(controle.className == 'pause'){
		clearInterval(timer);
		controle.className = 'play';
	} else {
		timer = setInterval(trocaBanner, 4000);
		controle.className = 'pause';
	}
	return false;
};
	