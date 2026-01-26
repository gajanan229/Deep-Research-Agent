# Question 3 - V08-3

                **Question ID:** Q3  
                **Title:** Cross-Border CBDC Regulatory Landscape  
                **Category:** professional_specialized  

                ---

                ## Original Question

                Central Bank Digital Currencies (CBDCs) are advancing rapidly with over 130 countries 
exploring or piloting implementations, yet regulatory frameworks remain fragmented 
across jurisdictions.

Analyze the emerging regulatory and operational landscape for CBDCs by examining:

1. How do the design choices of major CBDC projects (China's e-CNY, EU's digital euro 
   pilot, US research programs, India's e-rupee) differ in terms of privacy models, 
   programmability, and cross-border interoperability?

2. What are the key regulatory tensions between AML/KYC requirements and privacy 
   preservation in different CBDC implementations, and how are jurisdictions attempting 
   to balance these competing objectives?

3. How do different CBDC architectures (direct model, two-tier system, hybrid approaches) 
   affect the role of commercial banks and implications for financial stability?

4. What progress has been made on cross-border CBDC interoperability projects (mBridge, 
   Dunbar, Icebreaker) and what technical and regulatory barriers remain?

5. How are existing payment regulations (PSD2 in EU, money transmission laws in US) 
   being adapted or challenged to accommodate CBDC operations?

Synthesize these regulatory developments into a comparative framework showing how 
different jurisdictions are approaching CBDC deployment tradeoffs.


                ---

                ## Research Report

                # Central bank digital currencies (CBDCs) are forcing policymakers to reconcile competing objectives—privacy, AML/CFT, financial stability, and cross‑border interoperability—through divergent design and regulatory choices. Major projects (e‑CNY, digital euro pilots, US research, India’s digital rupee) reveal distinct privacy models, degrees of programmability, and architectural choices that reshape the role of commercial banks and systemic risk; cross‑border experiments (mBridge, Dunbar, Icebreaker) demonstrate technical feasibility but are constrained by legal, sanctions, data‑sharing, and standards gaps. A comparative regulatory framework can map these tradeoffs, identify policy levers (privacy‑enhancing tech, tiered KYC, two‑tier vs hybrid architectures, harmonized AML/CFT regimes, interoperability standards), and show how jurisdictions prioritize different risks and objectives.

## Introduction & Scope

This section defines the study’s research question, scope, methods, and thesis.

Research question: How do CBDC design and regulatory choices reconcile competing objectives of privacy, AML/CFT, financial stability, and cross‑border interoperability?  Methods: comparative policy analysis, case studies of listed projects, technical review of architectures, and regulatory gap analysis across jurisdictions.  Scope: the study compares major national and cross‑border CBDC initiatives, with explicit case studies of China’s e‑CNY and European digital euro pilots based on comparative literature that analyzes those projects and similar national efforts [https://www.researchgate.net/publication/393172546_A_Comparative_Analysis_of_the_Digital_Euro_Digital_Ruble_and_Digital_Yuan_in_Different_Aspects_Bachelor's_Thesis].  For cross‑border experiments, the report uses the retail‑focused Icebreaker project as an illustrative case to examine privacy/AML tradeoffs in multi‑jurisdictional retail CBDC arrangements [https://www.imf.org/-/media/Files/Publications/FTN063/2024/English/FTNEA2024002.ashx?utm_source=chatgpt.com].  Analytical focus and mechanisms: building on prior work that maps privacy protections against AML/CFT requirements, the study analyzes how multi‑CBDC models create tensions between data minimization (user privacy) and transactional transparency (AML/CFT compliance) and traces concrete mechanisms—such as tiered KYC thresholds, transaction metadata sharing protocols, and on‑demand disclosure arrangements—that jurisdictions use to navigate these tradeoffs [https://www.atlanticcouncil.org/wp-content/uploads/2022/09/Privacy_in_cross-border_digital_currency-_A_transatlantic_approach__-.pdf].  Examples grounded in evidence: the Icebreaker design serves as a retail example where privacy-preserving design choices are explicitly weighed against cross‑border compliance needs [https://www.imf.org/-/media/Files/Publications/FTN063/2024/English/FTNEA2024002.ashx?utm_source=chatgpt.com], while comparative studies of the digital euro and digital yuan provide national‑level contrasts in design and policy priorities [https://www.researchgate.net/publication/393172546_A_Comparative_Analysis_of_the_Digital_Euro_Digital_Ruble_and_Digital_Yuan_in_Different_Aspects_Bachelor's_Thesis].  Evidence gaps: the provided sources do not include direct, citable primary documentation for mBridge, Dunbar, the US Federal Reserve’s ongoing research outputs, or India’s digital rupee technical papers; those documents will be collected and analyzed in subsequent revisions to avoid unsupported assertions.

Next sections will present detailed case studies and a regulatory gap matrix, citing primary project documentation where available.

## Comparative Design Choices

Comparative overview of privacy, programmability, and cross-border design across selected CBDC projects.

The e‑CNY implements a centralized, account‑style model that combines limited small‑value anonymity with strong traceability for larger transactions, keeping the currency “loosely coupled” to bank accounts and enabling transaction-level monitoring for enforcement and AML purposes [https://www.mdpi.com/2673-8392/5/4/179]. Mechanistically, the MDPI analysis describes a modality in which small retail payments can operate with reduced identifying data while higher‑value flows are designed to remain auditable, which operationally privileges law‑enforcement and AML controls over broad retail privacy protections [https://www.mdpi.com/2673-8392/5/4/179].

By contrast, digital euro pilots are expressly framing “privacy by design” goals and exploring retail features intended to limit personal data exposure—such as tiered access levels and offline payment functionality—within the EU’s data‑protection framework, with the stated objective of safeguarding user rights in the digital age [https://www.ecb.europa.eu/euro/digital_euro/features/privacy/html/index.en.html]. The ECB material emphasizes designing the digital euro to minimize processed personal data and to provide stronger privacy guarantees for ordinary retail use cases, which implies constraints on how programmability can be implemented so as not to conflict with EU data‑protection norms [https://www.ecb.europa.eu/euro/digital_euro/features/privacy/html/index.en.html].

Direct comparisons on programmability and cross‑border design are limited by the supplied evidence: the MDPI source documents e‑CNY’s traceability and coupling choices but does not provide detailed technical rules for programmability or cross‑border settlement [https://www.mdpi.com/2673-8392/5/4/179], and the ECB privacy overview sets out policy goals and pilot features without full technical specifications for programmable rules or cross‑border interoperability [https://www.ecb.europa.eu/euro/digital_euro/features/privacy/html/index.en.html]. No supplied sources in the provided evidence set describe US research outcomes or India’s e‑rupee design, so I cannot make verified claims about those jurisdictions without additional evidence.

Gaps: further technical documentation is needed to compare programmability mechanisms and cross‑border arrangements for all four jurisdictions.

## AML/KYC vs Privacy Tensions

This section examines tensions between AML/CFT and privacy in retail payment implementations and evaluates tiering and privacy‑enhancing technologies as policy mechanisms.

Regulators face a persistent trade‑off between transaction privacy for retail users and the need for AML/CFT-compatible auditability in digital currency systems, a tension explored in recent CBDC policy literature [https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/central-bank-digital-currencies-cbdcs-and-democratic-values_81f16e0c/f3e70f1f-en.pdf].
Tiered KYC—i.e., applying identification and monitoring requirements based on value and velocity thresholds—is presented in the literature as a practicable mechanism to preserve greater privacy for low‑value retail activity while retaining stronger controls for higher‑risk flows [https://www.intechopen.com/online-first/1228691] [https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/central-bank-digital-currencies-cbdcs-and-democratic-values_81f16e0c/f3e70f1f-en.pdf].
However, the effectiveness of tiering depends critically on how thresholds are calibrated and on the jurisdiction’s capacity to monitor and enforce limits, because actors can attempt to circumvent balance or turnover limits if monitoring is weak [https://arxiv.org/html/2505.21008v1] [https://www.bankofcanada.ca/wp-content/uploads/2025/01/sdp2025-1.pdf].
Operationalizing tiering therefore requires durable measurement of transaction patterns, dynamic threshold review, and sufficient supervisory resources to detect structuring and aggregation attempts [https://www.intechopen.com/online-first/1228691] [https://arxiv.org/html/2505.21008v1].
Privacy‑enhancing technologies (PETs) such as selective disclosure schemes and zero‑knowledge proofs are identified as technical approaches that can enable transaction-level auditability without revealing full identity or transaction details to all parties [https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/central-bank-digital-currencies-cbdcs-and-democratic-values_81f16e0c/f3e70f1f-en.pdf] [https://arxiv.org/html/2505.21008v1].
At the same time, PETs introduce substantial technical complexity (cryptographic keys, verifier infrastructure) and create legal and supervisory uncertainties about how evidence produced by PETs meets AML compliance and reporting standards [https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/central-bank-digital-currencies-cbdcs-and-democratic-values_81f16e0c/f3e70f1f-en.pdf] [https://www.intechopen.com/online-first/1228691].
Evidence on large‑scale operational deployments of PETs within AML frameworks remains limited in the cited literature, indicating a gap between conceptual promise and empirically verified practice [https://www.intechopen.com/online-first/1228691] [https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/central-bank-digital-currencies-cbdcs-and-democratic-values_81f16e0c/f3e70f1f-en.pdf].

In sum, tiering and PETs are complementary policy levers: tiering offers an immediately practicable privacy/AML balance if thresholds and monitoring are robust, while PETs offer a technical pathway to privacy‑preserving auditability but require further empirical validation and legal clarity [https://www.intechopen.com/online-first/1228691] [https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/central-bank-digital-currencies-cbdcs-and-democratic-values_81f16e0c/f3e70f1f-en.pdf].

## Architectures and Financial Stability

This section evaluates how direct, two‑tier, and hybrid retail CBDC architectures affect commercial banks’ roles, liquidity, and systemic risk, using the provided sources.

Direct CBDC architectures—where the central bank offers retail accounts—shift private deposits onto the central bank’s balance sheet, increasing central bank liabilities and creating incentives for depositor migration away from commercial banks [https://www.bis.org/publ/work1280.pdf].  The BIS analysis frames this as potential “fast” (run‑like) and “slow” (structural) disintermediation, which raises systemic‑risk and liquidity‑management challenges for both banks and the central bank [https://www.bis.org/publ/work1280.pdf].  Mechanistically, deposit transfers reduce banks’ funding, forcing them to either run down liquid assets, sell less liquid assets, or curtail lending; those asset sales can transmit stress through fire‑sales and interbank markets, amplifying systemwide liquidity shortages [https://www.mdpi.com/2227-7072/12/1/19].  Empirical modeling in the literature shows that intermediary runs (in synthetic or intermediary‑based designs) would compel issuers and their bank counterparties to liquidate reserves, draining interbank market liquidity and creating contagion channels [https://www.mdpi.com/2227-7072/12/1/19] .
Two‑tier and hybrid architectures route retail access through intermediaries (banks or non‑bank providers), which mitigates direct depositor flight to the central bank by preserving a role for intermediaries in customer-facing services and credit intermediation [https://documents1.worldbank.org/curated/en/965451638867832702/pdf/Central-Bank-Digital-Currency-A-Payments-Perspective.pdf].  However, these models concentrate liquidity and operational risk in intermediaries and therefore require explicit liquidity backstops (for example, central‑bank facilities), robust settlement mechanisms to move reserves efficiently, and contingency frameworks for intermediary runs or operational outages [https://documents1.worldbank.org/curated/en/965451638867832702/pdf/Central-Bank-Digital-Currency-A-Payments-Perspective.pdf] [https://www.mdpi.com/2227-7072/12/1/19].  The literature highlights specific mechanisms—pre-funding, intraday settlement, tiered remuneration, and standing liquidity facilities—as realistic design tools to limit disintermediation or to backstop intermediaries, but it does not deliver consensus quantitative calibrations for those tools in stress scenarios [https://www.bis.org/publ/work1280.pdf] [https://documents1.worldbank.org/curated/en/965451638867832702/pdf/Central-Bank-Digital-Currency-A-Payments-Perspective.pdf].

Design choice implies trade-offs: direct architectures raise clearer disintermediation risks and central‑bank liability concentration, while two‑tier/hybrid approaches reduce direct flight but shift the policy challenge to provisioning liquidity backstops, settlement design, and contingency planning; the literature documents mechanisms but lacks settled quantitative calibrations for stress tests.

## Payment Regulation Adaptation

This section examines how U.S. money‑transmission and licensing regimes interact with the operational needs of CBDC intermediaries and where evidence is missing.

U.S. money‑transmission laws currently require businesses that handle or transmit funds to comply with state licensing regimes in addition to applicable federal rules, creating overlapping compliance obligations that vary by jurisdiction [https://www.moderntreasury.com/journal/how-do-money-transmission-laws-work]. Mechanistically, this fragmentation arises because states define “money transmission” differently and impose distinct licensing triggers and supervisory requirements (for example, registration, bonding, reporting and AML controls), so a single commercial or platform model can be treated as a regulated transmitter in some states but not others [https://www.moderntreasury.com/journal/how-do-money-transmission-laws-work]. Those diverging definitions and administrative regimes increase operational complexity: firms must budget for multiple license applications, varying capital or surety bond levels, and differing reporting systems, which raises fixed and ongoing costs and complicates nationwide scaling [https://www.moderntreasury.com/journal/how-do-money-transmission-laws-work]. The practical consequence for potential CBDC intermediaries is legal uncertainty about whether and how state licensing regimes will apply to CBDC distribution, custody, or settlement activities—Modern Treasury explicitly recommends seeking tailored legal advice given the state/federal overlap [https://www.moderntreasury.com/journal/how-do-money-transmission-laws-work]. The provided policy literature on CBDCs and payment resilience (focused on fragile and conflict‑affected states) does not analyze U.S. state licensing or offer a federal‑vs‑state jurisdictional prescription, leaving a gap in evidence on CBDC‑specific regulatory adaptation in the U.S. context [https://www.elibrary.imf.org/view/journals/063/2025/009/article-A001-en.xml] [https://www.tandfonline.com/doi/full/10.1080/09538259.2025.2573356]. Inference from the documented fragmentation suggests that clearer federal‑state jurisdictional guidance or coordination would reduce uncertainty and lower the scaling costs for CBDC intermediaries, but direct empirical or policy recommendations specific to CBDC implementations in the U.S. are not present in the supplied sources [https://www.moderntreasury.com/journal/how-do-money-transmission-laws-work] [https://www.elibrary.imf.org/view/journals/063/2025/009/article-A001-en.xml].

In short, the evidence documents state‑level fragmentation and compliance mechanisms that can impede scaling; however, direct, CBDC‑specific policy guidance on federal‑state clarity is absent in the supplied sources.

## Cross-Border Interoperability Progress

This section assesses pilot outcomes and remaining non‑technical barriers to cross‑border CBDC interoperability.

BIS-led pilots including mBridge and Project Dunbar have demonstrated that multi‑jurisdiction wholesale CBDC settlement and inter‑system messaging can be implemented using common rails and connector-style architectures, evidencing technical feasibility for cross‑CBDC settlement workflows [https://papers.ssrn.com/sol3/Delivery.cfm/5394110.pdf?abstractid=5394110&mirid=1] [https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/mBridge_publication.pdf].
mBridge experiments used a shared ledger model that allowed multiple central banks’ wholesale CBDCs to be issued and settled on a single platform, showing how tokenized central‑bank liabilities can achieve atomic settlement across jurisdictions and reduce reliance on correspondent accounts [https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/mBridge_publication.pdf] [https://papers.ssrn.com/sol3/Delivery.cfm/5394110.pdf?abstractid=5394110&mirid=1].
Project Dunbar tested a common settlement platform and connector approaches that link domestic systems to a common settlement rail, illustrating a practical mechanism for translating messaging and settlement instructions between heterogeneous domestic ledgers [https://papers.ssrn.com/sol3/Delivery.cfm/5394110.pdf?abstractid=5394110&mirid=1].
Analytically, these architectures separate messaging translation (connectors/adaptors) from final settlement (common rails/shared ledger), which can reduce integration complexity for participating jurisdictions by localizing regulatory and operational interfaces [https://www.omfif.org/2025/09/building-bridges-interoperability-for-a-resilient-digital-future/].
However, pilots also report that unresolved legal and regulatory frameworks limit real‑world deployment, including questions on liability, finality, and cross‑border recognition of central‑bank liabilities [https://www.omfif.org/2025/09/building-bridges-interoperability-for-a-resilient-digital-future/] [https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/mBridge_publication.pdf].
Separately, cross‑border CBDC usage faces material constraints from sanctions exposure and divergent KYC/data‑sharing requirements, which increase compliance risk for participants and can curtail routine correspondent relationships [https://www.elucidate.co/blog/sanctions-risks-kyc-challenges-and-how-to-overcome-them] [https://www.phoenixstrategy.group/blog/cross-border-blockchain-payments-legal-risks].
Evidence on the extent to which gaps in mutual legal assistance or formalized data‑sharing treaties specifically impede CBDC corridors is limited in the provided sources, indicating a need for targeted legal analysis and documentation of MLAT/data‑sharing constraints in pilot reporting [https://www.omfif.org/2025/09/building-bridges-interoperability-for-a-resilient-digital-future/].

In short, technical pathways for multi‑CBDC interoperability are proven in pilot form, while legal, sanctions‑related and data‑sharing issues remain the principal barriers to routine cross‑border use and scale-up.

## Comparative Framework & Recommendations

This section synthesizes prior analyses into a comparative framework and concrete recommendations for regulators and researchers.

A comparative framework that maps core design choices—privacy model, KYC tiering, system architecture, and programmability—to outcomes (privacy risk, AML efficacy, financial‑stability risk, and interoperability) enables structured tradeoff analysis and targeted policy levers. The CBDC literature shows that tiered privacy and embedded sanctions screening can be architected into payment rails, which supports using design‑choice mappings to reconcile enforcement and civil‑liberties goals [https://www.researchgate.net/publication/390940697_Interoperability_of_CBDCs_Optimising_Cross-Border_Settlements_through_the_lens_of_national_and_international_regulation] [https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4636197_code6293173.pdf?abstractid=4636197&mirid=1]. Privacy‑enhancing technologies (PETs) and standardized taxonomies help operationalize privacy models and enable privacy‑preserving analytics that can reduce disclosure while preserving compliance checks, as emphasized by recent privacy taxonomy work [https://iabtechlab.com/press-releases/iab-tech-lab-unveils-new-privacy-taxonomy-for-public-comment/]. Embedding compliance at the protocol layer creates mechanisms—automated sanctions screening, tiered KYC checkpoints, and auditable logs—that directly increase AML/CFT effectiveness but require careful legal and governance safeguards to protect civil liberties [https://www.researchgate.net/publication/390940697_Interoperability_of_CBDCs_Optimising_Cross-Border_Settlements_through_the_lens_of_national_and_international_regulation] [https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4636197_code6293173.pdf?abstractid=4636197&mirid=1]. Harmonized AML/CFT rules and interoperability standards across jurisdictions are repeatedly identified as necessary to realize cross‑border settlement efficiency and consistent enforcement outcomes [https://www.researchgate.net/publication/390940697_Interoperability_of_CBDCs_Optimising_Cross-Border_Settlements_through_the_lens_of_national_and_international_regulation]. Implementing these frameworks requires workforce and capability development aligned with privacy and compliance taxonomies, as highlighted in recent NIST work on privacy workforce taxonomies [https://csrc.nist.gov/News/2024/nist-privacy-workforce-taxonomy-initial-draft]. Evidence gaps: the provided sources document tiered privacy, sanctions screening, and taxonomy needs but do not contain systematic empirical analyses comparing two‑tier or hybrid architectures’ quantitative effects on disintermediation or stability; targeted empirical research is needed on those architecture‑outcome links (gap noted).

Recommendations: deploy PETs and privacy taxonomies; adopt tiered KYC embedded in infrastructure; prioritize harmonized AML/CFT and interoperability standards; and fund empirical research on architecture impacts and workforce readiness.

## References
- http://openviewjournal.com/index.php/mira/article/download/43/55
- http://www.diva-portal.org/smash/get/diva2:1500415/FULLTEXT01.pdf
- http://www.pbc.gov.cn/en/3688110/3688172/4157443/4293696/2021071614584691871.pdf
- https://academic.oup.com/book/35048/chapter/298946221
- https://academic.oup.com/policyandsociety/article/32/4/279/6422273
- https://allconfsbot.website/
- https://amlwatcher.com/news/china-to-recognize-virtual-asset-transactions-as-a-method-of-money-laundering/
- https://amlyze.com/wp-content/uploads/How-not-to-mess-up-your-correspondent-relationship.pdf
- https://arxiv.org/html/2505.21008v1
- https://arxiv.org/html/2507.08880v1
- https://baffi.unibocconi.eu/sites/default/files/media/attach/1%20-%20MINTS%20Report%20CBDC%20201222%20%281%29_0.pdf
- https://bankquality.com/blog/digital-currency-wars-the-digital-euro-vs-e-cny-vs-fedcoin
- https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/09/09-2022-Technical-Design-Choices-US-CBDC-System.pdf
- https://centralbank.ae/media/lnchuury/project-mbridge-connecting-economies-through-cbdc-final.pdf
- https://clsbluesky.law.columbia.edu/2025/08/11/do-the-anti-cbdc-surveillance-state-act-and-the-genius-act-jeopardize-u-s-digital-finance/
- https://cmlabs.co/en-il/seo-guidelines/canonical-urls
- https://cognitiveseo.com/blog/19204/canonical-urls-seo/
- https://commission.europa.eu/funding-tenders/procedures-guidelines-tenders/information-contractors-and-beneficiaries/exchange-rate-inforeuro_en
- https://cryptorank.io/news/feed/f4284-ecb-dlt-transactions-2026-digital-euro-privacy
- https://csep.org/blog/central-bank-digital-currency-chinas-first-mover-advantage-and-policy-pathways-for-india/
- https://csrc.nist.gov/News/2024/nist-privacy-workforce-taxonomy-initial-draft
- https://csrc.nist.gov/pubs/cswp/38/nist-privacy-workforce-taxonomy/ipd
- https://dcfintechweek.org/wp-content/uploads/2024/09/Legal-Considerations-for-the-Deployment-of-a-Central-Bank-Digital-Currency-2024.pdf
- https://digichina.stanford.edu/work/lexicon-controllable-anonymity-or-managed-anonymity-and-chinas-digital-yuan/
- https://digital-euro-association.de/hubfs/Privacy%20and%20CBDCs%20-%20Digital%20Euro%20Association%20Working%20Group.pdf?hsLang=en
- https://digitalcommons.osgoode.yorku.ca/cgi/viewcontent.cgi?article=1017&context=conference_papers
- https://digitalfinancenews.com/research-reports/a-comprehensive-analysis-of-know-your-customer-kyc-protocols-regulatory-frameworks-technological-innovations-and-implications-for-financial-inclusion/
- https://discussions.apple.com/thread/255109191
- https://discussions.apple.com/thread/255558948
- https://discussions.apple.com/thread/255798251
- https://discussions.apple.com/thread/255829818
- https://discussions.apple.com/thread/255926115
- https://discussions.apple.com/thread/256098199
- https://dkf1ato8y5dsg.cloudfront.net/uploads/52/504/kyc-2a-ma-summit-2023-the-journey-to-perpetual-kyc-case-study.pdf
- https://documents1.worldbank.org/curated/en/965451638867832702/pdf/Central-Bank-Digital-Currency-A-Payments-Perspective.pdf
- https://en.wikipedia.org/wiki/Central_bank_digital_currency
- https://eprint.iacr.org/2022/1443.pdf
- https://european-economy.eu/wp-content/uploads/2024/11/EE_2023_2024.pdf
- https://evidencefordemocracy.ca/wp-content/uploads/2024/02/Annotated-Bibliography-for-Transparency-In-Policy-Making-2.pdf
- https://finance.ec.europa.eu/news/commission-proposes-maintaining-current-liquidity-rules-strengthen-eu-financial-markets-2025-03-31_en
- https://finance.yahoo.com/news/eu-council-greenlights-digital-euro-120818927.html
- https://fineksus.com/how-economic-sanctions-impact-correspondent-banking/
- https://fwd-lawyermarketing.com/url-canonicalization-strategies-to-avoid-duplicate-content/
- https://global.chinadaily.com.cn/a/202512/29/WS69521db2a310d6866eb30f9b.html
- https://go.concordia.ca/workshops/upcomingworkshops/
- https://guides.library.cornell.edu/citing_us_gov_docs/agencies
- https://hal.science/hal-05048221v1/file/Digital%20Currency%20in%20China-%20Pilot%20implementation%2C%20Legal%20Challenges%20and%20Prospects%2C.pdf
- https://hospitalityinsights.ehl.edu/new-regulations-in-the-swiss-banking-sector-public-liquidity-backstop
- https://iabtechlab.com/press-releases/iab-tech-lab-unveils-new-privacy-taxonomy-for-public-comment/
- https://iasgoogle.com/admin/common_uploads/monthly_news_scan/94331768698596.pdf
- https://ideas.repec.org/a/eee/finlet/v67y2024ipbs1544612324008985.html
- https://ideas.repec.org/p/sek/iefpro/14115979.html
- https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=6636&context=sol_research
- https://ink.library.smu.edu.sg/context/sol_research/article/6259/viewcontent/How_to_Understand_China_s_Approach_CBDC_sv.pdf
- https://libguides.wlu.edu/c.php?g=158245&p=1036332
- https://link.springer.com/chapter/10.1007/978-3-031-73549-3_9
- https://link.springer.com/chapter/10.1007/978-3-031-74889-9_14
- https://links.sgx.com/FileOpen/Kioxia%20Holdings%20Corp_946237_010_CL_NoDISC_PW_17July0630H.ashx?App=Prospectus&FileID=66909
- https://longbridge.com/en/news/270332916
- https://longbridge.com/en/news/271025882
- https://m10.io/blog/account-based-vs-token-based-cbdc-stay-focused-on-what-matters
- https://northlark.com/cross-border-kyc-challenges-best-practices-for-multi-jurisdiction-compliance/
- https://now.solar/2026/01/24/
- https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.40.ipd.pdf
- https://onlinelibrary.wiley.com/doi/full/10.1111/1758-5899.13495
- https://openjournals.libs.uga.edu/fsr/article/download/4154/3554/13956
- https://openknowledge.worldbank.org/entities/publication/2df8caf9-3a5a-45e7-8c63-e5126a8ad0bd
- https://papers.ssrn.com/sol3/Delivery.cfm/5350710.pdf?abstractid=5350710&mirid=1
- https://papers.ssrn.com/sol3/Delivery.cfm/5368708.pdf?abstractid=5368708&mirid=1
- https://papers.ssrn.com/sol3/Delivery.cfm/5394110.pdf?abstractid=5394110&mirid=1
- https://papers.ssrn.com/sol3/Delivery.cfm/5842282.pdf?abstractid=5842282&mirid=1
- https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3759144_code4056862.pdf?abstractid=3759144
- https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4636197_code6293173.pdf?abstractid=4636197&mirid=1
- https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4663934_code10554.pdf?abstractid=4663934
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3759144
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4838345
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5170329
- https://paradigmresear.ch/cbdcs-worldwide-case-studies-and-implementation-strategies?id=67d43639128c61d0b4f80100&pageType=Blockchain%20%26%20Crypto
- https://pitt.libguides.com/citationhelp
- https://redandwhitechair.com/31936-the-journey-to-successful-kyc-implementation-case-studies-and-lessons-learned-12/
- https://rocketclicks.com/client-education/utilizing-canonical-tags-to-avoid-duplicate-content-issues/
- https://rpc.cfainstitute.org/sites/default/files/-/media/documents/survey/CBDC_Survey_Report_Online.pdf
- https://scholarlycommons.law.emory.edu/cgi/viewcontent.cgi?article=1375&context=eilr
- https://scholarship.law.duke.edu/cgi/viewcontent.cgi?article=5159&context=lcp
- https://scholarship.law.ufl.edu/cgi/viewcontent.cgi?article=2239&context=facultypub
- https://sciendo.com/pdf/10.2478/picbe-2025-0116
- https://tesi.luiss.it/41243/1/276421_DI%20FOLCO_LEONARDO.pdf
- https://theaspd.com/index.php/ijes/article/download/4469/3266/14414
- https://undcif.org/e-cny-advancing-functional-capabilities-in-sovereign-digital-currency/
- https://univ-pantheon-assas.hal.science/hal-04941246/document
- https://www.aimspress.com/article/doi/10.3934/QFE.2023032?viewType=HTML
- https://www.anderson.ucla.edu/sites/default/files/document/2023-05/5.26.23%20Paper%20Toni%20Whited%20CBDC.pdf
- https://www.astrid-online.it/static/upload/2306/230628-impact-assessment-digital-euro-regulation_en.pdf
- https://www.atlanticcouncil.org/blogs/new-atlanticist/central-banks-are-embracing-digital-currencies-will-the-us-lead-or-follow/
- https://www.atlanticcouncil.org/wp-content/uploads/2022/09/Privacy_in_cross-border_digital_currency-_A_transatlantic_approach__-.pdf
- https://www.bankingsupervision.europa.eu/press/conferences/shared/pdf/2024_research_conf/10_rottner.pdf
- https://www.bankofcanada.ca/wp-content/uploads/2025/01/sdp2025-1.pdf
- https://www.bbvaresearch.com/wp-content/uploads/2021/10/20211018_China_Central-Bank-Digital-Currency.pdf
- https://www.bibguru.com/g/chicago-report-citation/
- https://www.bis.org/about/bisih/topics/cbdc/icebreaker.htm
- https://www.bis.org/about/bisih/topics/cbdc/mcbdc_bridge.htm
- https://www.bis.org/innovation_hub/projects/mbridge_brochure_2311.pdf
- https://www.bis.org/press/p240605.htm
- https://www.bis.org/publ/bppdf/bispap123_e.pdf
- https://www.bis.org/publ/bppdf/bispap159.htm?
- https://www.bis.org/publ/brochure_mbridge.pdf
- https://www.bis.org/publ/othp40.htm
- https://www.bis.org/publ/othp42_system_design.pdf
- https://www.bis.org/publ/othp47.pdf
- https://www.bis.org/publ/othp51.pdf
- https://www.bis.org/publ/othp52.pdf
- https://www.bis.org/publ/othp57.pdf
- https://www.bis.org/publ/othp59.htm
- https://www.bis.org/publ/othp61.pdf
- https://www.bis.org/publ/othp81.pdf
- https://www.bis.org/publ/othp88_legal.pdf
- https://www.bis.org/publ/work1147.pdf
- https://www.bis.org/publ/work1280.htm
- https://www.bis.org/publ/work1280.pdf
- https://www.cbdc.cc/
- https://www.centralbankofindia.co.in/
- https://www.chainscorelabs.com/en/blog/web3-philosophy-sovereignty-and-ownership/zk-proofs-for-privacy-and-ownership/why-privacy-preserving-ownership-will-disrupt-traditional-finance
- https://www.chegg.com/writing/features/citation-generator/how-to-cite-policy
- https://www.cigionline.org/static/documents/DPH-paper-Freiman.pdf
- https://www.cnil.fr/en/digital-euro-what-stake-privacy-and-personal-data-protection
- https://www.conductor.com/academy/canonical/
- https://www.congress.gov/crs_external_products/R/PDF/R46850/R46850.3.pdf
- https://www.cov.com/-/media/files/corporate/publications/2025/10/correspondent-banking-related-risks-arising-from-cartels-designations-as-terrorist-organizations.pdf
- https://www.csbs.org/csbs-money-transmission-modernization-act-mtma
- https://www.db.com/news/detail/20210714-digital-yuan-what-is-it-and-how-does-it-work
- https://www.debevoisefintechblog.com/2022/02/01/the-state-of-money-transmission-regulation-and-digital-assets-in-2022/
- https://www.ecb.europa.eu/euro/digital_euro/features/privacy/html/index.en.html
- https://www.ecb.europa.eu/euro/digital_euro/how-it-works/html/index.en.html
- https://www.edpb.europa.eu/our-work-tools/our-documents/support-pool-experts-projects/digital-euro-and-its-token-based-offline_en
- https://www.edpb.europa.eu/system/files/2025-10/digitaleurotokenbasedofflinemodality_en.pdf
- https://www.eecg.utoronto.ca/~veneris/21icbc2.pdf
- https://www.eecg.utoronto.ca/~veneris/TNSM2021.pdf
- https://www.elibrary.imf.org/downloadpdf/view/journals/063/2023/007/article-A001-en.pdf
- https://www.elibrary.imf.org/view/journals/002/2022/318/article-A001-en.xml
- https://www.elibrary.imf.org/view/journals/007/2023/048/article-A001-en.xml
- https://www.elibrary.imf.org/view/journals/007/2024/052/article-A001-en.xml
- https://www.elibrary.imf.org/view/journals/063/2023/007/article-A001-en.xml
- https://www.elibrary.imf.org/view/journals/063/2024/004/article-A001-en.xml
- https://www.elibrary.imf.org/view/journals/063/2024/005/article-A001-en.xml
- https://www.elibrary.imf.org/view/journals/063/2025/006/article-A001-en.xml
- https://www.elibrary.imf.org/view/journals/063/2025/009/article-A001-en.xml
- https://www.elucidate.co/blog/sanctions-risks-kyc-challenges-and-how-to-overcome-them
- https://www.esma.europa.eu/sites/default/files/2025-06/High-level_Roadmap_to_T_1_Securities_Settlement_in_the_EU.pdf
- https://www.facebook.com/groups/263175136143745/posts/694164919711429/
- https://www.federalreserve.gov/econres/feds/files/2024021pap.pdf?utm_source=chatgpt.com
- https://www.federalreserve.gov/econres/notes/feds-notes/central-bank-liquidity-facilities-around-the-world-20250226.html
- https://www.federalreserve.gov/econres/notes/feds-notes/examining-cbdc-and-wholesale-payments-20230908.html
- https://www.firebrand.marketing/2024/12/best-practices-for-canonicalization-in-seo/
- https://www.fsb.org/uploads/P211024-1.pdf
- https://www.gfma.org/wp-content/uploads/2022/02/central-bank-digital-currencies-a-global-capital-markets-perspective-full-report-feb-2022-final.pdf
- https://www.gfma.org/wp-content/uploads/2025/08/1.-full-report-impact-of-dlt-in-cap-mkts-final-1.pdf
- https://www.gov.mt/en/Government/DOI/Government%20Gazette/Documents/2026/01/Government%20Gazette%20-%2016th%20January.pdf
- https://www.hkdca.com/project-mbridge-experimenting-with-a-multi-cbdc-platform-for-cross-border-payments/
- https://www.hkib.org/pdf/1696479792_HGCP00P23111+Advance+KYC+in+Practice+-+Best+Practical+Examples+and+Case+Studies+20231102.pdf
- https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/mBridge_publication.pdf
- https://www.huduser.gov/portal/periodicals/cityscape/vol25num1/Cityscape-March-2023.pdf
- https://www.iai.it/en/publications/c05/international-digital-yuan-vane-ambitions-excessive-alarmism-and-pragmatic
- https://www.icba.org/documents/45248/964997/Congressional+Research+Service+CBDC+white+paper.pdf/05f78eae-790a-3d83-3037-668e586d883b?version=1.0&t=1753988084815&download=true
- https://www.imf.org/-/media/Files/Publications/FTN063/2024/English/FTNEA2024002.ashx?utm_source=chatgpt.com
- https://www.imf.org/-/media/files/publications/ftn063/2024/english/ftnea2024002.pdf
- https://www.imf.org/-/media/files/publications/ftn063/2024/english/ftnea2024004.pdf
- https://www.imf.org/-/media/files/publications/ftn063/2025/english/ftnea2025010.pdf
- https://www.imf.org/-/media/files/publications/pp/2025/english/ppea2025041.pdf
- https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024177-print-pdf.pdf
- https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024226-print-pdf.pdf
- https://www.imf.org/en/publications/fintech-notes/issues/2024/08/30/central-bank-digital-currency-data-use-and-privacy-protection-554103
- https://www.imf.org/external/pubs/ft/sdn/2016/sdn1606.pdf
- https://www.intechopen.com/online-first/1228691
- https://www.interaction-design.org/literature/topics/digital-inclusion?srsltid=AfmBOopkMnzWQ7bJoUqtFlwYU3PvjbgOcxXIFnKXEK2bkdMpBTBsz-3E
- https://www.intereconomics.eu/contents/year/2023/number/4/article/the-business-case-for-exploration-of-a-us-central-bank-digital-currency.html
- https://www.itu.int/en/ITU-T/extcoop/dcgi/Documents/DCGI%20CBDC%20Reference%20Architecture%20Report-20-01-2025.pdf
- https://www.jbs.cam.ac.uk/wp-content/uploads/2024/12/2024-12-ccaf-wcbdcs-approaches-implementation-strategies-and-use-cases.pdf
- https://www.jsm.com/publications/2026/china-unveils-new-framework-for-digital-yuan-e-cny-operations-and-ecosystem/
- https://www.lawfaremedia.org/article/will-central-bank-digital-currencies-revolutionize-global-finance
- https://www.ledgerinsights.com/mbridge-multi-cbdc-cross-border-payments/
- https://www.lexology.com/library/detail.aspx?g=4416a5b4-69b7-4964-afa7-50d218c83af9
- https://www.linkedin.com/posts/norbertgehrke_imf-digital-yuan-prime-time-activity-7417955416703422464-zCdz
- https://www.linkedin.com/posts/tien-peng-ho-6b0881a4_the-key-insight-from-an-aml-and-financial-crime-activity-7415091100350304256-9Iu7
- https://www.linkedin.com/pulse/maintaining-privacy-digital-currencies-issued-central-mustafa-syed
- https://www.linkedin.com/pulse/summary-pbocs-white-paper-development-e-cny-glenn-wijaya
- https://www.markus-schall.de/en/2025/11/the-digital-euro-is-coming-what-it-means-what-it-must-not-do-and-what-it-could-do/
- https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/banks-and-credit-unions/other/mastercard-cbdc-whitepaper.pdf
- https://www.mdpi.com/2227-7072/12/1/19
- https://www.mdpi.com/2673-8392/5/4/179
- https://www.moderntreasury.com/journal/how-do-money-transmission-laws-work
- https://www.morganlewis.com/blogs/sourcingatmorganlewis/2025/11/eu-parliament-publishes-report-on-interaction-between-eu-digital-regulations
- https://www.nasdaq.com/articles/are-there-tech-solutions-to-the-privacy-and-compliance-trade-offs-for-cbdcs
- https://www.nst.com.my/newssummary/1361679?summary=1361679&date=1769005563
- https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/12/case-studies-on-the-regulatory-challenges-raised-by-innovation-and-the-regulatory-responses_82fcd441/8fa190b5-en.pdf
- https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/07/central-bank-digital-currencies-cbdcs-and-democratic-values_81f16e0c/f3e70f1f-en.pdf
- https://www.omfif.org/2025/09/building-bridges-interoperability-for-a-resilient-digital-future/
- https://www.papayaglobal.com/blog/global-kyc-navigating-challenges-across-borders/
- https://www.payments.ca/sites/default/files/2022-08/PaymentsCanada_2021CBDCRetailConsiderations_En.pdf
- https://www.pbc.gov.cn/en/3935690/3935759/4696741/2022110110142226519.pdf
- https://www.pbc.gov.cn/en/3935690/3935759/4749192/2022122913350138868.pdf
- https://www.phoenix.gov/content/dam/phoenix/cityclerksite/city-council-meeting-files/2025/9-17-25%20Formal%20Agenda-FINAL.pdf
- https://www.phoenixstrategy.group/blog/cross-border-blockchain-payments-legal-risks
- https://www.polytechnique-insights.com/en/columns/economy/strengths-and-constraints-of-the-central-banks-digital-euro/
- https://www.quantifind.com/resources/kyc-case-study/
- https://www.quetext.com/blog/how-to-cite-a-report-in-apa-mla-and-chicago-style
- https://www.researchgate.net/publication/309559826_Use_of_Comparative_Case_Study_Methodology_for_US_Public_Health_Policy_Analysis_A_Review
- https://www.researchgate.net/publication/353444913_Designing_a_Central_Bank_Digital_Currency_with_Support_for_Cash-Like_Privacy
- https://www.researchgate.net/publication/362657901_AT-CBDC_Achieving_Anonymity_and_Traceability_in_Central_Bank_Digital_Currency
- https://www.researchgate.net/publication/385513252_Untangling_Digital_Euro's_Personal_Data_Protection_Challenges_An_Exploration_of_Data_Processing_Activities_and_Latent_Privacy_Risks
- https://www.researchgate.net/publication/388341544_THE_DEVELOPMENT_STATUS_OF_CBDC_A_COMPARATIVE_STUDY
- https://www.researchgate.net/publication/389814116_Enhancing_Know_Your_Customer_KYC_and_Anti-Money_Laundering_AML_Compliance_Using_Blockchain_A_Business_Analysis_Approach
- https://www.researchgate.net/publication/390940697_Interoperability_of_CBDCs_Optimising_Cross-Border_Settlements_through_the_lens_of_national_and_international_regulation
- https://www.researchgate.net/publication/391231936_Selective_Disclosure_Mechanisms_Using_Zero-Knowledge_Proofs_Enhancing_Trust_and_Privacy_in_Blockchain-Based_Ecosystems
- https://www.researchgate.net/publication/393172546_A_Comparative_Analysis_of_the_Digital_Euro_Digital_Ruble_and_Digital_Yuan_in_Different_Aspects_Bachelor's_Thesis
- https://www.researchgate.net/publication/393884641_Cross-Border_Data_Sharing_for_AML_Compliance_Legal_Challenges_National_Interest_and_Policy_Recommendations
- https://www.researchgate.net/publication/394275013_The_Digital_Yuan_vs_the_Digital_Euro_Diverging_Paths_in_Central_Bank_Digital_Currency_Developments
- https://www.researchgate.net/publication/395255247_Comparative_Analysis_Of_Global_Central_Bank_Digital_Currency_CBDC_Projects
- https://www.researchgate.net/publication/395336704_On-Chain_Analytics_Privacy_Tradeoffs_Privacy-Enhancing_Technologies_vs_AML_Obligations
- https://www.researchgate.net/publication/395353957_Cross-Border_Data_Sharing_and_Sanctions_Compliance_Navigating_Privacy_and_Security_Conflicts
- https://www.researchgate.net/publication/395652272_Comparative_Analysis_of_CBDC_Adoption_across_Developing_and_Developed_Countries_A_Systematic_Literature_Review
- https://www.researchgate.net/publication/396137098_THE_DIGITAL_EURO_A_NEW_ERA_OF_PUBLIC_MONEY_AND_PRIVACY_PROTECTION_IN_THE_EUROZONE
- https://www.researchgate.net/publication/396179909_Privacy_vs_Transparency_The_Regulatory_Dilemma_in_CBDC_Implementation
- https://www.researchgate.net/publication/396647719_Case_Study_on_CBDC_Implementation_Lessons_from_Pioneer_Countries
- https://www.researchgate.net/publication/398598755_The_Impact_of_CBDC-Based_Disintermediation_on_the_Banking_Sector_and_the_Economy_An_SFC_Approach
- https://www.reuters.com/world/asia-pacific/china-led-cross-border-digital-currency-platform-sees-surge-2026-01-16/
- https://www.rws.com/media/images/RWS-2025-Annual-Report_tcm228-289771.pdf
- https://www.sciencedirect.com/science/article/abs/pii/S1572308923000888
- https://www.sciencedirect.com/science/article/pii/S0278425425000961/pdf
- https://www.sciencedirect.com/science/article/pii/S1057521923005471
- https://www.sciencedirect.com/science/article/pii/S1544612324008985
- https://www.sciencedirect.com/science/article/pii/S2212473X25001300
- https://www.sciencedirect.com/science/article/pii/S2666143821000028
- https://www.sciencedirect.com/science/article/pii/S2666143825000262
- https://www.sciencedirect.com/science/article/pii/S2949791425000594
- https://www.scribd.com/document/599278866/Project-Dunbar
- https://www.sec.gov/files/ctf-written-james-overdahl-tokenized-us-equities-01-22-2026.pdf
- https://www.securitiesfinancetimes.com/securitieslendingnews/technologyarticle.php?article_id=225876
- https://www.sidley.com/-/media/publications/united-states--the-virtual-currency-regulation-review--edition-2.pdf
- https://www.statestreet.com/web/insights/articles/documents/the-geopolitics-of-cross-border-cbdcs-whitepaper.pdf
- https://www.suerf.org/wp-content/uploads/2023/11/f_27a9a0db6ab0da9b4f98c0681956baff_54533_suerf.pdf
- https://www.suerf.org/wp-content/uploads/2024/10/SUERF-Policy-Brief-1004_Pfister.pdf
- https://www.tandfonline.com/doi/full/10.1080/09538259.2024.2366253
- https://www.tandfonline.com/doi/full/10.1080/09538259.2025.2573356
- https://www.tandfonline.com/doi/full/10.1080/13876988.2024.2426878
- https://www.theblock.co/post/195341/zero-knowledge-proof-cbdc-privacy
- https://www.ubs.com/content/dam/assets/ib/global/doc/m-cbdc-bridge.pdf
- https://www.weforum.org/organizations/international-monetary-fund-imf/
- https://www.weforum.org/stories/2023/04/3-key-charts-imf-world-economic-outlook/
- https://www.weforum.org/stories/2024/04/inflation-economic-growth-economics-news-19-april/
- https://www.weforum.org/stories/2024/04/the-international-monetary-fund-what-does-imf-do/
- https://www.weforum.org/stories/2025/04/inside-the-2025-world-bank-imf-spring-meetings/
- https://www.weforum.org/videos/what-to-know-the-imf-explained/
- https://www.youtube.com/watch?v=BbcKJctx5Ek
- https://www3.weforum.org/docs/WEF_Privacy_and_Confidentiality_Options_for_CBDCs_2021.pdf

                