---
layout: post
title: "BB weight comparison tool"
author: "adakar"
categories: resources
tags: [bb, weight, energy, joule, comparison, velocity, animation]
image: assets/images/004_resources/bbcomparisontool.jpeg
---

Compare how different BB weights travel over distance from the same muzzle energy. The race animation runs in real time — the dashed markers show exactly where a heavier BB first catches up to the lighter one.

Assumptions:
* Zero metres above sea level, standard air density (1.225 kg/m³)
* BB diameter 5.95mm, drag coefficient 0.47
* Gravity and hopups are not real

<script type="text/javascript">
var K = 1.225 * 0.0000278051 * 0.47; // combined drag constant

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
// Distance where heavier BB wh first arrives at target before lighter BB wl (both in grams, wl < wh)
// Solved numerically: find d where bbTimeToDist(wl,d) == bbTimeToDist(wh,d)
// E cancels out — crossover distance is energy-independent
function arrivalCrossoverDist(wl, wh) {
    var ml=wl/1000, mh=wh/1000;
    var al=K/(2*ml), ah=K/(2*mh);
    function f(d) {
        return (Math.exp(al*d)-1)*Math.pow(ml,1.5) - (Math.exp(ah*d)-1)*Math.pow(mh,1.5);
    }
    // f(0)=0, initially negative (lighter arrives sooner); scan for sign change
    for(var d=0.5;d<=100;d+=0.5) {
        if(f(d)>=0) {
            var lo=d-0.5, hi=d;
            for(var i=0;i<50;i++){var mid=(lo+hi)/2; if(f(mid)<0) lo=mid; else hi=mid;}
            return (lo+hi)/2;
        }
    }
    return null; // no crossover within 100 m
}


var COLORS=['#e74c3c','#3498db','#2ecc71','#f39c12','#9b59b6','#e67e22','#1abc9c','#e91e63'];
var animId=null;

function addWeight() {
    var c=document.getElementById("wt_rows");
    var n=c.children.length;
    if(n>=8){alert("Maximum 8 weights.");return;}
    var col=COLORS[n%COLORS.length];
    var common=[0.20,0.23,0.25,0.28,0.30,0.32,0.36,0.40];
    var used=Array.from(document.querySelectorAll(".wt_inp")).map(function(inp){return parseFloat(inp.value);});
    var maxUsed=Math.max.apply(null,used);
    var def=null;
    for(var k=0;k<common.length;k++){
        if(common[k]>maxUsed+0.005&&!used.some(function(u){return Math.abs(u-common[k])<0.005;})){def=common[k];break;}
    }
    if(def===null){
        for(var k=0;k<common.length;k++){
            if(!used.some(function(u){return Math.abs(u-common[k])<0.005;})){def=common[k];break;}
        }
    }
    if(def===null) def=0.30;
    var div=document.createElement("div");
    div.style.cssText="display:flex;align-items:center;gap:6px;margin-bottom:6px;";
    div.setAttribute("data-ci", n);
    div.innerHTML='<span style="width:11px;height:11px;border-radius:50%;background:'+col+
        ';flex-shrink:0;display:inline-block;"></span>'+
        '<input type="number" step="0.01" min="0.10" max="1.00" value="'+def+'" class="wt_inp" style="width:80px;"> g'+
        ' <button type="button" class="rm_btn" onclick="removeWeight(this);" style="padding:1px 7px;font-size:0.8em;cursor:pointer;">&#x2715;</button>';
    c.appendChild(div);
    updateRemoveBtns();
}

function removeWeight(btn) {
    var c=document.getElementById("wt_rows");
    if(c.children.length<=2) return;
    btn.parentElement.remove();
    updateRemoveBtns();
}

function updateRemoveBtns() {
    var show=document.getElementById("wt_rows").children.length>2;
    Array.from(document.querySelectorAll(".rm_btn")).forEach(function(b){
        b.style.display=show?"":"none";
    });
}

function getWeights() {
    return Array.from(document.querySelectorAll(".wt_inp"))
        .map(function(inp){
            var ci=parseInt(inp.closest("[data-ci]").getAttribute("data-ci"),10);
            return {w: parseFloat(inp.value), ci: ci};
        })
        .filter(function(e){return !isNaN(e.w)&&e.w>0;})
        .sort(function(a,b){return a.w-b.w;});
}

function setEnergyMode(mode) {
    document.getElementById("energy_joule_row").style.display=mode==="joule"?"":"none";
    document.getElementById("energy_fps_row").style.display=mode==="fps"?"":"none";
    document.getElementById("mode_btn_joule").setAttribute("data-active", mode==="joule"?"1":"0");
    document.getElementById("mode_btn_fps").setAttribute("data-active", mode==="fps"?"1":"0");
    document.getElementById("mode_btn_joule").style.cssText=modeBtnStyle(mode==="joule");
    document.getElementById("mode_btn_fps").style.cssText=modeBtnStyle(mode==="fps");
}
function modeBtnStyle(active) {
    return "padding:3px 14px;font-size:.85em;cursor:pointer;"+
        (active ? "font-weight:bold;" : "");
}

function getEnergy() {
    if(document.getElementById("energy_fps_row").style.display!=="none") {
        var fps=parseFloat(document.getElementById("fps_value").value);
        var wg=parseFloat(document.getElementById("fps_weight").value);
        if(isNaN(fps)||fps<=0||isNaN(wg)||wg<=0) return NaN;
        var ms=fps/3.28084;
        return 0.5*(wg/1000)*ms*ms;
    }
    return parseFloat(document.getElementById("bb_energy").value);
}

function runComparison() {
    var E=getEnergy();
    if(isNaN(E)||E<=0){alert("Enter a valid muzzle energy in joule.");return;}
    var ws=getWeights();
    if(ws.length<1){alert("Add at least one BB weight.");return;}

    // Find arrival crossover points: distance beyond which heavier BB arrives at target first
    var cross=[];
    for(var i=0;i<ws.length-1;i++) {
        for(var j=i+1;j<ws.length;j++) {
            if(Math.abs(ws[i].w-ws[j].w)<0.001) continue;
            var d=arrivalCrossoverDist(ws[i].w,ws[j].w);
            if(d!==null) cross.push({l:ws[i].w,h:ws[j].w,d:d});
        }
    }

    var html="";
    if(cross.length) {
        html='<div style="margin:.6em 0;padding:.5em .9em;border-left:3px solid #817055;">';
        cross.forEach(function(c){
            html+='<div style="margin:2px 0;"><b>'+c.h.toFixed(2)+'g</b> arrives at target before <b>'+
                c.l.toFixed(2)+'g</b> beyond <b>'+c.d.toFixed(1)+'&nbsp;m</b></div>';
        });
        html+='</div>';
    }
    document.getElementById("cross_info").innerHTML=html;

    document.getElementById("res_section").style.display="block";
    startAnimation(ws,E,cross);
}

// ── ANIMATION ────────────────────────────────────────────────────────────────

function startAnimation(ws,E,cross) {
    if(animId){cancelAnimationFrame(animId);animId=null;}
    var replayBtn=document.getElementById("replay_btn");
    var runBtn=document.getElementById("run_btn");
    replayBtn.style.display="none";
    runBtn.style.display="none";
    replayBtn.onclick=function(){ startAnimation(ws,E,cross); };
    runBtn.onclick=function(){ runComparison(); };
    var canvas=document.getElementById("race_canvas");
    var ctx=canvas.getContext("2d");

    var W=860, PL=68, PR=92, HEADER=28, FOOTER=24, LH=56;
    canvas.width=W;
    canvas.height=HEADER+ws.length*LH+FOOTER;
    var TW=W-PL-PR;

    var tMax=0;
    ws.forEach(function(e){tMax=Math.max(tMax,bbTimeToDist(e.w,E,100));});

    // Pre-compute time to each 10 m milestone (10–90 m) per BB
    var milestones=[10,20,30,40,50,60,70,80,90];
    var mTimes=ws.map(function(e){
        return milestones.map(function(m){return bbTimeToDist(e.w,E,m);});
    });

    var arrived=ws.map(function(){return false;});
    var t0=null;

    function draw(ts) {
        if(!t0) t0=ts;
        var elapsed=ts-t0;
        var simT=elapsed/1000; // real time in seconds

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

        // Arrival crossover markers
        cross.forEach(function(c){
            var cx=PL+(c.d/100)*TW;
            ctx.save();
            ctx.strokeStyle="rgba(174,151,114,0.5)";
            ctx.setLineDash([4,3]);ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(cx,HEADER);ctx.lineTo(cx,HEADER+ws.length*LH);ctx.stroke();
            ctx.setLineDash([]);
            ctx.restore();
        });

        // Lanes and BB dots
        ws.forEach(function(e,i){
            var col=COLORS[e.ci%COLORS.length];
            var ly=HEADER+i*LH;

            ctx.fillStyle=i%2?"#1a1a1a":"#161616";
            ctx.fillRect(0,ly,W,LH);

            // Weight label
            ctx.fillStyle=col;ctx.font="bold 13px monospace";ctx.textAlign="right";
            ctx.fillText(e.w.toFixed(2)+"g",PL-8,ly+LH/2+5);

            // Track line
            ctx.strokeStyle="#252525";ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(PL,ly+LH/2);ctx.lineTo(PL+TW,ly+LH/2);ctx.stroke();

            // BB position
            var dist=Math.min(bbDistAtTime(e.w,E,simT),100);
            if(dist>=100) arrived[i]=true;
            var bx=PL+(dist/100)*TW, by=ly+LH/2;

            // Trail
            if(bx>PL+2){
                ctx.save();
                ctx.globalAlpha=0.2;ctx.fillStyle=col;
                ctx.fillRect(Math.max(PL,bx-80),by-3,Math.min(80,bx-PL),6);
                ctx.restore();
            }

            // Time-to-target labels at each 10 m milestone (appear as BB passes)
            ctx.save();
            ctx.font="8px monospace";ctx.textAlign="center";
            ctx.globalAlpha=0.65;ctx.fillStyle=col;
            for(var k=0;k<milestones.length;k++){
                if(simT>=mTimes[i][k]){
                    ctx.fillText(mTimes[i][k].toFixed(2)+"s",PL+(milestones[k]/100)*TW,by+17);
                }
            }
            ctx.restore();

            // BB dot
            ctx.beginPath();ctx.arc(bx,by,5,0,2*Math.PI);ctx.fillStyle=col;ctx.fill();

            // Right side: show arrival time once done, otherwise current velocity
            ctx.font="11px monospace";ctx.textAlign="left";
            if(arrived[i]){
                ctx.fillStyle=col;
                ctx.fillText("\u2713 "+bbTimeToDist(e.w,E,100).toFixed(2)+"s",PL+TW+8,by+4);
            } else {
                ctx.fillStyle="#666";
                ctx.fillText(bbVelAtDist(e.w,E,dist).toFixed(1)+" m/s",PL+TW+8,by+4);
            }
        });

        // Elapsed time counter
        ctx.fillStyle="#444";ctx.font="11px monospace";ctx.textAlign="left";
        ctx.fillText("t = "+Math.min(simT,tMax).toFixed(2)+"s",PL,HEADER+ws.length*LH+18);

        if(simT < tMax){
            animId=requestAnimationFrame(draw);
        } else {
            animId=null;
            replayBtn.style.display="";
            runBtn.style.display="";
        }
    }
    animId=requestAnimationFrame(draw);
}

</script>

<div style="margin-bottom:1.5em;">
  <b>Muzzle energy</b><br>
  <div style="display:inline-flex;border-radius:4px;overflow:hidden;margin:6px 0 8px;">
    <button id="mode_btn_joule" type="button" onclick="setEnergyMode('joule');" style="padding:3px 14px;font-size:.85em;cursor:pointer;font-weight:bold;">Joule</button>
    <button id="mode_btn_fps" type="button" onclick="setEnergyMode('fps');" style="padding:3px 14px;font-size:.85em;cursor:pointer;">FPS</button>
  </div><br>
  <div id="energy_joule_row">
    <input type="number" step="0.05" min="0.1" max="5.0" value="0.9" id="bb_energy" style="width:90px;"> Joule
  </div>
  <div id="energy_fps_row" style="display:none;">
    <input type="number" step="1" min="1" max="999" value="328" id="fps_value" style="width:75px;"> FPS &nbsp;using a
    <input type="number" step="0.01" min="0.10" max="1.00" value="0.20" id="fps_weight" style="width:70px;"> g reference BB
  </div>
  <br>
  <b>BB weights to compare</b><br>
  <div id="wt_rows">
    <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;" data-ci="0">
      <span style="width:11px;height:11px;border-radius:50%;background:#e74c3c;flex-shrink:0;display:inline-block;"></span>
      <input type="number" step="0.01" min="0.10" max="1.00" value="0.20" class="wt_inp" style="width:80px;"> g
      <button type="button" class="rm_btn" onclick="removeWeight(this);" style="padding:1px 7px;font-size:0.8em;cursor:pointer;display:none;">&#x2715;</button>
    </div>
    <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;" data-ci="1">
      <span style="width:11px;height:11px;border-radius:50%;background:#3498db;flex-shrink:0;display:inline-block;"></span>
      <input type="number" step="0.01" min="0.10" max="1.00" value="0.30" class="wt_inp" style="width:80px;"> g
      <button type="button" class="rm_btn" onclick="removeWeight(this);" style="padding:1px 7px;font-size:0.8em;cursor:pointer;display:none;">&#x2715;</button>
    </div>
  </div>
  <button type="button" onclick="addWeight();" style="margin-right:8px;">+ Add weight</button>
  <button type="button" onclick="runComparison();">Run comparison</button>
</div>

<div id="cross_info"></div>

<div id="res_section" style="display:none;">
  <b>Travel time race - 0 to 100 m</b>
  <p>Real-time animation. Each time-to-target label appears at its 10 m marker as the BB passes it. Right column shows total travel time once a BB reaches 100 m. Dashed lines mark where the heavier BB begins arriving at targets first.</p>
  <canvas id="race_canvas" style="width:100%;max-width:860px;display:block;border:1px solid #222;box-sizing:border-box;"></canvas>
  <div style="margin-top:6px;">
    <button type="button" id="replay_btn" style="display:none;margin-right:8px;">Replay</button>
    <button type="button" id="run_btn" style="display:none;">Run</button>
  </div>
</div>

<br>


Relevant links:
* [FPS to joule calculator](https://airsoftnorge.com/fps-to-joule-calculator/).
* [residual energy calculator](https://airsoftnorge.com/residual-energy-at-distance-calculator/).
* [BB weight travel time chart](https://airsoftnorge.com/bb-weight-travel-time-chart/).
