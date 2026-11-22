/* Distinct motion kit: rotating words, pause control, flip cards. Scoped to this section only. */
(function(root){
  if(!root) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches, paused=false;
  [].forEach.call(root.querySelectorAll('[data-rot]'),function(r){
    var w=r.querySelectorAll('.dx-rot__w'),i=0,hover=false; if(!w.length) return;
    w[0].classList.add('is-on'); if(reduce) return;
    r.addEventListener('mouseenter',function(){hover=true}); r.addEventListener('mouseleave',function(){hover=false});
    setInterval(function(){
      if(paused||hover||document.hidden) return;
      var c=w[i]; c.classList.remove('is-on'); c.classList.add('is-out');
      setTimeout(function(){c.classList.remove('is-out')},800);
      i=(i+1)%w.length; w[i].classList.add('is-on');
    },+r.getAttribute('data-rot')||2600);
  });
  [].forEach.call(root.querySelectorAll('[data-pause]'),function(b){
    b.addEventListener('click',function(){
      paused=!paused; b.setAttribute('aria-pressed',paused);
      b.querySelector('[data-pause-label]').textContent=paused?'Play motion':'Pause motion';
      [].forEach.call(root.querySelectorAll('.dx-ribbon'),function(x){x.classList.toggle('is-paused',paused)});
    });
  });
  [].forEach.call(root.querySelectorAll('.dx-flips'),function(list){
    list.classList.add('is-live');
    var cards=list.querySelectorAll('.dx-flip');
    function set(card,on){
      card.classList.toggle('is-flipped',on);
      var f=card.querySelector('.dx-flip__front'), k=card.querySelector('.dx-flip__back');
      (on?f:k).setAttribute('inert',''); (on?k:f).removeAttribute('inert');
      [].forEach.call(card.querySelectorAll('.dx-flip__btn'),function(x){x.setAttribute('aria-expanded',on)});
    }
    [].forEach.call(cards,function(c){
      set(c,false);
      c.addEventListener('click',function(e){
        if(e.target.closest('a')) return;
        var on=!c.classList.contains('is-flipped'); set(c,on);
        if(e.detail===0){var t=c.querySelector(on?'.dx-flip__back .dx-flip__btn':'.dx-flip__front .dx-flip__btn'); if(t) t.focus();}
      });
    });
    if(!reduce&&cards[0]&&'IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){cards[0].classList.add('is-peek');io.disconnect();}},{threshold:.6});
      io.observe(cards[0]);
    }
  });
})(document.currentScript&&document.currentScript.closest('.dx'));
