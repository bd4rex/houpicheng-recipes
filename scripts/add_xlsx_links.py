"""Add native URL relationships for the exporter feature unavailable in this runtime.

All sheet values, styles and tables are authored by Artifact Tool. This fallback
only attaches OOXML hyperlinks to the existing URL cells, preserving their text.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse, json, re, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG='http://schemas.openxmlformats.org/package/2006/relationships'
ET.register_namespace('',NS);ET.register_namespace('r',REL)

def main():
    p=argparse.ArgumentParser();p.add_argument('xlsx',type=Path);args=p.parse_args()
    config=[('videos.json','D'),('dish_index.json','E'),('excluded.json','D')]
    with ZipFile(args.xlsx) as z:parts={x.filename:z.read(x.filename) for x in z.infolist()}
    total=0
    for number,(source,col) in enumerate(config,1):
        records=json.loads((ROOT/'data'/source).read_text())
        name=f'xl/worksheets/sheet{number}.xml';relname=f'xl/worksheets/_rels/sheet{number}.xml.rels'
        sheet=ET.fromstring(parts[name])
        old=sheet.find(f'{{{NS}}}hyperlinks')
        if old is not None:sheet.remove(old)
        rels=ET.fromstring(parts[relname]) if relname in parts else ET.Element(f'{{{PKG}}}Relationships')
        for e in list(rels):
            if e.get('Type','').endswith('/hyperlink'):rels.remove(e)
        links=ET.Element(f'{{{NS}}}hyperlinks')
        for row,r in enumerate(records,8):
            url=r['url']
            assert re.fullmatch(r'https://www\.bilibili\.com/video/BV[0-9A-Za-z]+/',url)
            rid=f'rIdRecipeURL{row}'
            ET.SubElement(links,f'{{{NS}}}hyperlink',{'ref':f'{col}{row}',f'{{{REL}}}id':rid})
            ET.SubElement(rels,f'{{{PKG}}}Relationship',{'Id':rid,'Type':REL+'/hyperlink','Target':url,'TargetMode':'External'})
            total+=1
        following={'printOptions','pageMargins','pageSetup','headerFooter','rowBreaks','colBreaks','drawing','legacyDrawing','tableParts','extLst'}
        where=next((i for i,e in enumerate(sheet) if e.tag.rsplit('}',1)[-1] in following),len(sheet))
        sheet.insert(where,links)
        parts[name]=ET.tostring(sheet,encoding='utf-8',xml_declaration=True)
        parts[relname]=ET.tostring(rels,encoding='utf-8',xml_declaration=True)
    temp=args.xlsx.with_suffix('.links.tmp.xlsx')
    with ZipFile(temp,'w',compression=ZIP_DEFLATED) as z:
        for name,value in parts.items():z.writestr(name,value)
    temp.replace(args.xlsx)
    print(f'Attached {total} native Bilibili hyperlinks.')

if __name__=='__main__':main()
