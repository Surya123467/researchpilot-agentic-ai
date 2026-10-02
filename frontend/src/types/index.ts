export type Source={id:string;title:string;publisher:string;url:string;type:string;credibility:number;snippet:string}
export type Claim={id:string;text:string;source_ids:string[];confidence:number;stance:string}
export type Task={id:string;title:string;objective:string;status:string}
export type Run={run_id:string;question:string;depth:string;status:string;plan:Task[];sources:Source[];claims:Claim[];memories_used:{id:string;topic:string;insight:string;confidence:number}[];report:{title:string;executive_summary:string;key_findings:string[];claims:Claim[];limitations:string[];next_questions:string[]};review:{approved:boolean;citation_coverage:number;confidence:number;issues:string[]};trace:string[]}
