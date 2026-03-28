---
layout: post
title: "BB weight comparison tool"
author: "adakar"
categories: resources
tags: [bb, weight, energy, joule, comparison, velocity, animation]
image: assets/images/004_resources/bbcomparisontool.jpeg
---

Compare how different BB weights travel over distance from the same muzzle energy. 

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

// ── WIND DEFLECTION PHYSICS ──────────────────────────────────────────────────
// 2D RK4 trajectory under WIND_SPEED m/s direct crosswind.
// Stops when x >= maxDist or lateral |y| >= DEFLECT_LIMIT.
function computeWindTrajectory(w_g, E, maxDist, windSpeed, deflectLimit) {
    var m=w_g/1000, kd=K/(2*m), Vw=windSpeed, dt=0.005;
    var pts=[{t:0,x:0,y:0}];
    var t=0,x=0,y=0,vx=bbV0(w_g,E),vy=0;
    function accel(vx_,vy_){
        var vxr=vx_,vyr=vy_-Vw,vr=Math.sqrt(vxr*vxr+vyr*vyr);
        return {ax:-kd*vr*vxr,ay:-kd*vr*vyr};
    }
    for(var n=0;n<200000;n++){
        var a1=accel(vx,vy);
        var tvx2=vx+0.5*dt*a1.ax,tvy2=vy+0.5*dt*a1.ay;
        var a2=accel(tvx2,tvy2);
        var tvx3=vx+0.5*dt*a2.ax,tvy3=vy+0.5*dt*a2.ay;
        var a3=accel(tvx3,tvy3);
        var tvx4=vx+dt*a3.ax,tvy4=vy+dt*a3.ay;
        var a4=accel(tvx4,tvy4);
        x+=dt/6*(vx+2*tvx2+2*tvx3+tvx4);
        y+=dt/6*(vy+2*tvy2+2*tvy3+tvy4);
        vx+=dt/6*(a1.ax+2*a2.ax+2*a3.ax+a4.ax);
        vy+=dt/6*(a1.ay+2*a2.ay+2*a3.ay+a4.ay);
        t+=dt;
        pts.push({t:t,x:x,y:y});
        if(x>=maxDist||Math.abs(y)>=deflectLimit) break;
    }
    return pts;
}

// Interpolate {x,y} at simT using binary search
function windTrajAtTime(pts,simT) {
    if(!pts.length) return {x:0,y:0};
    var last=pts[pts.length-1];
    if(simT>=last.t) return {x:last.x,y:last.y};
    var lo=0,hi=pts.length-1;
    while(hi-lo>1){var mid=(lo+hi)>>1;if(pts[mid].t<=simT)lo=mid;else hi=mid;}
    var f=(simT-pts[lo].t)/(pts[hi].t-pts[lo].t);
    return {x:pts[lo].x+f*(pts[hi].x-pts[lo].x),y:pts[lo].y+f*(pts[hi].y-pts[lo].y)};
}

// {t,y} where trajectory first crosses each milestone x, or null if not reached
function windMilestones(pts,mxs) {
    return mxs.map(function(mx){
        for(var i=1;i<pts.length;i++){
            if(pts[i].x>=mx){
                var f=(mx-pts[i-1].x)/(pts[i].x-pts[i-1].x);
                return {t:pts[i-1].t+f*(pts[i].t-pts[i-1].t),y:pts[i-1].y+f*(pts[i].y-pts[i-1].y)};
            }
        }
        return null;
    });
}


var COLORS=['#e74c3c','#3498db','#2ecc71','#f39c12','#9b59b6','#e67e22','#1abc9c','#e91e63'];
var animId=null;
var windAnimId=null;
function addWeight() {
    var c=document.getElementById("wt_rows");
    var n=c.children.length;
    if(n>=8){alert("Maximum 8 weights.");return;}
    // Pick the lowest color index not already in use by an existing row
    var usedCi=Array.from(c.querySelectorAll("[data-ci]")).map(function(el){
        return parseInt(el.getAttribute("data-ci"),10);
    });
    var ci=0;
    while(usedCi.indexOf(ci)!==-1) ci++;
    var col=COLORS[ci%COLORS.length];
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
    div.setAttribute("data-ci", ci);
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

function updateWindHelp() {
    var sel=document.getElementById("wind_type_sel");
    var opt=sel.options[sel.selectedIndex];
    document.getElementById("wind_type_help").textContent=opt.getAttribute("data-desc");
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
    document.getElementById("wind_section").style.display="block";
    var windSpeed=parseFloat(document.getElementById("wind_type_sel").value);
    var deflectLimit=parseFloat(document.getElementById("deflect_limit_slider").value)/100;
    startAnimation(ws,E,cross);
    startWindAnimation(ws,E,windSpeed,deflectLimit);
}

// ── ANIMATION ────────────────────────────────────────────────────────────────

function startAnimation(ws,E,cross) {
    if(animId){cancelAnimationFrame(animId);animId=null;}
    var replayBtn=document.getElementById("replay_btn");
    var runBtn=document.getElementById("run_btn");
    replayBtn.onclick=function(){ startAnimation(ws,E,cross); };
    runBtn.onclick=function(){ runComparison(); };
    var canvas=document.getElementById("race_canvas");
    var ctx=canvas.getContext("2d");

    var W=860, PL=68, PR=20, HEADER=28, FOOTER=24, LH=66;
    canvas.width=W;
    canvas.height=HEADER+ws.length*LH+FOOTER;
    var TW=W-PL-PR;

    var tMax=0;
    ws.forEach(function(e){tMax=Math.max(tMax,bbTimeToDist(e.w,E,100));});

    // Pre-compute time to each 10 m milestone (10–100 m) per BB
    var milestones=[10,20,30,40,50,60,70,80,90,100];
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
            ctx.font="12px monospace";ctx.textAlign="center";
            ctx.globalAlpha=0.9;ctx.fillStyle=col;
            for(var k=0;k<milestones.length;k++){
                if(simT>=mTimes[i][k]){
                    ctx.fillText(mTimes[i][k].toFixed(2)+"s",PL+(milestones[k]/100)*TW,by+22);
                }
            }
            ctx.restore();

            // BB dot
            ctx.beginPath();ctx.arc(bx,by,5,0,2*Math.PI);ctx.fillStyle=col;ctx.fill();
        });

        // Elapsed time counter
        ctx.fillStyle="#444";ctx.font="11px monospace";ctx.textAlign="left";
        ctx.fillText("t = "+Math.min(simT,tMax).toFixed(2)+"s",PL,HEADER+ws.length*LH+18);

        if(simT < tMax){
            animId=requestAnimationFrame(draw);
        } else {
            animId=null;
        }
    }
    animId=requestAnimationFrame(draw);
}

// ── WIND DEFLECTION ANIMATION ────────────────────────────────────────────────
function startWindAnimation(ws,E,windSpeed,deflectLimit) {
    if(windAnimId){cancelAnimationFrame(windAnimId);windAnimId=null;}
    var replayBtn=document.getElementById("wind_replay_btn");
    var windRunBtn=document.getElementById("wind_run_btn");
    replayBtn.onclick=function(){
        var spd=parseFloat(document.getElementById("wind_type_sel").value);
        var dl=parseFloat(document.getElementById("deflect_limit_slider").value)/100;
        startWindAnimation(ws,E,spd,dl);
    };
    windRunBtn.onclick=function(){ runComparison(); };
    var maxDist=100;
    var canvas=document.getElementById("wind_canvas");
    var ctx=canvas.getContext("2d");
    var W=860,PL=68,PR=20,HEADER=28,FOOTER=24,LH=66;
    canvas.width=W;
    canvas.height=HEADER+ws.length*LH+FOOTER;
    var TW=W-PL-PR;

    var trajs=ws.map(function(e){return computeWindTrajectory(e.w,E,maxDist,windSpeed,deflectLimit);});
    var milestoneXs=[];
    for(var m=10;m<=maxDist;m+=10) milestoneXs.push(m);
    var mData=trajs.map(function(pts){return windMilestones(pts,milestoneXs);});
    var tMax=0;
    trajs.forEach(function(pts){if(pts.length)tMax=Math.max(tMax,pts[pts.length-1].t);});

    var t0=null;
    function draw(ts){
        if(!t0) t0=ts;
        var simT=(ts-t0)/1000;

        ctx.fillStyle="#111";
        ctx.fillRect(0,0,W,canvas.height);

        // Distance ruler
        ctx.fillStyle="#1c1c1c";
        ctx.fillRect(PL,0,TW,HEADER-3);
        ctx.font="10px monospace";ctx.textAlign="center";
        for(var m=0;m<=maxDist;m+=10){
            var rx=PL+(m/maxDist)*TW;
            ctx.strokeStyle="#303030";ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(rx,2);ctx.lineTo(rx,HEADER-3);ctx.stroke();
            ctx.fillStyle="#888";ctx.fillText(m+"m",rx,14);
        }

        // Finish line
        ctx.strokeStyle="rgba(255,255,255,0.3)";ctx.lineWidth=2;
        ctx.beginPath();ctx.moveTo(PL+TW,HEADER);ctx.lineTo(PL+TW,HEADER+ws.length*LH);ctx.stroke();

        ws.forEach(function(e,i){
            var col=COLORS[e.ci%COLORS.length];
            var ly=HEADER+i*LH;
            var cy=ly+LH/2;
            var halfLane=Math.floor(LH/2)-5;
            var pxPerMeter=halfLane/deflectLimit;

            ctx.fillStyle=i%2?"#1a1a1a":"#161616";
            ctx.fillRect(0,ly,W,LH);

            // drift limit line
            ctx.save();
            ctx.strokeStyle="rgba(200,60,60,0.3)";ctx.lineWidth=1;ctx.setLineDash([3,3]);
            ctx.beginPath();ctx.moveTo(PL,cy+halfLane);ctx.lineTo(PL+TW,cy+halfLane);ctx.stroke();
            ctx.setLineDash([]);
            ctx.restore();

            // Weight label
            ctx.fillStyle=col;ctx.font="bold 13px monospace";ctx.textAlign="right";
            ctx.fillText(e.w.toFixed(2)+"g",PL-8,cy+5);

            // Zero-drift centre line
            ctx.strokeStyle="#2a2a2a";ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(PL,cy);ctx.lineTo(PL+TW,cy);ctx.stroke();

            var tPts=trajs[i];
            var lastPt=tPts[tPts.length-1];
            var hitDrift=Math.abs(lastPt.y)>=deflectLimit-0.001;
            var pos=windTrajAtTime(tPts,simT);
            var clampY=Math.min(deflectLimit,Math.max(-deflectLimit,pos.y));
            var bx=PL+(Math.min(pos.x,maxDist)/maxDist)*TW;
            var by=cy+clampY*pxPerMeter;

            // Curved trail
            if(tPts.length>1){
                ctx.save();
                ctx.strokeStyle=col;ctx.lineWidth=1.5;ctx.globalAlpha=0.5;
                ctx.beginPath();
                var started=false;
                for(var k=0;k<tPts.length;k++){
                    if(tPts[k].t>simT+0.001) break;
                    var tx=PL+(tPts[k].x/maxDist)*TW;
                    var ty=cy+Math.min(deflectLimit,tPts[k].y)*pxPerMeter;
                    if(!started){ctx.moveTo(tx,ty);started=true;}
                    else ctx.lineTo(tx,ty);
                }
                ctx.stroke();
                ctx.restore();
            }

            // Deflection labels at milestones (appear as BB passes each)
            ctx.save();
            ctx.font="11px monospace";ctx.textAlign="center";ctx.globalAlpha=0.9;ctx.fillStyle=col;
            for(var k=0;k<milestoneXs.length;k++){
                var mp=mData[i][k];
                if(mp&&simT>=mp.t){
                    var lx=PL+(milestoneXs[k]/maxDist)*TW;
                    var dc=Math.abs(mp.y)*100;
                    var lbl=dc<100?dc.toFixed(1)+"cm":(Math.abs(mp.y)).toFixed(2)+"m";
                    ctx.fillText(lbl,lx,cy-17);
                }
            }
            ctx.restore();

            // BB dot, or × at drift cutoff
            if(simT>=lastPt.t&&hitDrift){
                ctx.save();
                ctx.strokeStyle=col;ctx.lineWidth=2;
                ctx.beginPath();
                ctx.moveTo(bx-5,by-5);ctx.lineTo(bx+5,by+5);
                ctx.moveTo(bx+5,by-5);ctx.lineTo(bx-5,by+5);
                ctx.stroke();
                ctx.restore();
            } else {
                ctx.beginPath();ctx.arc(bx,by,5,0,2*Math.PI);ctx.fillStyle=col;ctx.fill();
            }
        });

        // Elapsed time
        ctx.fillStyle="#444";ctx.font="11px monospace";ctx.textAlign="left";
        ctx.fillText("t = "+Math.min(simT,tMax).toFixed(2)+"s",PL,HEADER+ws.length*LH+18);

        if(simT<tMax){
            windAnimId=requestAnimationFrame(draw);
        } else {
            windAnimId=null;
        }
    }
    windAnimId=requestAnimationFrame(draw);
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
  <canvas id="race_canvas" style="width:100%;max-width:860px;display:block;border:1px solid #222;box-sizing:border-box;"></canvas>
  <div style="margin-top:6px;">
    <button type="button" id="replay_btn" style="margin-right:8px;">Replay</button>
    <button type="button" id="run_btn">Recalculate</button>
  </div>
</div>

<div id="wind_section" style="display:none;margin-top:2em;">
  <b>Wind deflection with direct crosswind</b>
  <p>Lane centre is the zero-drift flight path. The BB stops when lateral drift reaches the deflection cutoff.</p>
  <div style="margin-bottom:10px;">
    Wind condition:
    <select id="wind_type_sel" onchange="updateWindHelp();" style="margin-left:4px;">
      <option value="0.9" data-desc="You can see wind direction from smoke drift." selected>Light air (0.3–1.5 m/s)</option>
      <option value="2.5" data-desc="You can feel the wind. Leaves on trees move, wind can lift small pennants.">Light breeze (1.6–3.3 m/s)</option>
      <option value="4.4" data-desc="Leaves and small twigs move. Wind extends light flags and pennants.">Gentle breeze (3.4–5.4 m/s)</option>
      <option value="6.7" data-desc="Wind lifts dust and loose papers, moves twigs and small branches, extends larger flags.">Moderate breeze (5.5–7.9 m/s)</option>
      <option value="9.4" data-desc="Small leafy trees begin to sway. On water, small waves begin to crest.">Fresh breeze (8.0–10.7 m/s)</option>
    </select>
    <span id="wind_type_help" style="margin-left:8px;font-size:.85em;">You can see wind direction from smoke drift.</span>
  </div>
  <div style="margin-bottom:10px;">
    Deflection cutoff (default 30cm as this will be off target if you aim center mass):
    <input type="range" id="deflect_limit_slider" min="10" max="300" step="10" value="30"
      style="width:180px;vertical-align:middle;"
      oninput="document.getElementById('deflect_limit_label').textContent=this.value+' cm';">
    <span id="deflect_limit_label">30 cm</span>
  </div>
  <canvas id="wind_canvas" style="width:100%;max-width:860px;display:block;border:1px solid #222;box-sizing:border-box;"></canvas>
  <div style="margin-top:6px;">
    <button type="button" id="wind_replay_btn" style="margin-right:8px;">Replay</button>
    <button type="button" id="wind_run_btn">Recalculate</button>
  </div>
</div>

<br>


Relevant links:
* [FPS to joule calculator](https://airsoftnorge.com/fps-to-joule-calculator/).
* [Residual energy calculator](https://airsoftnorge.com/residual-energy-calculator).
* [BB weight travel time chart](https://airsoftnorge.com/bbweighttraveltime/).
