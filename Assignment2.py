import os
import base64
import html
from IPython.display import HTML, display

# =========================
# 1. File paths
# =========================
image_path = "static_chart.png"
map1_path = "visualizations/assault_by_hour_district.html"
map2_path = "visualizations/assault_vs_selected_crime_map.html"

# =========================
# 2. Helpers
# =========================
def image_to_base64(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    ext = os.path.splitext(path)[1].lower().replace(".", "")
    if ext == "jpg":
        ext = "jpeg"
    return f"data:image/{ext};base64,{encoded}"

def html_file_to_srcdoc(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return html.escape(content)

# =========================
# 3. Load files if they exist
# =========================
img_src = image_to_base64(image_path) if os.path.exists(image_path) else None
map1_srcdoc = html_file_to_srcdoc(map1_path) if os.path.exists(map1_path) else None
map2_srcdoc = html_file_to_srcdoc(map2_path) if os.path.exists(map2_path) else None

# =========================
# 4. Build display blocks
# =========================
if img_src:
    fig1_block = f'''
    <img class="static-image" src="{img_src}" alt="Hourly distribution of assault incidents">
    '''
else:
    fig1_block = '''
    <div class="placeholder-box">
      Missing file: images/assault_hourly.png
    </div>
    '''

if map1_srcdoc:
    fig2_block = f'''
    <iframe class="figure-frame medium" srcdoc="{map1_srcdoc}"></iframe>
    '''
else:
    fig2_block = '''
    <div class="placeholder-box">
      Missing file: visualizations/assault_by_hour_district.html
    </div>
    '''

if map2_srcdoc:
    fig3_block = f'''
    <iframe class="figure-frame tall" srcdoc="{map2_srcdoc}"></iframe>
    '''
else:
    fig3_block = '''
    <div class="placeholder-box">
      Missing file: visualizations/assault_vs_selected_crime_map.html
    </div>
    '''

# =========================
# 5. Full website HTML
# =========================
page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SF Crime Data Story</title>
  <style>
    :root {{
      --bg: #0f172a;
      --card: #1e293b;
      --text: #e5e7eb;
      --muted: #94a3b8;
      --accent: #22c55e;
      --accent2: #38bdf8;
      --border: rgba(255,255,255,0.08);
      --shadow: 0 10px 30px rgba(0,0,0,0.28);
      --maxw: 1000px;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
      color: var(--text);
      line-height: 1.7;
    }}

    .container {{
      width: min(92%, var(--maxw));
      margin: 0 auto;
    }}

    .hero {{
      padding: 72px 0 46px;
      border-bottom: 1px solid var(--border);
      background:
        radial-gradient(circle at top right, rgba(56,189,248,0.13), transparent 28%),
        radial-gradient(circle at top left, rgba(34,197,94,0.12), transparent 24%);
    }}

    .eyebrow {{
      display: inline-block;
      padding: 6px 12px;
      border: 1px solid var(--border);
      border-radius: 999px;
      color: var(--muted);
      font-size: 0.9rem;
      margin-bottom: 18px;
      background: rgba(255,255,255,0.03);
    }}

    h1 {{
      font-size: clamp(2.2rem, 5vw, 4rem);
      line-height: 1.08;
      margin: 0 0 16px;
      letter-spacing: -0.03em;
    }}

    .subtitle {{
      font-size: 1.1rem;
      color: var(--muted);
      max-width: 760px;
      margin: 0 0 22px;
    }}

    .content {{
      padding: 40px 0 72px;
    }}

    .section, .intro, .closing {{
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border);
      border-radius: 22px;
      box-shadow: var(--shadow);
      padding: 30px;
      margin-bottom: 26px;
    }}

    .figure-card {{
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border);
      border-radius: 22px;
      box-shadow: var(--shadow);
      padding: 18px;
      margin: 22px 0 30px;
      overflow: hidden;
    }}

    h2 {{
      font-size: 1.7rem;
      line-height: 1.2;
      margin: 0 0 14px;
    }}

    h3 {{
      font-size: 1.15rem;
      margin: 0 0 12px;
    }}

    p {{
      margin: 0 0 14px;
    }}

    .muted {{
      color: var(--muted);
    }}

    .static-image {{
      width: 100%;
      border-radius: 16px;
      display: block;
      background: white;
    }}

    .figure-frame {{
      width: 100%;
      border: none;
      border-radius: 16px;
      display: block;
      background: white;
    }}

    .figure-frame.medium {{
      height: 620px;
    }}

    .figure-frame.tall {{
      height: 720px;
    }}

    .caption {{
      margin-top: 14px;
      padding-top: 14px;
      color: var(--muted);
      font-size: 0.98rem;
      border-top: 1px solid var(--border);
    }}

    .caption strong {{
      color: var(--text);
    }}

    .placeholder-box {{
      width: 100%;
      min-height: 300px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      border-radius: 16px;
      background: linear-gradient(135deg, #1f2937, #0f172a);
      color: #cbd5e1;
      border: 1px dashed rgba(255,255,255,0.15);
      padding: 24px;
    }}

    .footer {{
      padding: 20px 0 40px;
      color: var(--muted);
      text-align: center;
      font-size: 0.95rem;
    }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="container">
      <div class="eyebrow">Social Data Analysis · Assignment 2</div>
      <h1>Assault in San Francisco: Time, Place, and Comparison</h1>
      <p class="subtitle">
        This story explores when assault happens, how it varies across police districts, and how
        its spatial pattern compares with other crime categories.
      </p>
    </div>
  </header>

  <main class="content">
    <div class="container">

      <section class="intro">
        <h2>Introduction</h2>
        <p>
          Assault is not distributed evenly across the city or the day. Looking only at totals hides
          important variation in both time and geography. The three figures below build the story in stages:
          first the daily rhythm, then the district-level hourly map, and finally a comparison between assault
          and other crime types across districts.
        </p>
      </section>

      <section class="section">
        <h2>1. Assault has a clear daily rhythm</h2>
        <p>
          A first look at assault incidents shows that the pattern is far from uniform across the day.
          This gives the reader an immediate overview before adding spatial detail.
        </p>

        <article class="figure-card">
          <h3>Figure 1. Hourly distribution of assault incidents</h3>
          {fig1_block}
          <div class="caption">
            <strong>Caption:</strong> Assault incidents are relatively uncommon in the early morning hours
            and rise later in the day, remaining elevated into the evening. This shows that time of day is
            an important part of the assault pattern.
          </div>
        </article>
      </section>

      <section class="section">
        <h2>2. The district pattern changes over the day</h2>
        <p>
          The next figure adds geography. Instead of only asking when assault happens, it asks where
          assaults are concentrated at different times of day.
        </p>

        <article class="figure-card">
          <h3>Figure 2. Assault counts across police districts by hour</h3>
          {fig2_block}
          <div class="caption">
            <strong>Caption:</strong> This animated district choropleth shows how assault counts vary across
            San Francisco police districts throughout the day. Keeping the map fixed while changing the hour
            makes it easier to see which districts become more prominent at different times.
          </div>
        </article>
      </section>

      <section class="section">
        <h2>3. Assault can be compared with other crimes</h2>
        <p>
          The final figure lets the reader compare assault with a selected crime category using the same
          district-level map structure. This makes it possible to see whether other crimes share a similar
          spatial pattern or cluster differently across the city.
        </p>

        <article class="figure-card">
          <h3>Figure 3. Assault versus a selected crime category across districts</h3>
          {fig3_block}
          <div class="caption">
            <strong>Caption:</strong> The left side keeps assault fixed, while the right side updates to a
            selected crime category. This comparison helps reveal whether other crimes align with assault
            spatially or follow a different district profile.
          </div>
        </article>
      </section>

      <section class="closing">
        <h2>Conclusion</h2>
        <p>
          Together, these figures show that assault in San Francisco has both a temporal pattern and a spatial
          structure. It peaks at particular times, concentrates differently across districts over the day,
          and does not necessarily match the geography of other crimes.
        </p>
      </section>

      <div class="footer">
        Created by Fernando · SF Crime Data Story
      </div>
    </div>
  </main>
</body>
</html>
"""

display(HTML(page))
