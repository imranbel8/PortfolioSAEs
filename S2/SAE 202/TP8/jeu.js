// Des raccourcis
const tux=document.getElementById('tux');
const spanEtape=document.getElementById('etape');
const spanScore=document.getElementById('score');
const spanTemps=document.getElementById('temps');
const commencer=document.getElementById('commencer');

// Variables globales : L'état du jeu
let score=0;
let etape;
let temps;
let interval;

changer_etape('Début');

commencer.addEventListener('click',function(){
  if(etape==='Début' || etape==='Fin'){changer_etape('Jeu');}
});


function minuteur()
{
  temps-=1;
  spanTemps.textContent=temps;  
  if(temps<=0){
    changer_etape('Fin');
  }
}

function changer_etape(nouvelleEtape)
{
  if(nouvelleEtape==='Jeu'){
    document.getElementById('game-over').style.display='none';
    document.querySelectorAll('.splat').forEach(s=>s.remove());
    tux.style.left="";
    tux.style.top="";
    score=0;
    spanScore.textContent=score;
    temps=10;
    spanTemps.textContent=temps;
    interval=window.setInterval(minuteur,1000);
    commencer.style.opacity=0;
  }
  if(nouvelleEtape==='Fin'){
    document.getElementById('game-over').style.display='block';
    commencer.style.opacity=1;
    commencer.value='Recommencer';
    window.clearInterval(interval);
  }

  etape=nouvelleEtape;
  document.getElementById('etape').textContent=etape;
}

document.addEventListener('keydown',function(event){
  if(etape!=='Jeu'){return;}
  console.log('Touche enfoncée:',event.key);
  let rect=tux.getBoundingClientRect();
  console.log(rect);
  let d=100;
  let left=rect.left;
  let top=rect.top;
  if(event.key==='ArrowRight'){left+=d;}
  if(event.key==='ArrowLeft' ){left-=d;}
  if(event.key==='ArrowDown' ){top+=d;}
  if(event.key==='ArrowUp'   ){top-=d;}
  left=Math.max(10,left);
  top =Math.max(10,top);
  left=Math.min(510-rect.width ,left);
  top =Math.min(510-rect.height,top);
  tux.style.left=left+"px";
  tux.style.top=top+"px";
});

document.addEventListener('mousedown',function (event) 
{
  if(etape!=='Jeu'){return;}
  // Petit détail: éviter la sélection 
  event.preventDefault();

  if(event.pageX-16<10 || 
     event.pageY-16<10 || 
     event.pageX-16+32>500+10 || 
     event.pageY-16+40>500+10    ){return;} 

  let i=document.createElement('img');
  i.src='https://moodle.iutv.univ-paris13.fr/img/bjs/splat.png';
  i.className='splat';
  document.body.append(i);
  // Forcer le navigateur à prendre en compte la situation actuelle (position, scale).
  // Ceci permettra au navigateur de s'apercevoir d'un changement futur des propriétés CSS.
  window.getComputedStyle(i).top;
  // Changer les propriétés CSS qui transitionnent. 
  // Le navigateur s'aperçoit du changement et déclenche la transition.
  i.style.top =(event.pageY-16)+'px';
  i.style.left=(event.pageX-16)+'px'; 
  i.style.transform='scale(1)';
  setTimeout(function(){
	let rectTux=tux.getBoundingClientRect();
	let rectSplat=i.getBoundingClientRect();
	let touche=
		rectSplat.top +rectSplat.height >= rectTux.top                  &&
		rectSplat.top                   <  rectTux.top  +rectTux.height &&
		rectSplat.left+rectSplat.width  >= rectTux.left                 &&
		rectSplat.left                  <  rectTux.left +rectTux.width  ;
	if(touche){
	  i.src="https://moodle.iutv.univ-paris13.fr/img/bjs/splat2.png";
      getComputedStyle(i).top;
      i.style.opacity=0;
      setTimeout(function(){i.remove();},3000);
	  score+=10;
	}
	else
	{
	  i.style.zIndex=-1;
	  score-=5;
	}
    spanScore.textContent=score;
  },1000);
});