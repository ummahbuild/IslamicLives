"""Curated milestones and source snapshots; no interpolated historical populations."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sources={
 'quran':{'title':'Qur’an — Surah Ali ‘Imran 3:67; Ibrahim and submission to Allah','url':'https://quran.com/3/67','kind':'Scripture'},
 'birth':{'title':'The Met — The Birth of Islam','url':'https://www.metmuseum.org/essays/the-birth-of-islam','kind':'Historical scholarship'},
 'umayyad':{'title':'The Met — The Umayyad period, 661–750','url':'https://www.metmuseum.org/essays/the-art-of-the-umayyad-period-661-750','kind':'Historical scholarship'},
 'abbasid':{'title':'The Met — The Abbasid period, 750–1258','url':'https://www.metmuseum.org/essays/the-art-of-the-abbasid-period-750-1258','kind':'Historical scholarship'},
 'silk':{'title':'UNESCO — About the Silk Roads','url':'https://www.unesco.org/en/silk-roads/about-silk-roads','kind':'Historical scholarship'},
 'africa':{'title':'Stanford SPICE — The spread of Islam in West Africa','url':'https://spice.fsi.stanford.edu/docs/the_spread_of_islam_in_west_africa_containment_mixing_and_reform_from_the_eighth_to_the_twentieth_century','kind':'Historical scholarship'},
 'ottoman':{'title':'The Met — The Ottomans before 1600','url':'https://www.metmuseum.org/essays/the-art-of-the-ottomans-before-1600','kind':'Historical scholarship'},
 'safavid':{'title':'The Met — The Safavids before 1600','url':'https://www.metmuseum.org/essays/the-art-of-the-safavids-before-1600','kind':'Historical scholarship'},
 'mughal':{'title':'The Met — The Mughals before 1600','url':'https://www.metmuseum.org/essays/the-art-of-the-mughals-before-1600','kind':'Historical scholarship'},
 'america':{'title':'Smithsonian NMAAHC — African Muslims in early America','url':'https://nmaahc.si.edu/explore/stories/african-muslims-early-america','kind':'Historical scholarship'},
 'pew':{'title':'Pew Research Center — Muslim population change, 2010–2020 (2025)','url':'https://www.pewresearch.org/religion/2025/06/09/muslim-population-change/','kind':'Demographic estimates'},
 'regions':{'title':'Pew — Appendix B, page 1: regional population and Muslim shares (2025)','url':'https://www.pewresearch.org/wp-content/uploads/sites/20/2025/06/PR_2025.06.09_global-religious-change_appendix-b.pdf#page=1','kind':'Demographic estimates'},
 'drivers':{'title':'Pew — Factors driving religious change, 2010–2020','url':'https://www.pewresearch.org/religion/2025/06/09/factors-driving-religious-change-2010-2020/','kind':'Demographic research'},
 'wcd':{'title':'World Christian Database — Status of Global Christianity 2026, row 14: Muslims','url':'https://www.worldchristiandatabase.org/static/downloads/Status-of-Global-Christianity-2026.2b54be19fc0c.pdf','kind':'Historical and current demographic estimates'}
}
places=[
 ('mecca','Mecca',21.42,39.83),('medina','Medina',24.47,39.61),('damascus','Syria / Damascus',33.51,36.29),('egypt','Egypt',30,31.2),('iran','Iran',32.65,51.68),('maghreb','North Africa',35,10),('iberia','Iberia',37.89,-4.78),('sindh','Sindh / Indus region',25,68),('baghdad','Baghdad',33.32,44.37),('central','Central Asia',39.65,66.96),('china','Chinese maritime ports',24.87,118.68),('sahel','West African Sahel',16.77,-3.01),('east-africa','East African coast',-6.16,39.19),('malay','Malay Peninsula',2.2,102.25),('sumatra','Sumatra',5.5,95.3),('istanbul','Istanbul / Ottoman lands',41.01,28.98),('delhi','North India / Mughal lands',28.61,77.21),('atlantic','North America',32.78,-79.93)
]
places=[dict(id=i,name=n,lat=a,lon=o) for i,n,a,o in places]
events=[]
def event(id,year,date,title,text,mechanism,points,links,refs,pop=None):
 events.append(dict(id=id,year=year,date=date,title=title,text=text,mechanism=mechanism,places=points,links=links,sources=refs,population=pop))
def population(value,series,year,note):return dict(value=value,series=series,year=year,note=note)
event('tradition',None,'Before the dated timeline','From Adam, in Islamic belief','Islamic tradition understands the prophets’ message as submission to Allah. The Qur’an describes Ibrahim as a Muslim. These scriptural beginnings cannot be assigned a reliable calendar year, world population, or exact place on this map.','Scriptural account',[],[],['quran'])
event('610',610,'610 CE','A message in Mecca','Muhammad’s first revelation is traditionally dated to 610. His preaching in Mecca called people to the worship of one God.','Preaching',['mecca'],[],['birth'])
event('622',622,'622 CE','A community in Medina','The Hijrah took Muhammad and his followers from Mecca to Medina. The growing community there became the starting point of the Islamic calendar.','Migration & community',['mecca','medina'],[['mecca','medina']],['birth'])
event('650',650,'632–661 CE','Beyond the Arabian Peninsula','Under the early caliphs, Arab armies took Syria, Egypt, Iraq and Iran. Political control expanded rapidly; the populations of these lands did not all become Muslim at once.','Political expansion',['medina','damascus','egypt','iran'],[['medina','damascus'],['medina','egypt'],['medina','iran']],['birth'])
event('750',750,'661–750 CE','From the Atlantic to the Indus','The Umayyad caliphate, centred in Damascus, extended across North Africa and into Iberia and the Indus region. The markers locate selected parts of this realm; they do not measure conversion.','Political expansion',['damascus','maghreb','iberia','sindh'],[['damascus','maghreb'],['maghreb','iberia'],['damascus','sindh']],['umayyad'])
event('900',900,'8th–10th centuries','Cities connected by exchange','Baghdad became the Abbasid capital in 762. Overland and maritime networks connected the Islamic world with Central Asia and Chinese ports, carrying ideas and religious practices alongside goods.','Trade & scholarship',['baghdad','central','china'],[['baghdad','central'],['central','china']],['abbasid','silk'])
event('1300',1300,'8th–14th centuries','Across the Sahara','Muslim merchants, rulers and scholars helped Islam take root in West Africa over centuries. Communities adapted and debated religious practices; trade and political patronage were part of a gradual process.','Trade & local communities',['maghreb','sahel'],[['maghreb','sahel']],['africa'])
event('1500',1500,'Medieval maritime networks','Across the Indian Ocean','Maritime trade connected East Africa, Arabia, India and Southeast Asia. Merchants helped introduce Islam to Indonesia and Malaysia. These arcs show broad connections, not exact voyages or first-arrival dates.','Trade & community',['east-africa','mecca','sindh','sumatra','malay'],[['east-africa','mecca'],['mecca','sindh'],['sindh','sumatra'],['sumatra','malay']],['silk'])
event('1600',1600,'15th–17th centuries','Many Muslim political worlds','Ottoman expansion linked Anatolia, southeastern Europe and Arab lands. Safavid rulers established Shi‘i state patronage in Iran, while Mughal rule grew in South Asia. Their societies remained religiously diverse.','Rule & religious institutions',['istanbul','iran','delhi'],[],['ottoman','safavid','mughal'])
event('1800',1800,'16th–19th centuries','Across the Atlantic, under coercion','Muslims were among the Africans forcibly transported to the Americas through slavery. Their writings and lives preserve evidence of faith under oppression. This connection represents forced displacement.','Forced migration',['sahel','atlantic'],[['sahel','atlantic']],['america'])
for y,n in [(1900,200301000),(1970,576995000),(2000,1311342000)]:
 event(str(y),y,str(y)+' CE','A global population snapshot','This is a retrospective worldwide estimate from the World Christian Database’s 2026 table. Its methodology differs from Pew’s. No regional population distribution for this year is inferred from the total.','Demographic estimate',[],[],['wcd'],population(n,'wcd',y,'Retrospective estimate; rounded for display.'))
event('2010',2010,'2010 CE','Measuring a worldwide faith','Modern estimates bring the scale of Muslim communities into view. The regional circles use Pew’s population totals and rounded Muslim percentages. They represent whole regions, not the cities beneath them.','Demographic estimate',[],[],['pew','regions'],population(1700000000,'pew',2010,'Pew’s rounded global estimate, revised in its 2025 report.'))
event('2020',2020,'2020 CE','Around two billion people','Pew estimates about two billion Muslims worldwide in 2020. Its research identifies a younger population and higher fertility as important drivers of growth. Migration also changes where communities live.','Demography & migration',[],[],['pew','regions','drivers'],population(2000000000,'pew',2020,'Pew estimate, published in June 2025.'))
event('2026',2026,'2026 · Today’s chapter','A living, global faith','The World Christian Database’s 2026 table estimates about 2.1 billion Muslims. This is an annual demographic estimate, not a live census. Regional circles remain at Pew’s 2020 snapshot, clearly dated below.','Current estimate',[],[],['wcd','regions'],population(2105142000,'wcd',2026,'WCD 2026 estimate. Different series from Pew; do not infer growth by subtracting their totals.'))
regions=[]
for id,name,lat,lon,a,b in [
 ('asia','Asia–Pacific',23,100,(4128250000,24.8),(4544800000,26.1)),
 ('mena','Middle East & North Africa',27,30,(355630000,94.0),(439690000,94.2)),
 ('ssa','Sub-Saharan Africa',0,20,(861270000,32.0),(1124520000,32.8)),
 ('europe','Europe',53,25,(741700000,5.3),(752960000,6.0)),
 ('north-america','North America',40,-100,(345260000,1.1),(377610000,1.6)),
 ('latin-america','Latin America & Caribbean',-15,-60,(588470000,0.1),(646240000,0.1))]:
 regions.append(dict(id=id,name=name,lat=lat,lon=lon,source='regions',snapshots={str(y):dict(total=t,muslimPercent=p,value=round(t*p/100)) for y,(t,p) in [(2010,a),(2020,b)]}))
data=dict(reviewed='2026-09-08',sources=sources,places=places,events=events,regions=regions,methodology=[
 'The timeline advances through selected chapters, not evenly spaced years. Turquoise land extents are illustrative areas around sourced locations; they are not historical borders, territorial claims, first arrivals, conversion percentages, or conversion rates. Gold connections show earlier illustrative links.',
 'Historic place markers are equal-sized. Modern circle areas are proportional to regional counts before globe perspective; small circles have an outlined hit target. No territorial ownership or Muslim majority is implied.',
 'There are no global population estimates in this edition before 1900. Missing counts are unknown, not zero. No interpolation fills the gaps.',
 'Global snapshots use WCD 2026 (1900, 1970, 2000, 2026) and Pew 2025 (2010, 2020). These series differ: WCD estimates about 1.9 billion for 2020, versus Pew’s 2.0 billion. Do not treat the combined snapshots as one growth series.',
 'Regional counts equal Pew Appendix B population × rounded Muslim share. They are approximate and may differ from Pew’s unrounded counts or the global total. 2026 uses the 2020 regional map, without projecting it forward.',
 'Modern Natural Earth coastlines provide orientation only, including in the undated scriptural chapter. No ancient geography is reconstructed.'
])
data['populationSeries']=dict(source=sources['wcd'],points=[dict(year=y,value=v) for y,v in [(1900,200301000),(1970,576995000),(2000,1311342000),(2020,1917487000),(2026,2105142000)]])
(root/'public/data/atlas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(f'Atlas: {len(events)} chapters, {len(places)} historical places, {len(regions)} demographic regions')
