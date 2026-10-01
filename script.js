// Small progressive enhancement: reveal cards as they enter the viewport.
const items=document.querySelectorAll('.analysis-block,.chart-card,.kpi,.facility');
const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('show')}),{threshold:.08});
items.forEach(el=>{el.classList.add('reveal');observer.observe(el)});
