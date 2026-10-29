import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(16, 10.5), dpi=300)
ax.set_xlim(0, 16)
ax.set_ylim(0, 10.5)
ax.axis('off')

plt.text(8, 10.05, 'AI-Assisted Proposal Triage Architecture & Process Flow', 
         fontsize=17, fontweight='bold', ha='center', va='center', color='#0F172A', fontfamily='sans-serif')
plt.text(8, 9.68, 'Reference: MATACS-TH-2026-02  |  End-to-End Workflow: Ingestion, Hybrid AI/Rule Triage, Human Sign-Off', 
         fontsize=10.5, ha='center', va='center', color='#475569', fontfamily='sans-serif')

def draw_box(x, y, w, h, title, subtitle, bg_color, border_color, text_color='#0F172A'):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15,rounding_size=0.12',
                                 facecolor=bg_color, edgecolor=border_color, linewidth=1.8)
    ax.add_patch(box)
    cx = x + w/2
    if subtitle:
        cy_title = y + h * 0.65
        cy_sub = y + h * 0.32
        ax.text(cx, cy_title, title, fontsize=9.2, fontweight='bold', ha='center', va='center', color=text_color, wrap=True)
        ax.text(cx, cy_sub, subtitle, fontsize=7.6, ha='center', va='center', color='#334155', wrap=True)
    else:
        cy = y + h/2
        ax.text(cx, cy, title, fontsize=9.2, fontweight='bold', ha='center', va='center', color=text_color, wrap=True)

def draw_arrow(x1, y1, x2, y2, label='', color='#475569', style='->', lw=1.6):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw, shrinkA=3, shrinkB=3,
                                connectionstyle='arc3,rad=0'))
    if label:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        ax.text(mx, my + 0.14, label, fontsize=7.2, fontweight='bold', ha='center', va='center', color=color,
                bbox=dict(boxstyle='square,pad=0.12', facecolor='white', edgecolor='#CBD5E1', lw=0.6))

# Swimlanes
ax.axvspan(0.4, 3.8, ymin=0.03, ymax=0.88, facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=1, linestyle='--')
ax.text(2.1, 9.05, 'STAGE 1: INGESTION & CONFIG', fontsize=9.5, fontweight='bold', color='#1E293B', ha='center')

ax.axvspan(4.1, 7.8, ymin=0.03, ymax=0.88, facecolor='#FAF5FF', edgecolor='#DDD6FE', linewidth=1, linestyle='--')
ax.text(5.95, 9.05, 'STAGE 2: AI EXTRACTION & SAFETY', fontsize=9.5, fontweight='bold', color='#6B21A8', ha='center')

ax.axvspan(8.1, 11.8, ymin=0.03, ymax=0.88, facecolor='#EFF6FF', edgecolor='#BFDBFE', linewidth=1, linestyle='--')
ax.text(9.95, 9.05, 'STAGE 3: RULES & SCORING', fontsize=9.5, fontweight='bold', color='#1D4ED8', ha='center')

ax.axvspan(12.1, 15.6, ymin=0.03, ymax=0.88, facecolor='#F0FDF4', edgecolor='#BBF7D0', linewidth=1, linestyle='--')
ax.text(13.85, 9.05, 'STAGE 4: HUMAN AUDIT & DECISION', fontsize=9.5, fontweight='bold', color='#15803D', ha='center')

# Stage 1
draw_box(0.65, 7.3, 2.9, 1.25, '1.1 PDF Proposal Upload', 'Reviewer uploads bids (A-E)\nText & OCR conversion', '#F1F5F9', '#94A3B8')
draw_box(0.65, 5.3, 2.9, 1.25, '1.2 Admin Dynamic Config', 'Dynamic criteria & weights\nBudget CAD 260k | 16-wk ceiling', '#F1F5F9', '#94A3B8')
draw_box(0.65, 3.3, 2.9, 1.25, '1.3 Data Isolation & Tagging', 'Wrap text in <proposal_data>\nStrict Data vs Instruction boundary', '#F1F5F9', '#94A3B8')

draw_arrow(2.1, 7.3, 2.1, 6.55)
draw_arrow(2.1, 5.3, 2.1, 4.55)
draw_arrow(3.55, 3.92, 4.4, 3.92, 'Isolated Data')

# Stage 2
draw_box(4.4, 3.3, 3.1, 1.25, '2.1 Adversarial Injection Scan', 'LLM Guardrail detects directives\n(e.g., Proposal D pre-approval trick)', '#F3E8FF', '#A855F7', '#581C87')
draw_box(4.4, 5.3, 3.1, 1.25, '2.2 Structured LLM Extraction', 'temp=0.0 | Pydantic JSON Schema\nExtracts specs, licence, terms, costs', '#F3E8FF', '#A855F7', '#581C87')
draw_box(4.4, 7.3, 3.1, 1.25, '2.3 Source Quote Verifier', 'Regex matches extracted values\nagainst verbatim text in source PDF', '#F3E8FF', '#A855F7', '#581C87')

draw_arrow(5.95, 4.55, 5.95, 5.3, 'Clean / Flagged')
draw_arrow(5.95, 6.55, 5.95, 7.3, 'Raw JSON')

# Stage 3
draw_box(8.4, 7.3, 3.1, 1.25, '3.1 Mandatory Pass/Fail Gate', 'Rule: Bidder itself holds licence?\nRule: WSIB & 5M insurance valid?\n(Proposal B fails subcontractor)', '#DBEAFE', '#3B82F6', '#1E40AF')
draw_box(8.4, 5.3, 3.1, 1.25, '3.2 Ceiling & Completeness Gate', 'Price <= CAD 260k | Time <= 16w\n(Proposal D flagged: no schedule)', '#DBEAFE', '#3B82F6', '#1E40AF')
draw_box(8.4, 3.3, 3.1, 1.25, '3.3 Deterministic Scoring Formula', 'Multi-attribute formula (0-100):\nExp 30%, Price 25%, Time 15%,\nWarranty 15%, Team 15%', '#DBEAFE', '#3B82F6', '#1E40AF')

draw_arrow(7.5, 7.92, 8.4, 7.92, 'Verified Facts')
draw_arrow(9.95, 7.3, 9.95, 6.55, 'Passed')
draw_arrow(9.95, 5.3, 9.95, 4.55, 'Complete')

# Stage 4
draw_box(12.35, 7.3, 3.0, 1.25, '4.1 Triage Review Dashboard', 'Ranked: A (98.8), E (85.5), C (77.8)\nIneligible: B | Flagged: D\nEvidence quotes highlighted', '#FEF3C7', '#F59E0B', '#92400E')
draw_box(12.35, 5.3, 3.0, 1.25, '4.2 Human Overrides & Sign-Off', 'Reviewer validates disqualification,\nresolves flags, or adjusts score\n(Mandatory written rationale)', '#FEF3C7', '#F59E0B', '#92400E')
draw_box(12.35, 3.3, 3.0, 1.25, '4.3 Tamper-Evident Audit Log', 'Immutable log: doc hashes, prompt,\nmodel version, raw extraction, scores,\nreviewer edits & timestamps', '#DCFCE7', '#22C55E', '#166534')
draw_box(12.35, 1.4, 3.0, 1.25, '4.4 Final Award Decision', 'Official procurement officer\nmakes binding legal award', '#DCFCE7', '#22C55E', '#166534')

draw_arrow(11.5, 7.92, 12.35, 7.92, 'Triage State')
draw_arrow(11.5, 5.92, 12.35, 7.4, 'Flagged / Excluded')
draw_arrow(11.5, 3.92, 12.35, 7.2, 'Final Scores')

draw_arrow(13.85, 7.3, 13.85, 6.55)
draw_arrow(13.85, 5.3, 13.85, 4.55)
draw_arrow(13.85, 3.3, 13.85, 2.65)

# Legend Box
legend_box = patches.FancyBboxPatch((0.65, 0.45), 11.2, 2.2, boxstyle='round,pad=0.15,rounding_size=0.1',
                                   facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.2)
ax.add_patch(legend_box)
ax.text(0.85, 2.35, 'Architecture Responsibilities & Design Principles:', fontsize=8.8, fontweight='bold', color='#0F172A')

legend_items = [
    ('Ingestion & Config', '#F1F5F9', '#94A3B8', 'Admin dynamic criteria screens + document ingestion with strict data/instruction isolation tags.'),
    ('AI Layer (Probabilistic)', '#F3E8FF', '#A855F7', 'LLM entity extraction (temp=0.0) + adversarial injection detection + source citation quotes.'),
    ('Rules / Code (Deterministic)', '#DBEAFE', '#3B82F6', 'Mandatory pass/fail regex, hard ceiling enforcement, and zero-hallucination math scoring.'),
    ('Human Oversight (Review)', '#FEF3C7', '#F59E0B', 'Reviewer triage dashboard with one-click verification of ineligibility and manual override capabilities.'),
    ('Audit & Final Award', '#DCFCE7', '#22C55E', 'Cryptographically verifiable audit log tracking all edits, prompt versions, and human award decision.')
]

y_pos = 1.95
for name, fc, ec, desc in legend_items:
    patch = patches.Rectangle((0.85, y_pos - 0.08), 0.35, 0.22, facecolor=fc, edgecolor=ec, linewidth=1.2)
    ax.add_patch(patch)
    ax.text(1.3, y_pos + 0.03, f'{name}:', fontsize=7.6, fontweight='bold', color='#1E293B', va='center')
    ax.text(3.4, y_pos + 0.03, desc, fontsize=7.4, color='#475569', va='center')
    y_pos -= 0.36

plt.tight_layout()
plt.savefig('diagram/process_flow.png', dpi=300, bbox_inches='tight')
plt.savefig('diagram/process_flow.pdf', bbox_inches='tight')
print('Diagram updated with score 85.5!')
