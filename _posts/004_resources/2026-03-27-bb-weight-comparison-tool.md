---
layout: post
title: "BB weight comparison tool"
author: "adakar"
categories: resources
tags: [bb, weight, energy, joule, comparison, velocity, animation]
image: assets/images/004_resources/bbcomparisontool.jpeg
---

Compare how different BB weights travel over distance from the same muzzle energy. The race animation shows which BB arrives first — and the velocity chart shows exactly where a heavier BB overtakes a lighter one in speed.

Assumptions:
* Zero metres above sea level, standard air density (1.225 kg/m³)
* BB diameter 5.95mm, drag coefficient 0.47
* Lighter BBs leave the barrel faster but lose velocity more quickly over distance

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script type="text/javascript">
var K = 1.225 * 0.0000282743 * 0.47; // combined drag constant

function bbAlpha(w_g)          { return K / (2 * w_g / 1000); }
function bbV0(w_g, E)          { return Math.sqrt(E / (0.5 * w_g / 1000)); }
function bbVelAtDist(w_g,E,d)  { return bbV0(w_g,E) * Math.exp(-bbAlpha(w_g)*d); }
function bbTimeToDist(w_g,E,d) {
    var a=bbAlpha(w_g), v=bbV0(w_g,E);
    return (Math.exp(a*d)-1)/(v*a);
}
function bbDistAtTime(w_g,E,t) {
    var a=bbAlpha(w_g), v=bbV0(w_g,E);
    return Math.log(t*v*a+1)/a;
}
// Distance where heavier BB wh overtakes lighter BB wl in velocity (both in grams, wl < wh)
function velCrossoverDist(wl, wh) {
    var ml=wl/1000, mh=wh/1000;
    return Math.log(mh/ml) / (K*(1/ml-1/mh));
}

var COLORS=['#e74c3c','#3498db','#2ecc71','#f39c12','#9b59b6','#e67e22','#1abc9c','#e91e63'];
var animId=null, velChart=null;

function addWeight() {
    var c=document.getElementById("wt_rows");
    var n=c.children.length;
    if(n>=8){alert("Maximum 8 weights.");return;}
    var col=COLORS[n%COLORS.length];
    var div=document.createElement("div");
    div.style.cssText="display:flex;align-items:center;gap:6px;margin-bottom:6px;";
    div.innerHTML='<span style="width:11px;height:11px;border-radius:50%;background:'+col+
        ';flex-shrink:0;display:inline-block;"></span>'+
        '<input type="number" step="0.01" min="0.10" max="1.00" value="0.30" class="wt_inp" style="width:80px;"> g'+
        ' <button type="button" onclick="this.parentElement.remove();" style="padding:1px 7px;font-size:0.8em;cursor:pointer;">&#x2715;</button>';
    c.appendChild(div);
}

function getWeights() {
    return Array.from(document.querySelectorAll(".wt_inp"))
        .map(function(i){return parseFloat(i.value);})
        .filter(function(v){return !isNaN(v)&&v>0;})
        .sort(function(a,b){return a-b;});
}

function runComparison() {
    var E=parseFloat(document.getElementById("bb_energy").value);
    if(isNaN(E)||E<=0){alert("Enter a valid muzzle energy in joule.");return;}
    var ws=getWeights();
    if(ws.length<1){alert("Add at least one BB weight.");return;}

    // Find velocity crossover points for each lighter/heavier pair
    var cross=[];
    for(var i=0;i<ws.length-1;i++) {
        for(var j=i+1;j<ws.length;j++) {
            if(Math.abs(ws[i]-ws[j])<0.001) continue;
            var d=velCrossoverDist(ws[i],ws[j]);
            if(d>0&&d<=100) cross.push({l:ws[i],h:ws[j],d:d});
        }
    }

    var html="";
    if(cross.length) {
        html='<div style="margin:.6em 0;padding:.5em .9em;background:#0e1a0e;border-left:3px solid #2ecc71;font-size:.9em;">';
        cross.forEach(function(c){
            html+='<div style="margin:2px 0;">&#x26A1; <b>'+c.h.toFixed(2)+'g</b> becomes faster than <b>'+
                c.l.toFixed(2)+'g</b> at <b>'+c.d.toFixed(1)+'&nbsp;m</b></div>';
        });
        html+='</div>';
    }
    document.getElementById("cross_info").innerHTML=html;

    document.getElementById("res_section").style.display="block";
    startAnimation(ws,E,cross);
    drawVelChart(ws,E,cross);
}

// ── ANIMATION ────────────────────────────────────────────────────────────────

function startAnimation(ws,E,cross) {
    if(animId){cancelAnimationFrame(animId);animId=null;}
    var canvas=document.getElementById("race_canvas");
    var ctx=canvas.getContext("2d");

    var W=860, PL=68, PR=92, HEADER=28, FOOTER=24, LH=52;
    canvas.width=W;
    canvas.height=HEADER+ws.length*LH+FOOTER;
    var TW=W-PL-PR;

    var tMax=0;
    ws.forEach(function(w){tMax=Math.max(tMax,bbTimeToDist(w,E,100));});

    var ANIM_MS=5000; // total animation wall-clock duration in ms
    var arrived=ws.map(function(){return false;});
    var t0=null;

    function draw(ts) {
        if(!t0) t0=ts;
        var elapsed=ts-t0;
        var simT=(elapsed/ANIM_MS)*tMax; // simulated time in seconds

        // Background
        ctx.fillStyle="#111";
        ctx.fillRect(0,0,W,canvas.height);

        // Distance ruler
        ctx.fillStyle="#1c1c1c";
        ctx.fillRect(PL,0,TW,HEADER-3);
        ctx.font="10px monospace";
        ctx.textAlign="center";
        for(var m=0;m<=100;m+=10){
            var rx=PL+(m/100)*TW;
            ctx.strokeStyle="#303030";ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(rx,2);ctx.lineTo(rx,HEADER-3);ctx.stroke();
            ctx.fillStyle="#888";ctx.fillText(m+"m",rx,14);
        }

        // Finish line
        ctx.strokeStyle="rgba(255,255,255,0.3)";ctx.lineWidth=2;
        ctx.beginPath();ctx.moveTo(PL+TW,HEADER);ctx.lineTo(PL+TW,HEADER+ws.length*LH);ctx.stroke();

        // Velocity crossover markers (dashed green verticals)
        cross.forEach(function(c){
            var cx=PL+(c.d/100)*TW;
            ctx.save();
            ctx.strokeStyle="rgba(46,204,113,0.5)";
            ctx.setLineDash([4,3]);ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(cx,HEADER);ctx.lineTo(cx,HEADER+ws.length*LH);ctx.stroke();
            ctx.setLineDash([]);
            ctx.restore();
        });

        // Lanes and BB dots
        ws.forEach(function(w,i){
            var col=COLORS[i%COLORS.length];
            var ly=HEADER+i*LH;

            ctx.fillStyle=i%2?"#1a1a1a":"#161616";
            ctx.fillRect(0,ly,W,LH);

            // Weight label
            ctx.fillStyle=col;ctx.font="bold 13px monospace";ctx.textAlign="right";
            ctx.fillText(w.toFixed(2)+"g",PL-8,ly+LH/2+5);

            // Track line
            ctx.strokeStyle="#252525";ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(PL,ly+LH/2);ctx.lineTo(PL+TW,ly+LH/2);ctx.stroke();

            // BB position
            var dist=Math.min(bbDistAtTime(w,E,simT),100);
            if(dist>=100) arrived[i]=true;
            var bx=PL+(dist/100)*TW, by=ly+LH/2;

            // Trail
            if(bx>PL+2){
                ctx.save();
                ctx.globalAlpha=0.2;ctx.fillStyle=col;
                ctx.fillRect(Math.max(PL,bx-80),by-3,Math.min(80,bx-PL),6);
                ctx.restore();
            }

            // BB dot
            ctx.beginPath();ctx.arc(bx,by,5,0,2*Math.PI);ctx.fillStyle=col;ctx.fill();

            // Right side: show arrival time once done, otherwise current velocity
            ctx.font="11px monospace";ctx.textAlign="left";
            if(arrived[i]){
                ctx.fillStyle=col;
                ctx.fillText("\u2713 "+bbTimeToDist(w,E,100).toFixed(2)+"s",PL+TW+8,by+4);
            } else {
                ctx.fillStyle="#666";
                ctx.fillText(bbVelAtDist(w,E,dist).toFixed(1)+" m/s",PL+TW+8,by+4);
            }
        });

        // Elapsed time counter
        ctx.fillStyle="#444";ctx.font="11px monospace";ctx.textAlign="left";
        ctx.fillText("t = "+Math.min(simT,tMax).toFixed(2)+"s",PL,HEADER+ws.length*LH+18);

        if(elapsed < ANIM_MS*1.08){
            animId=requestAnimationFrame(draw);
        } else {
            animId=null;
            setTimeout(function(){ startAnimation(ws,E,cross); }, 1000);
        }
    }
    animId=requestAnimationFrame(draw);
}

// ── VELOCITY CHART ────────────────────────────────────────────────────────────

function drawVelChart(ws,E,cross) {
    var datasets=ws.map(function(w,i){
        var pts=[];
        for(var d=0;d<=100;d++) pts.push({x:d,y:+bbVelAtDist(w,E,d).toFixed(3)});
        return {label:w.toFixed(2)+"g",data:pts,
            borderColor:COLORS[i%COLORS.length],backgroundColor:"transparent",
            fill:false,tension:.1,pointRadius:0};
    });
    // Crossover annotation lines (hidden from legend/tooltip)
    cross.forEach(function(c,ci){
        datasets.push({
            label:"_x"+ci,
            data:[{x:c.d,y:0},{x:c.d,y:bbV0(c.l,E)*1.05}],
            borderColor:"rgba(46,204,113,0.5)",
            borderDash:[5,4],
            backgroundColor:"transparent",
            fill:false,pointRadius:0,borderWidth:1.5
        });
    });
    var ctx2=document.getElementById("vel_chart").getContext("2d");
    if(velChart) velChart.destroy();
    velChart=new Chart(ctx2,{
        type:"line",data:{datasets:datasets},
        options:{
            responsive:true,
            interaction:{mode:"index",intersect:false},
            scales:{
                x:{type:"linear",min:0,max:100,
                    title:{display:true,text:"Distance (m)",color:"#ccc"},
                    ticks:{color:"#ccc"},grid:{color:"rgba(255,255,255,0.06)"}},
                y:{min:0,
                    title:{display:true,text:"Velocity (m/s)",color:"#ccc"},
                    ticks:{color:"#ccc"},grid:{color:"rgba(255,255,255,0.06)"}}
            },
            plugins:{
                legend:{labels:{color:"#ccc",filter:function(item){
                    return !item.text.startsWith("_x");
                }}},
                tooltip:{callbacks:{label:function(c){
                    if(c.dataset.label.startsWith("_x")) return null;
                    return c.dataset.label+": "+c.parsed.y.toFixed(2)+" m/s";
                }}}
            }
        }
    });
}
</script>

<div style="margin-bottom:1.5em;">
  <b>Muzzle energy</b><br>
  <input type="number" step="0.05" min="0.1" max="5.0" value="0.9" id="bb_energy" style="width:90px;"> Joule
  <br><br>
  <b>BB weights to compare</b><br>
  <div id="wt_rows">
    <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;">
      <span style="width:11px;height:11px;border-radius:50%;background:#e74c3c;flex-shrink:0;display:inline-block;"></span>
      <input type="number" step="0.01" min="0.10" max="1.00" value="0.20" class="wt_inp" style="width:80px;"> g
    </div>
    <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;">
      <span style="width:11px;height:11px;border-radius:50%;background:#3498db;flex-shrink:0;display:inline-block;"></span>
      <input type="number" step="0.01" min="0.10" max="1.00" value="0.28" class="wt_inp" style="width:80px;"> g
    </div>
  </div>
  <button type="button" onclick="addWeight();" style="margin-right:8px;">+ Add weight</button>
  <button type="button" onclick="runComparison();">Run comparison</button>
</div>

<div id="cross_info"></div>

<div id="res_section" style="display:none;">
  <b>Travel time race &mdash; 0 to 100 m</b>
  <div style="font-size:0.82em;color:#888;margin-bottom:6px;">Time-compressed animation (fits to 5 s). Right column shows arrival time once a BB reaches 100 m, otherwise current velocity. Dashed green lines mark velocity crossover points.</div>
  <canvas id="race_canvas" style="width:100%;max-width:860px;display:block;border:1px solid #222;box-sizing:border-box;"></canvas>
  <br><br>
  <b>Velocity at distance</b>
  <div style="font-size:0.82em;color:#888;margin-bottom:6px;">After the dashed green crossover line, the heavier BB is travelling faster than the lighter one.</div>
  <canvas id="vel_chart" style="width:100%;max-width:860px;height:380px;"></canvas>
</div>

<br>

For muzzle velocity conversion see the [FPS to joule calculator](https://airsoftnorge.com/fps-to-joule-calculator/).
For residual energy at a specific distance see the [residual energy calculator](https://airsoftnorge.com/residual-energy-at-distance-calculator/).
For time to target comparisons see the [BB weight travel time chart](https://airsoftnorge.com/bb-weight-travel-time-chart/).
