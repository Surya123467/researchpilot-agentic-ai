import type {Run} from '../types'
const API=import.meta.env.VITE_API_URL || 'http://localhost:8000'
export async function runResearch(question:string,depth:string):Promise<Run>{
 const r=await fetch(`${API}/api/research/run`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question,depth})})
 if(!r.ok) throw new Error('Research request failed')
 return r.json()
}
export async function getDemo():Promise<Run>{const r=await fetch(`${API}/api/research/demo`);if(!r.ok)throw new Error('Demo failed');return r.json()}
