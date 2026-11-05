# ---- EDIT THESE, then run: python build.py ----
FONT_HEADING = "Bricolage Grotesque"   # any name from fonts.google.com
FONT_BODY = "IBM Plex Sans"            # any name from fonts.google.com
HEADING_WEIGHTS = "400;700"            # use "400" if the font has only one weight
BODY_WEIGHTS = "400;700"               # use "400" if the font has only one weight
BASE_SIZE = "17px"                     # body text size; headings scale with it
# -----------------------------------------------

fonts_url = ("https://fonts.googleapis.com/css2?family=" + FONT_HEADING.replace(" ", "+") + ":wght@" + HEADING_WEIGHTS
             + "&family=" + FONT_BODY.replace(" ", "+") + ":wght@" + BODY_WEIGHTS + "&display=swap")
open("theme.css", "w").write(f':root{{--font-heading:"{FONT_HEADING}",system-ui,sans-serif;--font-body:"{FONT_BODY}",system-ui,sans-serif;--base-size:{BASE_SIZE}}}\n')

# Generates the static site. Run: python build.py
NAME = "Sai Veeresh Bandi"
pages = [("index", "Home"), ("engineering", "Engineering"), ("programming", "Programming"),
         ("astrophysics", "Astrophysics"), ("publications", "Publications"),
         ("about", "About"), ("contact", "Contact")]

import os
# Background image for each page. Replace the file, or change the path here and run build.py again.
images = {slug: f"images/bg-{slug}.svg" for slug, _ in pages}
os.makedirs("images", exist_ok=True)
tints = {"index": "#0b7a75", "engineering": "#3b6ea5", "programming": "#5b5ea6", "astrophysics": "#1c2b5a", "publications": "#2f7d6b", "about": "#4a6a85", "contact": "#0b7a75"}
for slug, path in images.items():
    if not os.path.exists(path):  # never overwrite an image you have replaced
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{tints[slug]}"/><stop offset="1" stop-color="#112233"/></linearGradient></defs><rect width="1600" height="900" fill="url(#g)"/><g fill="none" stroke="#fff" stroke-opacity=".25" stroke-width="2"><circle cx="1200" cy="300" r="120"/><circle cx="1200" cy="300" r="220"/><circle cx="1200" cy="300" r="340"/></g></svg>'
        open(path, "w").write(svg)

hero_svg = """<svg class="shock" viewBox="0 0 320 200" role="img" aria-label="Bow shock ahead of a blunt body">
<path d="M10 100 H110" stroke="currentColor" stroke-width="1" stroke-dasharray="4 5" opacity=".5"/>
<path d="M150 20 Q70 100 150 180" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
<path d="M175 40 Q110 100 175 160" fill="none" stroke="var(--accent)" stroke-width="1.2" opacity=".5"/>
<path d="M190 60 Q175 100 190 140 L290 140 L290 60 Z" fill="currentColor"/>
<path d="M150 20 Q250 12 310 14 M150 180 Q250 188 310 186" fill="none" stroke="currentColor" stroke-width="1" opacity=".35"/>
</svg>"""

content = {}

content["index"] = f"""
<section class="hero"><div><h1>{NAME}</h1>
<p class="lead">Product design engineer working on EV components, and a self-driven researcher in computational fluid dynamics and astrophysics.</p>
<p><a class="btn" href="publications.html">Read my publications</a> <a class="btn ghost" href="contact.html">Get in touch</a></p></div>{hero_svg}</section>
<section><h2>What I work on</h2><div class="grid">
<a class="card" href="engineering.html"><h3>Engineering</h3><p>Mechanical design and CFD in ANSYS Fluent and OpenFOAM.</p></a>
<a class="card" href="programming.html"><h3>Programming</h3><p>Python solvers and C++ OpenFOAM development.</p></a>
<a class="card" href="astrophysics.html"><h3>Astrophysics</h3><p>Stellar evolution and astrophysical fluid dynamics.</p></a>
</div></section>"""

content["engineering"] = """
<h1>Engineering</h1><p class="lead">Product design and computational analysis, from component CAD to rarefied hypersonic flow.</p>
<section id="design"><h2>Design</h2>
<p>I design EV components as a Product Design Engineer at HRBL Group, Gurugram, using SolidWorks for modelling and ANSYS and Nastran for analysis, including CFD thermal studies.</p>
<ul><li>3D modelling and drawings in SolidWorks</li><li>Structural and thermal analysis in ANSYS and Nastran</li><li>Design for manufacture of EV components</li></ul></section>
<section id="cfd"><h2>CFD</h2>
<div class="grid two">
<div class="card" id="fluent"><h3>ANSYS Fluent</h3><p>Continuum and DSMC-approximation simulations of the Hayabusa capsule re-entry, and a spiked blunt body (aerospike) study for high-speed aerodynamics.</p><ul><li>Hypersonic external flow</li><li>Aerothermal heating</li></ul></div>
<div class="card" id="openfoam"><h3>OpenFOAM</h3><p>dsmcFoam simulations of an inclined flat plate across rarefied regimes, and mhdFoam backward-step cases with imposed magnetic field.</p><ul><li>Rarefied gas dynamics (DSMC)</li><li>Magnetohydrodynamics</li></ul></div>
</div></section>"""

content["programming"] = """
<h1>Programming</h1><p class="lead">Numerical code for fluid dynamics, written to be read and reproduced.</p>
<div class="grid two">
<section class="card" id="python"><h3>Python</h3><p>Finite-volume solvers and analysis notebooks.</p><ul>
<li>1D Riemann solvers: Sod shock tube with Rusanov, HLL and HLLC, moving on to HLLD</li>
<li>HLLC solver for relativistic fluids</li><li>Post-processing and plotting of simulation output</li></ul></section>
<section class="card" id="cpp"><h3>C++</h3><p>Solver development inside OpenFOAM.</p><ul>
<li>Custom solvers and boundary conditions for astrophysical flows (AstroFoam)</li>
<li>Case set-up and customisation of dsmcFoam and mhdFoam</li></ul></section>
</div>
<p>Code is on <a href="https://github.com/YOUR-USERNAME">GitHub</a>.</p>"""

content["astrophysics"] = """
<h1>Astrophysics</h1><p class="lead">Computational work on how stars evolve and how astrophysical gas flows.</p>
<section id="stellar"><h2>Stellar evolution</h2>
<p>Low-metallicity (Z = 10<sup>-4</sup>) stellar models computed with MESA for a grid of 0.5 to 2 solar masses, used to study zero-age main sequence properties and mass-luminosity scaling relations.</p></section>
<section id="fluid"><h2>Astrophysical fluid dynamics</h2>
<p>Hydrodynamics and MHD simulations with Athena++, PLUTO and RAMSES, including one-dimensional and two-dimensional Bondi accretion with and without a wind, and a review of relativistic fluid methods.</p>
<ul><li>Bondi accretion: 1D, 2D, 2D with wind</li><li>Riemann solvers for relativistic flows</li><li>Long-term goal: astrophysical solvers in OpenFOAM</li></ul></section>"""

content["publications"] = """
<h1>Publications</h1>
<section id="aerospace"><h2>Aerospace</h2>
<ul class="pubs"><li><strong>[Title of aerothermal CFD paper]</strong><br>Sai Veeresh Bandi, [co-authors]. <em>[Journal or conference]</em>, [year]. <a href="#">DOI</a></li></ul></section>
<section id="astro"><h2>Astrophysics</h2>
<ul class="pubs"><li><strong>[Title of MESA scaling-relations manuscript]</strong><br>Sai Veeresh Bandi, [co-authors]. Under revision.</li>
<li><strong>[Title of relativistic fluids review]</strong><br>Sai Veeresh Bandi. In preparation.</li></ul></section>"""

content["about"] = f"""
<h1>About me</h1>
<p class="lead">I am {NAME}, a mechanical engineer from India with a research focus on computational astrophysics.</p>
<p>I work as a Product Design Engineer at HRBL Group in Gurugram, designing EV components and running thermal CFD. Outside work I build and run simulations of astrophysical flows, hypersonic and rarefied gases, and MHD, and I develop OpenFOAM solvers in C++.</p>
<p>I have also done freelance aerospace work and published an aerothermal CFD paper. I am open to relocating for a PhD or research role.</p>
<h2>Education</h2><p>B.Tech in Mechanical Engineering, University College of Engineering Narasaraopeta (JNTUK), 2016 to 2020.</p>"""

content["contact"] = """
<h1>Contact</h1><p class="lead">For research collaboration, PhD opportunities or design work, send me an email.</p>
<ul class="contact"><li>Email: <a href="mailto:you@example.com">you@example.com</a></li>
<li>GitHub: <a href="https://github.com/YOUR-USERNAME">github.com/YOUR-USERNAME</a></li>
<li>LinkedIn: <a href="https://www.linkedin.com/in/YOUR-HANDLE">linkedin.com/in/YOUR-HANDLE</a></li></ul>"""

for slug, title in pages:
    nav = ""
    for s, t in pages:
        cur = ' aria-current="page"' if s == slug else ""
        nav += f'<a href="{s}.html"{cur}>{t}</a>'
    page_title = NAME if slug == "index" else f"{title} | {NAME}"
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<meta name="description" content="Portfolio of {NAME}: engineering, CFD, programming and astrophysics.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts_url}" rel="stylesheet">
<link rel="stylesheet" href="theme.css"><link rel="stylesheet" href="style.css"></head>
<body style="--page-bg:url('{images[slug]}')"><header><a class="brand" href="index.html">{NAME}</a><nav>{nav}</nav></header>
<main>{content[slug]}</main>
<footer>&copy; 2026 {NAME}</footer></body></html>"""
    open(slug + ".html", "w", encoding="utf-8").write(html)
