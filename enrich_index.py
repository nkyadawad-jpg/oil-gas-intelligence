import re

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# 1. Update hardcoded Header values in HTML
content = content.replace(
    '<span id="hdrPipelineVal" class="font-bold text-cyan-300 ml-1">QAR 4.85M</span>',
    '<span id="hdrPipelineVal" class="font-bold text-cyan-300 ml-1">QAR 15.11M</span>'
)
content = content.replace(
    '<span id="hdrWeightedVal" class="font-bold text-amber-300 ml-1">QAR 2.74M</span>',
    '<span id="hdrWeightedVal" class="font-bold text-amber-300 ml-1">QAR 13.78M</span>'
)
content = content.replace(
    '<span id="hdrCoverageVal" class="font-bold text-cyan-400 ml-1">2.4X</span>',
    '<span id="hdrCoverageVal" class="font-bold text-cyan-400 ml-1">7.6X</span>'
)

# 2. Update hardcoded KPI 2 & 3 values in HTML
content = content.replace(
    '<h3 id="kpiTotalPipelineVal" class="text-2xl font-black text-cyan-300 mt-1">QAR 4.85M</h3>',
    '<h3 id="kpiTotalPipelineVal" class="text-2xl font-black text-cyan-300 mt-1">QAR 15.11M</h3>'
)
content = content.replace(
    '<span id="kpiCoverageBadge" class="bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-xs px-2 py-0.5 rounded font-bold">2.4X Cov</span>',
    '<span id="kpiCoverageBadge" class="bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-xs px-2 py-0.5 rounded font-bold">7.6X Cov</span>'
)
content = content.replace(
    '<p class="text-[11px] text-slate-400 mt-2">Weighted Expected Value: <strong id="kpiWeightedVal" class="text-white">QAR 2.74M</strong></p>',
    '<p class="text-[11px] text-slate-400 mt-2">Weighted Expected Value: <strong id="kpiWeightedVal" class="text-white">QAR 13.78M</strong></p>'
)
content = content.replace(
    '<span>Pre-RFQ Stage: <strong id="kpiPreRfqVal" class="text-amber-300">QAR 3.10M</strong></span>',
    '<span>Pre-RFQ Stage: <strong id="kpiPreRfqVal" class="text-amber-300">QAR 10.86M</strong></span>'
)
content = content.replace(
    '<span>Live ITT: <strong id="kpiLiveIttVal" class="text-emerald-300">QAR 1.75M</strong></span>',
    '<span>Live ITT: <strong id="kpiLiveIttVal" class="text-emerald-300">QAR 4.25M</strong></span>'
)
content = content.replace(
    '<h3 id="kpiHotLeadsCount" class="text-2xl font-black text-red-400 mt-1">11 Leads</h3>',
    '<h3 id="kpiHotLeadsCount" class="text-2xl font-black text-red-400 mt-1">18 Leads</h3>'
)
content = content.replace(
    '<span id="kpiTotalLeadsCount" class="font-bold text-white">12 active scopes</span>',
    '<span id="kpiTotalLeadsCount" class="font-bold text-white">18 active scopes</span>'
)
content = content.replace(
    '<span>High Potential (&gt;80): <strong id="kpiHighPotCount" class="text-amber-400">11</strong></span>',
    '<span>High Potential (&gt;80): <strong id="kpiHighPotCount" class="text-amber-400">18</strong></span>'
)
content = content.replace(
    '<span>Watchlist: <strong id="kpiWatchlistCount" class="text-slate-300">1</strong></span>',
    '<span>Watchlist: <strong id="kpiWatchlistCount" class="text-slate-300">0</strong></span>'
)
content = content.replace(
    '<span id="pbTotalPoolVal" class="text-xs bg-slate-800 text-slate-300 px-2.5 py-1 rounded border border-slate-700 font-mono">Total Opportunity Pool: QAR 4.85M</span>',
    '<span id="pbTotalPoolVal" class="text-xs bg-slate-800 text-slate-300 px-2.5 py-1 rounded border border-slate-700 font-mono">Total Opportunity Pool: QAR 15.11M</span>'
)

# 3. Comprehensive SOURCE_URL_MAP covering EVERY SINGLE Qatar Client and EPC
full_source_map = """    const SOURCE_URL_MAP = {
      "QatarEnergy": { name: "QatarEnergy Official State Portal", url: "https://www.qatarenergy.qa" },
      "QatarEnergy LNG": { name: "QatarEnergy LNG Official Supplier Notices", url: "https://www.qatarenergylng.qa" },
      "QAFCO": { name: "QAFCO Fertilizer Official Procurement", url: "https://www.qafco.qa" },
      "Q-Chem": { name: "Q-Chem / RLOC Official Chemical Portal", url: "https://www.qchem.com.qa" },
      "RLOC": { name: "Q-Chem / RLOC Official Chemical Portal", url: "https://www.qchem.com.qa" },
      "QAPCO": { name: "QAPCO Official Corporate Portal", url: "https://www.qapco.com" },
      "North Oil Company": { name: "North Oil Company (NOC) Official Portal", url: "https://www.noc.qa" },
      "Pearl GTL": { name: "Qatar Shell Pearl GTL Official Site", url: "https://www.shell.com.qa" },
      "Dolphin Energy": { name: "Dolphin Energy Official Qatar Portal", url: "https://www.dolphinenergy.com" },
      "Oryx GTL": { name: "Oryx GTL Official Corporate Site", url: "https://www.oryxgtl.com.qa" },
      "WOQOD": { name: "WOQOD Commercial Distribution Portal", url: "https://www.woqod.com" },
      "QAFAC": { name: "QAFAC Petrochemical Portal", url: "https://www.qafac.com.qa" },
      "UHP": { name: "Umm Al Houl Power Portal", url: "https://www.uhp.com.qa" },
      "Mpower": { name: "Mpower Ras Laffan Portal", url: "https://www.mpower.com.qa" },
      "DOPET": { name: "DOPET Engineering & Contracting Portal", url: "https://www.dopet.com" },
      "QCON": { name: "QCON Turnaround & Construction Disclosures", url: "https://www.qcon.com.qa" },
      "TRAGS": { name: "TRAGS Electrical & Engineering Qatar", url: "https://www.tragsqatar.com" },
      "Medgulf": { name: "Medgulf Construction Official Site", url: "https://www.medgulfconstruction.com" },
      "Blackcat": { name: "Blackcat Engineering & Construction", url: "https://www.blackcat.qa" },
      "Madina Group": { name: "Madina Group Qatar Official Portal", url: "https://www.madinagroup.com" },
      "Roots Energy": { name: "Roots Energy & Engineering Portal", url: "https://www.rootsenergy.com" },
      "GDI": { name: "Gulf Drilling International Portal", url: "https://www.gdi.com.qa" },
      "Al Balagh": { name: "Al Balagh Trading & Contracting", url: "https://www.albalagh.com" },
      "Al Muftah": { name: "Al Muftah Contracting Qatar", url: "https://www.almuftah.com" }
    };"""

pattern_source_map = r'    const SOURCE_URL_MAP = \{.*?\n    \};'
content = re.sub(pattern_source_map, full_source_map, content, flags=re.DOTALL)

# 4. Update loadAndSyncOpportunities so all 18 opportunities are permanently and fully loaded
sync_func = """    function loadAndSyncOpportunities() {
      // Always guarantee all 18 monitored scopes and hot leads are fully loaded and synced
      opportunities = DEFAULT_OPPORTUNITIES.map(item => ({ ...item }));
      localStorage.setItem('qatar_radar_leads', JSON.stringify(opportunities));
      return opportunities;
    }"""
pattern_sync_func = r'    function loadAndSyncOpportunities\(\) \{.*?\n    \}'
content = re.sub(pattern_sync_func, sync_func, content, count=1, flags=re.DOTALL)

# 5. Update renderTopOpportunities: remove slice(0, 6) and display all 18 leads with Live ITT / Pre-RFQ badges and direct source links
top_opps_func = """    function renderTopOpportunities(filter = 'all') {
      const container = document.getElementById('topOpportunitiesGrid');
      if (!container) return;

      let filtered = [...opportunities];
      if (filter === 'hot') filtered = filtered.filter(o => o.score >= 90);
      if (filter === 'shutdown') filtered = filtered.filter(o => o.project.toLowerCase().includes('overhaul') || o.project.toLowerCase().includes('turnaround') || o.project.toLowerCase().includes('replacement') || (o.stageBadge && o.stageBadge.includes('Execution')));

      container.innerHTML = filtered.map((opp, idx) => {
        const isItt = opp.stage.includes('Level 4') || (opp.stageBadge && opp.stageBadge.includes('Live')) || opp.status === 'RFQ Received' || opp.status === 'Quotation';
        const clientSource = opp.sourceUrl || (SOURCE_URL_MAP[opp.client] ? SOURCE_URL_MAP[opp.client].url : 'https://www.qatarenergy.qa');
        const epcSource = SOURCE_URL_MAP[opp.epc] ? SOURCE_URL_MAP[opp.epc].url : 'https://www.dopet.com';

        return `
        <div class="glass-panel p-4 rounded-xl border-l-4 ${opp.score >= 90 ? 'border-l-red-500' : 'border-l-amber-500'} hover:border-slate-600 transition space-y-3 relative group">
          <div class="flex justify-between items-start">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-xs font-black ${opp.score >= 90 ? 'bg-red-500/20 text-red-400 border border-red-500/30' : 'bg-amber-500/20 text-amber-300 border border-amber-500/30'} px-2 py-0.5 rounded">
                #${String(idx + 1).padStart(2, '0')} ${opp.score >= 90 ? '🔥 HOT LEAD' : '🟠 HIGH POTENTIAL'}
              </span>
              <span class="text-xs font-bold text-white">${opp.client}</span>
              <span class="text-[10px] ${isItt ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40' : 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40'} px-2 py-0.5 rounded font-bold border">
                ${isItt ? '<i class="fa-solid fa-file-signature mr-1"></i> LIVE ITT / TENDER' : '<i class="fa-solid fa-crosshairs mr-1"></i> PRE-RFQ STAGE'}
              </span>
            </div>
            <div class="flex items-center gap-1.5 shrink-0">
              <span class="text-xs font-black text-amber-300 bg-slate-900 px-2 py-0.5 rounded border border-slate-700">
                Score: ${opp.score}/100
              </span>
            </div>
          </div>

          <div>
            <h4 class="font-bold text-sm text-white group-hover:text-amber-300 transition">${opp.project}</h4>
            <div class="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-slate-400 mt-1">
              <span><i class="fa-solid fa-location-dot text-red-400 mr-1"></i>${opp.facility}</span>
              <span><i class="fa-solid fa-layer-group text-cyan-400 mr-1"></i>${opp.stage}</span>
              <span><i class="fa-solid fa-helmet-safety text-yellow-400 mr-1"></i>EPC: <strong class="text-white">${opp.epc}</strong></span>
            </div>
          </div>

          <div class="p-2.5 bg-slate-950/70 rounded-lg border border-slate-800/80 text-xs space-y-1.5">
            <div class="flex justify-between text-slate-300">
              <span>Matching OEM Line:</span>
              <span class="font-bold text-cyan-300">${opp.product} (${opp.brand})</span>
            </div>
            <div class="flex justify-between text-slate-300">
              <span>Est. Pipeline Value:</span>
              <span class="font-bold text-emerald-400">QAR ${(opp.value).toLocaleString()}</span>
            </div>
            <div class="flex justify-between text-slate-400 text-[11px]">
              <span>Expected Procurement Window:</span>
              <span class="text-amber-300 font-medium">${opp.expectedRfq}</span>
            </div>
          </div>

          <div class="p-2 bg-qatar/15 border border-qatar/30 rounded text-[11px] text-amber-200 flex items-start gap-2">
            <i class="fa-solid fa-compass text-qatar-gold mt-0.5"></i>
            <div>
              <strong class="text-white">Actionable Approach Track:</strong> ${opp.nextAction}
            </div>
          </div>

          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pt-2 border-t border-slate-800/80 text-xs">
            <span class="text-[11px] text-slate-500">Live Ingested: ${opp.detectedAgo}</span>
            <div class="flex items-center gap-1.5 flex-wrap">
              <a href="${clientSource}" target="_blank" rel="noopener noreferrer" class="flex-1 sm:flex-none text-cyan-300 hover:text-white bg-cyan-600/30 hover:bg-cyan-600/50 px-2.5 py-1.5 rounded border border-cyan-400/50 text-[11px] font-bold flex items-center justify-center gap-1 shadow transition" title="Open official corporate website directly">
                <i class="fa-solid fa-arrow-up-right-from-square text-cyan-400 text-[10px]"></i> Client Portal ↗
              </a>
              <a href="${epcSource}" target="_blank" rel="noopener noreferrer" class="flex-1 sm:flex-none text-amber-300 hover:text-white bg-amber-600/20 hover:bg-amber-600/40 px-2.5 py-1.5 rounded border border-amber-400/40 text-[11px] font-bold flex items-center justify-center gap-1 shadow transition" title="Open EPC contractor portal">
                <i class="fa-solid fa-building text-amber-400 text-[10px]"></i> EPC Site ↗
              </a>
              <button onclick="openDataAuditModal('${opp.id}')" class="flex-1 sm:flex-none text-emerald-400 hover:text-emerald-300 bg-emerald-500/10 px-2.5 py-1.5 rounded border border-emerald-500/20 text-[11px] flex items-center justify-center gap-1 font-medium" title="Verify 100% digital data footprint & source">
                <i class="fa-solid fa-shield-check"></i> Audit Lineage
              </button>
              <button onclick="openWhyLeadModal('${opp.id}')" class="flex-1 sm:flex-none text-slate-300 hover:text-white bg-slate-800 px-2.5 py-1.5 rounded border border-slate-700 text-[11px] flex items-center justify-center gap-1 font-medium">
                <i class="fa-solid fa-circle-question"></i> Why Lead?
              </button>
              <button onclick="prepareOutreachForLead('${opp.id}')" class="w-full sm:w-auto text-white bg-qatar hover:bg-qatar-light px-3 py-1.5 rounded font-bold text-[11px] flex items-center justify-center gap-1 shadow">
                <i class="fa-solid fa-wand-magic-sparkles"></i> AI Outreach
              </button>
            </div>
          </div>
        </div>
        `;
      }).join('');
    }"""

pattern_top_opps = r'    function renderTopOpportunities\(filter = \'all\'\) \{.*?\n    \}'
content = re.sub(pattern_top_opps, top_opps_func, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] index.html successfully enriched with full 18-lead pipeline, comprehensive source links, and ITT data!")
