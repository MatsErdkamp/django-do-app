import{r as u,o as d,a as w,b as m,c as f,d as t,t as p}from"./index-DS2--0Ft.js";const S={__name:"CounterView",setup(h){const c=u(0);function s(){var n=window.location.protocol==="https:"?"wss:":"ws:",e=window.location.host;(window.location.hostname==="localhost"||window.location.hostname==="127.0.0.1")&&(e="localhost:8000");var l="/ws/counter/",i=n+"//"+e+l;return new WebSocket(i)}let o=s();function a(){o.send(JSON.stringify({action:"increment"}))}function r(){o.send(JSON.stringify({action:"decrement"}))}return d(()=>{o.onopen=function(){console.log("WebSocket connected.")},o.onmessage=function(n){const e=JSON.parse(n.data);c.value=e.count},o.onerror=function(n){console.log("WebSocket Error: ",n)},o.onclose=function(n){console.log("WebSocket closed.")}}),w(()=>{o.close()}),(n,e)=>(m(),f("div",null,[t("h1",null,"Counter: "+p(c.value),1),t("button",{onClick:a},"Increment"),t("button",{onClick:r},"Decrement")]))}};export{S as default};