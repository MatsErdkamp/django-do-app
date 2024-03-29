import{_ as $,r as d,o as w,a as n,c as s,t as v,F as b,b as k,d as _,p as C,e as x,w as I,n as S,f as R,g as y}from"./index-Rck8z4VY.js";const N=c=>(C("data-v-07354cc4"),c=c(),x(),c),q=N(()=>_("h1",null,"Calendar Data",-1)),B={key:0},E={key:1,class:"error"},F={key:2},L={class:"calendar-item"},U={__name:"DashboardCalendar",setup(c){const p=d(null),a=d(!1),l=d(null),f={weekday:"long",year:"numeric",month:"long",day:"numeric",hour:"2-digit",minute:"2-digit"};function i(r){return new Intl.DateTimeFormat("en-US",f).format(new Date(r))}function e(r){let o="https://charging-twin-qw8ag.ondigitalocean.app";return(window.location.hostname==="localhost"||window.location.hostname==="127.0.0.1")&&(o="http://localhost:8000"),o+r}async function h(){a.value=!0;let r=e("/api/calendar/");try{const o=await fetch(r);if(!o.ok)throw new Error("Failed to fetch");const t=await o.json();p.value=t[0].google_response.items}catch(o){l.value=o.message}finally{a.value=!1}}return w(()=>{h()}),(r,o)=>(n(),s("div",null,[q,a.value?(n(),s("div",B,"Loading...")):l.value?(n(),s("div",E,v(l.value),1)):(n(),s("div",F,[(n(!0),s(b,null,k(p.value,t=>(n(),s("div",L,[_("h2",null,v(t.summary),1),_("div",null,v(i(t.start.dateTime)),1)]))),256))]))]))}},W=$(U,[["__scopeId","data-v-07354cc4"]]),D=c=>(C("data-v-aaf33a34"),c=c(),x(),c),H=D(()=>_("h1",null,"Battery State",-1)),T={key:0},j={key:1,class:"error"},M={key:2},O={class:"calendar-item"},P=D(()=>_("div",null,"NOT CONNECTED",-1)),V={style:{"border-top":"1px solid #212121","margin-top":"8px","padding-top":"4px"}},z=D(()=>_("div",null,"For 100% charge",-1)),J={__name:"DashboardBattery",props:{charge:Number,hours:Number},setup(c){const p=d(null),a=d(!1),l=d(null),f=c;async function i(){a.value=!0;try{const e=await fetch("http://127.0.0.1:8000/api/calendar/");if(!e.ok)throw new Error("Failed to fetch");const h=await e.json();p.value=h[0].google_response.items}catch(e){l.value=e.message}finally{a.value=!1}}return w(()=>{i()}),(e,h)=>(n(),s("div",null,[H,a.value?(n(),s("div",T,"Loading...")):l.value?(n(),s("div",j,v(l.value),1)):(n(),s("div",M,[_("div",O,[_("h2",null,v(f.charge)+"%",1),P,_("h2",V,v(f.hours)+" hours ",1),z])]))]))}},A=$(J,[["__scopeId","data-v-aaf33a34"]]),G=_("h1",null,"Charge Moments",-1),K={class:"charge-histogram"},Q={class:"charge-histogram-charging-indicator"},X=["onClick"],Y={__name:"DashboardHistogram",props:{hoursRequired:Number},setup(c){const p=d(10),a=d(!0),l=c;function f(t,u){return u==p.value?"background:orange;":t==!1?"background:red;":"background:green;"}d([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);function i(t){p.value=t,o()}function e(t){let u="https://charging-twin-qw8ag.ondigitalocean.app";return(window.location.hostname==="localhost"||window.location.hostname==="127.0.0.1")&&(u="http://localhost:8000"),u+t}const h=d(null),r=d(null);I(()=>l.hoursRequired,(t,u)=>{o()});async function o(){a.value=!0;let t=e("/api/curve/");try{const u=await fetch(t+"?deadline="+p.value+"&hours="+l.hoursRequired);if(!u.ok)throw new Error("Failed to fetch");const g=await u.json();r.value=g.best_options,h.value=g.scores.split(",").map(function(m){return parseInt(m,10)})}catch(u){u.value=u.message}finally{a.value=!1}}return w(()=>{o()}),(t,u)=>(n(),s("div",null,[G,_("div",K,[(n(!0),s(b,null,k(h.value,(g,m)=>(n(),s("div",{class:"price-bar",style:S({height:g+"%"})},null,4))),256))]),_("div",Q,[(n(!0),s(b,null,k(r.value,(g,m)=>(n(),s("div",{class:"charge-bar",style:S(f(g,m)),onClick:ee=>i(m)},null,12,X))),256))])]))}},Z={class:"dashboard-container"},ae={__name:"DashboardView",setup(c){function p(){var i=window.location.protocol==="https:"?"wss:":"ws:",e=window.location.host;(window.location.hostname==="localhost"||window.location.hostname==="127.0.0.1")&&(e="localhost:8000");var h="/ws/car/",r=i+"//"+e+h;return new WebSocket(r)}let a=p();const l=d(0),f=d(0);return w(()=>{a.onopen=function(){console.log("WebSocket connected.")},a.onmessage=function(i){var o,t;const e=JSON.parse(i.data);let h=(o=e==null?void 0:e.car)==null?void 0:o.battery_percentage;h!=null&&(l.value=h);let r=(t=e==null?void 0:e.car)==null?void 0:t.estimated_time_until_full;if(r!=null){let g=parseInt(r,10);f.value=g}},a.onerror=function(i){console.log("WebSocket Error: ",i)},a.onclose=function(i){console.log("WebSocket closed.")}}),R(()=>{a.close()}),(i,e)=>(n(),s("div",Z,[y(W,{class:"dashboard-item"}),y(A,{class:"dashboard-item",charge:l.value,hours:f.value},null,8,["charge","hours"]),y(Y,{class:"dashboard-item",hoursRequired:f.value},null,8,["hoursRequired"])]))}};export{ae as default};
