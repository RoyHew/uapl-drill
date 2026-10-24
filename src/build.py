"""Rebuild uapl-drill.html and docs/ from questions/*.json.  Usage: python3 src/build.py"""
import json, base64, hashlib, os, shutil, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, Q, SITE = f'{R}/src', f'{R}/questions', f'{R}/docs'
ORDER = ['q_uas.json', 'q_pof.json', 'q_airlaw.json', 'q_extra.json', 'q_navmet.json', 'q_hf.json', 'q_safety.json']
bank, ids = [], set()
for f in ORDER:
    for q in json.load(open(f'{Q}/{f}', encoding='utf-8')):
        assert q['id'] not in ids, f"duplicate id {q['id']}"
        ids.add(q['id'])
        assert len(q['options']) == 4 and sum(o['correct'] for o in q['options']) == 1, q['id']
        assert all(o['why'].strip() for o in q['options']), q['id']
        bank.append({k: q[k] for k in ['id', 'module', 'topic', 'difficulty', 'question', 'options', 'source', 'note'] if q.get(k)})
print(len(bank), 'questions', dict(collections.Counter(q['module'] for q in bank)))
t = open(f'{SRC}/template.html', encoding='utf-8').read()
fish = base64.b64encode(open(f'{SRC}/fish160.png', 'rb').read()).decode()
body = t.replace('/*__FISH__*/', fish).replace('/*__DATA__*/', json.dumps(bank, ensure_ascii=False).replace('</', '<\\/'))
cut = body.index('<header class="top">')
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + body[:cut] + '</head>\n<body>\n' + body[cut:] + '\n</body>\n</html>\n')
version = hashlib.sha1(html.encode()).hexdigest()[:10]
open(f'{R}/uapl-drill.html', 'w', encoding='utf-8').write(html)
os.makedirs(SITE, exist_ok=True)
open(f'{SITE}/index.html', 'w', encoding='utf-8').write(html)
for a in ['manifest.webmanifest', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png']:
    shutil.copy(f'{SRC}/{a}', SITE)
open(f'{SITE}/sw.js', 'w', encoding='utf-8').write(open(f'{SRC}/sw.js', encoding='utf-8').read().replace('__VERSION__', version))
print('built', version)
