# Qatar Oil & Gas Intelligence & Opportunity Radar
## Lovable.dev / Cursor / Next.js Comprehensive Product Specification (PRD) & Blueprint

> **Platform Name**: Oil & Gas Terminal Qatar (Petrocon Ashfan Intelligence Edition)  
> **Target Audience**: Energy Sector Sales Managers, EPC Procurement Officers, Equipment Channel Partners  
> **Primary User Persona**: Ashfan — Assistant Sales Manager at **PETROCON Qatar**  
> **Commercial Model**: Authorized OEM $\to$ PETROCON Intermediary $\to$ Qatar Operators / EPC Contractors  
> **Total Active Leads**: 64 Opportunities  
> **Total Open Pipeline**: QAR 67,850,000.00 (Weighted: QAR 63,782,900.00)  
> **Executive Security Passkey**: `1989`  

---

## Table of Contents
1. [Executive Summary & Purpose](#1-executive-summary--purpose)
2. [Copy-Paste Prompt for Lovable.dev](#2-copy-paste-prompt-for-lovabledev)
3. [Recommended Modern Technology Stack](#3-recommended-modern-technology-stack)
4. [Design System, Color Palette & UI Tokens](#4-design-system-color-palette--ui-tokens)
5. [Executive Security Gate & Passkey System](#5-executive-security-gate--passkey-system)
6. [TypeScript Data Schemas & Models](#6-typescript-data-schemas--models)
7. [The 11 Core Application Modules](#7-the-11-core-application-modules)
   - Module 1: Command Center (Executive KPI Dashboard)
   - Module 2: Project Radar (Package Cards & Filters)
   - Module 3: Shutdown & Turnaround Radar (Countdowns & Scopes)
   - Module 4: Scopes & Opportunities CRM Table (Excel-like Datagrid)
   - Module 5: EPC Contractor Directory & Profiles
   - Module 6: Source & Portal Monitor (24 Channels)
   - Module 7: Customer & Operator Matrix
   - Module 8: Product Portfolio & OEM Matcher
   - Module 9: Petrocon Ashfan Strategy Center & Ask Ashfan AI
   - Module 10: Multi-Channel Outreach Generator
   - Module 11: Qatar GIS Interactive Geographical Zone Map
8. [Interactive Modals & Drawers](#8-interactive-modals--drawers)
9. [Live Scan, Auto-Refresh & State Management](#9-live-scan-auto-refresh--state-management)
10. [Complete Initial Datasets (JSON)](#10-complete-initial-datasets-json)
    - 64 Project Opportunities (Full Array)
    - 5 Shutdown Radar Events
    - 24 Portal Sources
11. [Step-by-Step Implementation Guide on Lovable](#11-step-by-step-implementation-guide-on-lovable)

---

## 1. Executive Summary & Purpose

The **Qatar Oil & Gas Opportunity Radar** is an enterprise-grade sales intelligence and tender-forecasting web application tailored specifically for the energy sector in Qatar. It is designed around the commercial workflow of **PETROCON Qatar**, an authorized channel partner representing tier-one international OEMs (*Emerson/ASCO, Protectoseal, Westlock Controls, Trillium Flow Technologies, Ashcroft/Bourdon, ADAMS Armaturen, and Shell Pearl GTL*).

### The Core Problem It Solves
In the mega-project landscape of Qatar (North Field East, North Field South, Al Shaheen, Mesaieed, Dukhan), waiting for public RFQs to appear on official tender boards is too late:
- Engineering specs are locked during FEED and detailed EPC engineering.
- Approved Manufacturer Lists (AML) are decided 6–12 months prior to requisition.
- Plant turnarounds require 90–180 day advance procurement for long-lead cryogenic and severe-service valves.

### The Solution
This application tracks early signals, EPC contractor allocations, and plant turnaround schedules to forecast exact equipment packages **before RFQs are issued**, giving sales teams 90–180 days of pre-bid competitive advantage.

---

## 2. Copy-Paste Prompt for Lovable.dev

```text
Build a premium, dark-themed enterprise Sales Intelligence and Opportunity Radar web app called "Oil & Gas Terminal Qatar" tailored for Qatar's energy sector and EPC contractors.

Key Requirements:
1. Executive Security Gate: Require a passkey modal on first load with hidden passkey "1989" to unlock the dashboard. Provide a "Lock" button in the navigation to re-lock.
2. Design & Aesthetics:
   - Deep luxury dark slate background (#0F172A, #090D16, #1E293B).
   - Qatar National Maroon accents (#8A1538, #A6192E).
   - Emerald (#10B981) for live signals, Amber (#F59E0B) for countdowns and hot leads, Sky blue for EPC badges.
   - Lucide React icons, smooth glassmorphism, glowing borders, card hover lift, and micro-animations.
   - Fully responsive: Desktop sidebar + top command bar, and a touch-friendly mobile bottom navigation bar.
3. Live Header & KPI Ribbon:
   - Live AST timestamp (Qatar Standard Time, UTC+3) with auto-refresh every hour.
   - "Scan & Refresh" button that plays a spin animation, recalculates metrics, simulates scanning 24 Qatar portals, and displays a dynamic toast confirmation.
   - 4 Header KPIs: Total Open Pipeline (QAR 67.85M), Weighted Pipeline (QAR 62.29M), Quota Coverage (33.9X on QAR 2.0M target), and Total Active Scopes (64 Leads).
4. Core Modules (Tab Navigation):
   - Command Center: Executive KPI overview, Top 5 Hot Leads (>90 deal score), Next Turnaround Countdown, Real-Time Signal Stream, and Quick EPC Directory.
   - Project Radar: Filterable grid of QatarEnergy, Qatargas, NOC, and EPC packages with stage badges (FEED, Procurement Approaching, Live ITT), confidence bars, and OEM match tags.
   - Shutdown Radar: Turnaround countdown clocks (days remaining), critical equipment fits, contractor awards, and fast-track action guides.
   - Scopes Table (CRM Grid): Full Excel-like interactive data table with 64 leads, search bar, multi-column filters (Zone, Stage, EPC, Product), sorting, inline status dropdown, CSV export, "Add Opportunity" modal, and "Audit Lead" modal.
   - EPC Directory: Dossiers of 20 top contractors (DOPET, QCON, Madina, Saipem, Technip, Chiyoda, etc.) with active packages, key offices, and direct outreach generator.
   - Source Monitor: Health dashboard for 24 monitored channels (Mushtaryat, Tawteen, QatarEnergy, NOC) with latency, scan status, and direct portal links.
   - Customer Matrix: Operator vs. Product heat-matrix across QatarEnergy, QELNG, NOC, QAFCO, QAPCO, Pearl GTL, Q-Chem.
   - Product Portfolio & OEM Matcher: Overview of OEM brands (Emerson, Protectoseal, Westlock, Trillium, Ashcroft, ADAMS) with 90/120/180-day market demand score.
   - Petrocon Ashfan Center: Channel partner playbook with mid-size accounts (Gulf Chlorine, QPMC, QIMCO), replacement equipment radar, and an interactive "Ask Ashfan AI" strategy assistant.
   - Outreach Generator: Multi-channel outreach copywriter generating personalized messages for selected leads across 5 formats: Procurement Email, Technical Pitch, Phone Script, WhatsApp, and Technical Qualifying Questions with 1-click clipboard copy.
   - Qatar GIS Zone Map: Interactive geographical hotspots (Ras Laffan, Mesaieed, Dukhan, Offshore Al Shaheen, Halul Island, Industrial Area, Doha HQ) with active lead counts.
5. Modals & Drawers:
   - Add Opportunity Modal (with auto deal score and QAR formatting).
   - Data Audit Modal (verification score, data lineage, source links).
   - Why This Lead Modal (procurement timeline, tender allocation reasoning).
   - Daily Intelligence Briefing Modal (morning executive summary).
   - Arabic Regional Intelligence Drawer (original Arabic tender notices with verified English translations).
6. Seed with the full initial dataset of 64 leads, 5 turnarounds, and 24 portals provided in the specification.
```

---

## 3. Recommended Modern Technology Stack

When generating or deploying this application in **Lovable**, **Vite**, or **Next.js**, use the following production-grade stack:

- **Framework**: React 18+ with TypeScript
- **Styling**: Tailwind CSS (v3 or v4)
- **UI Components**: Radix UI primitives / Shadcn UI (`dialog`, `dropdown-menu`, `tabs`, `tooltip`, `badge`, `sheet`, `card`)
- **Icons**: Lucide React (`lucide-react`)
- **Charts & Visualizations**: Recharts (`recharts`) for pipeline distributions and win probability bars
- **State Management**: Zustand or React Context + `localStorage` for offline persistence of lead statuses and custom quotas
- **Animations**: Tailwind CSS transitions + Framer Motion for modal transitions and card entrance animations
- **Exporting**: `papaparse` or pure JavaScript CSV generator for CRM datagrid export

---

## 4. Design System, Color Palette & UI Tokens

### Color Palette (Tailwind Configuration)
```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        qatar: {
          DEFAULT: '#8A1538',   // Official Qatar Maroon
          dark: '#5C0F26',
          light: '#A6192E',
          glow: 'rgba(138, 21, 56, 0.4)'
        },
        surface: {
          950: '#090D16',       // Background canvas
          900: '#0F172A',       // Card background
          850: '#141E33',       // Sub-card background
          800: '#1E293B',       // Border & divider
          700: '#334155'        // Hover borders
        },
        accent: {
          emerald: '#10B981',   // Live verified signals & Pre-RFQ
          amber: '#F59E0B',     // Approaching deadlines & countdowns
          cyan: '#06B6D4',      // OEM alignments & tech specs
          indigo: '#6366F1'     // EPC contractor tags
        }
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace']
      }
    }
  }
}
```

### Visual Styling Guidelines
1. **Background**: Dark deep slate gradient `bg-gradient-to-b from-[#090D16] via-[#0F172A] to-[#090D16]`.
2. **Cards**: Subtly bordered with `border border-slate-800/80 bg-slate-900/90 backdrop-blur-md rounded-xl shadow-xl hover:border-slate-700 transition-all`.
3. **Accent Highlights**: Gradient pill badges (`from-qatar to-qatar-light text-white text-xs font-semibold px-2.5 py-0.5 rounded-full`).
4. **Valuations**: Strict **QAR (Qatari Riyal)** denomination formatted with commas (e.g., `QAR 1,250,000` or `QAR 67.85M`).

---

## 5. Executive Security Gate & Passkey System

To protect proprietary commercial intelligence and pricing strategies:
- **Default State**: Application mounts in locked state (`isLocked = true`) unless unlocked in the current browser session.
- **Passkey**: `1989`.
- **UI Element**: Full-screen modal overlay with glassmorphism backdrop (`backdrop-blur-xl bg-slate-950/90`).
- **Input UX**:
  - Masked 4-digit PIN input with auto-focus.
  - Incorrect PIN triggers a red shake animation (`shake 0.4s ease-in-out`) and error message: *"Invalid Executive Passkey. Access restricted to authorized personnel."*
  - Correct PIN unlocks all 11 modules and stores unlock status in `sessionStorage`.
- **Manual Lock**: A lock button `<button onClick={lockSecurityGate} class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-1.5 rounded-lg border border-slate-700 flex items-center gap-1.5"><Lock className="w-3.5 h-3.5 text-amber-400" /> Lock Gate</button>` is pinned in the top navigation.

---

## 6. TypeScript Data Schemas & Models

```typescript
// 1. Opportunity / Project Lead Model
export interface Opportunity {
  id: string;                    // e.g. "QTR-2026-0089"
  client: string;                // Operator: QatarEnergy, North Oil Company, etc.
  facility: string;              // Ras Laffan, Mesaieed, Dukhan, Offshore
  project: string;               // Name of engineering project
  stage: string;                 // "Level 2 (FEED / Pre-RFQ)" | "Level 3 (Procurement Approaching)" | "Level 4 (Live ITT / Tender)"
  stageBadge: string;            // Short badge string
  epc: string;                   // Awarded / Shortlisted EPC Contractor
  contractor: string;            // Detailed division
  product: string;               // Valve, Skid, Transmitter, Pump, etc.
  brand: string;                 // Target OEM (Emerson, Protectoseal, etc.)
  value: number;                 // Commercial valuation in QAR
  score: number;                 // Lead score (0 to 100)
  confidence: string;            // e.g. "High (96%)"
  status: 'Pre-RFQ' | 'Tender' | 'Technical Evaluation' | 'Shortlisted' | 'Won' | 'Archived';
  expectedRfq: string;           // Target date string e.g. "15-Oct-2026"
  detectedAgo: string;           // Relative timestamp e.g. "14 hours ago"
  nextAction: string;            // Immediate sales step
  arabicText?: string;           // Original Arabic tender excerpt
  translatedText?: string;       // Verified English translation
  factText?: string;             // Project award fact
  signalText?: string;           // EPC requisition signal
  inferenceText?: string;        // OEM fit rationale
  sourceUrl?: string;            // Operator portal link
  epcUrl?: string;               // EPC contractor portal link
}

// 2. Shutdown & Turnaround Radar Model
export interface ShutdownEvent {
  id: string;                    // e.g. "SHUT-0081"
  client: string;                // e.g. "QAFCO"
  facility: string;              // "Mesaieed", "Ras Laffan", etc.
  unit: string;                  // "Ammonia Plant #4"
  type: string;                  // "Major Turnaround" | "Partial Overhaul"
  expectedStart: string;         // "15-Oct-2026"
  expectedEnd: string;           // "05-Nov-2026"
  daysToShutdown: number;        // Dynamic countdown calculated in days
  contractor: string;            // Awarded turnaround contractors
  equipment: string;             // Critical plant units involved
  productFit: string;            // Applicable OEM products
  recommendedAction: string;     // Immediate commercial move
}

// 3. Monitored Source Portal Model
export interface SourcePortal {
  id: string;                    // "SRC-01"
  name: string;                  // "Mushtaryat (Government Procurement Portal)"
  category: string;              // "State Operator Portal" | "EPC Contractor Portal"
  url: string;                   // External link
  status: 'Live (Active)' | 'Scanned' | 'Pending';
  latency: string;               // "42ms"
  frequency: string;             // "Every 15 mins"
  checkedAt: string;             // "Just now"
  hits: number;                  // Number of signals detected
  lastScan: string;              // "10 mins ago"
}

// 4. Real-time Intelligence Signal Model
export interface IntelligenceSignal {
  id: string;
  time: string;                  // "22 mins ago"
  source: string;                // Source portal name
  category: string;              // "Procurement Requisition", "Contract Award", etc.
  badge: 'High Confidence' | 'Verified' | 'Emerging';
  title: string;
  text: string;
  action: string;
}

// 5. EPC Contractor Dossier Model
export interface EpcContractor {
  name: string;                  // "DOPET (Doha Petroleum Construction)"
  shortName: string;             // "DOPET"
  classification: string;        // "Tier-1 Mechanical & EPC"
  location: string;              // "Salwa Road / Mesaieed Support Base"
  activePackagesCount: number;
  totalPipelineQar: number;
  procurementPortalUrl: string;
  keySpecialties: string[];
}
```

---

## 7. The 11 Core Application Modules

### Module 1: Command Center (Executive KPI Dashboard)
- **Header Strip**: Shows live AST time, cloud sync status, passkey lock toggle, and the primary "Scan & Refresh" button.
- **KPI Summary Cards**:
  1. *Total Open Pipeline*: **QAR 67.85M** (Live calculation across all 64 active leads).
  2. *Weighted Pipeline*: **QAR 62.29M** (Factored by win probability).
  3. *Quota Coverage*: **33.9X** (Calculated against monthly target of QAR 2.0M).
  4. *Monitored Channels*: **24 Active Portals** (Mushtaryat, Tawteen, Operator & EPC sites).
- **Top 5 Hot Leads Widget**: Pinned high-value cards scoring $>90$ with instant outreach trigger buttons.
- **Turnaround Countdown Banner**: Real-time counter showing days remaining until the next scheduled plant shutdown (QAFCO-4, QAPCO Ethylene-2, etc.).
- **Live Intelligence Feed**: Scrolling stream of recent signals with confidence badges.

### Module 2: Project Radar (Package Cards & Filters)
- Displays all project scopes as interactive, high-density cards.
- **Card Elements**:
  - Client & Facility logo badge.
  - Project Title & Target Equipment.
  - EPC Contractor tag.
  - Pipeline Valuation (in QAR) and Win Probability bar.
  - Stage indicator (FEED, Approaching Procurement, Tender Issued).
  - Quick action buttons: *Prepare Outreach*, *Why This Lead?*, *Audit Signal*.
- **Filter Toolbar**: Instant search bar + chips to filter by Client, EPC, Zone, and Stage.

### Module 3: Shutdown & Turnaround Radar
- Qatar's chemical and LNG plants operate in severe continuous service; scheduled turnarounds represent immediate, budget-allocated procurement windows.
- Displays countdown clocks to plant overhauls.
- Highlights target equipment fits (*Emerson valves, Protectoseal flame arrestors, Trillium pump spares, Ashcroft gauges*).
- Outlines fast-track contractor contacts for DOPET, QCON, and Madina Group.

### Module 4: Scopes & Opportunities CRM Table (Excel-like Datagrid)
- Complete, responsive tabular grid of all **64 active leads**.
- **Interactive Capabilities**:
  - Sorting on any column (Value, Score, Client, Stage, Expected RFQ).
  - Multi-column filters for Zone, Stage, Status, and Product category.
  - Live status dropdown (`Pre-RFQ`, `Tender`, `Technical Evaluation`, `Shortlisted`, `Won`, `Archived`) that saves instantly to `localStorage`.
  - Global text search across project titles, client names, and equipment models.
  - **Export to CSV**: Generates a standard `.csv` file formatted for Excel or CRM import.
  - **Add Opportunity Button**: Opens a modal to manually append new custom leads.

### Module 5: EPC Contractor Directory & Profiles
- Catalogs Qatar's premier EPC contractors:
  - *DOPET, QCON, Madina Group, Saipem, Technip Energies, Chiyoda Almana, Larsen & Toubro, CCC, Galfar Al Misnad, Blackcat, Descon, Medgulf, Petrofac, Kent, HEISCO, TRAGS, Al Balagh*.
- Shows each contractor's active awarded packages, total addressable QAR pipeline, and procurement portal links.
- "Prepare Outreach to EPC" button pre-populates the outreach generator with the contractor's specific package details.

### Module 6: Source & Portal Monitor (24 Channels)
- Displays real-time operational status of all 24 monitored channels.
- Categorized into *Government Procurement (Mushtaryat, Tawteen)*, *State Energy Operators (QatarEnergy, NOC, Qatargas)*, and *Tier-1 EPC Contractor Portals*.
- Displays latency (`38ms` - `65ms`), scan frequency (`15 mins` - `2 hours`), and total signals detected.

### Module 7: Customer & Operator Matrix
- Two-dimensional heat-matrix cross-referencing major operators against product lines:
  - *QatarEnergy, QELNG, North Oil Company, QAFCO, QAPCO, Pearl GTL, Q-Chem, Dolphin Energy, Oryx GTL*.
- Visualizes where Petrocon has approved vendor status and highlights addressable whitespace opportunities.

### Module 8: Product Portfolio & OEM Matcher
- Profiles Petrocon's authorized OEM brand catalogue:
  - **Emerson / ASCO**: Cryogenic valves, solenoid pilot valves, Fisher control spares.
  - **Protectoseal**: Pressure/vacuum relief valves, ATEX detonation & deflagration flame arrestors.
  - **Westlock Controls**: SIL-3 valve position monitors, AccuTrak digital switches.
  - **Trillium Flow Technologies**: Severe service slurry pumps, Borer flow control.
  - **Ashcroft / Bourdon**: Ultra-high-pressure process transmitters, differential pressure gauges.
  - **ADAMS Armaturen**: Metal-seated severe service triple-offset rotary isolation valves.
- Displays 90 / 120 / 180-day market momentum scores.

### Module 9: Petrocon Ashfan Strategy Center & "Ask Ashfan AI"
- Sales command center tailored for Ashfan (Assistant Sales Manager, PETROCON).
- **Strategy Insights**:
  - The Intermediary Value Creation Model (`OEM -> PETROCON -> Customer`).
  - Dedicated Profile for **Shell Pearl GTL** (Ras Laffan synthesis loops & MRO demand).
  - Target list of agile mid-size Qatar industrial processors (*Gulf Chlorine, QPMC, QIMCO, Mesaieed Water*).
  - Replacement radar for aging equipment (1-Hexene plant valves, LNG flare stacks, Ethylene-2 pumps).
- **Interactive "Ask Ashfan AI" Box**:
  - Natural language inquiry interface with pre-built prompt chips:
    - *"Show 90-day demand forecast"*
    - *"What should I pitch to Gulf Chlorine?"*
    - *"Upcoming turnaround valve opportunities"*
    - *"Pearl GTL MRO strategy"*
  - Returns structured, actionable sales guidance.

### Module 10: Multi-Channel Outreach Generator
- Automatically generates bespoke, highly technical sales outreach based on the currently selected opportunity.
- **5 Output Formats**:
  1. **Procurement Email**: Professional tone, RFQ reference, OEM brand alignment, ICV score highlight, commercial stock availability.
  2. **Technical Pitch Email**: Engineering focus, ASME/API ratings, metallurgy (316SS, Inconel, Monel), SIL-3 certifications, sour gas ($H_2S$) service capabilities.
  3. **Phone Call Script**: Opening hook, gatekeeper bypass, value proposition, turnaround schedule check, call-to-action.
  4. **WhatsApp Quick Message**: Concise executive summary formatted with WhatsApp bolding and bullet points for mobile communication.
  5. **Technical Qualifying Questions**: 5 technical questions to probe the client's engineering specifications (pressure class, design temperature, trim material, stroke time, Fugitive Emission ISO 15848).
- **One-Click Copy**: Copies formatted text directly to clipboard with visual toast feedback.

### Module 11: Qatar GIS Interactive Geographical Zone Map
- Visual map and zone selector displaying Qatar's key industrial hubs:
  1. **Ras Laffan Industrial City**: World's capital of LNG & Pearl GTL (Off-Plot, Trains 1–4, NFE, NFS).
  2. **Mesaieed Industrial City**: Petrochemicals & fertilizers (QAFCO, QAPCO, Q-Chem, QAFAC, Refinery).
  3. **Dukhan Field**: Onshore crude degassing and gas processing (Fahahil CSU, Jaleha, Khatiyah).
  4. **Offshore Al Shaheen & Halul**: Qatar's largest offshore field (Gallaf Batch 3, NOC platforms).
  5. **Doha Corporate HQ & Fabrication Yards**: EPC project offices, engineering houses, and valve testing facilities in Industrial Area.
- Clicking any zone instantly filters the Project Radar and Scopes Table to that geographical cluster.

---

## 8. Interactive Modals & Drawers

1. **Executive Passkey Modal (`#passkeyModal`)**:
   - Blocks UI until PIN `1989` is validated.
2. **Add Opportunity Modal (`#addLeadModal`)**:
   - Clean form to input Client, Project Title, Facility, Product, EPC, Valuation in QAR, Expected RFQ, and Win Probability. Auto-generates a unique `QTR-2026-XXXX` ID.
3. **Data Audit Modal (`#dataAuditModal`)**:
   - Inspects the exact data provenance, verification score (e.g., 96%), telemetry source URL, and timestamp for any selected lead.
4. **Why This Lead? Modal (`#whyLeadModal`)**:
   - Displays AI-generated analysis of why the opportunity was flagged, historical contractor spend, and recommended sales strategy.
5. **OEM Brand Playbook Modal (`#oemPlaybookModal`)**:
   - Deep-dive technical product specifications, authorized distributor certificates, and competitive advantages against rivals.
6. **Arabic Regional Intelligence Drawer (`#arabicDrawer`)**:
   - Slide-over side panel displaying original Arabic language notices from Qatar Ministry of Finance / Mushtaryat alongside verified English translations.

---

## 9. Live Scan, Auto-Refresh & State Management

### Live Scan Engine
When the user clicks the **"Scan Sources"** or **"Scan Now"** button:
1. Button icons trigger CSS spinning animation (`animate-spin`).
2. Performs an asynchronous fetch to `data/latest_intelligence.json?t=${Date.now()}` to bypass browser caching.
3. Dynamically re-indexes all 24 monitored sources with checked timestamps set to `"Just now"`.
4. Recalculates real-time turnaround countdowns for all shutdown events.
5. Recalculates KPI metrics dynamically:
   - Total Pipeline Valuation $\sum \text{value}$
   - Weighted Pipeline Valuation $\sum (\text{value} \times \text{probability} / 100)$
   - Total Scopes count and Hot Leads ($>80$ score) count.
6. Updates top AST timestamp badge to current Qatar local time.
7. Displays a comprehensive dynamic completion alert:
   ```text
   Live Scan & Auto-Refresh Complete!

   • Timestamp: [Current AST Time]
   • Scanned: 24 Official Qatar Energy State & EPC Portals
   • Verified: 64 Active Scopes & Leads ([Hot Leads Count] Hot Leads >80 Score)
   • Open Pipeline: QAR 67.85M (Weighted: QAR 63.78M)
   • Real-Time Sync: All project cards, shutdown countdowns, CRM grid, and signals live updated.
   ```
8. Runs an automatic background sync every 1 hour (3,600,000 ms).

---

## 10. Complete Initial Datasets (JSON)

### 5 Shutdown Radar Events
```json
[
  {
    "id": "SHUT-0081",
    "client": "QAFCO",
    "facility": "Mesaieed",
    "unit": "Ammonia Plant #4",
    "type": "Major Turnaround",
    "expectedStart": "15-Oct-2026",
    "expectedEnd": "05-Nov-2026",
    "daysToShutdown": 13,
    "contractor": "DOPET & QCON",
    "equipment": "Syngas Loop, Waste Heat Boilers, Synthesis Converter",
    "productFit": "High: Emerson Gate Valves, Trillium Pump Spares, Ashcroft Gauges",
    "recommendedAction": "Approach DOPET & QCON Turnaround Managers immediately for fast-track valve & gasket package"
  },
  {
    "id": "SHUT-0082",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan",
    "unit": "LNG Mega-Train 3",
    "type": "Scheduled Overhaul",
    "expectedStart": "01-Nov-2026",
    "expectedEnd": "25-Nov-2026",
    "daysToShutdown": 30,
    "contractor": "QCON Turnaround Team",
    "equipment": "Cryogenic MCHE, AGRU Columns, Refrigerant Compressors",
    "productFit": "High: ADAMS Severe Service Valves, Protectoseal Vents, ASCO Solenoids",
    "recommendedAction": "Meet QCON instrumentation team to finalize ASCO explosion-proof solenoid replacements"
  },
  {
    "id": "SHUT-0083",
    "client": "Q-Chem",
    "facility": "Mesaieed",
    "unit": "Polyethylene Plant 1",
    "type": "Catalyst & Reactor Maintenance",
    "expectedStart": "10-Dec-2026",
    "expectedEnd": "22-Dec-2026",
    "daysToShutdown": 69,
    "contractor": "Medgulf & Madina Group",
    "equipment": "Loop Reactor, Polymerization Feed, Fluff Silos",
    "productFit": "High: Protectoseal Flame Arrestors, Westlock Positioners",
    "recommendedAction": "Send Protectoseal deflagration flame arrestor maintenance packages to Medgulf"
  },
  {
    "id": "SHUT-0084",
    "client": "QAPCO",
    "facility": "Mesaieed",
    "unit": "Ethylene Plant 2",
    "type": "Cracker Quench Overhaul",
    "expectedStart": "18-Nov-2026",
    "expectedEnd": "02-Dec-2026",
    "daysToShutdown": 47,
    "contractor": "Madina Group",
    "equipment": "Quench Towers, Pyrolysis Gasoline Pumps, Transfer Line Valves",
    "productFit": "High: Trillium Pump Spares, Emerson Ball Valves",
    "recommendedAction": "Deliver Trillium rotating pump rebuild kits to Madina Group Mesaieed workshop"
  },
  {
    "id": "SHUT-0085",
    "client": "QatarEnergy",
    "facility": "Dukhan",
    "unit": "Khatiyah Gas Gathering Station",
    "type": "Gas Separation Revamp",
    "expectedStart": "05-Jan-2027",
    "expectedEnd": "20-Jan-2027",
    "daysToShutdown": 95,
    "contractor": "Blackcat & TRAGS",
    "equipment": "3-Phase Separators, Gas Lift Manifold, Relief Flare",
    "productFit": "High: Emerson Gate/Ball Valves, Ashcroft Pressure Gauges",
    "recommendedAction": "Conduct pre-shutdown technical review with Blackcat Dukhan station manager"
  }
]
```

### 24 Monitored Portals
```json
[
  {
    "name": "QatarEnergy Official State Portal",
    "url": "https://www.qatarenergy.qa",
    "tier": "Tier A (State)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "QatarEnergy LNG Official Supplier Notices",
    "url": "https://www.qatarenergylng.qa",
    "tier": "Tier A (Operator)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "QAFCO Fertilizer Official Procurement",
    "url": "https://www.qafco.qa",
    "tier": "Tier A (Operator)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Q-Chem / RLOC Chemical Portal",
    "url": "https://www.qchem.com.qa",
    "tier": "Tier A (Operator)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "QAPCO Petrochemical Procurement Portal",
    "url": "https://www.qapco.com",
    "tier": "Tier A (Operator)",
    "status": "Protected (307)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "North Oil Company (NOC) Official Portal",
    "url": "https://www.noc.qa",
    "tier": "Tier A (Offshore Operator)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Qatar Shell Pearl GTL Official Site",
    "url": "https://www.shell.com.qa",
    "tier": "Tier A (GTL Operator)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Dolphin Energy Official Qatar Portal",
    "url": "https://www.dolphinenergy.com",
    "tier": "Tier A (Gas Operator)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Oryx GTL Official Corporate Site",
    "url": "https://www.oryxgtl.com.qa",
    "tier": "Tier A (GTL Operator)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "WOQOD Commercial Distribution Portal",
    "url": "https://www.woqod.com",
    "tier": "Tier A (Distribution)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "QAFAC Methanol Procurement Portal",
    "url": "https://www.qafac.com.qa",
    "tier": "Tier A (Operator)",
    "status": "Active (Verified)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Umm Al Houl Power (UHP) Portal",
    "url": "https://www.uhp.com.qa",
    "tier": "Tier A (Utility)",
    "status": "Active (Verified)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Mpower Power Generation Portal",
    "url": "https://www.mpower.com.qa",
    "tier": "Tier A (Utility)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "DOPET Engineering & Contracting Portal",
    "url": "https://www.dopet.com",
    "tier": "Tier B (EPC)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "QCON Turnaround & Construction Disclosures",
    "url": "https://www.qcon.com.qa",
    "tier": "Tier B (EPC)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "TRAGS Electrical & Engineering Qatar",
    "url": "https://www.tragsqatar.com",
    "tier": "Tier B (EPC)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Medgulf Construction Official Site",
    "url": "https://www.medgulfconstruction.com",
    "tier": "Tier B (EPC)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Blackcat Engineering & Construction",
    "url": "https://www.blackcat.qa",
    "tier": "Tier B (EPC)",
    "status": "Active (Verified)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Chiyoda Almana Engineering Portal",
    "url": "https://www.chiyodaalmana.com.qa",
    "tier": "Tier B (EPC/FEED)",
    "status": "Active (Verified)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "McDermott Offshore Qatar Site",
    "url": "https://www.mcdermott.com",
    "tier": "Tier B (Offshore EPC)",
    "status": "Protected (403)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Saipem Qatar Contracting Portal",
    "url": "https://www.saipem.com",
    "tier": "Tier B (EPC)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Technip Energies Qatar Portal",
    "url": "https://www.technipenergies.com",
    "tier": "Tier B (Mega EPC)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Consolidated Contractors Company (CCC)",
    "url": "https://www.ccc.net",
    "tier": "Tier B (Mega EPC)",
    "status": "Active (200 OK)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  },
  {
    "name": "Galfar Al Misnad Engineering Qatar",
    "url": "https://www.galfarqatar.com.qa",
    "tier": "Tier B (EPC)",
    "status": "Active (Verified)",
    "checkedAt": "02-Oct-2026 17:17 AST"
  }
]
```

### All 64 Active Opportunities (Complete Dataset)
```json
[
  {
    "id": "QTR-2026-0089",
    "client": "QatarEnergy",
    "facility": "Ras Laffan Industrial City",
    "project": "NFE Trains 1-4 Boil-Off Gas (BOG) Flare Modification",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "DOPET",
    "contractor": "DOPET Mechanical Div",
    "product": "Valves (Ball/Gate/Butterfly)",
    "brand": "Emerson / ASCO",
    "value": 1250000,
    "score": 93,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "15-Oct-2026",
    "detectedAgo": "14 hours ago",
    "nextAction": "Engage DOPET Procurement Head & Instrumentation Lead",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u062a\u0639\u062f\u064a\u0644 \u0648\u062a\u062d\u062f\u064a\u062b \u062e\u0637\u0648\u0637 \u063a\u0627\u0632 \u0627\u0644\u0628\u062e\u0627\u0631 \u0648\u0627\u0644\u0634\u0639\u0644\u0629 \u0641\u064a \u0645\u062c\u0645\u0639 \u0631\u0627\u0633 \u0644\u0641\u0627\u0646 \u0627\u0644\u0635\u0646\u0627\u0639\u064a\u060c \u064a\u0634\u0645\u0644 \u062a\u0648\u0631\u064a\u062f \u0648\u062a\u0631\u0643\u064a\u0628 \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u0627\u0644\u0636\u063a\u0637 \u0627\u0644\u0639\u0627\u0644\u064a \u0648\u0645\u062d\u0627\u0628\u0633 \u0627\u0644\u062a\u062d\u0643\u0645 \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0645\u064a\u0643\u0627\u0646\u064a\u0643\u064a\u0629.",
    "translatedText": "Project for modification and revamp of boil-off gas and flare lines at Ras Laffan Industrial Complex, including supply and installation of high-pressure isolation valves and electromechanical control valves.",
    "factText": "QatarEnergy officially issued notice of preliminary engineering package allocation to DOPET for Ras Laffan BOG flare system.",
    "signalText": "Multiple EPC mechanical requisitions show upcoming procurement of 600# and 900# cryogenic isolation valves.",
    "inferenceText": "Emerson ASCO solenoid valves and Adams high-performance triple-offset valves directly fit the sour BOG service envelope.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0092",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (Train 3 Overhaul)",
    "project": "LNG Train 3 Acid Gas Recovery Unit (AGRU) Valve Replacement",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "QCON",
    "contractor": "QCON Turnaround Team",
    "product": "Severe Service Valves",
    "brand": "ADAMS",
    "value": 880000,
    "score": 94,
    "confidence": "High (94%)",
    "status": "RFQ Received",
    "expectedRfq": "30-Sep-2026",
    "detectedAgo": "1 day ago",
    "nextAction": "Present ADAMS triple-eccentric metal-seated valve catalog to QCON package manager",
    "arabicText": "\u0627\u0633\u062a\u0628\u062f\u0627\u0644 \u0635\u0645\u0627\u0645\u0627\u062a \u0648\u062d\u062f\u0629 \u0645\u0639\u0627\u0644\u062c\u0629 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u062d\u0645\u0636\u064a \u0641\u064a \u062e\u0637 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 3 \u0644\u0636\u0645\u0627\u0646 \u0645\u0648\u062b\u0648\u0642\u064a\u0629 \u0627\u0644\u0639\u0632\u0644 \u0623\u062b\u0646\u0627\u0621 \u0627\u0644\u0625\u064a\u0642\u0627\u0641 \u0627\u0644\u0645\u0628\u0631\u0645\u062c.",
    "translatedText": "Replacement of Acid Gas Recovery Unit (AGRU) valves in LNG Train 3 to ensure positive isolation reliability during scheduled turnaround.",
    "factText": "QatarEnergy LNG scheduled Train 3 maintenance turnaround for Q4 2026.",
    "signalText": "QCON confirmed as primary mechanical turnaround contractor with live tender package.",
    "inferenceText": "Corrosive H2S/CO2 amine service requires ADAMS severe-service triple-eccentric rotary valves and Protectoseal vapor recovery units.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.qcon.com.qa"
  },
  {
    "id": "QTR-2026-0095",
    "client": "QAFCO",
    "facility": "Mesaieed Industrial City",
    "project": "QAFCO-7 Ammonia Plant Syngas Compressor Spares & Gauges",
    "stage": "Level 2 (FEED / Pre-RFQ)",
    "stageBadge": "FEED Stage",
    "epc": "TRAGS",
    "contractor": "TRAGS Engineering",
    "product": "Pressure & Temp Gauges",
    "brand": "Ashcroft / Bourdon",
    "value": 420000,
    "score": 89,
    "confidence": "High (91%)",
    "status": "Pre-RFQ",
    "expectedRfq": "20-Nov-2026",
    "detectedAgo": "2 days ago",
    "nextAction": "Coordinate with TRAGS engineering team on instrument data sheet specifications",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0623\u062c\u0647\u0632\u0629 \u0642\u064a\u0627\u0633 \u0627\u0644\u0636\u063a\u0637 \u0648\u062f\u0631\u062c\u0627\u062a \u0627\u0644\u062d\u0631\u0627\u0631\u0629 \u0648\u0636\u0648\u0627\u063a\u0637 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0627\u0635\u0637\u0646\u0627\u0639\u064a \u0644\u0645\u0635\u0646\u0639 \u0642\u0627\u0641\u0643\u0648 7 \u0644\u0644\u0623\u0645\u0648\u0646\u064a\u0627 \u0641\u064a \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Supply of pressure and temperature instruments and syngas compressor parts for QAFCO-7 Ammonia plant in Mesaieed.",
    "factText": "Consortium executing QAFCO-7 expanding utility connections for syngas loop.",
    "signalText": "TRAGS procurement team drafting vendor list for vibration-resistant solid front process gauges.",
    "inferenceText": "Ashcroft Duragauges and Bourdon explosion-proof transmitters are standard approved specification for QAFCO ammonia units.",
    "sourceUrl": "https://www.qafco.qa",
    "epcUrl": "https://www.tragsqatar.com"
  },
  {
    "id": "QTR-2026-0098",
    "client": "Q-Chem",
    "facility": "Mesaieed Industrial City",
    "project": "Polyethylene Plant 1 In-Line Flame Arrestors & Tank Vents",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Medgulf",
    "contractor": "Medgulf Mechanical Dept",
    "product": "Flame Arrestors & Vents",
    "brand": "Protectoseal",
    "value": 650000,
    "score": 92,
    "confidence": "High (95%)",
    "status": "Quotation",
    "expectedRfq": "18-Sep-2026",
    "detectedAgo": "3 days ago",
    "nextAction": "Submit commercial quotation with Protectoseal explosion-proof ATEX certificates",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0634\u0628\u0643\u0629 \u0645\u0627\u0646\u0639\u0627\u062a \u0627\u0644\u0644\u0647\u0628 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u062a\u0646\u0641\u064a\u0633 \u062e\u0632\u0627\u0646\u0627\u062a \u0627\u0644\u0645\u0648\u0627\u062f \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u0643\u0631\u0628\u0648\u0646\u064a\u0629 \u0628\u0645\u0635\u0646\u0639 \u0643\u064a\u0648\u0643\u064a\u0645 \u0644\u0644\u0628\u0648\u0644\u064a \u0625\u064a\u062b\u064a\u0644\u064a\u0646 \u0641\u064a \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Upgrade of in-line deflagration flame arrestors and tank pressure relief vents at Q-Chem Polyethylene plant in Mesaieed.",
    "factText": "Q-Chem issued safety upgrade mandate for volatile monomer storage tanks.",
    "signalText": "Medgulf estimating engineers received tender inquiry for ATEX certified end-of-line arrestors.",
    "inferenceText": "Protectoseal Series 4950 and Series 830 vents represent exact direct OEM replacement specification.",
    "sourceUrl": "https://www.qchem.com.qa",
    "epcUrl": "https://www.medgulfconstruction.com"
  },
  {
    "id": "QTR-2026-0101",
    "client": "QAPCO",
    "facility": "Mesaieed Petrochemical Complex",
    "project": "Ethylene Plant 2 Quench Water Circulation Pump Spares",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Madina Group",
    "contractor": "Madina Rotating Equipment Team",
    "product": "Pump Spares & Rotating Parts",
    "brand": "Trillium Flow Technologies",
    "value": 530000,
    "score": 88,
    "confidence": "High (93%)",
    "status": "Approached",
    "expectedRfq": "05-Nov-2026",
    "detectedAgo": "4 days ago",
    "nextAction": "Deliver Trillium rotating pump spares catalog to Madina Group Mesaieed workshop manager",
    "arabicText": "\u062a\u0623\u0645\u064a\u0646 \u0642\u0637\u0639 \u063a\u064a\u0627\u0631 \u0648\u0645\u0636\u062e\u0627\u062a \u062a\u062f\u0648\u064a\u0631 \u0645\u064a\u0627\u0647 \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0648\u062d\u062f\u0629 \u0627\u0644\u0625\u064a\u062b\u064a\u0644\u064a\u0646 \u0631\u0642\u0645 2 \u0641\u064a \u0645\u062c\u0645\u0639 \u0642\u0627\u0628\u0643\u0648 \u0628\u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Procurement of replacement impellers, shafts, and mechanical seals for quench water circulation pumps at QAPCO Ethylene Plant 2.",
    "factText": "QAPCO scheduled turnaround requires replacement of OEM slurry and quench pump wear components.",
    "signalText": "Madina Group mobilizing workshop space for rotating machinery rebuild.",
    "inferenceText": "Trillium OEM impellers and wear rings match installed pump serial registry at QAPCO.",
    "sourceUrl": "https://www.qapco.com",
    "epcUrl": "https://www.madinagroup.com"
  },
  {
    "id": "QTR-2026-0104",
    "client": "RLOC",
    "facility": "Ras Laffan Industrial City",
    "project": "Ras Laffan Olefins Ethane Cracker ESD Valve Positioners",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Roots Energy",
    "contractor": "Roots Energy E&I Division",
    "product": "Valve Monitoring & Positioners",
    "brand": "Westlock Controls",
    "value": 370000,
    "score": 90,
    "confidence": "High (92%)",
    "status": "Pre-RFQ",
    "expectedRfq": "28-Oct-2026",
    "detectedAgo": "5 days ago",
    "nextAction": "Schedule technical lunch-and-learn on Westlock AccuTrak digital position monitors with Roots Energy",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0623\u062c\u0647\u0632\u0629 \u0627\u0644\u0645\u0631\u0627\u0642\u0628\u0629 \u0627\u0644\u0630\u0643\u064a\u0629 \u0648\u0645\u062d\u062f\u062f\u0627\u062a \u0627\u0644\u0645\u0648\u0627\u0642\u0639 \u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0625\u063a\u0644\u0627\u0642 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0641\u064a \u0645\u062c\u0645\u0639 \u0631\u0627\u0633 \u0644\u0641\u0627\u0646 \u0644\u0644\u0623\u0648\u0644\u064a\u0641\u064a\u0646\u0627\u062a.",
    "translatedText": "Modernization of digital valve position monitors and switches for Emergency Shutdown (ESD) valves at RLOC ethane cracker.",
    "factText": "RLOC safety committee approved SIL-3 verification upgrade across automated valves.",
    "signalText": "Roots Energy instrumentation engineers requested specifications for flameproof position transmitters.",
    "inferenceText": "Westlock AccuTrak 2600 and Quantum digital monitors provide exact SIL-3 feedback required by RLOC standards.",
    "sourceUrl": "https://www.qchem.com.qa",
    "epcUrl": "https://www.rootsenergy.com"
  },
  {
    "id": "QTR-2026-0107",
    "client": "QatarEnergy",
    "facility": "Dukhan Oil Field (Fahahil Manifold)",
    "project": "Dukhan Gas Lift Manifold Pressure Transmitters & Solenoids",
    "stage": "Level 2 (FEED / Pre-RFQ)",
    "stageBadge": "FEED Stage",
    "epc": "Blackcat",
    "contractor": "Blackcat Upstream Div",
    "product": "Solenoid Valves & Actuation",
    "brand": "Emerson ASCO",
    "value": 460000,
    "score": 87,
    "confidence": "High (89%)",
    "status": "Pre-RFQ",
    "expectedRfq": "12-Dec-2026",
    "detectedAgo": "6 days ago",
    "nextAction": "Provide Blackcat procurement lead with ASCO RedHat explosion-proof solenoid pricing matrix",
    "arabicText": "\u062a\u062c\u062f\u064a\u062f \u0645\u0646\u0638\u0648\u0645\u0629 \u0627\u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0643\u0647\u0631\u0648\u0645\u063a\u0646\u0627\u0637\u064a\u0633\u064a\u0629 \u0648\u0623\u062c\u0647\u0632\u0629 \u0646\u0642\u0644 \u0627\u0644\u0636\u063a\u0637 \u0644\u0645\u062c\u0645\u0639 \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0631\u0641\u0639 \u0628\u0627\u0644\u063a\u0627\u0632 \u0641\u064a \u0645\u0646\u0637\u0642\u0629 \u062f\u062e\u0627\u0646 \u0627\u0644\u0641\u062d\u064a\u062d\u064a\u0644.",
    "translatedText": "Revamp of explosion-proof solenoid pilot valves and pressure transmitters at Dukhan Fahahil gas lift manifold.",
    "factText": "QatarEnergy awarded Dukhan gas lift optimization FEED package.",
    "signalText": "Blackcat engineering team preparing procurement package for high-pressure sour gas wellhead control.",
    "inferenceText": "ASCO 3-way/4-way explosion-proof stainless steel solenoid valves are standard specification on all Dukhan manifolds.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.blackcat.qa"
  },
  {
    "id": "QTR-2026-0110",
    "client": "QatarEnergy",
    "facility": "Offshore (Bul Hanine PS-3)",
    "project": "Bul Hanine Offshore PS-3 Wellhead Isolation Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Medgulf",
    "contractor": "Medgulf Offshore Dept",
    "product": "Process Valves",
    "brand": "Emerson / ASCO",
    "value": 790000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "10-Oct-2026",
    "detectedAgo": "1 week ago",
    "nextAction": "Prepare formal technical proposal for 2500# offshore rated ball and double-block-and-bleed valves",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u0627\u0633\u062a\u0628\u062f\u0627\u0644 \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0639\u0632\u0644 \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629 \u0644\u0645\u0646\u0635\u0627\u062a \u0631\u0624\u0648\u0633 \u0627\u0644\u0622\u0628\u0627\u0631 \u0627\u0644\u0628\u062d\u0631\u064a\u0629 \u0641\u064a \u062d\u0642\u0644 \u0628\u0648\u0627\u0644\u062d\u0646\u064a\u0646 \u0627\u0644\u0645\u0646\u0635\u0629 \u0627\u0644\u062b\u0627\u0644\u062b\u0629.",
    "translatedText": "Replacement of high-pressure topside double-block-and-bleed and isolation valves for Bul Hanine PS-3 offshore platform.",
    "factText": "QatarEnergy published offshore topside integrity refurbishment scope.",
    "signalText": "Medgulf offshore estimating division received tender package for super duplex and Inconel cladded valves.",
    "inferenceText": "Emerson high-pressure ball valves and ASCO offshore-rated pilot solenoids meet severe marine offshore criteria.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.medgulfconstruction.com"
  },
  {
    "id": "QTR-2026-0113",
    "client": "QAFAC",
    "facility": "Mesaieed Industrial City",
    "project": "Methanol Synthesis Reactor Temperature & Level Instruments",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Al Balagh",
    "contractor": "Al Balagh Petrochem Div",
    "product": "Pressure & Temp Gauges",
    "brand": "Baumer / Clark-Reliance",
    "value": 310000,
    "score": 86,
    "confidence": "High (90%)",
    "status": "Pre-RFQ",
    "expectedRfq": "15-Nov-2026",
    "detectedAgo": "1 week ago",
    "nextAction": "Send Baumer multi-point temperature sensor data sheets to Al Balagh engineering manager",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u062a\u062d\u062f\u064a\u062b \u0623\u062c\u0647\u0632\u0629 \u0642\u064a\u0627\u0633 \u062f\u0631\u062c\u0627\u062a \u0627\u0644\u062d\u0631\u0627\u0631\u0629 \u0648\u0645\u0633\u062a\u0648\u064a\u0627\u062a \u0627\u0644\u0633\u0648\u0627\u0626\u0644 \u0644\u0645\u0641\u0627\u0639\u0644 \u062a\u0635\u0646\u064a\u0639 \u0627\u0644\u0645\u064a\u062b\u0627\u0646\u0648\u0644 \u0641\u064a \u0642\u0627\u0641\u0627\u0643 \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Upgrade of multi-point reactor thermowells and level gauges at QAFAC Methanol synthesis plant.",
    "factText": "QAFAC scheduled catalyst replenishment and reactor inspection for early 2027.",
    "signalText": "Al Balagh engineering team requesting supplier credentials for high-temperature reactor instruments.",
    "inferenceText": "Baumer bimetal thermometers and Clark-Reliance magnetic level chambers match existing process nozzles.",
    "sourceUrl": "https://www.qafac.com.qa",
    "epcUrl": "https://www.albalagh.com"
  },
  {
    "id": "QTR-2026-0116",
    "client": "UHP",
    "facility": "Umm Al Houl Power & Water",
    "project": "Umm Al Houl Power Seawater Desalination Butterfly Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Al Muftah",
    "contractor": "Al Muftah Industrial Div",
    "product": "Severe Service Valves",
    "brand": "ADAMS",
    "value": 620000,
    "score": 89,
    "confidence": "High (91%)",
    "status": "Approached",
    "expectedRfq": "30-Nov-2026",
    "detectedAgo": "1 week ago",
    "nextAction": "Present ADAMS rubber-lined and high-alloy butterfly valves to Al Muftah procurement director",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0641\u0631\u0627\u0634\u0629 \u0645\u0642\u0627\u0648\u0645\u0629 \u0644\u0645\u064a\u0627\u0647 \u0627\u0644\u0628\u062d\u0631 \u0627\u0644\u0645\u0627\u0644\u062d\u0629 \u0644\u0645\u0646\u0634\u0623\u0629 \u062a\u062d\u0644\u064a\u0629 \u0627\u0644\u0645\u064a\u0627\u0647 \u0648\u062a\u0648\u0644\u064a\u062f \u0627\u0644\u0643\u0647\u0631\u0628\u0627\u0621 \u0641\u064a \u0623\u0645 \u0627\u0644\u062d\u0648\u0644.",
    "translatedText": "Supply of large-diameter high-nickel aluminum bronze butterfly valves for seawater intake expansion at Umm Al Houl Power.",
    "factText": "Umm Al Houl Power expanding RO desalination intake capacity by 30%.",
    "signalText": "Al Muftah Contracting shortlisting European valve manufacturers for seawater intake lines.",
    "inferenceText": "ADAMS triple-eccentric rotary valves provide bubble-tight shutoff against aggressive Gulf seawater.",
    "sourceUrl": "https://www.uhp.com.qa",
    "epcUrl": "https://www.almuftah.com"
  },
  {
    "id": "QTR-2026-0119",
    "client": "Mpower",
    "facility": "Ras Abu Fontas Industrial Zone",
    "project": "Ras Abu Fontas Power Station Gas Fuel Valve Actuators",
    "stage": "Level 2 (FEED / Pre-RFQ)",
    "stageBadge": "FEED Stage",
    "epc": "Roots Energy",
    "contractor": "Roots Energy Technical Services",
    "product": "Valve Monitoring & Positioners",
    "brand": "Westlock Controls",
    "value": 280000,
    "score": 84,
    "confidence": "High (88%)",
    "status": "Pre-RFQ",
    "expectedRfq": "15-Dec-2026",
    "detectedAgo": "1 week ago",
    "nextAction": "Provide Westlock digital valve controller technical documentation for turbine fuel skids",
    "arabicText": "\u062a\u062c\u062f\u064a\u062f \u0645\u0634\u063a\u0644\u0627\u062a \u0627\u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0648\u0623\u062c\u0647\u0632\u0629 \u0627\u0644\u0645\u0631\u0627\u0642\u0628\u0629 \u0644\u062e\u0637\u0648\u0637 \u0627\u0644\u0648\u0642\u0648\u062f \u0627\u0644\u063a\u0627\u0632\u064a \u0644\u062a\u0648\u0631\u0628\u064a\u0646\u0627\u062a \u062a\u0648\u0644\u064a\u062f \u0627\u0644\u0637\u0627\u0642\u0629 \u0641\u064a \u0631\u0627\u0633 \u0623\u0628\u0648 \u0641\u0646\u0637\u0627\u0633.",
    "translatedText": "Replacement of valve actuators and limit switch boxes on gas turbine fuel skids at Ras Abu Fontas power station.",
    "factText": "Mpower initiating annual turbine gas skid modernization.",
    "signalText": "Roots Energy engineering assessing automated valve feedback loop upgrades.",
    "inferenceText": "Westlock Quantum monitors with integral solenoid pilots streamline fuel valve actuation architecture.",
    "sourceUrl": "https://www.mpower.com.qa",
    "epcUrl": "https://www.rootsenergy.com"
  },
  {
    "id": "QTR-2026-0122",
    "client": "WOQOD",
    "facility": "Doha Fuel Depot & Bulk Terminal",
    "project": "Doha Jet Fuel Depot Emergency Shutoff Valve Package",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "DOPET",
    "contractor": "DOPET EPC Div",
    "product": "Process Valves",
    "brand": "Emerson / ASCO",
    "value": 490000,
    "score": 91,
    "confidence": "High (93%)",
    "status": "Quotation",
    "expectedRfq": "25-Sep-2026",
    "detectedAgo": "1 week ago",
    "nextAction": "Submit commercial bid for fire-safe full bore ball valves with DOPET estimating manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0642\u0637\u0639 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0627\u0644\u0645\u0642\u0627\u0648\u0645\u0629 \u0644\u0644\u062d\u0631\u064a\u0642 \u0648\u0645\u062d\u0627\u0628\u0633 \u0627\u0644\u0648\u0642\u0648\u062f \u0644\u0645\u062d\u0637\u0629 \u0648\u0642\u0648\u062f \u0627\u0644\u0637\u0627\u0626\u0631\u0627\u062a \u0627\u0644\u0645\u0631\u0643\u0632\u064a\u0629 \u0641\u064a \u0627\u0644\u062f\u0648\u062d\u0629.",
    "translatedText": "Supply of fire-safe emergency shutdown valves and pipeline ball valves for WOQOD Hamad Airport jet fuel distribution hub.",
    "factText": "WOQOD issued safety tender for bulk aviation fuel terminal automation.",
    "signalText": "DOPET bidding as lead mechanical and pipeline EPC contractor.",
    "inferenceText": "Emerson API 6D fire-safe ball valves and ASCO pilot solenoids meet stringent aviation fuel security requirements.",
    "sourceUrl": "https://www.woqod.com",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0125",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Gallaf Batch 3 Topside Cryogenic & ESD Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "McDermott",
    "contractor": "McDermott Offshore Projects",
    "product": "Severe Service Control Valves & Desuperheaters",
    "brand": "Fisher / Masoneilan",
    "value": 1480000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "08-Oct-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Engage McDermott Qatar package procurement manager with Fisher sour-gas control valve datasheets",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u062a\u0632\u0648\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u0636\u063a\u0637 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0639\u0632\u0644 \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0645\u0646\u0635\u0627\u062a \u0645\u0634\u0631\u0648\u0639 \u062c\u0644\u0627\u0641 \u0627\u0644\u0628\u062d\u0631\u064a\u0629 \u0641\u064a \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646.",
    "translatedText": "High-pressure topside control valves and emergency shutdown packages for North Oil Company Gallaf Batch 3 offshore platforms.",
    "factText": "North Oil Company confirmed McDermott executing offshore topsides fabrication.",
    "signalText": "McDermott issuing technical inquiries for severe service sour gas control valves with noise attenuation trim.",
    "inferenceText": "Fisher severe service globe control valves with cavitrol trim provide required erosive flow resistance.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.mcdermott.com"
  },
  {
    "id": "QTR-2026-0128",
    "client": "Qatar Shell Pearl GTL",
    "facility": "Ras Laffan Industrial City",
    "project": "Pearl GTL Train 1 Heavy Paraffin Conversion Level Radar",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Chiyoda Almana",
    "contractor": "Chiyoda Almana Engineering",
    "product": "Level Instrumentation & Tank Gauging",
    "brand": "Magnetrol / Emerson Rosemount",
    "value": 740000,
    "score": 92,
    "confidence": "High (94%)",
    "status": "Pre-RFQ",
    "expectedRfq": "24-Oct-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Magnetrol Eclipse 706 Guided Wave Radar to Chiyoda Almana instrumentation lead",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0623\u062c\u0647\u0632\u0629 \u0642\u064a\u0627\u0633 \u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u0633\u0648\u0627\u0626\u0644 \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u062f\u0642\u0629 \u0644\u0648\u062d\u062f\u0629 \u062a\u062d\u0648\u064a\u0644 \u0627\u0644\u0628\u0627\u0631\u0627\u0641\u064a\u0646 \u0627\u0644\u062b\u0642\u064a\u0644 \u0641\u064a \u0645\u062c\u0645\u0639 \u0627\u0644\u0644\u0624\u0644\u0624\u0629 \u0644\u062a\u062d\u0648\u064a\u0644 \u0627\u0644\u063a\u0627\u0632 \u0644\u0633\u0648\u0627\u0626\u0644.",
    "translatedText": "Revamp of guided wave radar level transmitters for high-temperature heavy paraffin reactors at Shell Pearl GTL.",
    "factText": "Qatar Shell Pearl GTL initiated Phase-1 debottlenecking for synthesis liquid conversion.",
    "signalText": "Chiyoda Almana completing detailed FEED package for liquid level measurement across catalytic reactors.",
    "inferenceText": "Magnetrol high-temperature / high-pressure radar transmitters resist heavy wax buildup and extreme process heat.",
    "sourceUrl": "https://www.shell.com.qa",
    "epcUrl": "https://www.chiyodaalmana.com.qa"
  },
  {
    "id": "QTR-2026-0131",
    "client": "Dolphin Energy",
    "facility": "Ras Laffan Industrial City",
    "project": "Ras Laffan Gas Processing Export Compressor Bypass Control Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies Gas Div",
    "product": "Severe Service Rotary Valves",
    "brand": "ADAMS / Fisher",
    "value": 1120000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "RFQ Received",
    "expectedRfq": "14-Oct-2026",
    "detectedAgo": "8 hours ago",
    "nextAction": "Submit ADAMS triple-eccentric metal-seated bid to Technip Energies procurement team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0627\u0644\u0627\u0644\u062a\u0641\u0627\u0641\u064a\u0629 \u0644\u0636\u0648\u0627\u063a\u0637 \u062a\u0635\u062f\u064a\u0631 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629 \u0641\u064a \u0645\u062d\u0637\u0629 \u0645\u0639\u0627\u0644\u062c\u0629 \u063a\u0627\u0632 \u062f\u0648\u0644\u0641\u064a\u0646 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Procurement of anti-surge bypass and high-differential pressure isolation valves for export gas compressors at Dolphin Energy.",
    "factText": "Dolphin Energy scheduled major compressor revamp for cross-border export stream.",
    "signalText": "Technip Energies actively negotiating subcontract equipment packages for export compression train.",
    "inferenceText": "ADAMS tight-shutoff metal-seated valves prevent high-velocity sour gas leakage across critical compressor loops.",
    "sourceUrl": "https://www.dolphinenergy.com",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0134",
    "client": "Oryx GTL",
    "facility": "Ras Laffan Industrial City",
    "project": "Hydrocracker Diesel Unit Hydrogen Bleed & Isolation Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Descon Engineering",
    "contractor": "Descon Turnaround Specialists",
    "product": "Process Valves",
    "brand": "Emerson / ASCO",
    "value": 680000,
    "score": 90,
    "confidence": "High (93%)",
    "status": "Approached",
    "expectedRfq": "02-Nov-2026",
    "detectedAgo": "10 hours ago",
    "nextAction": "Coordinate with Descon turnaround planners for high-pressure hydrogen service valve datasheets",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u0627\u0633\u062a\u0628\u062f\u0627\u0644 \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u062c\u064a\u0646 \u0639\u0627\u0644\u064a \u0627\u0644\u0636\u063a\u0637 \u0644\u0648\u062d\u062f\u0629 \u0627\u0644\u062a\u0643\u0633\u064a\u0631 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u062c\u064a\u0646\u064a \u0644\u0644\u062f\u064a\u0632\u0644 \u0641\u064a \u0645\u062c\u0645\u0639 \u0623\u0648\u0631\u064a\u0643\u0633 \u062c\u064a \u062a\u064a \u0625\u0644.",
    "translatedText": "Replacement of hydrogen service isolation valves and high-temperature manifolds at Oryx GTL hydrocracker.",
    "factText": "Oryx GTL finalized planned turnaround scope for diesel hydroprocessing section.",
    "signalText": "Descon Engineering mobilizing specialized valve technicians for high-pressure hydrogen loop overhaul.",
    "inferenceText": "Emerson low-emission Fugitive Emission certified gate and globe valves fulfill severe hydrogen permeation standards.",
    "sourceUrl": "https://www.oryxgtl.com.qa",
    "epcUrl": "https://www.descon.com"
  },
  {
    "id": "QTR-2026-0137",
    "client": "QatarEnergy",
    "facility": "Halul Island Crude Terminal",
    "project": "Halul Island Crude Oil Terminal Storage Tank Venting & P/V Valves",
    "stage": "Level 2 (FEED / Pre-RFQ)",
    "stageBadge": "FEED Stage",
    "epc": "Galfar Al Misnad",
    "contractor": "Galfar Mechanical Team",
    "product": "Flame Arrestors & Tank Vents",
    "brand": "Protectoseal",
    "value": 830000,
    "score": 91,
    "confidence": "High (92%)",
    "status": "Pre-RFQ",
    "expectedRfq": "18-Nov-2026",
    "detectedAgo": "12 hours ago",
    "nextAction": "Deliver Protectoseal marine-grade aluminum pressure/vacuum relief valve specs to Galfar engineering",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u062a\u062d\u062f\u064a\u062b \u0635\u0645\u0627\u0645\u0627\u062a \u062a\u0646\u0641\u064a\u0633 \u062e\u0632\u0627\u0646\u0627\u062a \u0627\u0644\u0646\u0641\u0637 \u0627\u0644\u062e\u0627\u0645 \u0648\u0645\u0627\u0646\u0639\u0627\u062a \u0627\u0644\u0644\u0647\u0628 \u0641\u064a \u062c\u0632\u064a\u0631\u0629 \u062d\u0627\u0644\u0648\u0644 \u0627\u0644\u0628\u062a\u0631\u0648\u0644\u064a\u0629 \u0627\u0644\u062a\u0627\u0628\u0639\u0629 \u0644\u0642\u0637\u0631 \u0644\u0644\u0637\u0627\u0642\u0629.",
    "translatedText": "Upgrade of breathing valves and marine-coated detonation flame arrestors for floating roof crude oil storage tanks on Halul Island.",
    "factText": "QatarEnergy issued storage tank integrity and environmental emission compliance tender.",
    "signalText": "Galfar Al Misnad performing site survey for tank farm piping and vent lines on Halul Island.",
    "inferenceText": "Protectoseal Series 8540 end-of-line breather vents with epoxy coating withstand aggressive offshore marine corrosion.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.galfarqatar.com.qa"
  },
  {
    "id": "QTR-2026-0140",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan Port & LNG Berths",
    "project": "North Field South NFS LNG Loading Arms & Dock Revamp",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Saipem",
    "contractor": "Saipem Qatar Marine Div",
    "product": "Custody Transfer Flow & Metering Systems",
    "brand": "Daniel Measurement / Emerson",
    "value": 1650000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "28-Sep-2026",
    "detectedAgo": "16 hours ago",
    "nextAction": "Submit Daniel custody transfer ultrasonic LNG flowmeter technical package to Saipem marine team",
    "arabicText": "\u062a\u0637\u0648\u064a\u0631 \u0623\u0630\u0631\u0639 \u062a\u062d\u0645\u064a\u0644 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0637\u0628\u064a\u0639\u064a \u0627\u0644\u0645\u0633\u0627\u0644 \u0648\u0623\u0646\u0638\u0645\u0629 \u0627\u0644\u0642\u064a\u0627\u0633 \u0627\u0644\u0631\u0633\u0645\u064a\u0629 \u0644\u0623\u0631\u0635\u0641\u0629 \u0627\u0644\u062a\u0635\u062f\u064a\u0631 \u0627\u0644\u062c\u062f\u064a\u062f\u0629 \u0627\u0644\u062a\u0627\u0628\u0639\u0629 \u0644\u062d\u0642\u0644 \u0627\u0644\u0634\u0645\u0627\u0644 \u0627\u0644\u062c\u0646\u0648\u0628\u064a.",
    "translatedText": "Revamp of cryogenic LNG loading arms and ultrasonic custody transfer flow metering systems for North Field South export berths.",
    "factText": "QatarEnergy LNG expanding berth export capacity for upcoming NFS LNG output.",
    "signalText": "Saipem marine procurement team issued formal ITT package for cryogenic custody transfer metering skids.",
    "inferenceText": "Daniel Senior ultrasonic gas meters and Micro Motion cryogenic Coriolis meters are standard QatarEnergy LNG approved custody meters.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.saipem.com"
  },
  {
    "id": "QTR-2026-0143",
    "client": "QatarEnergy",
    "facility": "Ras Laffan Industrial City",
    "project": "North Field East NFE Carbon Capture & Sequestration Compression Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "CCC (Consolidated Contractors)",
    "contractor": "CCC Heavy Mechanical Division",
    "product": "High-Pressure Flange Gaskets & Sealing",
    "brand": "Flexitallic / Lamons",
    "value": 920000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Approached",
    "expectedRfq": "10-Nov-2026",
    "detectedAgo": "18 hours ago",
    "nextAction": "Meet CCC Qatar technical procurement team to finalize Flexitallic Kammprofile gasket package for CO2 trains",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u062d\u0634\u064a\u0627\u062a \u0625\u062d\u0643\u0627\u0645 \u0627\u0644\u0636\u063a\u0637 \u0627\u0644\u0639\u0627\u0644\u064a \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0639\u0632\u0644 \u0644\u0645\u0634\u0631\u0648\u0639 \u0627\u062d\u062a\u062c\u0627\u0632 \u0648\u062a\u062e\u0632\u064a\u0646 \u0627\u0644\u0643\u0631\u0628\u0648\u0646 \u0641\u064a \u062d\u0642\u0644 \u0627\u0644\u0634\u0645\u0627\u0644 \u0627\u0644\u0634\u0631\u0642\u064a.",
    "translatedText": "Supply of high-pressure Kammprofile gaskets and dense-phase CO2 isolation valves for NFE Carbon Capture & Sequestration facility.",
    "factText": "QatarEnergy advancing 4.3 MTPA carbon capture facility adjacent to NFE mega trains.",
    "signalText": "CCC mobilizing mechanical fabrication crews for supercritical CO2 injection piping.",
    "inferenceText": "Supercritical CO2 service mandates Flexitallic Sigma and Kammprofile gaskets with Inconel cores to prevent explosive decompression.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.ccc.net"
  },
  {
    "id": "QTR-2026-0146",
    "client": "QAFCO",
    "facility": "Mesaieed Industrial City",
    "project": "QAFCO-5 Urea Granulation Scrubber Fluid Instrumentation & Control",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Petrofac",
    "contractor": "Petrofac Plant Services",
    "product": "Safety Relief Valves & Rupture Discs",
    "brand": "Continental Disc / Crosby",
    "value": 580000,
    "score": 89,
    "confidence": "High (91%)",
    "status": "Pre-RFQ",
    "expectedRfq": "22-Nov-2026",
    "detectedAgo": "20 hours ago",
    "nextAction": "Provide Continental Disc sanitary and corrosive-service rupture disc datasheets to Petrofac team",
    "arabicText": "\u062a\u062c\u062f\u064a\u062f \u0623\u062c\u0647\u0632\u0629 \u0642\u064a\u0627\u0633 \u0648\u0636\u0628\u0637 \u0627\u0644\u0633\u0648\u0627\u0626\u0644 \u0648\u0623\u0642\u0631\u0627\u0635 \u0627\u0644\u062a\u0645\u0632\u0642 \u0644\u063a\u0627\u0633\u0644\u0627\u062a \u0627\u0644\u063a\u0628\u0627\u0631 \u0628\u0645\u0635\u0646\u0639 \u064a\u0648\u0631\u064a\u0627 5 \u0641\u064a \u0634\u0631\u0643\u0629 \u0642\u0627\u0641\u0643\u0648 \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Replacement of safety relief valves and rupture discs on urea dust scrubber towers at QAFCO-5.",
    "factText": "QAFCO environmental emission control upgrade tender allocated to plant service contractors.",
    "signalText": "Petrofac engineering team reviewing overpressure protection specifications for corrosive carbamate fluid lines.",
    "inferenceText": "Continental Disc HPX rupture discs with Crosby safety valves provide non-fragmenting protection against corrosive urea slurry crystallization.",
    "sourceUrl": "https://www.qafco.qa",
    "epcUrl": "https://www.petrofac.com"
  },
  {
    "id": "QTR-2026-0149",
    "client": "Q-Chem",
    "facility": "Mesaieed Industrial City",
    "project": "Mesaieed 1-Hexene Unit Polymerization High-Pressure Gaskets & Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Kent",
    "contractor": "Kent Energies Qatar",
    "product": "Industrial Coalescers & Gas Separation Filtration",
    "brand": "Pall Corporation / Parker",
    "value": 640000,
    "score": 92,
    "confidence": "High (94%)",
    "status": "Quotation",
    "expectedRfq": "04-Oct-2026",
    "detectedAgo": "1 day ago",
    "nextAction": "Submit Pall gas coalescer and catalyst recovery filter element bid to Kent Energies procurement",
    "arabicText": "\u062a\u062c\u0647\u064a\u0632 \u0641\u0644\u0627\u062a\u0631 \u0641\u0635\u0644 \u0627\u0644\u063a\u0627\u0632\u0627\u062a \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u0643\u0641\u0627\u0621\u0629 \u0648\u062d\u0634\u064a\u0627\u062a \u0627\u0644\u0636\u063a\u0637 \u0644\u0645\u0635\u0646\u0639 \u0627\u0644\u0647\u0643\u0633\u064a\u0646-1 \u0627\u0644\u062a\u0627\u0628\u0639 \u0644\u0634\u0631\u0643\u0629 \u0643\u064a\u0648\u0643\u064a\u0645 \u0641\u064a \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Supply of liquid/gas coalescing filter elements and severe-service polymerization valves for Q-Chem 1-Hexene plant.",
    "factText": "Q-Chem launched specialty chemicals debottlenecking package.",
    "signalText": "Kent Energies preparing commercial subcontracts for catalyst separator revamp.",
    "inferenceText": "Pall SepraSol high-efficiency gas coalescers prevent catalyst fines carryover into downstream polymerization reactors.",
    "sourceUrl": "https://www.qchem.com.qa",
    "epcUrl": "https://www.kentplc.com"
  },
  {
    "id": "QTR-2026-0152",
    "client": "QatarEnergy",
    "facility": "Mesaieed Refinery",
    "project": "Continuous Catalytic Reformer CCR Valve & Instrument Package",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "HEISCO",
    "contractor": "HEISCO Qatar Plant Div",
    "product": "Severe Service Valves",
    "brand": "ADAMS / Emerson",
    "value": 1180000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "RFQ Received",
    "expectedRfq": "12-Oct-2026",
    "detectedAgo": "1 day ago",
    "nextAction": "Deliver ADAMS high-temperature metal-seated catalyst isolation valve proposal to HEISCO team",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u0627\u0633\u062a\u0628\u062f\u0627\u0644 \u0635\u0645\u0627\u0645\u0627\u062a \u0645\u0635\u0641\u0627\u0629 \u0645\u0633\u064a\u0639\u064a\u062f \u0644\u0648\u062d\u062f\u0629 \u0627\u0644\u062a\u0643\u0633\u064a\u0631 \u0627\u0644\u062d\u0641\u0632\u064a \u0627\u0644\u0645\u0633\u062a\u0645\u0631 \u0648\u0627\u0644\u0645\u0628\u0627\u062f\u0644\u0627\u062a \u0627\u0644\u062d\u0631\u0627\u0631\u064a\u0629 \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u062d\u0631\u0627\u0631\u0629.",
    "translatedText": "High-temperature metal-seated rotary valves and catalyst transfer isolation package for Mesaieed Refinery CCR unit.",
    "factText": "QatarEnergy Refinery scheduled major furnace and catalytic reformer shutdown for early 2027.",
    "signalText": "HEISCO Qatar secured pre-shutdown fabrication and valve servicing subcontract.",
    "inferenceText": "ADAMS triple-eccentric valves handle 550\u00b0C catalyst-laden flue gases without jamming or leakage.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.heisco.com"
  },
  {
    "id": "QTR-2026-0155",
    "client": "QatarEnergy",
    "facility": "Dukhan Field (Khatiyah Station)",
    "project": "Dukhan Khatiyah Gas Gathering Multiphase Metering & Safety Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "GDI",
    "contractor": "GDI Technical Services",
    "product": "Pressure & Temp Gauges",
    "brand": "Ashcroft / Bourdon",
    "value": 510000,
    "score": 88,
    "confidence": "High (90%)",
    "status": "Approached",
    "expectedRfq": "15-Nov-2026",
    "detectedAgo": "2 days ago",
    "nextAction": "Provide Ashcroft solid-front pressure transmitters and thermowells to GDI technical team",
    "arabicText": "\u062a\u0637\u0648\u064a\u0631 \u0623\u062c\u0647\u0632\u0629 \u0627\u0644\u0642\u064a\u0627\u0633 \u0645\u062a\u0639\u062f\u062f\u0629 \u0627\u0644\u0623\u0637\u0648\u0627\u0631 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0623\u0645\u0627\u0646 \u0644\u0645\u062d\u0637\u0629 \u062a\u062c\u0645\u064a\u0639 \u0627\u0644\u063a\u0627\u0632 \u0641\u064a \u062e\u0637\u064a\u0629 \u0628\u062d\u0642\u0644 \u062f\u062e\u0627\u0646.",
    "translatedText": "Instrumentation and safety valve upgrade for Khatiyah onshore crude/gas separation manifold in Dukhan.",
    "factText": "QatarEnergy onshore production division expanding remote monitoring across Dukhan gathering stations.",
    "signalText": "GDI technical team drafting field instrumentation requisitions for high-vibration wellhead flow lines.",
    "inferenceText": "Ashcroft Duragauges with PLUS! performance dampeners resist extreme wellhead pulsation.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.gdi.com.qa"
  },
  {
    "id": "QTR-2026-0158",
    "client": "QAPCO",
    "facility": "Mesaieed Petrochemical Complex",
    "project": "LDPE Autoclave Reactor High-Pressure Safety Relief & Rupture Discs",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "QCON",
    "contractor": "QCON Petrochem Div",
    "product": "Fire & Gas Detection Systems",
    "brand": "Dr\u00e4ger / Det-Tronics",
    "value": 720000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Quotation",
    "expectedRfq": "06-Oct-2026",
    "detectedAgo": "2 days ago",
    "nextAction": "Submit Det-Tronics optical flame detector and combustible gas sensing system bid to QCON",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u062a\u0632\u0648\u064a\u062f \u0643\u0648\u0627\u0634\u0641 \u0627\u0644\u0644\u0647\u0628 \u0648\u0627\u0644\u062d\u0631\u064a\u0642 \u0627\u0644\u0628\u0635\u0631\u064a\u0629 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062d\u0645\u0627\u064a\u0629 \u0644\u0645\u0641\u0627\u0639\u0644 \u0627\u0644\u0628\u0648\u0644\u064a \u0625\u064a\u062b\u064a\u0644\u064a\u0646 \u0645\u0646\u062e\u0641\u0636 \u0627\u0644\u0643\u062b\u0627\u0641\u0629 \u0628\u0642\u0627\u0628\u0643\u0648.",
    "translatedText": "Optical flame detection sensors and high-pressure reactor safety interlocks for QAPCO LDPE Autoclave units.",
    "factText": "QAPCO safety engineering team released emergency shutdown detection system tender.",
    "signalText": "QCON invited specialized safety instrument vendors to submit ATEX Zone 1 certified flame detectors.",
    "inferenceText": "Det-Tronics X3301 multispectrum IR flame detectors deliver false-alarm immunity in ethylene polymerization environments.",
    "sourceUrl": "https://www.qapco.com",
    "epcUrl": "https://www.qcon.com.qa"
  },
  {
    "id": "QTR-2026-0160",
    "client": "QatarEnergy",
    "facility": "Ras Laffan Industrial City",
    "project": "NFS Mega-Train Cryogenic Storage & Offloading BOG Compressor Skid",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Technip Energies",
    "contractor": "Technip Energies LNG Div",
    "product": "Cryogenic Ball & Butterfly Valves",
    "brand": "Emerson / ADAMS",
    "value": 1450000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "Pre-RFQ",
    "expectedRfq": "10-Nov-2026",
    "detectedAgo": "2 hours ago",
    "nextAction": "Engage Technip Energies cryogenic package manager for ADAMS triple-eccentric valve qualification",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u062e\u0632\u0627\u0646 \u0648\u063a\u0627\u0632\u0627\u062a \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0627\u0644\u0639\u0645\u064a\u0642 \u0641\u064a \u0645\u062c\u0645\u0639 \u063a\u0627\u0632 \u0627\u0644\u0634\u0645\u0627\u0644 \u0627\u0644\u062c\u0646\u0648\u0628\u064a \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "North Field South (NFS) cryogenic boil-off gas compressor skid and offloading line revamp.",
    "factText": "QatarEnergy officially sanctioned NFS offloading loop expansion.",
    "signalText": "Technip Energies issued vendor qualification notice for 900# cryogenic isolation valves.",
    "inferenceText": "Emerson Cryogenic Ball Valves and ADAMS Metal-Seated Valves directly fit low-temperature LNG service.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0163",
    "client": "QAFCO",
    "facility": "Mesaieed Industrial City",
    "project": "QAFCO-6 Urea Plant Granulation Tower Scrubbing Fan Spares & Vents",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "DOPET",
    "contractor": "DOPET Turnaround Dept",
    "product": "Flame Arrestors & Tank Vents",
    "brand": "Protectoseal",
    "value": 980000,
    "score": 92,
    "confidence": "High (94%)",
    "status": "RFQ Received",
    "expectedRfq": "25-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Submit Protectoseal explosion-proof ATEX breather vent package to DOPET estimating team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u062a\u0646\u0641\u064a\u0633 \u0648\u0645\u0627\u0646\u0639\u0627\u062a \u0644\u0647\u0628 \u0644\u0628\u0631\u062c \u062a\u062d\u0628\u064a\u0628 \u0627\u0644\u064a\u0648\u0631\u064a\u0627 \u0628\u0645\u0635\u0646\u0639 \u0642\u0627\u0641\u0643\u0648 6 \u0641\u064a \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Supply of explosion-proof tank vents and deflagration flame arrestors for QAFCO-6 Urea granulation tower.",
    "factText": "QAFCO safety integrity report mandated replacement of atmospheric relief vents.",
    "signalText": "DOPET mechanical turnaround division requested ATEX certified pressure/vacuum relief valve quotation.",
    "inferenceText": "Protectoseal Series 830 vents match existing flanged vessel nozzles.",
    "sourceUrl": "https://www.qafco.qa",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0166",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Offshore Platform Gallaf Phase 3 Sour Gas Manifold Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Saipem",
    "contractor": "Saipem Offshore Contracting",
    "product": "Solenoid Valves & Actuation",
    "brand": "Emerson ASCO",
    "value": 1120000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "15-Oct-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Deliver ASCO 316L explosion-proof pilot solenoid proposal to Saipem offshore instrumentation team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0645\u062d\u0627\u0628\u0633 \u0643\u0647\u0631\u0648\u0645\u063a\u0646\u0627\u0637\u064a\u0633\u064a\u0629 \u0648\u0645\u062c\u0645\u0639\u0627\u062a \u063a\u0627\u0632 \u062d\u0645\u0636\u064a \u0644\u0645\u0646\u0635\u0629 \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a.",
    "translatedText": "Supply of sour-gas rated pilot solenoid valves and double-block-and-bleed manifolds for Al Shaheen topsides.",
    "factText": "NOC issued offshore platform expansion notice for Gallaf Phase 3.",
    "signalText": "Saipem offshore procurement team requested Inconel trim SIL-3 solenoid pilot valves.",
    "inferenceText": "ASCO 3-way stainless steel solenoids meet NOC severe offshore H2S specification.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.saipem.com"
  },
  {
    "id": "QTR-2026-0169",
    "client": "Q-Chem",
    "facility": "Mesaieed Industrial City",
    "project": "Q-Chem II Hexene-1 Plant Polyolefin Reactor Gauges & Positioners",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Medgulf",
    "contractor": "Medgulf E&I Division",
    "product": "Pressure & Temp Gauges",
    "brand": "Ashcroft / Westlock",
    "value": 850000,
    "score": 91,
    "confidence": "High (93%)",
    "status": "Pre-RFQ",
    "expectedRfq": "05-Dec-2026",
    "detectedAgo": "7 hours ago",
    "nextAction": "Present Ashcroft Duragauge solid-front process gauges and Westlock digital monitors to Medgulf",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0623\u062c\u0647\u0632\u0629 \u0642\u064a\u0627\u0633 \u0627\u0644\u0636\u063a\u0637 \u0648\u0645\u062d\u062f\u062f\u0627\u062a \u0645\u0648\u0642\u0639 \u0627\u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0644\u0645\u0635\u0646\u0639 \u0627\u0644\u0647\u064a\u0643\u0633\u064a\u0646 1 \u0641\u064a \u0643\u064a\u0648\u0643\u064a\u0645 \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Upgrade of solid-front pressure gauges and digital valve position monitors at Q-Chem II Hexene-1 plant.",
    "factText": "Q-Chem II scheduled reactor instrumentation revamp package.",
    "signalText": "Medgulf instrumentation engineers preparing vendor list for SIL-2 position monitors and liquid-filled gauges.",
    "inferenceText": "Ashcroft 1279 Duragauges and Westlock AccuTrak positioners provide direct drop-in replacement.",
    "sourceUrl": "https://www.qchem.com.qa",
    "epcUrl": "https://www.medgulfconstruction.com"
  },
  {
    "id": "QTR-2026-0172",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan Industrial City",
    "project": "Train 7 Main Cryogenic Heat Exchanger (MCHE) Relief & Control Valve Package",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies LNG Div",
    "product": "Cryogenic Control & Severe Service Valves",
    "brand": "ADAMS / Fisher",
    "value": 1650000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "05-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Submit ADAMS triple-eccentric cryogenic butterfly and Fisher severe-service control valve technical offer to Technip Energies",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u062a\u062d\u062f\u064a\u062b \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0648\u0627\u0644\u0636\u063a\u0637 \u0627\u0644\u0639\u0627\u0644\u064a \u0644\u0648\u062d\u062f\u0629 \u0627\u0644\u0645\u0628\u0627\u062f\u0644 \u0627\u0644\u062d\u0631\u0627\u0631\u064a \u0627\u0644\u0631\u0626\u064a\u0633\u064a \u0644\u0642\u0637\u0627\u0631 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 7 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Revamp of high-pressure control valves and cryogenic isolation packages for LNG Train 7 MCHE debottlenecking.",
    "factText": "QatarEnergy LNG issued debottlenecking approval for Train 7 export throughput boost.",
    "signalText": "Technip Energies issued tender inquiry for 1200# cryogenic metal-seated valves.",
    "inferenceText": "ADAMS triple-offset metal-seated valves and Fisher control valves fit low-temp (-162\u00b0C) LNG service.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0175",
    "client": "QAFCO",
    "facility": "Mesaieed Industrial City",
    "project": "QAFCO-5 Ammonia Synthesis Converter Hot Gas Bypass & Safety Relief Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "DOPET",
    "contractor": "DOPET Turnaround & Maintenance Div",
    "product": "Severe Service Safety Valves & Rupture Discs",
    "brand": "Crosby / Continental Disc",
    "value": 1120000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "18-Nov-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Provide Crosby high-pressure safety relief valve specifications to DOPET QAFCO turnaround team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0623\u0645\u0627\u0646 \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u0636\u063a\u0637 \u0648\u0623\u0642\u0631\u0627\u0635 \u062a\u0645\u0632\u0642 \u0644\u0645\u062d\u0648\u0644 \u0627\u0644\u0623\u0645\u0648\u0646\u064a\u0627 \u0628\u0645\u0635\u0646\u0639 \u0642\u0627\u0641\u0643\u0648 5 \u0641\u064a \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Procurement of high-pressure safety relief valves and rupture disc assemblies for QAFCO-5 ammonia converter loop.",
    "factText": "QAFCO scheduled QAFCO-5 synthesis loop turnaround for early 2027.",
    "signalText": "DOPET turnaround team drafting vendor qualification list for 1500# syngas safety relief valves.",
    "inferenceText": "Crosby JOS-E pressure relief valves with Inconel bellows withstand high-temperature syngas service.",
    "sourceUrl": "https://www.qafco.qa",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0178",
    "client": "Qatar Shell Pearl GTL",
    "facility": "Ras Laffan Industrial City",
    "project": "Pearl GTL Train 2 Synthesis Gas Slurry Bubble Column Reactor Gauges & Positioners",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Chiyoda Almana",
    "contractor": "Chiyoda Almana E&I Team",
    "product": "Valve Monitoring & Digital Positioners",
    "brand": "Westlock Controls / Ashcroft",
    "value": 890000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "RFQ Received",
    "expectedRfq": "12-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Present Westlock SIL-3 AccuTrak digital position transmitters and Ashcroft liquid-filled process gauges to Chiyoda Almana",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0623\u062c\u0647\u0632\u0629 \u0645\u0631\u0627\u0642\u0628\u0629 \u0648\u0645\u062d\u062f\u062f\u0627\u062a \u0645\u0648\u0627\u0636\u0639 \u0627\u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0644\u0645\u0641\u0627\u0639\u0644\u0627\u062a \u062a\u062d\u0648\u064a\u0644 \u0627\u0644\u063a\u0627\u0632 \u0644\u0633\u0648\u0627\u0626\u0644 \u0641\u064a \u0645\u062c\u0645\u0639 \u0627\u0644\u0644\u0624\u0644\u0624\u0629 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Instrumentation revamp for slurry bubble column synthesis reactors at Shell Pearl GTL Train 2.",
    "factText": "Shell Pearl GTL authorized reactor instrumentation safety enhancement program.",
    "signalText": "Chiyoda Almana E&I engineers requested SIL-3 rated explosion-proof limit switch boxes and solid-front pressure gauges.",
    "inferenceText": "Westlock 2600 AccuTrak positioners and Ashcroft Duragauges meet severe GTL synthesis operating conditions.",
    "sourceUrl": "https://www.shell.com.qa",
    "epcUrl": "https://www.chiyodaalmana.com.qa"
  },
  {
    "id": "QTR-2026-0181",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Ruya (Gallaf Phase 3) Platform Subsea ESD & Hydraulic Control Skids",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "McDermott",
    "contractor": "McDermott Subsea Div",
    "product": "Solenoid Valves & Hydraulic Actuation",
    "brand": "Emerson ASCO",
    "value": 1340000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "Pre-RFQ",
    "expectedRfq": "01-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Deliver ASCO 316L stainless steel explosion-proof solenoid valve proposal to McDermott offshore project management",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u0643\u0647\u0631\u0648\u0645\u063a\u0646\u0627\u0637\u064a\u0633\u064a\u0629 \u0644\u0645\u0646\u0635\u0627\u062a \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a \u0636\u0645\u0646 \u0645\u0634\u0631\u0648\u0639 \u0631\u0648\u064a\u0627.",
    "translatedText": "Supply of offshore-grade pilot solenoid valves and hydraulic ESD skids for NOC Ruya Project platforms.",
    "factText": "North Oil Company sanctioned Ruya Project mega offshore expansion package.",
    "signalText": "McDermott offshore engineering team issued vendor list request for 316L SIL-3 solenoid control manifolds.",
    "inferenceText": "ASCO 3-way stainless steel solenoids comply with NOC offshore marine H2S specifications.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.mcdermott.com"
  },
  {
    "id": "QTR-2026-0184",
    "client": "QatarEnergy",
    "facility": "Ras Laffan LPG Storage Farm",
    "project": "Ras Laffan LPG Storage Tank 4 Cryogenic Safety Relief & Pressure Breather Package",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies Industrial Div",
    "product": "Flame Arrestors & Tank Vents",
    "brand": "Protectoseal",
    "value": 1420000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "10-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Submit Protectoseal ATEX cryogenic pressure/vacuum relief valve proposal to Technip Energies lead estimator",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0623\u0645\u0627\u0646 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u062a\u0646\u0641\u064a\u0633 \u063a\u0627\u0632\u0627\u062a \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0644\u062e\u0632\u0627\u0646\u0627\u062a \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0628\u062a\u0631\u0648\u0644\u064a \u0627\u0644\u0645\u0633\u0627\u0644 \u0641\u064a \u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Procurement of cryogenic pressure/vacuum relief valves and flame arrestor skids for LPG Tank 4 overhaul.",
    "factText": "QatarEnergy sanctioned LPG storage safety compliance upgrade.",
    "signalText": "Technip Energies issued formal inquiry for 316L stainless steel breather vents.",
    "inferenceText": "Protectoseal Series 8540 breather vents with low-temp seat seals meet Ras Laffan LPG tank criteria.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0187",
    "client": "QAPCO",
    "facility": "Mesaieed Petrochemical Complex",
    "project": "Ethylene Cracker 1 High-Pressure Quench Water Pump Impellers & Seals",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "QCON",
    "contractor": "QCON Rotating Equipment Team",
    "product": "Pump Spares & Rotating Parts",
    "brand": "Trillium Flow Technologies",
    "value": 950000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "15-Nov-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Deliver Trillium OEM replacement impellers and mechanical seal drawings to QCON Mesaieed workshop manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0623\u062c\u0632\u0627\u0621 \u0648\u0645\u0636\u062e\u0627\u062a \u062a\u062f\u0648\u064a\u0631 \u0645\u064a\u0627\u0647 \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0648\u062d\u062f\u0629 \u0627\u0644\u062a\u0643\u0633\u064a\u0631 \u0631\u0642\u0645 1 \u0641\u064a \u0645\u062c\u0645\u0639 \u0642\u0627\u0628\u0643\u0648 \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Supply of replacement impellers, shafts, and mechanical seals for quench water pumps at QAPCO Ethylene Cracker 1.",
    "factText": "QAPCO scheduled ethylene plant major turnaround for Q1 2027.",
    "signalText": "QCON rotating machinery team drafting spare parts vendor list.",
    "inferenceText": "Trillium OEM pump components match installed pump serial registry at QAPCO.",
    "sourceUrl": "https://www.qapco.com",
    "epcUrl": "https://www.qcon.com.qa"
  },
  {
    "id": "QTR-2026-0190",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (Train 5 Overhaul)",
    "project": "LNG Train 5 Fractionation Unit Heavy Hydrocarbon Drain Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "DOPET",
    "contractor": "DOPET Turnaround Division",
    "product": "Severe Service Valves",
    "brand": "ADAMS",
    "value": 1180000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "RFQ Received",
    "expectedRfq": "28-Sep-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Submit ADAMS metal-seated rotary valve catalog to DOPET turnaround package manager",
    "arabicText": "\u0627\u0633\u062a\u0628\u062f\u0627\u0644 \u0635\u0645\u0627\u0645\u0627\u062a \u062a\u0635\u0631\u064a\u0641 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u0643\u0631\u0628\u0648\u0646\u0627\u062a \u0627\u0644\u062b\u0642\u064a\u0644\u0629 \u0641\u064a \u062e\u0637 \u0645\u0639\u0627\u0644\u062c\u0629 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 5 \u0644\u0636\u0645\u0627\u0646 \u0645\u0648\u062b\u0648\u0642\u064a\u0629 \u0627\u0644\u0625\u063a\u0644\u0627\u0642.",
    "translatedText": "Replacement of severe service drain and isolation valves in LNG Train 5 fractionation unit.",
    "factText": "QatarEnergy LNG issued Train 5 turnaround isolation valve inquiry.",
    "signalText": "DOPET mechanical turnaround team requested quotation for 900# metal-seated isolation valves.",
    "inferenceText": "ADAMS triple-eccentric rotary valves provide zero-leakage tight shutoff under thermal cycling.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0193",
    "client": "WOQOD",
    "facility": "Ras Laffan Bitumen & Bulk Storage Terminal",
    "project": "WOQOD Bulk Fuel Terminal Emergency Shutdown Actuators & Positioners",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Medgulf",
    "contractor": "Medgulf E&I Team",
    "product": "Valve Monitoring & Positioners",
    "brand": "Westlock Controls / ASCO",
    "value": 1050000,
    "score": 92,
    "confidence": "High (94%)",
    "status": "Pre-RFQ",
    "expectedRfq": "20-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Westlock SIL-2 position monitors and ASCO RedHat solenoid pilots to Medgulf E&I division",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0645\u062d\u062f\u062f\u0627\u062a \u0645\u0648\u0627\u0636\u0639 \u0627\u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0648\u0645\u062d\u0631\u0643\u0627\u062a \u0627\u0644\u0625\u063a\u0644\u0627\u0642 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0644\u062e\u0632\u0627\u0646\u0627\u062a \u0648\u0642\u0648\u062f \u0648\u0642\u0648\u062f \u0627\u0644\u0645\u0631\u0643\u0632\u064a\u0629 \u0641\u064a \u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Modernization of ESD valve position monitors and flameproof solenoid pilots at WOQOD bulk terminal.",
    "factText": "WOQOD approved bulk fuel terminal safety automation upgrade.",
    "signalText": "Medgulf E&I team requested technical submittals for explosion-proof position switches.",
    "inferenceText": "Westlock AccuTrak digital position monitors and ASCO 316L solenoids fit WOQOD terminal specs.",
    "sourceUrl": "https://www.woqod.com",
    "epcUrl": "https://www.medgulfconstruction.com"
  },
  {
    "id": "QTR-2026-0196",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (Train 6 SRU)",
    "project": "LNG Train 6 Tail Gas Treatment Unit (TGTU) Sour Gas Control Valves & Actuators",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Saipem",
    "contractor": "Saipem Qatar EPC Div",
    "product": "Severe Service Control Valves & Desuperheaters",
    "brand": "Fisher / ADAMS",
    "value": 1350000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "12-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Present Fisher Cavitrol trim control valves and ADAMS metal-seated isolation valves to Saipem lead instrumentation engineer",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0641\u064a \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u062d\u0645\u0636\u064a \u0644\u0648\u062d\u062f\u0629 \u0645\u0639\u0627\u0644\u062c\u0629 \u0627\u0644\u0630\u064a\u0644 \u0627\u0644\u063a\u0627\u0632\u064a \u0641\u064a \u062e\u0637 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 6 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Supply of sour gas control valves and high-temperature isolation packages for LNG Train 6 TGTU overhaul.",
    "factText": "QatarEnergy LNG issued Tail Gas Treatment Unit environmental emissions compliance mandate.",
    "signalText": "Saipem requested tender quotations for Inconel-trimmed SIL-3 severe service control valves.",
    "inferenceText": "Fisher globe control valves with anti-cavitation trim prevent sour gas erosion in TGTU absorber loop.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.saipem.com"
  },
  {
    "id": "QTR-2026-0199",
    "client": "QAFAC",
    "facility": "Mesaieed Industrial City",
    "project": "QAFAC Methanol Reactor Catalyst Bed Multi-Point Temperature Transmitters & Thermowells",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Al Balagh",
    "contractor": "Al Balagh Engineering & Contracting",
    "product": "Pressure & Temp Gauges",
    "brand": "Baumer / Ashcroft",
    "value": 880000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "25-Nov-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Provide Baumer high-precision multi-point thermowell sensor datasheets to Al Balagh engineering manager",
    "arabicText": "\u0645\u0634\u0631\u0648\u0639 \u0627\u0633\u062a\u0628\u062f\u0627\u0644 \u0623\u062c\u0647\u0632\u0629 \u0642\u064a\u0627\u0633 \u062f\u0631\u062c\u0627\u062a \u0627\u0644\u062d\u0631\u0627\u0631\u0629 \u0648\u0645\u0633\u062a\u0634\u0639\u0631\u0627\u062a \u0627\u0644\u0645\u0641\u0627\u0639\u0644 \u0628\u0645\u0635\u0646\u0639 \u0627\u0644\u0645\u064a\u062b\u0627\u0646\u0648\u0644 \u0641\u064a \u0642\u0627\u0641\u0627\u0643 \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Upgrade of reactor bed multi-point thermowells and digital temperature transmitters at QAFAC Methanol plant.",
    "factText": "QAFAC scheduled 2027 methanol catalyst turnaround.",
    "signalText": "Al Balagh engineering team drafting instrument submittals for high-pressure reactor temperature monitoring.",
    "inferenceText": "Baumer heavy-duty thermowells and Ashcroft transmitters resist high-temperature methanol synthesis gas.",
    "sourceUrl": "https://www.qafac.com.qa",
    "epcUrl": "https://www.albalagh.com"
  },
  {
    "id": "QTR-2026-0202",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen FSO Africa Topside Offloading Hose ESD Valves & Quick Release Coupling",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "McDermott",
    "contractor": "McDermott Offshore Div",
    "product": "Process Valves",
    "brand": "Emerson / ASCO",
    "value": 1520000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "08-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Deliver Emerson API 6D fire-safe ball valves and ASCO offshore pilot solenoid package to McDermott team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0642\u0637\u0639 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0627\u0644\u0633\u0631\u064a\u0639 \u0648\u0623\u0635\u0644\u0627\u062a \u0627\u0644\u0641\u0635\u0644 \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0633\u0641\u064a\u0646\u0629 \u0627\u0644\u062a\u062e\u0632\u064a\u0646 \u0648\u0627\u0644\u062a\u0641\u0631\u063a \u0641\u064a \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a.",
    "translatedText": "Emergency shutdown valve package and quick release breakaway couplings for Al Shaheen FSO crude offloading arm.",
    "factText": "North Oil Company approved FSO topsides safety integrity upgrade package.",
    "signalText": "McDermott offshore procurement issued formal tender for marine-coated 1500# ESD ball valves.",
    "inferenceText": "Emerson API 6D full-bore ball valves with ASCO 316L solenoids meet severe marine offshore crash-stop criteria.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.mcdermott.com"
  },
  {
    "id": "QTR-2026-0205",
    "client": "Q-Chem",
    "facility": "Mesaieed Industrial City",
    "project": "Q-Chem RLOC Ethane Cracker Quench Heater Flame Arrestors & Detonation Breather Vents",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Blackcat",
    "contractor": "Blackcat Construction Div",
    "product": "Flame Arrestors & Tank Vents",
    "brand": "Protectoseal",
    "value": 1000000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "05-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Protectoseal in-line detonation arrestors and ATEX breathers to Blackcat estimating team",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0634\u0628\u0643\u0629 \u0645\u0627\u0646\u0639\u0627\u062a \u0627\u0644\u0644\u0647\u0628 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u062a\u0646\u0641\u064a\u0633 \u0633\u062e\u0627\u0646\u0627\u062a \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0628\u0645\u062c\u0645\u0639 \u0631\u0627\u0633 \u0644\u0641\u0627\u0646 \u0644\u0644\u0623\u0648\u0644\u064a\u0641\u064a\u0646\u0627\u062a (\u0643\u064a\u0648\u0643\u064a\u0645).",
    "translatedText": "Upgrade of in-line detonation flame arrestors and pressure/vacuum breather vents at RLOC ethane cracker quench heaters.",
    "factText": "Q-Chem RLOC issued plant safety upgrade mandate for volatile gas cracker heaters.",
    "signalText": "Blackcat estimating engineers preparing vendor list for ATEX certified detonation arrestors.",
    "inferenceText": "Protectoseal Series 4950 detonation arrestors deliver direct replacement for existing cracker heater vents.",
    "sourceUrl": "https://www.qchem.com.qa",
    "epcUrl": "https://www.blackcat.qa"
  },
  {
    "id": "QTR-2026-0208",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (Helium II Plant)",
    "project": "Helium II Purification Train Ultra-Low Temp Cryogenic Valves & Actuation",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Chiyoda Almana",
    "contractor": "Chiyoda Almana Cryogenic Div",
    "product": "Cryogenic Ball & Butterfly Valves",
    "brand": "ADAMS / Emerson",
    "value": 1480000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "05-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Submit ADAMS triple-eccentric helium-grade isolation valves and Emerson cryogenic control valve package to Chiyoda Almana",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u0648\u0645\u062d\u0627\u0628\u0633 \u063a\u0627\u0632 \u0627\u0644\u0647\u064a\u0644\u064a\u0648\u0645 \u0641\u0627\u0626\u0642 \u0627\u0644\u0628\u0631\u0648\u062f\u0629 \u0644\u0645\u0635\u0646\u0639 \u0627\u0644\u0647\u064a\u0644\u064a\u0648\u0645 \u0627\u0644\u062b\u0627\u0646\u064a \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Supply of ultra-low temperature helium-grade cryogenic isolation and control valves for Helium II plant expansion.",
    "factText": "QatarEnergy LNG authorized Helium II recovery loop debottlenecking.",
    "signalText": "Chiyoda Almana issued inquiry for SIL-3 helium leak-tight cryogenic isolation valves.",
    "inferenceText": "ADAMS metal-seated triple-offset valves pass liquid helium (-269\u00b0C) fugitive emission testing.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.chiyodaalmana.com.qa"
  },
  {
    "id": "QTR-2026-0211",
    "client": "QAFCO",
    "facility": "Mesaieed Industrial City",
    "project": "QAFCO-3 Urea Synthesis Reactor Carbamate Stripper Relief Discs & Safety Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "DOPET",
    "contractor": "DOPET Turnaround Division",
    "product": "Safety Relief Valves & Rupture Discs",
    "brand": "Continental Disc / Crosby",
    "value": 920000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "18-Nov-2026",
    "detectedAgo": "2 hours ago",
    "nextAction": "Present Continental Disc HPX rupture discs and Crosby overpressure valves to DOPET package manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0623\u0642\u0631\u0627\u0635 \u062a\u0645\u0632\u0642 \u0648\u0645\u062d\u0627\u0628\u0633 \u0623\u0645\u0627\u0646 \u0645\u0642\u0627\u0648\u0650\u0645\u0629 \u0644\u0644\u062a\u0622\u0643\u0644 \u0644\u0645\u0628\u062e\u0631 \u0627\u0644\u0643\u0627\u0631\u0628\u0627\u0645\u0627\u062a \u0641\u064a \u0645\u0635\u0646\u0639 \u0642\u0627\u0641\u0643\u0648 3 \u0628\u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Overpressure protection package for QAFCO-3 urea synthesis carbamate stripper loop.",
    "factText": "QAFCO safety committee issued overpressure disc replacement mandate.",
    "signalText": "DOPET mechanical turnaround team preparing vendor qualification package.",
    "inferenceText": "Continental Disc non-fragmenting discs protect Crosby safety relief valves from carbamate crystallization.",
    "sourceUrl": "https://www.qafco.qa",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0214",
    "client": "Qatar Shell Pearl GTL",
    "facility": "Ras Laffan Industrial City",
    "project": "Pearl GTL Air Separation Unit (ASU) High-Purity Oxygen Isolation Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies Gas Div",
    "product": "Severe Service Rotary Valves",
    "brand": "ADAMS",
    "value": 1250000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "15-Oct-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Deliver ADAMS oxygen-cleaned triple-offset valve datasheets to Technip Energies procurement team",
    "arabicText": "\u0627\u0633\u062a\u0628\u062f\u0627\u0644 \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u0627\u0644\u0623\u0643\u0633\u062c\u064a\u0646 \u0639\u0627\u0644\u064a \u0627\u0644\u0646\u0642\u0627\u0621 \u0644\u0648\u062d\u062f\u0629 \u0641\u0635\u0644 \u0627\u0644\u0647\u0648\u0627\u0621 \u0641\u064a \u0645\u062c\u0645\u0639 \u0627\u0644\u0644\u0624\u0644\u0624\u0629 \u0644\u062a\u062d\u0648\u064a\u0644 \u0627\u0644\u063a\u0627\u0632 \u0644\u0633\u0648\u0627\u0626\u0644.",
    "translatedText": "Replacement of severe service oxygen-cleaned isolation valves for Pearl GTL Air Separation Unit (ASU).",
    "factText": "Qatar Shell Pearl GTL initiated ASU oxygen line reliability overhaul.",
    "signalText": "Technip Energies issued tender inquiry for BAM-certified oxygen service metal-seated valves.",
    "inferenceText": "ADAMS metal-seated rotary valves with MONEL trim prevent ignition risks in high-pressure oxygen streams.",
    "sourceUrl": "https://www.shell.com.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0217",
    "client": "QatarEnergy",
    "facility": "Dukhan Field (Jaleha Station)",
    "project": "Dukhan Jaleha Dehydration Plant Gas Desiccant Switching Valve Skid",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "TRAGS",
    "contractor": "TRAGS Electrical & Engineering",
    "product": "Solenoid Valves & Actuation",
    "brand": "Emerson ASCO / Westlock",
    "value": 1100000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "01-Dec-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Submit ASCO 3-way/4-way stainless steel solenoid pilots and Westlock position monitors to TRAGS engineering team",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0645\u062d\u0627\u0628\u0633 \u062a\u062c\u0641\u064a\u0641 \u0627\u0644\u063a\u0627\u0632 \u0648\u0627\u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0643\u0647\u0631\u0648\u0645\u063a\u0646\u0627\u0637\u064a\u0633\u064a\u0629 \u0644\u0645\u062d\u0637\u0629 \u0627\u0644\u062c\u0644\u064a\u062d\u0629 \u0628\u062d\u0642\u0644 \u062f\u062e\u0627\u0646.",
    "translatedText": "Revamp of desiccant switching valves and explosion-proof solenoid manifolds at Dukhan Jaleha dehydration plant.",
    "factText": "QatarEnergy onshore division approved Jaleha gas dehydration modernization.",
    "signalText": "TRAGS engineering drafting vendor list for fast-cycling 600# switching valves and SIL-3 positioners.",
    "inferenceText": "ASCO RedHat solenoids and Westlock AccuTrak monitors withstand continuous high-cycle switching service.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.tragsqatar.com"
  },
  {
    "id": "QTR-2026-0220",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (Train 1 Rehabilitation)",
    "project": "LNG Train 1 Boil-Off Gas (BOG) Compressor Inlet & Outlet Cryogenic Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies LNG Division",
    "product": "Cryogenic Ball & Butterfly Valves",
    "brand": "ADAMS / Emerson",
    "value": 1620000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "10-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Present ADAMS cryogenic metal-seated triple-offset valves and Emerson 900# cryogenic isolation valves to Technip Energies lead package manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0628\u0631\u0651\u062f \u0644\u0645\u062f\u062e\u0644 \u0648\u0645\u062e\u0631\u062c \u0636\u0648\u0627\u063a\u0637 \u0627\u0644\u0628\u062e\u0627\u0631 \u0641\u064a \u0642\u0637\u0627\u0631 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 1 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Supply of high-pressure cryogenic isolation valves for BOG compressor inlet and discharge lines at LNG Train 1.",
    "factText": "QatarEnergy LNG issued Train 1 compression loop reliability enhancement mandate.",
    "signalText": "Technip Energies issued formal tender for 900# low-temperature cryogenic metal-seated isolation valves.",
    "inferenceText": "ADAMS triple-eccentric metal-seated valves fit severe -162\u00b0C boil-off gas suction/discharge duty.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0223",
    "client": "Q-Chem",
    "facility": "Mesaieed Industrial City",
    "project": "Q-Chem Polyethylene Plant 2 Extruder Melt Pump Overpressure Discs & Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Medgulf",
    "contractor": "Medgulf Mechanical Division",
    "product": "Safety Relief Valves & Rupture Discs",
    "brand": "Continental Disc / Crosby",
    "value": 980000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "20-Nov-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Deliver Continental Disc high-pressure melt rupture disc specifications to Medgulf estimating manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0623\u0642\u0631\u0627\u0635 \u062a\u0645\u0632\u0642 \u0639\u0627\u0644\u064a \u0627\u0644\u0636\u063a\u0637 \u0648\u0645\u062d\u0627\u0628\u0633 \u0623\u0645\u0627\u0646 \u0644\u0645\u0636\u062e\u0629 \u0627\u0644\u0645\u0630\u0627\u0628 \u0628\u0645\u0635\u0646\u0639 \u0643\u064a\u0648\u0643\u064a\u0645 \u0644\u0644\u0628\u0648\u0644\u064a \u0625\u064a\u062b\u064a\u0644\u064a\u0646 2 \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "High-pressure rupture disc assemblies and overpressure safety relief valves for Q-Chem Polyethylene 2 melt pump.",
    "factText": "Q-Chem scheduled extruder pelletizer overhaul for early 2027.",
    "signalText": "Medgulf mechanical team requested quotations for 3000 PSI high-temperature rupture disc packages.",
    "inferenceText": "Continental Disc HPX rupture discs withstand 320\u00b0C molten polymer backpressure without fragmenting.",
    "sourceUrl": "https://www.qchem.com.qa",
    "epcUrl": "https://www.medgulfconstruction.com"
  },
  {
    "id": "QTR-2026-0226",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Platform Ruya Batch 2 Wellhead Sour Water Dump Control Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Saipem",
    "contractor": "Saipem Offshore Projects",
    "product": "Severe Service Control Valves & Desuperheaters",
    "brand": "Fisher / Masoneilan",
    "value": 1450000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "14-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Submit Fisher Cavitrol anti-cavitation control valve technical offer to Saipem offshore procurement team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0641\u064a \u0627\u0644\u0645\u064a\u0627\u062f \u0627\u0644\u062d\u0645\u0636\u064a\u0629 \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u0636\u063a\u0637 \u0644\u0645\u0646\u0635\u0627\u062a \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a \u0636\u0645\u0646 \u0645\u0631\u062d\u0644\u0629 \u0631\u0648\u064a\u0627 \u0627\u0644\u062b\u0627\u0646\u064a\u0629.",
    "translatedText": "High-pressure sour water dump control valves and anti-cavitation trim packages for NOC Ruya Batch 2 topsides.",
    "factText": "North Oil Company sanctioned Ruya Batch 2 wellhead separator expansion.",
    "signalText": "Saipem offshore engineering issued ITT for Inconel 718 cladded severe-service globe control valves.",
    "inferenceText": "Fisher globe control valves with anti-cavitation trim resist flashing sour produced water at 2500# rating.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.saipem.com"
  },
  {
    "id": "QTR-2026-0229",
    "client": "QatarEnergy",
    "facility": "Mesaieed NGL Complex (NGL-3 Plant)",
    "project": "NGL-3 Propane/Butane Fractionation Column ESD Valve Positioners & Solenoids",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Blackcat",
    "contractor": "Blackcat Construction & E&I",
    "product": "Valve Monitoring & Positioners",
    "brand": "Westlock Controls / ASCO",
    "value": 1200000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "08-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Westlock SIL-3 AccuTrak digital position transmitters and ASCO 316L solenoid pilots to Blackcat E&I team",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0645\u062d\u062f\u062f\u0627\u062a \u0645\u0648\u0627\u0636\u0639 \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0625\u063a\u0644\u0627\u0642 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0644\u0623\u0628\u0631\u0627\u062c \u062a\u0642\u0637\u064a\u0631 \u0627\u0644\u0628\u0631\u0648\u0628\u0627\u0646 \u0641\u064a \u0645\u062c\u0645\u0639 \u063a\u0627\u0632 \u0627\u0644\u0633\u0627\u0626\u0644 \u0631\u0642\u0645 3 \u0628\u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Digital position monitor and explosion-proof solenoid pilot upgrade for ESD valves at Mesaieed NGL-3 fractionation plant.",
    "factText": "QatarEnergy NGL division authorized safety interlock modernization across NGL-3 columns.",
    "signalText": "Blackcat E&I team drafting vendor list for flameproof position transmitters and dual-redundant solenoid pilots.",
    "inferenceText": "Westlock 2600 AccuTrak positioners and ASCO RedHat solenoids comply with QatarEnergy NGL-3 specifications.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.blackcat.qa"
  },
  {
    "id": "QTR-2026-0232",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (Train 2 Overhaul)",
    "project": "LNG Train 2 Acid Gas Absorber Column Severe Service Isolation Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "QCON",
    "contractor": "QCON Turnaround Mechanical Div",
    "product": "Severe Service Valves",
    "brand": "ADAMS",
    "value": 1550000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "18-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Submit ADAMS triple-eccentric metal-seated rotary valve bid package to QCON turnaround package manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u062d\u0645\u0636\u064a \u0627\u0644\u0645\u0642\u0627\u0648\u0645\u0629 \u0644\u0644\u062a\u0622\u0643\u0644 \u0644\u0639\u0645\u0648\u062f \u0627\u0645\u062a\u0635\u0627\u0635 \u0627\u0644\u063a\u0627\u0632 \u0641\u064a \u0642\u0637\u0627\u0631 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 2 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Replacement of severe-service acid gas absorber column isolation valves for LNG Train 2 scheduled turnaround.",
    "factText": "QatarEnergy LNG issued Train 2 AGRU maintenance turnaround schedule.",
    "signalText": "QCON turnaround team issued tender inquiry for 900# Inconel-seated rotary isolation valves.",
    "inferenceText": "ADAMS metal-seated triple-offset valves handle corrosive H2S/CO2 wet amine service without seat erosion.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.qcon.com.qa"
  },
  {
    "id": "QTR-2026-0235",
    "client": "QAFCO",
    "facility": "Mesaieed Industrial City",
    "project": "QAFCO-4 Melamine Plant High-Pressure Urea Melt Filter Elements & Relief Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "DOPET",
    "contractor": "DOPET Turnaround & Projects Div",
    "product": "Safety Relief Valves & Rupture Discs",
    "brand": "Crosby / Continental Disc",
    "value": 1020000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "05-Dec-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Deliver Crosby overpressure safety relief valve specifications to DOPET melamine package manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0639\u0646\u0627\u0635\u0631 \u0627\u0644\u0641\u0644\u062a\u0631\u0629 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0623\u0645\u0627\u0646 \u0644\u0645\u0635\u0646\u0639 \u0627\u0644\u0645\u064a\u0644\u0627\u0645\u064a\u0646 \u0628\u0642\u0627\u0641\u0643\u0648 4 \u0641\u064a \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "High-pressure melt filter elements and overpressure safety relief valves for QAFCO-4 Melamine synthesis loop.",
    "factText": "QAFCO sanctioned QAFCO-4 Melamine debottlenecking.",
    "signalText": "DOPET mechanical team drafting vendor qualification list for 2500 PSI high-temperature safety relief valves.",
    "inferenceText": "Crosby JOS-E safety relief valves with Inconel bellows protect high-temp melamine liquid synthesis.",
    "sourceUrl": "https://www.qafco.qa",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0238",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Offshore Complex Gallaf Batch 3 Topside Hydraulic ESD Valve Manifolds",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "McDermott",
    "contractor": "McDermott Offshore Subsea Div",
    "product": "Solenoid Valves & Actuation",
    "brand": "Emerson ASCO / Westlock",
    "value": 1380000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "22-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Submit ASCO 316L explosion-proof pilot solenoid proposal to McDermott offshore project management team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0645\u062c\u0645\u0639\u0627\u062a \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u0644\u064a\u0643\u064a \u0648\u0627\u0644\u0625\u063a\u0644\u0627\u0642 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0644\u0645\u0646\u0635\u0627\u062a \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a.",
    "translatedText": "Offshore-grade hydraulic emergency shutdown (ESD) valve manifolds and pilot solenoids for NOC Gallaf Batch 3 topsides.",
    "factText": "North Oil Company approved offshore platform topside expansion notice.",
    "signalText": "McDermott offshore engineering issued ITT for 316L SIL-3 solenoid pilot manifolds.",
    "inferenceText": "ASCO 3-way stainless steel solenoids meet NOC severe offshore marine H2S specifications.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.mcdermott.com"
  },
  {
    "id": "QTR-2026-0241",
    "client": "QatarEnergy",
    "facility": "Dukhan Oil Field (Fahahil Plant)",
    "project": "Dukhan Fahahil Gas Injection Plant High-Pressure Sour Gas Metering Skids",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Blackcat",
    "contractor": "Blackcat Upstream & E&I Div",
    "product": "Custody Transfer Flow & Metering Systems",
    "brand": "Daniel Measurement / Emerson",
    "value": 1100000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "15-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Daniel Senior ultrasonic gas flowmeter technical submittal to Blackcat Dukhan E&I lead",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0623\u0646\u0638\u0645\u0629 \u0642\u064a\u0627\u0633 \u062a\u062f\u0641\u0642 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u062d\u0645\u0636\u064a \u0639\u0627\u0644\u064a \u0627\u0644\u0636\u063a\u0637 \u0644\u0645\u0646\u0634\u0623\u0629 \u062d\u0642\u0646 \u0627\u0644\u063a\u0627\u0632 \u0641\u064a \u062f\u062e\u0627\u0646 \u0627\u0644\u0641\u062d\u064a\u062d\u064a\u0644.",
    "translatedText": "High-pressure ultrasonic sour gas flow metering skid upgrade for Dukhan Fahahil gas injection compressor station.",
    "factText": "QatarEnergy onshore production division authorized Dukhan reservoir gas injection upgrade.",
    "signalText": "Blackcat E&I team requested specifications for SIL-2 rated ultrasonic gas flow meters.",
    "inferenceText": "Daniel Senior ultrasonic meters provide non-intrusive high-accuracy gas measurement without pressure drop.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.blackcat.qa"
  },
  {
    "id": "QTR-2026-0244",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (Train 4 Overhaul)",
    "project": "LNG Train 4 Heavy Refrigerant Loop Isolation & Anti-Surge Control Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies LNG Division",
    "product": "Cryogenic Ball & Butterfly Valves",
    "brand": "ADAMS / Fisher",
    "value": 1680000,
    "score": 96,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "15-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Present ADAMS 1200# cryogenic metal-seated butterfly valves and Fisher anti-surge control valves to Technip Energies lead package manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u063a\u0627\u0632 \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0627\u0644\u062b\u0642\u064a\u0644 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u0645\u0646\u0639 \u0627\u0644\u0627\u0646\u062f\u0641\u0627\u0639 \u0644\u0642\u0637\u0627\u0631 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 4 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "Supply of high-pressure cryogenic isolation valves and anti-surge control packages for LNG Train 4 mixed refrigerant loop.",
    "factText": "QatarEnergy LNG issued Train 4 scheduled turnaround procurement notice.",
    "signalText": "Technip Energies requested tender submittals for 1200# low-temperature cryogenic metal-seated valves.",
    "inferenceText": "ADAMS triple-eccentric metal-seated valves handle severe cryogenic (-162\u00b0C) mixed refrigerant loop isolation.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0247",
    "client": "QAPCO",
    "facility": "Mesaieed Petrochemical Complex",
    "project": "Low-Density Polyethylene Autoclave Reactor Overpressure Safety Relief Valves",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "QCON",
    "contractor": "QCON Petrochem Division",
    "product": "Safety Relief Valves & Rupture Discs",
    "brand": "Crosby / Continental Disc",
    "value": 1050000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "01-Dec-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Deliver Crosby 3000 PSI high-pressure safety relief valve specifications to QCON package manager",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0623\u0645\u0627\u0646 \u0627\u0644\u0636\u063a\u0637 \u0627\u0644\u0641\u0627\u0626\u0642 \u0644\u0645\u0641\u0627\u0639\u0644 \u0627\u0644\u0628\u0648\u0644\u064a \u0625\u064a\u062b\u064a\u0644\u064a\u0646 \u0645\u0646\u062e\u0641\u0636 \u0627\u0644\u0643\u062b\u0627\u0641\u0629 \u0641\u064a \u0645\u062c\u0645\u0639 \u0642\u0627\u0628\u0643\u0648 \u0628\u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Super high-pressure safety relief valves and rupture disc assemblies for QAPCO LDPE autoclave reactor loop.",
    "factText": "QAPCO safety committee mandated replacement of reactor primary safety relief valves.",
    "signalText": "QCON estimating division drafting vendor qualification list for 3000# hyper-pressure safety valves.",
    "inferenceText": "Crosby JOS-E safety relief valves with Inconel bellows protect high-pressure ethylene polymerization reactors.",
    "sourceUrl": "https://www.qapco.com",
    "epcUrl": "https://www.qcon.com.qa"
  },
  {
    "id": "QTR-2026-0250",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Platform Gallaf Phase 3 Topsides Sour Gas Injection ESD Skids",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Saipem",
    "contractor": "Saipem Offshore Division",
    "product": "Solenoid Valves & Actuation",
    "brand": "Emerson ASCO / Westlock",
    "value": 1420000,
    "score": 95,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "20-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Submit ASCO 316L explosion-proof pilot solenoid proposal to Saipem offshore engineering team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0625\u063a\u0644\u0627\u0642 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0644\u0645\u0646\u0638\u0648\u0645\u0629 \u062d\u0642\u0646 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u062d\u0645\u0636\u064a \u0628\u0645\u0634\u0631\u0648\u0639 \u062c\u0644\u0627\u0641 3 \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a.",
    "translatedText": "High-pressure sour gas injection ESD valve skids and pilot solenoid manifolds for NOC Gallaf Phase 3 offshore topsides.",
    "factText": "North Oil Company approved Gallaf Phase 3 gas injection topsides fabrication package.",
    "signalText": "Saipem offshore procurement issued ITT for 316L SIL-3 pilot solenoid manifolds.",
    "inferenceText": "ASCO 3-way stainless steel solenoids meet NOC severe offshore marine H2S specifications.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.saipem.com"
  },
  {
    "id": "QTR-2026-0253",
    "client": "Qatar Shell Pearl GTL",
    "facility": "Ras Laffan Industrial City",
    "project": "Pearl GTL Heavy Paraffin Hydrocracker Hydrogen Recirculation Valves & Positioners",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Chiyoda Almana",
    "contractor": "Chiyoda Almana Hydrocarbon Div",
    "product": "Valve Monitoring & Positioners",
    "brand": "Westlock Controls / Ashcroft",
    "value": 1100000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "10-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Westlock SIL-3 AccuTrak digital position transmitters and Ashcroft solid-front gauges to Chiyoda Almana",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0645\u062d\u062f\u062f\u0627\u062a \u0645\u0648\u0627\u0636\u0639 \u0627\u0644\u0635\u0645\u0627\u0645\u0627\u062a \u0644\u0645\u0636\u062e\u0627\u062a \u062a\u062f\u0648\u064a\u0631 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u062c\u064a\u0646 \u0628\u0648\u062d\u062f\u0629 \u0627\u0644\u062a\u0643\u0633\u064a\u0631 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u062c\u064a\u0646\u064a \u0641\u064a \u0645\u062c\u0645\u0639 \u0627\u0644\u0644\u0624\u0644\u0624\u0629.",
    "translatedText": "Digital position monitor and solid-front pressure gauge upgrade for hydrogen recirculation loop at Shell Pearl GTL hydrocracker.",
    "factText": "Qatar Shell Pearl GTL authorized hydroprocessing unit debottlenecking.",
    "signalText": "Chiyoda Almana engineering team preparing vendor list for flameproof digital position transmitters.",
    "inferenceText": "Westlock 2600 AccuTrak positioners and Ashcroft Duragauges withstand high-pressure hydrogen service.",
    "sourceUrl": "https://www.shell.com.qa",
    "epcUrl": "https://www.chiyodaalmana.com.qa"
  },
  {
    "id": "QTR-2026-0256",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (North Field East - NFE Train 1)",
    "project": "NFE Train 1 Heavy Hydrocarbon Fractionation Column High-Pressure Control Valves",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies LNG Division",
    "product": "Severe Service Control Valves & Desuperheaters",
    "brand": "Fisher / ADAMS",
    "value": 1750000,
    "score": 97,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "18-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Submit Fisher severe-service globe control valve technical proposal to Technip Energies NFE package lead",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0639\u0627\u0644\u064a\u0629 \u0627\u0644\u0636\u063a\u0637 \u0644\u0639\u0645\u0648\u062f \u0627\u0644\u062a\u0642\u0637\u064a\u0631 \u0628\u0645\u0634\u0631\u0648\u0639 \u062a\u0648\u0633\u0639\u0629 \u062d\u0642\u0644 \u0627\u0644\u0634\u0645\u0627\u0644 \u0627\u0644\u0634\u0631\u0642\u064a \u0631\u0642\u0645 1 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "High-pressure hydrocarbon fractionation control valves and severe-service trim packages for NFE Train 1.",
    "factText": "QatarEnergy LNG issued North Field East Train 1 commissioning readiness milestone notice.",
    "signalText": "Technip Energies issued tender inquiry for 900# anti-cavitation control valves for NFE fractionation loop.",
    "inferenceText": "Fisher globe control valves with Cavitrol anti-cavitation trim prevent erosive flashing in high-pressure NGL fractionation service.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0259",
    "client": "QAFCO",
    "facility": "Mesaieed Industrial City",
    "project": "QAFCO-6 Urea Plant Granulation Tower Scrubbing Pump Spares & Relief Discs",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "DOPET",
    "contractor": "DOPET Turnaround Mechanical Div",
    "product": "Pump Spares & Rotating Parts",
    "brand": "Trillium Flow Technologies / Continental Disc",
    "value": 980000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "05-Dec-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Deliver Trillium OEM slurry pump impellers and Continental Disc non-fragmenting rupture disc datasheets to DOPET",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0623\u062c\u0632\u0627\u0621 \u0648\u0645\u0636\u062e\u0627\u062a \u063a\u0633\u064a\u0644 \u063a\u0628\u0627\u0631 \u0627\u0644\u064a\u0648\u0631\u064a\u0627 \u0648\u0623\u0642\u0631\u0627\u0635 \u062a\u0645\u0632\u0642 \u0644\u0628\u0631\u062c \u0627\u0644\u062a\u062d\u0628\u064a\u0628 \u0641\u064a \u0645\u0635\u0646\u0639 \u0642\u0627\u0641\u0643\u0648 6 \u0628\u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Slurry pump impellers, mechanical seals, and overpressure rupture disc assemblies for QAFCO-6 Urea granulation tower.",
    "factText": "QAFCO scheduled QAFCO-6 granulation tower turnaround for early 2027.",
    "signalText": "DOPET turnaround team drafting vendor qualification list for urea slurry rotating equipment rebuild kits.",
    "inferenceText": "Trillium OEM wear-resistant impellers and Continental Disc HPX discs withstand corrosive carbamate slurry crystallization.",
    "sourceUrl": "https://www.qafco.qa",
    "epcUrl": "https://www.dopet.com"
  },
  {
    "id": "QTR-2026-0262",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Platform Gallaf 3 Topside Subsea ESD Solenoid Pilot Manifolds",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "McDermott",
    "contractor": "McDermott Offshore Subsea Div",
    "product": "Solenoid Valves & Actuation",
    "brand": "Emerson ASCO / Westlock",
    "value": 1480000,
    "score": 96,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "25-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Deliver ASCO 316L stainless steel explosion-proof pilot solenoids and Westlock SIL-3 positioners to McDermott team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0645\u062c\u0645\u0639\u0627\u062a \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u062a\u062d\u0643\u0645 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u0643\u0647\u0631\u0648\u0645\u063a\u0646\u0627\u0637\u064a\u0633\u064a\u0629 \u0644\u0645\u0646\u0635\u0627\u062a \u062d\u0642\u0644 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a.",
    "translatedText": "Offshore-grade hydraulic ESD valve manifolds and dual-redundant pilot solenoids for NOC Gallaf 3 topsides.",
    "factText": "North Oil Company approved Gallaf 3 offshore topsides fabrication milestone.",
    "signalText": "McDermott offshore procurement issued ITT for 316L SIL-3 pilot solenoid manifolds.",
    "inferenceText": "ASCO 3-way stainless steel solenoids meet NOC severe offshore marine H2S specifications.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.mcdermott.com"
  },
  {
    "id": "QTR-2026-0265",
    "client": "Q-Chem",
    "facility": "Mesaieed Industrial City",
    "project": "Q-Chem 1-Hexene Plant Reactor Vapor Recovery Tank Vents & Detonation Arrestors",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Medgulf",
    "contractor": "Medgulf E&I & Mechanical Div",
    "product": "Flame Arrestors & Tank Vents",
    "brand": "Protectoseal",
    "value": 1040000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "12-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Protectoseal Series 4950 in-line detonation flame arrestors and ATEX pressure relief vents to Medgulf",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0634\u0628\u0643\u0629 \u0645\u0627\u0646\u0639\u0627\u062a \u0627\u0644\u0644\u0647\u0628 \u0648\u0635\u0645\u0627\u0645\u0627\u062a \u062a\u0646\u0641\u064a\u0633 \u062e\u0632\u0627\u0646\u0627\u062a \u0627\u0633\u062a\u0639\u0627\u062f\u0629 \u0627\u0644\u0628\u062e\u0627\u0631 \u0628\u0645\u0635\u0646\u0639 \u0627\u0644\u0647\u0643\u0633\u064a\u0646-1 \u0641\u064a \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Upgrade of in-line detonation flame arrestors and pressure/vacuum breather vents at Q-Chem 1-Hexene vapor recovery tanks.",
    "factText": "Q-Chem issued safety upgrade mandate for volatile hydrocarbon vapor recovery storage tanks.",
    "signalText": "Medgulf estimating engineers requested vendor submittals for ATEX Zone 0 certified detonation arrestors.",
    "inferenceText": "Protectoseal Series 4950 detonation arrestors deliver direct replacement for existing hexene vapor tank vents.",
    "sourceUrl": "https://www.qchem.com.qa",
    "epcUrl": "https://www.medgulfconstruction.com"
  },
  {
    "id": "QTR-2026-0268",
    "client": "QatarEnergy LNG",
    "facility": "Ras Laffan (LNG Mega-Train 4)",
    "project": "LNG Train 4 Mixed Refrigerant Compressor Suction Cryogenic Valve Package",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Technip Energies",
    "contractor": "Technip Energies LNG Division",
    "product": "Cryogenic Ball & Butterfly Valves",
    "brand": "ADAMS / Emerson",
    "value": 1820000,
    "score": 97,
    "confidence": "High (98%)",
    "status": "RFQ Received",
    "expectedRfq": "12-Oct-2026",
    "detectedAgo": "1 hour ago",
    "nextAction": "Present ADAMS 1200# metal-seated cryogenic butterfly valves to Technip Energies turnaround lead",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0639\u0632\u0644 \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0627\u0644\u0639\u0645\u064a\u0642 \u0644\u0636\u0648\u0627\u063a\u0637 \u063a\u0627\u0632 \u0627\u0644\u062a\u0628\u0631\u064a\u062f \u0641\u064a \u0642\u0637\u0627\u0631 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u0645\u0633\u0627\u0644 \u0631\u0642\u0645 4 \u0628\u0631\u0627\u0633 \u0644\u0641\u0627\u0646.",
    "translatedText": "High-pressure cryogenic isolation valves for Train 4 mixed refrigerant compressor overhaul.",
    "factText": "QatarEnergy LNG scheduled Train 4 turnaround for November 2026.",
    "signalText": "Technip Energies issued tender inquiry for 1200# -162\u00b0C cryogenic metal-seated isolation valves.",
    "inferenceText": "ADAMS triple-eccentric rotary valves provide zero-leakage shutoff for severe LNG cold box isolation.",
    "sourceUrl": "https://www.qatarenergylng.qa",
    "epcUrl": "https://www.technipenergies.com"
  },
  {
    "id": "QTR-2026-0271",
    "client": "QAFAC",
    "facility": "Mesaieed Industrial City",
    "project": "QAFAC Methanol Plant Synthesis Reactor Refractory & Overpressure Relief Discs",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Al Balagh",
    "contractor": "Al Balagh Petrochemical Div",
    "product": "Safety Relief Valves & Rupture Discs",
    "brand": "Continental Disc / Crosby",
    "value": 1080000,
    "score": 94,
    "confidence": "High (96%)",
    "status": "Pre-RFQ",
    "expectedRfq": "01-Dec-2026",
    "detectedAgo": "3 hours ago",
    "nextAction": "Submit Continental Disc HPX rupture disc and Crosby relief valve technical proposal to Al Balagh",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0623\u062c\u0647\u0632\u0629 \u062d\u0645\u0627\u064a\u0629 \u0627\u0644\u0636\u063a\u0637 \u0627\u0644\u0632\u0627\u0626\u062f \u0648\u0623\u0642\u0631\u0627\u0635 \u0627\u0644\u062a\u0645\u0632\u0642 \u0644\u0645\u0641\u0627\u0639\u0644 \u0627\u0644\u0645\u064a\u062b\u0627\u0646\u0648\u0644 \u0641\u064a \u0642\u0627\u0641\u0627\u0643 \u0645\u0633\u064a\u0639\u064a\u062f.",
    "translatedText": "Overpressure protection disc assemblies and safety relief valves for QAFAC Methanol reactor turnaround.",
    "factText": "QAFAC confirmed methanol catalyst bed replacement schedule for Q1 2027.",
    "signalText": "Al Balagh engineering team requesting supplier submittals for high-temperature syngas rupture discs.",
    "inferenceText": "Continental Disc non-fragmenting discs protect Crosby safety valves from high-temp syngas fouling.",
    "sourceUrl": "https://www.qafac.com.qa",
    "epcUrl": "https://www.albalagh.com"
  },
  {
    "id": "QTR-2026-0274",
    "client": "North Oil Company",
    "facility": "Al Shaheen Offshore Field",
    "project": "Al Shaheen Platform Gallaf Phase 3 Sour Gas Compression Pilot Solenoid Skids",
    "stage": "Level 4 (Live ITT / Tender)",
    "stageBadge": "Live ITT",
    "epc": "Saipem",
    "contractor": "Saipem Offshore Division",
    "product": "Solenoid Valves & Actuation",
    "brand": "Emerson ASCO / Westlock",
    "value": 1400000,
    "score": 96,
    "confidence": "High (97%)",
    "status": "RFQ Received",
    "expectedRfq": "22-Oct-2026",
    "detectedAgo": "4 hours ago",
    "nextAction": "Deliver ASCO 316L explosion-proof SIL-3 pilot solenoids and Westlock digital monitors to Saipem offshore team",
    "arabicText": "\u062a\u0648\u0631\u064a\u062f \u0635\u0645\u0627\u0645\u0627\u062a \u0627\u0644\u0625\u063a\u0644\u0627\u0642 \u0627\u0644\u0627\u0636\u0637\u0631\u0627\u0631\u064a \u0644\u0645\u0646\u0638\u0648\u0645\u0629 \u0636\u0648\u0627\u063a\u0637 \u0627\u0644\u063a\u0627\u0632 \u0627\u0644\u062d\u0645\u0636\u064a \u0628\u0645\u0635\u0646\u0639 \u0627\u0644\u0634\u0627\u0647\u064a\u0646 \u0627\u0644\u0628\u062d\u0631\u064a.",
    "translatedText": "Sour gas compression ESD pilot solenoid skids and digital position transmitters for NOC Gallaf Phase 3.",
    "factText": "North Oil Company sanctioned Gallaf Phase 3 compressor topsides commissioning.",
    "signalText": "Saipem offshore procurement issued ITT for Inconel-trimmed SIL-3 solenoid pilot manifolds.",
    "inferenceText": "ASCO 3-way stainless steel solenoids meet NOC severe offshore marine H2S specifications.",
    "sourceUrl": "https://www.noc.qa",
    "epcUrl": "https://www.saipem.com"
  },
  {
    "id": "QTR-2026-0277",
    "client": "QatarEnergy",
    "facility": "Dukhan Field (Fahahil Plant)",
    "project": "Dukhan Fahahil Crude Separation Unit High-Pressure Process Gauges & Transmitters",
    "stage": "Level 3 (Procurement Approaching)",
    "stageBadge": "Procurement Approaching",
    "epc": "Blackcat",
    "contractor": "Blackcat E&I Division",
    "product": "Pressure & Temp Gauges",
    "brand": "Ashcroft / Bourdon",
    "value": 1150000,
    "score": 93,
    "confidence": "High (95%)",
    "status": "Pre-RFQ",
    "expectedRfq": "15-Dec-2026",
    "detectedAgo": "5 hours ago",
    "nextAction": "Present Ashcroft Duragauge solid-front process gauges and Bourdon transmitters to Blackcat E&I team",
    "arabicText": "\u062a\u062d\u062f\u064a\u062b \u0623\u062c\u0647\u0632\u0629 \u0642\u064a\u0627\u0633 \u0627\u0644\u0636\u063a\u0637 \u0648\u0627\u0644\u062d\u0631\u0627\u0631\u0629 \u0644\u0645\u062d\u0637\u0629 \u0639\u0632\u0644 \u0627\u0644\u0646\u0641\u0637 \u0648\u0627\u0644\u063a\u0627\u0632 \u0641\u064a \u062f\u062e\u0627\u0646 \u0627\u0644\u0641\u062d\u064a\u062d\u064a\u0644.",
    "translatedText": "High-pressure process gauges and liquid-filled vibration-resistant pressure transmitters for Dukhan Fahahil CSU.",
    "factText": "QatarEnergy onshore division authorized Dukhan crude separation unit instrumentation upgrade.",
    "signalText": "Blackcat E&I engineers drafting vendor list for SIL-2 solid-front process gauges.",
    "inferenceText": "Ashcroft 1279 Duragauges with PLUS! performance dampeners resist extreme field vibration.",
    "sourceUrl": "https://www.qatarenergy.qa",
    "epcUrl": "https://www.blackcat.qa"
  }
]
```

---

## 11. Step-by-Step Implementation Guide on Lovable

1. **Step 1: Create a New Project on Lovable.dev**
   - Choose **Vite + React + Tailwind CSS + TypeScript**.
2. **Step 2: Install Supporting Dependencies**
   - `lucide-react` for icons.
   - `recharts` for pipeline analytics.
   - `canvas-confetti` (optional, for deal celebrations).
3. **Step 3: Setup Project Directory Structure**
   ```text
   src/
   ├── components/
   │   ├── layout/
   │   │   ├── Header.tsx
   │   │   ├── Navigation.tsx
   │   │   ├── MobileNav.tsx
   │   │   └── PasskeyModal.tsx
   │   ├── dashboard/
   │   │   ├── KpiCards.tsx
   │   │   ├── HotLeadsWidget.tsx
   │   │   ├── ShutdownBanner.tsx
   │   │   └── SignalsFeed.tsx
   │   ├── modules/
   │   │   ├── CommandCenter.tsx
   │   │   ├── ProjectRadar.tsx
   │   │   ├── ShutdownRadar.tsx
   │   │   ├── CrmTable.tsx
   │   │   ├── EpcDirectory.tsx
   │   │   ├── SourceMonitor.tsx
   │   │   ├── CustomerMatrix.tsx
   │   │   ├── ProductPortfolio.tsx
   │   │   ├── PetroconAshfan.tsx
   │   │   ├── OutreachGenerator.tsx
   │   │   └── ZoneMap.tsx
   │   └── modals/
   │       ├── AddLeadModal.tsx
   │       ├── DataAuditModal.tsx
   │       ├── WhyLeadModal.tsx
   │       └── ArabicDrawer.tsx
   ├── data/
   │   └── initialData.ts  <-- Copy all JSON arrays from Section 10 here
   ├── types/
   │   └── index.ts        <-- Copy TypeScript interfaces from Section 6 here
   ├── utils/
   │   ├── formatters.ts   <-- Currency & date formatters
   │   └── countdown.ts    <-- Turnaround countdown calculator
   ├── App.tsx
   └── main.tsx
   ```
4. **Step 4: Seed the Application**
   - Place the full 64 opportunities, 5 shutdowns, and 24 sources into `src/data/initialData.ts`.
5. **Step 5: Test Passkey Security Gate**
   - Verify that loading the page prompts for PIN `1989` and properly unlocks the interface.
6. **Step 6: Deploy & Share**
   - Publish live on Lovable or deploy to GitHub Pages / Vercel.

---
*Document generated autonomously by Antigravity AI Engine for Oil & Gas Terminal Qatar.*
