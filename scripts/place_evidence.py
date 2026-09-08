"""Reviewed date/place claims; region knowledge is separate from coordinate precision."""
def apply(people,q):
 by={p['id']:p for p in people}
 for id,place,ref,text in [
  ('musa','Egypt; later Madyan','10:87','The Qur’an explicitly locates Musa and his brother’s community in Egypt. This identifies a region, not a precise house or birthplace.'),
  ('harun','Egypt','10:87','Egypt is explicitly named in the instruction addressed to Musa and his brother. This is an associated region, not a verified birthplace.'),
  ('yusuf','Egypt','12:99','Yusuf welcomes his parents to Egypt in the Qur’anic account. The region is named even though the verse does not establish a birth date or exact city.')]:
  p=by[id];i=len(p['sources']);p['sources'].append(q(ref));p['place']=place
  p['placeEvidence']=dict(status='Named in scripture',text=text,sources=[i])
  p['chapters'].append(dict(title='A place named in the account',text=text,sources=[i]))
 p=by['musa'];i=len(p['sources']);p['sources'].append(q('28:22'));p['placeEvidence']['sources'].append(i);p['placeEvidence']['text']+=' Surah al-Qasas also names Madyan as the direction of his journey.'
 p=by['ibn-sina'];p['date']='c. 970 or 980–1037 CE · birth year disputed';p['place']='Afshana near Bukhara; later Hamadan and Isfahan'
 p['dateEvidence']=dict(status='Disputed birth year',text='980 is the conventional birth year. The consulted Stanford biography argues for approximately 970. His death in Hamadan is dated to 1037.',sources=[0])
 p['placeEvidence']=dict(status='Documented associated places',text='His autobiography, continued by al-Juzjani, places his birth in Afshana near Bukhara. The map locates the Bukhara region; it does not mark an exact birth house.',sources=[0])
 p['uncertainty']='The birth-year estimates are displayed as alternatives, not an exact date or a continuous confidence interval. Bukhara is an approximate regional locator. The principal biographical source is his autobiography with al-Juzjani’s continuation, discussed in the linked scholarship.'
