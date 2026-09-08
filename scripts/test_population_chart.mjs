import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {chartX,populationChart} from '../public/population-chart.mjs';
const series=JSON.parse(fs.readFileSync(new URL('../public/data/atlas.json',import.meta.url))).populationSeries;
test('both time scales preserve endpoints and exclude unsupported dates',()=>{
 for(const scale of ['log','linear']){assert.equal(chartX(1900,scale),58);assert.equal(chartX(2026,scale),568);assert.equal(chartX(1800,scale),null);assert.equal(chartX(2027,scale),null)}
 assert.notEqual(chartX(2000,'log'),chartX(2000,'linear'));
});
test('one-source series is ordered and retains the published 2020 WCD estimate',()=>{
 assert.deepEqual(series.points.map(p=>p.year),[1900,1970,2000,2020,2026]);assert.equal(series.points[3].value,1917487000);assert.ok(series.source.url.includes('worldchristiandatabase.org'));
});
test('chart controls, accessible values and missing-data fallback survive rendering',()=>{
 for(const scale of ['log','linear']){const html=populationChart(series,scale);assert.ok(html.includes(`data-chart-scale="${scale}" aria-pressed="true"`));assert.ok(html.includes('1,917,487,000'));assert.ok(html.includes('No estimates before 1900'));assert.ok(!html.includes('NaN'))}
 assert.ok(populationChart(null).includes('temporarily unavailable'));
});
