(function(){
  requestAnimationFrame(function(){requestAnimationFrame(function(){
    document.documentElement.classList.add('ready');
  })});
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ecualizador del hero */
  var eq=document.getElementById('eq');
  if(eq){
    var n=window.innerWidth<760?22:38,html='';
    for(var i=0;i<n;i++){
      var h=14+Math.round(Math.abs(Math.sin(i*.5))*34+Math.random()*16);
      html+='<i style="--h:'+h+'%;animation-duration:'+(2.6+Math.random()*2.2).toFixed(2)+
            's;animation-delay:-'+(Math.random()*4).toFixed(2)+'s"></i>';
    }
    eq.innerHTML=html;
  }

  /* header, progreso, boton subir */
  var hdr=document.getElementById('hdr'),bar=document.getElementById('bar'),top=document.getElementById('top'),tick=false;
  function onScroll(){
    var y=window.scrollY,max=document.documentElement.scrollHeight-innerHeight;
    hdr.classList.toggle('on',y>40);
    bar.style.width=(max>0?y/max*100:0)+'%';
    top.classList.toggle('show',y>innerHeight);
    tick=false;
  }
  addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});
  onScroll();
  top.addEventListener('click',function(){scrollTo({top:0,behavior:'smooth'})});

  /* menu mobile */
  var burger=document.getElementById('burger'),nav=document.getElementById('nav');
  burger.addEventListener('click',function(){
    burger.setAttribute('aria-expanded',nav.classList.toggle('open'));
  });
  nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){
    nav.classList.remove('open');burger.setAttribute('aria-expanded','false');
  })});

  /* reveal al entrar en pantalla */
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})
  },{threshold:.15,rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.rv,.line').forEach(function(el){io.observe(el)});

  /* seccion activa en el nav */
  var links=[].slice.call(nav.querySelectorAll('a')),
      secs=links.map(function(a){return document.querySelector(a.getAttribute('href'))}).filter(Boolean);
  var spy=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting)return;
      links.forEach(function(a){a.classList.toggle('act',a.getAttribute('href')==='#'+e.target.id)});
    });
  },{rootMargin:'-45% 0px -50% 0px'});
  secs.forEach(function(s){spy.observe(s)});

  /* halo que sigue al mouse */
  if(!reduce&&matchMedia('(hover:hover)').matches){
    var glow=document.getElementById('glow'),gx=0,gy=0,tx=0,ty=0,on=false;
    addEventListener('pointermove',function(e){
      tx=e.clientX;ty=e.clientY;
      if(!on){on=true;glow.style.opacity=1}
    },{passive:true});
    (function loop(){
      gx+=(tx-gx)*.08;gy+=(ty-gy)*.08;
      glow.style.transform='translate('+gx+'px,'+gy+'px)';
      requestAnimationFrame(loop);
    })();
  }

  /* parallax suave del emblema */
  if(!reduce){
    var em=document.querySelector('.emblem');
    addEventListener('scroll',function(){
      var y=Math.min(window.scrollY,900);
      em.style.transform='translateY('+(y*.14)+'px) scale('+(1-y*.00008)+')';
      em.style.opacity=Math.max(0,1-y/760);
    },{passive:true});
  }

  document.getElementById('year').textContent=new Date().getFullYear();
})();
