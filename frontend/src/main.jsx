import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, BadgeCheck, Brain, Camera, Compass, Gauge, Image, Layers3, LineChart as LineIcon, MousePointerClick, Search, Settings2, Sparkles, Target } from 'lucide-react';
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Cell, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import './styles.css';

const pages = ['Overview', 'Search Studio', 'Recommendations', 'Embedding Explorer', 'Ranking Controls', 'Personalization', 'Analytics', 'Evaluation'];
const catalog = [
  {id:'SKU-101',title:'Premium travel backpack',category:'Travel',score:0.94,tags:['durable','waterproof','laptop'],color:'#38bdf8'},
  {id:'SKU-221',title:'Minimal running shoes',category:'Sports',score:0.88,tags:['lightweight','training','comfort'],color:'#a78bfa'},
  {id:'SKU-332',title:'Smart noise headphones',category:'Electronics',score:0.84,tags:['audio','wireless','premium'],color:'#22c55e'},
  {id:'SKU-410',title:'Organic cotton hoodie',category:'Fashion',score:0.79,tags:['soft','casual','winter'],color:'#f59e0b'}
];
const trend = [{d:'Mon',ctr:7.1,latency:142},{d:'Tue',ctr:7.8,latency:137},{d:'Wed',ctr:8.4,latency:129},{d:'Thu',ctr:8.9,latency:121},{d:'Fri',ctr:9.6,latency:118}];
const mix = [{name:'Text',value:52,color:'#38bdf8'},{name:'Image',value:21,color:'#a78bfa'},{name:'Hybrid',value:27,color:'#22c55e'}];
const evalRows = [
  ['EXP-118','hybrid-v3','NDCG@10','0.842','winner'],
  ['EXP-119','text-only-v2','NDCG@10','0.791','baseline'],
  ['EXP-120','image-v1','Recall@20','0.764','watch'],
  ['EXP-121','personalized-v4','CTR lift','+12.4%','winner']
];

function fallbackSearch(form){
  const query = form.query.toLowerCase();
  const ranked = catalog.map(item => {
    let score = item.score;
    if (query.includes(item.category.toLowerCase())) score += 0.04;
    if (item.tags.some(t => query.includes(t))) score += 0.05;
    if (form.mode === 'hybrid') score += 0.03;
    return {...item, score: Math.min(score, 0.99), reason: `${form.mode} match using category, tags, and metadata affinity`};
  }).sort((a,b)=>b.score-a.score);
  return { request_id:`SRCH-${Date.now().toString().slice(-5)}`, ranking_version:'hybrid-ranker-v3', latency_ms:118, results:ranked };
}
function fallbackRecommend(form){
  return { request_id:`REC-${Date.now().toString().slice(-5)}`, ranking_version:'affinity-rec-v2', latency_ms:104, results: catalog.map((item,i)=>({...item, score: Math.max(0.72, item.score - i*0.03), reason:`Recommended from ${form.user_segment} affinity and ${form.seed_item} similarity`})) };
}

function App(){
  const [active,setActive] = useState('Overview');
  const [searchForm,setSearchForm] = useState({query:'waterproof premium travel laptop backpack',mode:'hybrid',category:'Travel'});
  const [recForm,setRecForm] = useState({user_segment:'premium travelers',seed_item:'SKU-101'});
  const [searchResult,setSearchResult] = useState(fallbackSearch(searchForm));
  const [recResult,setRecResult] = useState(fallbackRecommend(recForm));
  const metrics = useMemo(()=>[
    ['Search Requests','2.8M','+24%',Search],['CTR Lift','12.4%','+3.6%',MousePointerClick],['Avg Latency','118ms','-17%',Gauge],['Ranking Quality','0.842','+0.05',BadgeCheck]
  ],[]);
  const runSearch = async()=>{try{const r=await fetch('/search',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(searchForm)});if(!r.ok)throw new Error('offline');setSearchResult(await r.json());}catch{setSearchResult(fallbackSearch(searchForm));}};
  const runRecommend = async()=>{try{const r=await fetch('/recommend',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(recForm)});if(!r.ok)throw new Error('offline');setRecResult(await r.json());}catch{setRecResult(fallbackRecommend(recForm));}};
  return <main className="app-shell"><aside className="sidebar"><div className="brand"><Compass/><div><strong>DiscoveryAI</strong><span>Multimodal Search Cloud</span></div></div>{pages.map(p=><button className={active===p?'active':''} onClick={()=>setActive(p)} key={p}>{p}</button>)}</aside><section className="workspace"><header className="topbar"><div><p className="eyebrow">AI discovery and recommendations</p><h1>{active}</h1></div><button onClick={active==='Recommendations'?runRecommend:runSearch}>Run ranking</button></header>{active==='Overview'&&<Overview metrics={metrics}/>} {active==='Search Studio'&&<SearchStudio form={searchForm} setForm={setSearchForm} result={searchResult} runSearch={runSearch}/>} {active==='Recommendations'&&<Recommendations form={recForm} setForm={setRecForm} result={recResult} runRecommend={runRecommend}/>} {active==='Embedding Explorer'&&<EmbeddingExplorer/>} {active==='Ranking Controls'&&<RankingControls/>} {active==='Personalization'&&<Personalization/>} {active==='Analytics'&&<Analytics/>} {active==='Evaluation'&&<Evaluation/>}</section></main>;
}
function Overview({metrics}){return <><section className="metrics">{metrics.map(([l,v,d,Icon])=><article className="card" key={l}><Icon/><span>{l}</span><strong>{v}</strong><small>{d}</small></article>)}</section><section className="grid"><Panel title="CTR and latency" icon={<Activity/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={trend}><CartesianGrid strokeDasharray="3 3" stroke="#26374a"/><XAxis dataKey="d" stroke="#9badc1"/><YAxis stroke="#9badc1"/><Tooltip/><Area dataKey="ctr" stroke="#22c55e" fill="#14532d"/><Area dataKey="latency" stroke="#38bdf8" fill="#0e7490"/></AreaChart></ResponsiveContainer></Panel><Panel title="Query modality mix" icon={<Layers3/>}><ResponsiveContainer width="100%" height={260}><PieChart><Pie data={mix} dataKey="value" nameKey="name" outerRadius={92}>{mix.map(m=><Cell key={m.name} fill={m.color}/>)}</Pie><Tooltip/></PieChart></ResponsiveContainer></Panel></section></>}
function SearchStudio({form,setForm,result,runSearch}){return <section className="grid"><Panel title="Multimodal search input" icon={<Search/>}>{Object.entries(form).map(([k,v])=><label key={k}>{k.replaceAll('_',' ')}<input value={v} onChange={e=>setForm({...form,[k]:e.target.value})}/></label>)}<button onClick={runSearch}>Search catalog</button></Panel><ResultsPanel title="Ranked search results" result={result}/></section>}
function Recommendations({form,setForm,result,runRecommend}){return <section className="grid"><Panel title="Recommendation context" icon={<Sparkles/>}>{Object.entries(form).map(([k,v])=><label key={k}>{k.replaceAll('_',' ')}<input value={v} onChange={e=>setForm({...form,[k]:e.target.value})}/></label>)}<button onClick={runRecommend}>Generate recommendations</button></Panel><ResultsPanel title="Personalized recommendations" result={result}/></section>}
function ResultsPanel({title,result}){return <Panel title={title} icon={<Target/>}><div className="summary"><strong>{result.request_id}</strong><span>{result.ranking_version} · {result.latency_ms}ms</span></div><div className="cards">{(result.results||[]).map(item=><div className="product" key={item.id}><div style={{background:item.color}}></div><strong>{item.title}</strong><span>{item.category} · score {Number(item.score).toFixed(2)}</span><small>{item.reason}</small></div>)}</div></Panel>}
function EmbeddingExplorer(){return <section className="grid"><Panel title="Embedding space" icon={<Brain/>}><div className="embedding-grid">{catalog.map((item,i)=><div className="dot" style={{left:`${18+i*19}%`,top:`${24+(i%2)*32}%`,background:item.color}} key={item.id}><span>{item.id}</span></div>)}</div></Panel><Panel title="Similarity explanation" icon={<Image/>}><div className="reason">Text, tags, category metadata, and image descriptors are projected into a shared similarity space.</div><div className="reason">Hybrid queries blend keyword and semantic ranking signals.</div><div className="reason">Result explanations describe why each item was retrieved.</div></Panel></section>}
function RankingControls(){return <section className="grid"><Panel title="Ranking weights" icon={<Settings2/>}><div className="reason">Text relevance weight: 45%</div><div className="reason">Image similarity weight: 25%</div><div className="reason">Personalization weight: 20%</div><div className="reason">Freshness and availability weight: 10%</div></Panel><Panel title="Business guardrails" icon={<BadgeCheck/>}><div className="reason">Inactive catalog items are filtered.</div><div className="reason">Tenant-specific inventory and metadata controls apply.</div><div className="reason">Diversity constraints prevent duplicate result clusters.</div></Panel></section>}
function Personalization(){return <section className="grid"><Panel title="User affinity profile" icon={<Camera/>}><div className="reason">Premium traveler: backpacks, headphones, durable accessories.</div><div className="reason">Sports buyer: shoes, breathable apparel, fitness gear.</div><div className="reason">Fashion explorer: hoodies, seasonal styles, soft materials.</div></Panel><Panel title="Next-best recommendation" icon={<Sparkles/>}><div className="summary"><strong>SKU-101 → SKU-332</strong><span>Travel backpack buyers often convert on premium headphones within 7 days.</span></div></Panel></section>}
function Analytics(){return <section className="grid"><Panel title="Discovery analytics" icon={<LineIcon/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={trend}><XAxis dataKey="d" stroke="#9badc1"/><YAxis stroke="#9badc1"/><Tooltip/><Area dataKey="ctr" stroke="#22c55e" fill="#14532d"/></AreaChart></ResponsiveContainer></Panel><Panel title="Conversion insights" icon={<MousePointerClick/>}><div className="reason">Hybrid search improved CTR by 12.4%.</div><div className="reason">Personalized recommendations increased add-to-cart rate by 8.1%.</div><div className="reason">Latency stayed below 150ms target for 97% of requests.</div></Panel></section>}
function Evaluation(){return <Panel title="Ranking experiment results" icon={<BadgeCheck/>}><div className="table">{evalRows.map(row=><div className="row" key={row[0]}>{row.map(cell=><span key={cell}>{cell}</span>)}</div>)}</div></Panel>}
function Panel({title,icon,children}){return <article className="panel"><div className="panel-title">{icon}<h2>{title}</h2></div>{children}</article>}

createRoot(document.getElementById('root')).render(<App/>);
