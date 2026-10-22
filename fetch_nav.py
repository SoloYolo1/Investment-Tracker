import html,json,re,urllib.request
URL="https://www.almeezangroup.com/"
MO={m:i for i,m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(),1)}
PAT=re.compile(r"Meezan Balanced Fund Offer Price \(Rs\.\) ([\d,.]+) Redemption Price \(Rs\.\) ([\d,.]+) NAV \(Rs\.\) ([\d,.]+) Launch Date \d{1,2} \w{3} \d{4} Validity Date (\d{1,2}) (\w{3}) (\d{4})")
def parse(raw):
    t=re.sub(r"<(script|style)[\s\S]*?</\1>"," ",raw)
    t=re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",t)))
    m=PAT.search(t)
    if not m:return None
    offer,red,nav,d,mon,y=m.groups()
    price=float(red.replace(",",""))or float(nav.replace(",",""))
    if not price or mon not in MO:return None
    return "%s-%02d-%02d"%(y,MO[mon],int(d)),price
def main():
    try:
        req=urllib.request.Request(URL,headers={"User-Agent":"Mozilla/5.0 (compatible; NAVTracker/1.0)"})
        r=parse(urllib.request.urlopen(req,timeout=30).read().decode("utf-8","ignore"))
    except Exception as e:
        print("fetch failed:",e);return
    if not r:
        print("price not found on page");return
    date,price=r
    try:data=json.load(open("data.json"))
    except Exception:data={"navs":[]}
    rows={x["date"]:x for x in data.get("navs",[])}
    if date in rows and abs(rows[date]["nav"]-price)<1e-9:
        print("no change",date,price);return
    rows[date]={"date":date,"nav":price}
    data["navs"]=sorted(rows.values(),key=lambda x:x["date"])
    json.dump(data,open("data.json","w"),indent=1)
    print("updated",date,price)
if __name__=="__main__":main()
