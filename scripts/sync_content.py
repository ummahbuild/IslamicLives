"""Copy generated public data into the shared workspace content package."""
from pathlib import Path
import shutil

root=Path(__file__).resolve().parents[1]
source=root/'public/data'
target=root/'packages/content/data'
target.mkdir(parents=True,exist_ok=True)
for name in ['people.json','spread.json','coverage.json','quran-mentions.json','atlas.json']:
 shutil.copy2(source/name,target/name)
print('Synced shared content package')
